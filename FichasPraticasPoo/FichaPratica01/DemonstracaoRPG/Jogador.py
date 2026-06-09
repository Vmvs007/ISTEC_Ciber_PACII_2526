class Jogador:
    def __init__(self, nome, vida, ataque, pocoes):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.pocoes = pocoes

    def atacar(self, npc):
        print(f"{self.nome} atacou {npc.nome} e causou {self.ataque} de dano!")
        npc.receber_dano(self.ataque)

    def receber_dano(self, dano):
        self.vida -= dano

        if self.vida < 0:
            self.vida = 0

        print(f"{self.nome} recebeu {dano} de dano. Vida atual: {self.vida}")

    def usar_pocao(self):
        if self.pocoes > 0:
            self.vida += 40
            self.pocoes -= 1
            print(f"{self.nome} usou uma poção e recuperou 20 de vida!")
        else:
            print(f"{self.nome} não tem mais poções!")

    def esta_vivo(self):
        return self.vida > 0


