from os import system


def color(color_name: str, bold=False, underline=False, inverse=False, background=False):

    b = 1 if bold else ''
    u = 4 if underline else ''
    i = 7 if inverse else ''
    colors_list = ('black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'light gray', 'black gray',
                   'light red', 'light green', 'light yellow', 'light blue', 'light magenta', 'light cyan', 'white',
                   'reset')

    variation = 3
    position_color = colors_list.index(color_name) if color_name in colors_list else 15

    if 7 < position_color <= 16:
        variation = 9
        position_color -= 8

    color_ = 40 + position_color if background else 30 + position_color

    if variation == 9:
        color_ = 100 + position_color if background else 90 + position_color

    return f'[{b};{i};{u};{color_}m'


frase = 'O rato roeu a roupa do rei de Roma'

preto = color('black')
vermelho = color('red', bold=True, underline=False, inverse=False, background=True)
verde = color('green')
amarelo = color('yellow')
azul = color('blue')
magenta = color('magenta')
cyan = color('cyan')
cinza_claro = color('light gray')
cinca_escuro = color('black gray')
vermelho_claro = color('light red')
verde_claro = color('light green')
amarelo_claro = color('light yellow')
azul_claro = color('light blue')
magenta_claro = color('light magenta')
cyan_claro = color('light cyan')
branco = color('white')
julietea = color('whilow')
reset = color('reset')


system(f"echo {preto}{frase}{reset} 01")
system(f"echo {vermelho}{frase}{reset} 02")
system(f"echo {verde}{frase}{reset} 03")
system(f"echo {amarelo}{frase} 04")
system(f"echo {azul}{frase} 05")
system(f"echo {magenta}{frase} 06")
system(f"echo {cyan}{frase} 07")
system(f"echo {cinza_claro}{frase} 08")
print('')
system(f"echo {cinca_escuro}{frase} 09")
system(f"echo {vermelho_claro}{frase} 10")
system(f"echo {verde_claro}{frase} 11")
system(f"echo {amarelo_claro}{frase} 12")
system(f"echo {azul_claro}{frase} 13")
system(f"echo {magenta_claro}{frase} 14")
system(f"echo {cyan_claro}{frase} 15")
system(f"echo {branco}{frase} 16")
print('')
system(f"echo {julietea}{frase} 17")
print('')

input('Aperte qualquer tecla para sair.')
