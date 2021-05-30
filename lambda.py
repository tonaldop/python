# list comprehension
# otimização e performance
# escrever menos linhas

lista = [x*2 for x in range(10)]
print(lista)

lista_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new = [k for k in lista_]
print(new)

new_tuplas = [(k, v) for k in lista_ for v in lista_]
print(new_tuplas)

# com if
lista_b = list(range(100))
exemplo = [x for x in lista_b if x % 7 == 0]
# lista_c = [k for k in range(10)]
for k, v in enumerate(range(10), 1):
    print(f'{v} x {k} = {v*k}')
