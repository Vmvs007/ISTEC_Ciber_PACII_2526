
class Jogador:
    def __init__(self, nome, vidaMaxima, ataque, defesa, nivel, experiencia, moedas):
        self.__nome = nome
        self.__vidaMaxima = vidaMaxima
        self.__vida = vidaMaxima
        self.__ataque = ataque
        self.__defesa = defesa
        self.__nivel = nivel
        self.__experiencia = experiencia
        self.__moedas = moedas
        self.__arma = None
        self.__armadura = None
        self.__pocao = None

    def getNome(self):
        # TODO:
        # 1. Retornar o nome do Jogador
        return ""

    def getVida(self):
        # TODO:
        # 1. Retornar a vida do Jogador
        return 0

    def getVidaMaxima(self):
        return self.__vidaMaxima

    def getAtaque(self):
        # TODO:
        # 1. Retornar o ataque do Jogador
        return 0

    def getDefesa(self):
        return self.__defesa

    def getNivel(self):
        return self.__nivel

    def getExperiencia(self):
        return self.__experiencia

    def getMoedas(self):
        # TODO:
        # 1. Retornar a quantidade de moedas do Jogador
        return 0

    def getArma(self):
        return self.__arma

    def getArmadura(self):
        return self.__armadura

    def getPocao(self):
        return self.__pocao

    def setNome(self, nome):
        self.__nome = nome

    def setVida(self, vida):
        self.__vida = vida

    def setVidaMaxima(self, vidaMaxima):
        self.__vidaMaxima = vidaMaxima

    def setAtaque(self, ataque):
        self.__ataque = ataque

    def setDefesa(self, defesa):
        self.__defesa = defesa

    def setNivel(self, nivel):
        self.__nivel = nivel

    def setExperiencia(self, experiencia):
        self.__experiencia = experiencia

    def setMoedas(self, moedas):
        # TODO:
        # 1. Alterar a quantidade de moedas do Jogador
        pass

    def setArma(self, arma):
        # TODO:
        # 1. Alterar a arma do Jogador
        pass

    def setArmadura(self, armadura):
        self.__armadura = armadura

    def setPocao(self, pocao):
        self.__pocao = pocao

    def getAtaqueTotal(self):
        # TODO:
        # 1. Começar pelo ataque base do jogador.
        # 2. Se o jogador tiver arma equipada, somar o bónus da arma.
        # 3. Devolver o ataque total.

        return self.__ataque

    def getDefesaTotal(self):
        # TODO:
        # 1. Começar pela defesa base do jogador.
        # 2. Se o jogador tiver armadura equipada, somar o bónus da armadura.
        # 3. Devolver a defesa total.

        return self.__defesa

    def receberDano(self, dano):
        # TODO:
        # 1. Calcular o dano real recebido pelo jogador.
        # 2. O dano real deve ter em conta a defesa total do jogador.
        # 3. O dano mínimo deve ser 1.
        # 4. Atualizar a vida do jogador.
        # 5. Garantir que a vida nunca fica abaixo de 0.

        print("[TODO] O método receberDano() do jogador ainda não foi implementado.")

    def atacar(self, inimigo):
        # TODO:
        # 1. Calcular o ataque total do jogador.
        # 2. Chamar o método receberDano() do inimigo.
        # 3. Mostrar uma mensagem com o nome do jogador, inimigo e dano causado.

        print("[TODO] O método atacar() do jogador ainda não foi implementado.")

    def curar(self, valor):
        # TODO:
        # 1. Aumentar a vida do jogador de acordo com o valor recebido.
        # 2. Garantir que a vida não ultrapassa a vida máxima.
        # 3. Mostrar mensagem com a vida recuperada.

        print("[TODO] O método curar() ainda não foi implementado.")

    def ganharExperiencia(self, valor):
        # TODO:
        # 1. Somar a experiência recebida à experiência atual.
        # 2. Verificar se o jogador deve subir de nível.
        # 3. Chamar o método subirNivel(), se necessário.

        print("[TODO] O método ganharExperiencia() ainda não foi implementado.")

    def subirNivel(self):
        # TODO:
        # 1. Definir a experiência necessária para subir de nível.
        # 2. Se o jogador tiver experiência suficiente:
        #    - aumentar o nível
        #    - aumentar a vida máxima
        #    - aumentar o ataque
        #    - aumentar a defesa
        #    - restaurar a vida
        # 3. Devolver True se subiu de nível, False caso contrário.

        print("[TODO] O método subirNivel() ainda não foi implementado.")
        return False

    def ganharMoedas(self, valor):
        # TODO:
        # Somar as moedas recebidas ao total de moedas do jogador.

        print("[TODO] O método ganharMoedas() ainda não foi implementado.")

    def gastarMoedas(self, valor):
        # TODO:
        # 1. Verificar se o jogador tem moedas suficientes.
        # 2. Se tiver, subtrair o valor e devolver True.
        # 3. Caso contrário, devolver False.

        print("[TODO] O método gastarMoedas() ainda não foi implementado.")
        return False

    def equiparArma(self, arma):
        # TODO:
        # Guardar a arma recebida no atributo __arma.

        print("[TODO] O método equiparArma() ainda não foi implementado.")

    def equiparArmadura(self, armadura):
        # TODO:
        # Guardar a armadura recebida no atributo __armadura.

        print("[TODO] O método equiparArmadura() ainda não foi implementado.")

    def guardarPocao(self, pocao):
        # TODO:
        # Guardar a poção recebida no atributo __pocao.

        print("[TODO] O método guardarPocao() ainda não foi implementado.")

    def usarPocao(self):
        # TODO:
        # 1. Verificar se o jogador tem uma poção.
        # 2. Se tiver, curar o jogador.
        # 3. Depois de usar, remover a poção.
        # 4. Devolver True se usou poção, False caso contrário.

        print("[TODO] O método usarPocao() ainda não foi implementado.")
        return False

    def estaVivo(self):
        # TODO:
        # Devolver True se a vida do jogador for maior do que 0.
        # Devolver False caso contrário.

        return self.__vida > 0

    def mostrarEstado(self):
        print("\n===== ESTADO DO JOGADOR =====")
        print("Nome:", self.__nome)
        print("Vida:", self.__vida, "/", self.__vidaMaxima)
        print("Nível:", self.__nivel)
        print("Experiência:", self.__experiencia)
        print("Moedas:", self.__moedas)
        print("Ataque base:", self.__ataque)
        print("Defesa base:", self.__defesa)
        print("Ataque total:", self.getAtaqueTotal())
        print("Defesa total:", self.getDefesaTotal())

        if self.__arma is None:
            print("Arma equipada: nenhuma")
        else:
            print("Arma equipada:", self.__arma.getNome())

        if self.__armadura is None:
            print("Armadura equipada: nenhuma")
        else:
            print("Armadura equipada:", self.__armadura.getNome())

        if self.__pocao is None:
            print("Poção guardada: nenhuma")
        else:
            print("Poção guardada:", self.__pocao.getNome())

