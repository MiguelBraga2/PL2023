class Processo:
    def __init__(self, pasta, data, nome, nome_pai, nome_mae, obs):
        self.pasta = pasta
        self.data = data
        self.nome = nome
        self.nome_pai = nome_pai
        self.nome_mae = nome_mae
        self.obs = obs

    def __str__(self) -> str:
        return f"{self.__pasta} - {self.__data} - {self.__nome} - {self.__nome_pai} - {self.__nome_mae} - {self.__obs}"
    
    def __repr__(self) -> str:
        return self.__str__()