from sistema import *

try:
    menuPrincipal()
except ValueError:
    print(INR, 'Deve digitar o nº correspondente a opção desejada e em seguida tecle [ENTER]!!!', CN)
    sleep(3)
    menuPrincipal()
