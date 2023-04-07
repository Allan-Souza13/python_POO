def cria_conta(numero,titular,saldo,limite):
    conta = {"numero": numero, "titular": titular,"saldo":saldo,"limite":limite}
    return conta

#Colocar no Python console: from (nome da pasta) import criar_conta(nome da função)
#conta = cria_conta(123, "Allan,500.0,1000.0)
#conta["numero]

#-----#
def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor


def extrato(conta):
    print("saldo é {}".format(conta["saldo"]))
#from testeoo import cria_conta,deposita,saca,extrato
#conta = cria_conta(123,"Allan",500.0,1000.0)
#deposita(conta,40.0)
#extrato(conta)
#saldo é 540.0
#saca(conta,20)
#extrato(conta)
#------------------------------#