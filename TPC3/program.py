import re
import json
from processo import Processo

file = open('processos.txt')
json_file = open('processos.json', "w")

lines = file.readlines()

por_ano = {}
nomes_por_seculo = {}
apelidos_por_seculo = {}
por_relacao = {}

linhas_invalidas = 0

# Função de comparação (nome, count)
def cmp(a):
    return a[1]

index = 0
json_max = 20
json_list = []

for line in lines:
    # Sintaxe -> Pasta::Data::Nome::Pai::Mãe::(Observações)::
    # Observações -> 

    result = re.search(r"^(\d+)::((\d{4})-\d{2}-\d{2})::((\w+).*?\b(\w+)(?:\s\(.*\))?)::((\w+).*?\b(\w+)(?:\s\(.*\))?)?::((\w+).*?\b(\w+)(?:\s\(.*\))?)?::(.+)?::$", line)
    # Pode não incluir pai, mãe e observações
    # Permite aliases Ex. Ana Lopes Coelho (ou Ana Fernandes Lopes)

    if result is not None:
        pasta = result.group(1)
        data = result.group(2)
        ano = result.group(3)
        nome_pessoa = result.group(4)
        nome = result.group(5)
        apelido = result.group(6)
        nome_pai = result.group(7)
        nome_mae = result.group(10)
        obs = result.group(13)

        # Calcular século 
        seculo = int(ano[0:2])

        if ano[2:4] != "00":
            seculo += 1

        # Distribuição por ano
        if ano not in por_ano:
            por_ano[ano] = 0
        por_ano[ano] += 1

        # Distribuições por seculo
        if seculo not in nomes_por_seculo:
            nomes_por_seculo[seculo] = {}
        if nome not in nomes_por_seculo[seculo]:
            nomes_por_seculo[seculo][nome] = 0
        nomes_por_seculo[seculo][nome] += 1

        if seculo not in apelidos_por_seculo:
            apelidos_por_seculo[seculo] = {}
        if apelido not in apelidos_por_seculo[seculo]:
            apelidos_por_seculo[seculo][apelido] = 0
        apelidos_por_seculo[seculo][apelido] += 1

        # Distribuição por relação
        if obs is not None:
            relacoes = re.findall(r"[a-z],([A-Z][\s\w]+)\.", obs)
            if relacoes is not None:
                for relacao in relacoes:
                    if relacao not in por_relacao:
                        por_relacao[relacao] = 0
                    por_relacao[relacao] += 1
        # Converter os primeros 20 registos para um formato JSON

        p = Processo(pasta, data, nome_pessoa, nome_pai, nome_mae, obs)
        
        if index < json_max:
            json_list.append(p.__dict__) # Convert para formato dict
            index += 1
        if index == json_max:
            index += 1
            json.dump(json_list, json_file, indent=4)        
    else:
        linhas_invalidas += 1

# Imprimir resultados

# Processos por ano
print("\n///// Processos por ano /////\n")
anos = list(por_ano.keys())
anos.sort()

for ano in anos:
    print(f"{ano} - {por_ano[ano]}")

# Nomes por seculo
print("\n///// Nomes por seculo /////\n")
seculos = list(nomes_por_seculo.keys())
seculos.sort()
top = 5
for seculo in seculos:
    print(f"\n{seculo}\n")
    l = list(nomes_por_seculo[seculo].items())
    l.sort(key=cmp, reverse=True)
    i = 0
    for nome, count in l:
        print(f"{nome} - {count}")
        i += 1
        if i == top:
            break

# Apelidos por seculo
print("\n///// Apelidos por seculo /////\n")
seculos = list(apelidos_por_seculo.keys())
seculos.sort()
top = 5
for seculo in seculos:
    print(f"\n{seculo}\n")
    l = list(apelidos_por_seculo[seculo].items())
    l.sort(key=cmp, reverse=True)
    i = 0
    for apelido, count in l:
        print(f"{apelido} - {count}")
        i += 1
        if i == top:
            break

# Por relação

print("\n///// Distribuição das relações /////\n")
relacoes = list(por_relacao.items())
relacoes.sort(key=cmp, reverse=True)

for relacao, count in relacoes:
    print(f"{relacao} - {count}")