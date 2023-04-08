#Para criar uma instância, é obrigatório preencher os valores de todos os atributos.

#receita de bolo
class Conta:

    def __init__(self,numero,titular,saldo,limite):#função construtora, que constroe o objeto/inicialização
        print("Construindo objeto...{}".format(self))#self é a referença desse objeto que guardou o endereço
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("saldo de {} do titular {} ".format(self.saldo,self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor


