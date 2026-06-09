from FichaPratica01.DemonstracaoRPG.Jogador import Jogador
from FichaPratica01.DemonstracaoRPG.NPC import NPC

# Programa principal

startFile = open('../../Files/rpg_start.txt', 'r')
file_contents = startFile.read()
print (file_contents)
startFile.close()

print("\n\n")

criarPersonagemFile = open('../../Files/rpg_criar_personagem.txt', 'r')
file_contents = criarPersonagemFile.read()
print (file_contents)
criarPersonagemFile.close()

print("\n\n")

nomeInput = input("Insira o seu nome: ")

jogador = Jogador(nomeInput, 100, 15, 3)
inimigo1 = NPC("Goblin", 20, 10)
inimigo2 = NPC("Esqueleto", 50, 30)

print("\n=== MINI RPG ===")
print(f"Um {inimigo1.nome} apareceu!")
print(f"Um {inimigo2.nome} apareceu!")

while jogador.esta_vivo() and (inimigo1.esta_vivo() or inimigo2.esta_vivo()):

    print("\n--- Estado Atual ---")
    print(f"{jogador.nome} | Vida: {jogador.vida} | Poções: {jogador.pocoes}")
    print(f"{inimigo1.nome} | Vida: {inimigo1.vida}")
    print(f"{inimigo2.nome} | Vida: {inimigo2.vida}")

    print("\nEscolhe uma ação:")
    print(f"1 - Atacar {inimigo1.nome}")
    print(f"2 - Atacar {inimigo2.nome}")
    print("3 - Usar poção")

    opcao = input("Opção: ")

    if opcao == "1":
        if inimigo1.esta_vivo():
            jogador.atacar(inimigo1)
        else:
            print(f"O {inimigo1.nome} já estava morto. Desperdiçaste a vez!")
    elif opcao == "2":
        jogador.atacar(inimigo2)
    elif opcao == "3":
        jogador.usar_pocao()
    else:
        print("Opção inválida. Perdeste a vez!")

    if inimigo1.esta_vivo():
        print()
        inimigo1.atacar(jogador)

    if inimigo2.esta_vivo():
        print()
        inimigo2.atacar(jogador)


print("\n=== FIM DO JOGO ===")

if jogador.esta_vivo():
    print(f"Parabéns! Derrotaste o {inimigo1.nome} e {inimigo2.nome}!")
else:
    print(f"Foste derrotado pelo {inimigo1.nome} e {inimigo2.nome}...")