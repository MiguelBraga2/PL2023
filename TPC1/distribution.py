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

    def add_element(self, val):
        if val in self.dist:
            self.dist[val] += 1
        else:
            self.dist[val] = 1
