class NPC:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, jogador):
        print(f"{self.nome} atacou {jogador.nome} e causou {self.ataque} de dano!")
        jogador.receber_dano(self.ataque)

    def receber_dano(self, dano):
        self.vida -= dano

        if self.vida < 0:
            self.vida = 0

        print(f"{self.nome} recebeu {dano} de dano. Vida atual: {self.vida}")

    def esta_vivo(self):
        return self.vida > 0