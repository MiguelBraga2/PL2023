import csv

def reader():
    with open('myheart.csv') as csvfile:
        csvfile.readline()
        reader = csv.reader(csvfile)
        # Lista de listas
        info = list(reader)
        return info

def by_sex(registers):
    dist = {}
    for line in registers:
        if line[1] in dist:
            dist[line[1]] += 1
        else:
            dist[line[1]] = 1
    
    return dist

def by_age(registers):
    dist = {}
    # Key -> Limite inferior do intervalo
    # Exemplo: dist[30] -> [30-34]
    for line in registers:
        age = int(line[0])
        lower_limit = (age//5)*5
        if lower_limit in dist:
            dist[lower_limit] += 1
        else:
            dist[lower_limit] = 1
    
    return dist

def print_ages(ages_dist:dict):
    keys = list(ages_dist.keys())
    keys.sort()

    for key in keys:
        print(f"{key}: {ages_dist[key]}")


print_ages(by_age(reader()))
