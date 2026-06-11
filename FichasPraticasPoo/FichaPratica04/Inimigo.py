
class Inimigo:
    def __init__(self, nome, vida, ataque, defesa, experiencia, moedas):
        self.__nome = nome
        self.__vida = vida
        self.__ataque = ataque
        self.__defesa = defesa
        self.__experiencia = experiencia
        self.__moedas = moedas

    def getNome(self):
        # TODO:
        # 1. Retornar o nome do Inimigo
        return ""

    def getVida(self):
        # TODO:
        # 1. Retornar a vida do Inimigo
        return 0

    def getAtaque(self):
        # TODO:
        # 1. Retornar o ataque do Inimigo
        return 0

    def getDefesa(self):
        # TODO:
        # 1. Retornar a defesa do Inimigo
        return ""

    def getExperiencia(self):
        return self.__experiencia

    def getMoedas(self):
        return self.__moedas

    def setNome(self, nome):
        self.__nome = nome

    def setVida(self, vida):
        # TODO:
        # 1. Mudar a vida do Inimigo
        pass

    def setAtaque(self, ataque):
        self.__ataque = ataque

    def setDefesa(self, defesa):
        self.__defesa = defesa

    def setExperiencia(self, experiencia):
        self.__experiencia = experiencia

    def setMoedas(self, moedas):
        self.__moedas = moedas

    def receberDano(self, dano):
        # TODO:
        # 1. Calcular o dano real recebido pelo inimigo.
        # 2. O dano real deve ter em conta a defesa do inimigo.
        # 3. O dano mínimo deve ser 1.
        # 4. Atualizar a vida do inimigo.
        # 5. Garantir que a vida não fica abaixo de 0.

        print("[TODO] O método receberDano() do inimigo ainda não foi implementado.")

    def atacar(self, jogador):
        # TODO:
        # 1. Calcular o dano causado ao jogador.
        # 2. Chamar o método receberDano() do jogador.
        # 3. Mostrar uma mensagem com o ataque.

        print("[TODO] O método atacar() do inimigo ainda não foi implementado.")

    def estaVivo(self):
        # TODO:
        # Devolver True se a vida do inimigo for maior do que 0.
        # Devolver False caso contrário.

        return self.__vida > 0

    def mostrarEstado(self):
        print("\n===== ESTADO DO INIMIGO =====")
        print("Nome:", self.__nome)
        print("Vida:", self.__vida)
        print("Ataque:", self.__ataque)
        print("Defesa:", self.__defesa)
