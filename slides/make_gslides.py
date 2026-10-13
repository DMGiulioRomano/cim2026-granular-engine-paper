#!/usr/bin/env python3
"""
make_gslides.py — la presentazione Google per il CIM (issue #40), da
slides/media/pge_cim2026_google.pptx (make_pptx.py, soli poster).

1. carica su Drive, in una cartella «PGE CIM 2026 slides», i video delle MAP
   e dei terminali (elencati in slides/media/pptx/videos.json);
2. carica il PPTX convertendolo in Google Presentazioni;
3. inserisce ogni video da Drive sopra il suo poster (API Slides): quelli da
   terminale partono da soli e senza audio, le MAP al clic, con l'audio;
4. esporta il PDF da Google Presentazioni: è ciò che verrà proiettato.

Ogni esecuzione crea una presentazione nuova (nuovo link). La cartella del
comitato resta un passo a mano: copiare la presentazione e il PDF lì.

Credenziali, una volta sola: un client OAuth «Desktop app» da Google Cloud
Console (API Drive e Slides abilitate) salvato come slides/credentials.json.
Al primo avvio si apre il browser per il consenso; il token resta in
slides/.gtoken.json. Entrambi sono fuori da git.

Uso:
    python slides/make_gslides.py
"""
import json
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SLIDES = os.path.dirname(os.path.abspath(__file__))
MEDIA = os.path.join(SLIDES, "media")
DECK = os.path.join(MEDIA, "pge_cim2026_google.pptx")
VIDEOS = os.path.join(MEDIA, "pptx", "videos.json")
PDF = os.path.join(MEDIA, "pge_cim2026_gslides.pdf")
CREDS = os.path.join(SLIDES, "credentials.json")
TOKEN = os.path.join(SLIDES, ".gtoken.json")
FOLDER = "PGE CIM 2026 slides"
TITLE = "PythonGranularEngine — CIM 2026"
# drive.file: solo i file che questo script crea, niente accesso al resto del Drive
SCOPES = ["https://www.googleapis.com/auth/drive.file",
          "https://www.googleapis.com/auth/presentations"]


def credentials():
    creds = Credentials.from_authorized_user_file(TOKEN, SCOPES) if os.path.exists(TOKEN) else None
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    if not creds or not creds.valid:
        if not os.path.exists(CREDS):
            raise SystemExit(f"manca {CREDS}: vedi la docstring di questo script")
        creds = InstalledAppFlow.from_client_secrets_file(CREDS, SCOPES).run_local_server(port=0)
    open(TOKEN, "w").write(creds.to_json())
    return creds


def upload(drive, path, parent, mime, convert_to=None):
    meta = {"name": os.path.basename(path), "parents": [parent]}
    if convert_to:
        meta.update(name=TITLE, mimeType=convert_to)
    f = drive.files().create(body=meta, fields="id",
                             media_body=MediaFileUpload(path, mimetype=mime, resumable=True)).execute()
    print(f"caricato {os.path.basename(path)}")
    return f["id"]


def main():
    creds = credentials()
    drive = build("drive", "v3", credentials=creds)
    slides = build("slides", "v1", credentials=creds)

    q = (f"name = '{FOLDER}' and mimeType = 'application/vnd.google-apps.folder' "
         "and trashed = false")
    found = drive.files().list(q=q, fields="files(id)").execute()["files"]
    folder = found[0]["id"] if found else drive.files().create(
        body={"name": FOLDER, "mimeType": "application/vnd.google-apps.folder"},
        fields="id").execute()["id"]

    videos = json.load(open(VIDEOS))
    ids = {}
    for v in videos:
        if v["file"] not in ids:
            ids[v["file"]] = upload(drive, os.path.join(MEDIA, v["file"]), folder, "video/mp4")

    pres_id = upload(drive, DECK, folder,
                     "application/vnd.openxmlformats-officedocument.presentationml.presentation",
                     convert_to="application/vnd.google-apps.presentation")
    pages = slides.presentations().get(presentationId=pres_id,
                                       fields="slides.objectId").execute()["slides"]

    reqs = []
    for k, v in enumerate(videos):
        x, y, w, h = v["emu"]
        oid = f"pge_video_{k}"
        reqs.append({"createVideo": {
            "objectId": oid, "source": "DRIVE", "id": ids[v["file"]],
            "elementProperties": {
                "pageObjectId": pages[v["slide"]]["objectId"],
                "size": {"width": {"magnitude": w, "unit": "EMU"},
                         "height": {"magnitude": h, "unit": "EMU"}},
                "transform": {"scaleX": 1, "scaleY": 1, "translateX": x, "translateY": y,
                              "unit": "EMU"}}}})
        if v["muted"]:
            reqs.append({"updateVideoProperties": {
                "objectId": oid, "fields": "autoPlay,mute",
                "videoProperties": {"autoPlay": True, "mute": True}}})
    slides.presentations().batchUpdate(presentationId=pres_id, body={"requests": reqs}).execute()
    print(f"inseriti {len(videos)} video")

    pdf = drive.files().export(fileId=pres_id, mimeType="application/pdf").execute()
    open(PDF, "wb").write(pdf)
    print(f"=== https://docs.google.com/presentation/d/{pres_id}/edit ===")
    print(f"=== {PDF} ===")


if __name__ == "__main__":
    main()
