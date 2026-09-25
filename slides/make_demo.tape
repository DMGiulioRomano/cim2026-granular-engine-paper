# make_demo.tape — video del lancio da terminale per la slide 3.
# Registra nel repo PGE di lavoro (sibling del repo del paper) lo YAML di
# complete_example: cat della specifica, make all, file prodotti.
#
# Uso (dalla radice del repo del paper, serve vhs):
#   vhs slides/make_demo.tape
# Lo YAML copiato in configs/ e gli output in output/ vengono rimossi alla fine.

Output slides/media/complete_example_make.mp4

Set Shell "bash"
Set FontSize 30
Set Width 1200
Set Height 900
Set Padding 24
Set Theme "Monokai Vivid"
Set TypingSpeed 45ms

Hide
Type "cd ../PythonGranularEngine && cp ../cim2026-granular-engine-paper/paper/examples/complete_example/complete_example.yml configs/" Enter
# flag di comodità fuori dall'inquadratura: niente stem, niente apertura automatica
Type "export MAKEFLAGS='STEMS=false AUTOPEN=false AUTOKILL=false' PS1='\[\e[32m\]PythonGranularEngine\[\e[0m\] $ '" Enter
Type "clear" Enter
Show

Type "cat configs/complete_example.yml" Sleep 400ms Enter
Sleep 5s
Type "make all FILE=complete_example RENDERER=csound AUTOVISUAL=true" Sleep 600ms Enter
Wait@120s /\$ *$/
Sleep 2s
Type "ls output/complete_example.*" Sleep 400ms Enter
Sleep 4s

Hide
Type "rm -f configs/complete_example.yml output/complete_example.*" Enter
