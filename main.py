#NOTE: Criar uma classe 
#Usar PascalCase (CarroDeRally). (diferente da snake_case (carro_grande) das variaveis)
#tem 2 elementos: atributos e metodos
#atributos: caracteristicas
#metodos: acoes, uma funcao, usa snake_case e usar nomes no infinitivo(verbo). 
# Se um metodo de uma classe nao receber parametros é mentira pois sempre recebe parametros(em python), se nao tiver nada, pode ou nao ter retorno
#'self' se refere aos atributos da classe, funcoes sempre recebe o self
#instanciar a classe(criar um objeto, pense como se fosse uma pessoa, é a mesma coisa de uma pessoa nascer)

#pode ser feito tudo dentro de um arquivo, o programa todo num arquivo só, classes, funcoes, codigos 

class Carro:
    #atributos
    fabricante  = 'Volkswagem'
    modelo      = 'Gol'
    ano         = '2000' #ano de fabricacao coloca em string
    cor         = 'Vermelho'
    placa       = 'ABC-1234'

    #metodos
    def ligar(self,ignicao):
        if ignicao:
            return f'{self.modelo} está ligado.'
        else:
            return f'{self.modelo} está desligado.' 

if __name__ == '__main__': #programa principal, __main__ é para que nao consiga incorporar o programa principal para outro lugar
    #instanciar a classe
    meu_carro = Carro()

    #exibir atributos do objeto
    print(f'Fabricante: {meu_carro.fabricante}')
    print(f'Modelo: {meu_carro.modelo}')
    print(f'Ano de fabricação: {meu_carro.ano}')
    print(f'Cor do carro: {meu_carro.cor}')
    print(f'Placa de carro: {meu_carro.placa}')
    
    #ligar (ou nao) o carro
    ligar_carro = True

    #chamo o metodo do objeto
    print(meu_carro.ligar(ligar_carro)) 

