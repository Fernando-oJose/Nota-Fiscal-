class Produto:
    def __init__(self, codigo, descricao, precoUnitario):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__precoUnitario = precoUnitario

    def getCodigo(self):
        return self.__codigo
    
    def getDescricao(self):
        return self.__descricao

    def getPrecoUnitario(self):
        return self.__precoUnitario

    
class NotaFiscal:
    def __init__(self, nroNF, nomeCliente, itensNF):
        self.__nroNF = nroNF
        self.__nomeCliente = nomeCliente
        self.__itensNF = []
        self.__valorTotalNota = 0

    def getNroNF(self):
        return self.__nroNF

    def getNomeCliente(self):
        return self.__nomeCliente

    def getItensNF(self):
        return self.__itensNF
    
    #preciso passar o estoque pq senão não consigo atualiza-lo
    def addProdutos(self, produto, qtde, estoque):
        if produto.getCodigo() not in estoque or qtde > estoq[produto.getCodigo()]:
            print('Produto não inserido')
            print()
        else:
            self.__itensNF.append([produto, qtde])
            valorTotal_produto = produto.getPrecoUnitario() * qtde
            #atualizar o estoque
            estoque[produto.getCodigo()] = estoque[produto.getCodigo()] - qtde
            #para atualizar o valor da nota
            self.__valorTotalNota += valorTotal_produto
    
    def printDescricao(self):
        print('Número da nota: {} Nome do cliente: {} '.format(self.__nroNF, self.__nomeCliente))
        print()
        for it in self.__itensNF:
            print('Produto: {} Preço: {} Quantidade vendida: {}'.format(it[0].getDescricao(), it[0].getPrecoUnitario(), it[1]))
            print()
        print('Valor total da nota: {}'.format(self.__valorTotalNota))

        
if __name__ == "__main__":
    p1 = Produto(101, "Calca jeans", 99)
    p2 = Produto(102, "Calca moletom", 59)
    p3 = Produto(103, "Camisa", 39)
    p4 = Produto(104, "Camisa botão", 109)
    p5 = Produto(105, "Casaco couro", 299)
    p6 = Produto(106, "Chinelo", 19)

    listaProdutos = []
    listaProdutos = [p1, p2, p3, p4, p5, p6]

    estoq = {}
    estoq[p1.getCodigo()] = 5
    estoq[p2.getCodigo()] = 1
    estoq[p3.getCodigo()] = 2
    estoq[p4.getCodigo()] = 92
    estoq[p5.getCodigo()] = 12
    estoq[p6.getCodigo()] = 20
    
    
    itens_nota = []
    n1 = NotaFiscal(1, 'Marcio', itens_nota)

    #todos os produtos que eu quero adicionar
    produtos_add = []
    produtos_add = [p1, p2, p4]

    n1.addProdutos(p1, 3, estoq)
    n1.addProdutos(p2, 2, estoq)
    n1.addProdutos(p4, 32, estoq)

    queria_add = len(produtos_add)
    tamanho_nota = len(n1.getItensNF())

    if tamanho_nota == 0:
        print()
        print('Nota fiscal não criada')
        print()
    
    elif tamanho_nota > 0 and tamanho_nota < queria_add:
        print()
        print('Nota fiscal criada parcialmente')
        n1.printDescricao()
        print()
    
    else:
        print() 
        print('Nota fiscal criada com sucesso')
        print()
        n1.printDescricao()
        print()




  

    

    

    
