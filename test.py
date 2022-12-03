# Este script prueba diferentes funcionalidades para comprobar rápidamente que
# todo funiona correctamente

from matrices import Matriz

mimatriz = Matriz(4,5)

mimatriz.cambia_elemento(2,3,414243)
print(mimatriz.elemento(2,3))
print(mimatriz)
mimatriz.cambia_elemento(-2,81,41)
print(mimatriz.elemento("A","B"))
