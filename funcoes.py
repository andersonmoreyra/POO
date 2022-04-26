import classe_Lojas
import classe_Clientes


#Inserindo lojas e quantidades de bicicletas
loja_1 = classe_Lojas.Lojas('Rent a Bike', 20)
loja_2 = classe_Lojas.Lojas('Duas Rodas', 25)
loja_3 = classe_Lojas.Lojas('Pedala Felicidade ', 5)

cliente_1 = classe_Clientes.cliente('Anderson', 40)
cliente_2 = classe_Clientes.cliente('Daniele', 36)
cliente_3 = classe_Clientes.cliente('Lorena', 6)
cliente_4 = classe_Clientes.cliente('Rebeca', 4)

aluguel_loja_01= []
aluguel_loja_02= []
aluguel_loja_03= []

#print(loja_1.__dict__)
#print(loja_2.__dict__)
#print(loja_3.__dict__)

#Ver bicicletas disponiveis nas lojas
def lojas_disponibilidade():
    print(loja_1.__dict__)
    print(loja_2.__dict__)
    print(loja_3.__dict__)

def loja_disponibilidade():
    aux = input('Qual numero da Loja (1,2,3): ')
    if aux == '1':
        print(loja_1.__dict__)
    if aux == '2':
        print(loja_2.__dict__)
    if aux == '3':
        print(loja_3.__dict__)

#estoque_loja = lojas_disponibilidade()
#loja_estoque = loja_disponibilidade()

def aluguel_hora(cliente, horas = None):
        loja = input('Alugar da loja (1,2,3): ')
        if loja == '1':
            dic_aux = {'cliente':cliente , 'horas': horas, 'valor': horas*5}
            aluguel_loja_01.append(dic_aux)
            loja_1.qtd_bicicletas -= 1
        if loja == '2':
            dic_aux = {'cliente':cliente , 'horas': horas, 'valor': horas*5}
            aluguel_loja_01.append(dic_aux)
            loja_1.qtd_bicicletas -= 1
        if loja == '2':
            dic_aux = {'cliente':cliente , 'horas': horas, 'valor': horas*5}
            aluguel_loja_01.append(dic_aux)
            loja_1.qtd_bicicletas -= 1


alugar = aluguel_hora('Carlos', 4)
print(aluguel_loja_01)
print(loja_1.__dict__)

