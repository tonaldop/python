from os import system


class Colors(object):

    def __init__(self):
        self.__color = ''

    def color(self, color_name: str, bold=False, underline=False, inverse=False, background=False):

        b, u, i = '', '', ''
        if bold:
            b = 1
        if underline:
            u = 4
        if inverse:
            i = 7

        colors_list = ('black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'light gray', 'black gray',
                       'light red', 'light green', 'light yellow', 'light blue', 'light magenta', 'light cyan', 'white',
                       'reset')

        variation = 3
        position_color = colors_list.index(color_name)
        if 7 < position_color <= 16:
            variation = 9
            position_color -= 8

        if variation == 3:
            self.__color = 30 + position_color
            if background:
                self.__color = 40 + position_color

        if variation == 9:
            self.__color = 90 + position_color
            if background:
                self.__color = 100 + position_color

        return f'[{b};{i};{u};{self.__color}m'


frase = 'O rato roeu a roupa do rei de Roma'
teste = Colors()

preto = teste.color('black')
vermelho = teste.color('red', bold=True, underline=True, background=True)
verde = teste.color('green')
amarelo = teste.color('yellow')
azul = teste.color('blue')
magenta = teste.color('magenta')
cyan = teste.color('cyan')
cinza_claro = teste.color('light gray')
cinca_escuro = teste.color('black gray')
vermelho_claro = teste.color('light red')
verde_claro = teste.color('light green')
amarelo_claro = teste.color('light yellow')
azul_claro = teste.color('light blue')
magenta_claro = teste.color('light magenta')
cyan_claro = teste.color('light cyan')
branco = teste.color('white')
reset = teste.color('reset')


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

input('Aperte qualquer tecla para sair.')
