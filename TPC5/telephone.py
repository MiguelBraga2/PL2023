import sys
import re

on = False
troco = 0

def saldo():
    print('saldo = ' + str(troco))

def levantar(line):
    global on

    if on is True: # Telefone levantado
        print('maq: "Telefone já levantado!"')
    else: # Telefone pousado
        on = True
        print('maq: "Introduza moedas."')

def pousar(line):
    global on

    if on is True: # Telefone levantado
        on = False
        saldo()
    else: # Telefone pousado
        print('maq: "Telefone já pousado!"')

def moeda(line):
    global troco, on

    if on is True: # Telefone levantado
        moedas = re.finditer(r"(\d+)([ce])", line)
        for moeda in moedas:
            type = moeda.group(2)
            val = moeda.group(1)

            print('maq: "', end="")

            if type == 'c':
                if val in ['1', '2', '5', '10', '20', '50']:
                    troco += int(val) / 100
                else:
                    print(str(moeda.group(0)) + ' - moeda inválida; ', end='')
            elif type == 'e':
                if val in ['1', '2']:
                    troco += int(val)
                else:
                    print(str(moeda.group(0)) + ' - moeda inválida; ', end='')
        print('saldo = ' + str(int(troco // 1)) + 'e' + str(int((troco % 1) * 100)) + 'c"')
    else: # Telefone pousado
        print('maq: "Telefone já pousado!"')
    
def telefone(line):
    if on is True: # Telefone levantado
        if m := re.match(r"(00\d+|\d{9})$", line):
            number = m.group(1)
            if m := re.match(r"601\d+", line):
                print('maq: "Esse número não é permitido neste telefone. Queira discar novo número!"')
            elif m := re.match(r"00\d+", line):
                if saldo < 1.5:
                    print('maq: Saldo insuficiente')
                else:
                    saldo -= 1.5
            elif m := re.match(r"2\d+", line):
                if saldo < 0.25:
                    print('maq: Saldo insuficiente')
                else:
                    saldo -= 0.25
            elif m := re.match(r"800\d+", line):
                saldo -= 0
            elif m := re.match(r"808\d+", line):
                if saldo < 0.1:
                    print('maq: Saldo insuficiente')
                else:
                    saldo -= 0.1
            else: 
                print('maq: "Número inválido!"')
        else: 
            print('maq: "Número inválido!"')
    else: # Telefone pousado
        print('maq: "Telefone pousado. Não é possível realizar chamadas!"')

def abortar(line):
    if on is True: # Telefone levantado
        on = False
        saldo()
    else: # Telefone pousado
        print('maq: "Telefone já pousado!"')


def main():
    commands = {
        'LEVANTAR': levantar,
        'POUSAR': pousar,
        'MOEDA': moeda,
        'T=': telefone,
        'ABORTAR': abortar
    }

    for line in sys.stdin:
        for command, f in commands.items():
            if line.startswith(command):
                l = re.split(command, line)[1]
                f(l)

if __name__ == '__main__':
    main()