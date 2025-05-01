#Codigo Ruim 

class Relatorio: 
    def gravar_relatorio(self):
        print("Gerando um relatorio...")
    def enviar_email(self):
        print("Enviando e-mail...")

#Codigo bom

class GerandoRelatorio:
     def gravar_relatorio(self):
        print("Gerando um relatorio...")
class EnviandoEmail:
    def enviar_email(self):
        print("Enviando e-mail...")