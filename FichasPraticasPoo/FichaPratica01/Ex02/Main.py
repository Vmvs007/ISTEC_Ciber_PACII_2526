from FichaPratica01.Ex02.Edificio import Edificio

edificio1 = Edificio("Edifício do Sol", "Rua da Liberdade", "Porto", "Azul", 4, True)
edificio2 = Edificio("Edifício Capital", "Rua das Flores", "Braga", "Branca", 8, False)

print(f"{edificio1.getNome()} | {edificio1.getRua()} | {edificio1.getCorFachada()}")

edificio1.setCorFachada("Amarelo")

print(f"{edificio1.getNome()} | {edificio1.getRua()} | {edificio1.getCorFachada()}")
