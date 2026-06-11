from FichaPratica04.Inimigo import Inimigo
from FichaPratica04.Jogador import Jogador
from FichaPratica04.Loja import Loja
from FichaPratica04.Masmorra import Masmorra
from FichaPratica04.Recursos import Recursos


class Jogo:
    def __init__(self):
        self.__jogador = None
        self.__masmorraAtual = 1
        self.__inimigoAtual = None
        self.__loja = Loja()
        self.__terminado = False

    def getJogador(self):
        return self.__jogador

    def getMasmorraAtual(self):
        return self.__masmorraAtual

    def getInimigoAtual(self):
        return self.__inimigoAtual

    def getLoja(self):
        return self.__loja

    def getTerminado(self):
        return self.__terminado

    def setJogador(self, jogador):
        self.__jogador = jogador

    def setMasmorraAtual(self, masmorraAtual):
        self.__masmorraAtual = masmorraAtual

    def setInimigoAtual(self, inimigoAtual):
        self.__inimigoAtual = inimigoAtual

    def setLoja(self, loja):
        self.__loja = loja

    def setTerminado(self, terminado):
        self.__terminado = terminado

    def iniciarJogo(self):
        self.mostrarIntroducao()

        nome = input("\nInsere o nome da tua personagem: ")

        if nome == "":
            nome = "Joaquim"
            print("Não escreveste nome. O sistema medieval atribuiu-te um nome altamente épico:")
            print("Joaquim.")

        self.criarJogador(nome)

        while self.__terminado is False:
            self.mostrarMenuPrincipal()
            opcao = input("Escolha: ")

            Recursos.limparConsola()

            if opcao == "1":
                self.__jogador.mostrarEstado()

            elif opcao == "2":
                self.explorarMasmorra()

            elif opcao == "3":
                self.visitarLoja()

            elif opcao == "4":
                self.descansar()

            elif opcao == "5":
                print("\nDecidiste sair do jogo.")
                print("A máquina do tempo fica para outro dia.")
                print("O ano 1272 agradece a tua curta visita.")
                self.__terminado = True

            else:
                print("\nOpção inválida.")
                print("Até no ano 1272 era esperado saber escolher uma opção do menu.")

    def mostrarIntroducao(self):
        Recursos.limparConsola()
        Recursos.tocarAudio("assets/audio/intro.wav")
        Recursos.imprimirAscii(
            "assets/ascii/logo.txt",
            """
    ======================================
               CYBERDUNGEONS
    ======================================
            """
        )

        Recursos.pausa(1)

        print("\nAno 2077.")
        Recursos.pausa(1)
        print("A humanidade finalmente conseguiu viajar no tempo.")
        Recursos.pausa(1)
        print("Infelizmente, alguém decidiu testar a máquina numa sexta-feira à tarde.")
        Recursos.pausa(1)
        print("Como seria de esperar, correu mal.")
        print()
        Recursos.pausa(1)
        print("Durante a viagem, ocorreu uma ruptura temporal.")
        print("A tua personagem foi enviada para o ano 1272.")
        print("Sem internet. Sem GPS. Sem carregador. Sem garantias.")
        print()
        Recursos.pausa(1)
        print("A máquina do tempo caiu algures no fundo de várias masmorras medievais.")
        print("Para regressares ao ano 2077, tens de sobreviver, lutar e recuperar o núcleo temporal.")
        print()
        Recursos.pausa(1)
        print("Bem-vindo a Cyberdungeons.")
        print("Um RPG medieval com problemas tecnológicos que ninguém pediu.")

    def criarJogador(self, nome):
        # TODO:
        # O aluno pode alterar os atributos iniciais do jogador.
        #
        # Sugestão:
        # - vidaMaxima: vida inicial e limite máximo de vida
        # - ataque: ataque base
        # - defesa: defesa base
        # - nivel: nível inicial
        # - experiencia: experiência inicial
        # - moedas: moedas iniciais

        vidaMaxima = 100
        ataque = 10
        defesa = 5
        nivel = 1
        experiencia = 0
        moedas = 40

        self.__jogador = Jogador(nome, vidaMaxima, ataque, defesa, nivel, experiencia, moedas)

        print("\nPersonagem criada com sucesso.")
        print("Nome:", nome)
        print("Ano de origem: 2077")
        print("Ano atual: 1272")
        print("Estado emocional: confuso, mas funcional.")

    def mostrarMenuPrincipal(self):
        Recursos.limparConsola()
        print("\n===== MENU PRINCIPAL =====")
        print("Masmorra atual:", self.__masmorraAtual)
        print("1 - Ver estado do jogador")
        print("2 - Explorar masmorra")
        print("3 - Visitar loja")
        print("4 - Descansar")
        print("5 - Sair")

    def criarMasmorraAtual(self):
        # TODO:
        # O aluno pode alterar os atributos de cada masmorra.

        if self.__masmorraAtual == 1:
            return Masmorra(
                1,
                "Masmorra da Floresta Perdida",
                "Uma floresta húmida onde até as árvores parecem julgar as tuas escolhas."
            )

        elif self.__masmorraAtual == 2:
            return Masmorra(
                2,
                "Cripta dos Ecos Temporais",
                "Uma cripta onde se ouvem vozes do passado, do futuro e de alunos a perguntar se isto sai no teste."
            )

        elif self.__masmorraAtual == 3:
            return Masmorra(
                3,
                "Fortaleza do Gelo Eterno",
                "Uma fortaleza gelada. O frio é tanto que até os bugs congelam."
            )

        elif self.__masmorraAtual == 4:
            return Masmorra(
                4,
                "Templo da Fenda Temporal",
                "Um templo instável onde ontem, hoje e amanhã discutem quando é que se assinam as folhas."
            )

        else:
            return Masmorra(
                5,
                "Câmara da Máquina do Tempo",
                "A última masmorra. A máquina está perto. O Wi-Fi ainda não."
            )

    def criarInimigoDaMasmorra(self):
        # TODO:
        # O aluno pode alterar os atributos dos inimigos.
        #
        # Cada inimigo deve ter:
        # nome, vida, ataque, defesa, experiencia, moedas
        #
        # Não usar listas de objetos.

        if self.__masmorraAtual == 1:
            return Inimigo("Dar nome ao inimigo 1", 30, 7, 2, 20, 15)

        elif self.__masmorraAtual == 2:
            return Inimigo("Dar nome ao inimigo 2", 45, 10, 4, 30, 25)

        elif self.__masmorraAtual == 3:
            return Inimigo("Dar nome ao inimigo 3", 65, 13, 6, 45, 35)

        elif self.__masmorraAtual == 4:
            return Inimigo("Dar nome ao inimigo 4", 85, 17, 8, 60, 50)

        else:
            return Inimigo("Dar nome ao inimigo 5", 120, 22, 12, 100, 100)

    def explorarMasmorra(self):
        masmorra = self.criarMasmorraAtual()
        self.__inimigoAtual = self.criarInimigoDaMasmorra()

        masmorra.mostrarInfo()

        print("\nAo entrares, sentes uma energia estranha no ar.")
        print("O teu relógio futurista mostra a seguinte mensagem:")
        print('"Erro 1272: realidade medieval não suportada."')

        print("\nUm inimigo apareceu!")
        print("Inimigo:", self.__inimigoAtual.getNome())

        self.iniciarCombate()

    def iniciarCombate(self):
        # TODO:
        # Implementar o ciclo de combate.
        #
        # Durante o combate, o jogador deve poder:
        # 1 - Atacar
        # 2 - Usar poção
        # 3 - Ver estado
        # 4 - Fugir
        #
        # Regras esperadas:
        # - Se o jogador atacar, o inimigo recebe dano.
        # - Se o inimigo continuar vivo, ataca o jogador.
        # - Se o inimigo morrer, chamar processarVitoria().
        # - Se o jogador morrer, chamar processarDerrota().
        # - Se o jogador fugir, terminar o combate sem recompensa.

        print("\n===== COMBATE =====")
        print("[TODO] O sistema de combate ainda não foi implementado.")
        print("Neste momento, tu e o inimigo ficam a olhar um para o outro.")
        print("É constrangedor, mas pelo menos o programa não dá erro.")

    def processarVitoria(self):
        # TODO:
        # 1. Mostrar mensagem de vitória.
        # 2. Dar experiência ao jogador.
        # 3. Dar moedas ao jogador.
        # 4. Verificar se o jogador subiu de nível.
        # 5. Se a masmorra atual for a última, terminar o jogo com vitória.
        # 6. Caso contrário, avançar para a próxima masmorra.

        print("[TODO] O método processarVitoria() ainda não foi implementado.")

    def processarDerrota(self):
        # TODO:
        # 1. Mostrar mensagem de derrota.
        # 2. Alterar o estado do jogo para terminado.

        print("[TODO] O método processarDerrota() ainda não foi implementado.")

    def avancarMasmorra(self):
        # TODO:
        # 1. Aumentar o número da masmorra atual.
        # 2. Garantir que não ultrapassa a última masmorra.
        # 3. Mostrar mensagem de avanço.

        print("[TODO] O método avancarMasmorra() ainda não foi implementado.")

    def visitarLoja(self):
        self.__loja.gerarProdutos(self.__masmorraAtual)
        self.__loja.mostrarProdutos()

        print("\n===== MENU DA LOJA =====")
        print("1 - Comprar arma")
        print("2 - Comprar armadura")
        print("3 - Comprar poção")
        print("4 - Sair da loja")

        opcao = input("Escolha: ")

        if opcao == "1":
            self.__loja.comprarArma(self.__jogador)

        elif opcao == "2":
            self.__loja.comprarArmadura(self.__jogador)

        elif opcao == "3":
            self.__loja.comprarPocao(self.__jogador)

        elif opcao == "4":
            print("\nSaíste da loja.")
            print("O ferreiro grita: 'Volta sempre! E traz moedas, não aceitamos MB Way!'")

        else:
            print("\nOpção inválida na loja.")
            print("O ferreiro suspira medievalmente.")

    def descansar(self):
        # TODO:
        # 1. Definir um valor de recuperação.
        # 2. Chamar o método curar() do jogador.
        # 3. Mostrar uma mensagem adequada.
        #
        # Sugestão:
        # O descanso pode recuperar 25 pontos de vida.

        print("\n[TODO] O método descansar() ainda não foi implementado.")
        print("Tentaste dormir, mas lembraste-te que estás no ano 1272.")
        print("A almofada é uma pedra. O cobertor é outra pedra.")

    def verificarFimDoJogo(self):
        # TODO:
        # Este método pode ser usado para verificar se o jogo terminou.
        # Por exemplo:
        # - jogador morreu
        # - boss final foi derrotado
        # - máquina do tempo foi recuperada

        return self.__terminado
