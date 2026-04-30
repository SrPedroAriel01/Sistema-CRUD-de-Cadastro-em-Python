class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome.strip()
        self.idade = idade

    def mostrar(self):
        print(f"Nome: {self.nome} | Idade: {self.idade}")

    def to_dict(self):
        return {
            "nome": self.nome,
            "idade": self.idade
        }

    @staticmethod
    def from_dict(dado):
        return Pessoa(dado["nome"], dado["idade"])