class Distribution:
    def __init__(self):
        self.dist = {}

    def __str__(self):
        str = ""
        for key in self.dist.keys():
            value = self.dist[key]
            str += f"{key} : {value}\n"
        return str

    def __repr__(self):
        return str(self)

    def print_sex_distribution(self):
        str =  "|-----------------|\n"
        str += "|  Sex  |  Count  |\n"
        str += "|-----------------|\n"

        for (chave, valor) in self.dist.items():
            str += f"|   {chave}   |   {valor}   |\n"
            str += "|-----------------|\n"

        print(str)

    def print_age_distribution(self):
        keys = list(self.dist.keys())
        keys.sort()
        str =  "|-------------------|\n"
        str += "|   Age    |  Count |\n"
        str += "|-------------------|\n"

        for key in keys:
            str += f"| [{key}, {key+5}] |   {self.dist[key]}   |\n"
            str += "|-------------------|\n"

        print(str)

    def print_cholesterol_distribution(self):
        keys = list(self.dist.keys())
        keys.sort()
        str =  "|----------------------|\n"
        str += "| Cholesterol |  Count |\n"
        str += "|----------------------|\n"

        for key in keys:
            str += f"| [{key}, {key + 10}]  |    {self.dist[key]}   |\n"
            str += "|----------------------|\n"

        print(str)


    def add_element(self, val):
        if val in self.dist:
            self.dist[val] += 1
        else:
            self.dist[val] = 1
