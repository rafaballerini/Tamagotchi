class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 20
        self.saude = 80
        self.idade = 1
    def AlterarNome(self, novoNome):
        self.nome = novoNome
    def AlterarFome(self, valorF):
        self.fome += valorF
        if self.fome > 100:
            self.fome = 100
        elif self.fome < 0:
            self.fome = 0
    def AlterarSaude(self, valorS):
        self.saude += valorS
        if self.saude > 100:
            self.saude = 100
        elif self.saude < 0:
            self.saude = 0
    def AlterarIdade(self):
        self.idade += 1
    def RetornarNome(self):
        return self.nome
    def RetornarFome(self):
        return self.fome
    def RetornarSaude(self):
        return self.saude
    def RetornarIdade(self):
        return self.idade
    def RetornarHumor(self):
        humor = self.saude + self.fome 
        return humor
    def retornar_visao_geral(self):
        print('------------------ VISÃO GERAL ------------------')
        print(f'Fome: {self.fome}\nHumor: {self.saude + self.fome}\nSaúde: {self.saude}')
        print('------------------------------------')

def solicitarAcao(Bichinho):
    acoes = ['Alimentar (-10 de fome)', 'Dormir (+10 de saúde)', 'Alterar nome', 'Visualizar humor', 'Visualizar idade', 'Visualizar fome', 'Visualizar saúde']
    
    Bichinho.retornar_visao_geral()

    for indice, acao in enumerate(acoes):
        print(f'{indice + 1}.', acao)

    while True:
        try:
            resposta = int(input('\nResposta: '))
        except ValueError:
            print('Informe um número inteiro!')
            continue

        if resposta == 1:
            Bichinho.AlterarFome(-10)
            print("-10 de fome! Obrigado!")
        elif resposta == 2:
            Bichinho.AlterarSaude(+10)
            print("+10 de saúde! Obrigado!")
        elif resposta == 3:
            nome2 = input('Qual nome deseja colocar? \n')
            Bichinho.AlterarNome(nome2)
        elif resposta == 4:
            print("Humor: ", Bichinho.RetornarHumor())
        elif resposta == 5:
            print("Idade: ", Bichinho.RetornarIdade())
        elif resposta == 6:
            print("Fome: ", Bichinho.RetornarFome())
        elif resposta == 7:
            print("Saude: ", Bichinho.RetornarSaude())
        else:
            print('Escolha um número válido!')
            continue

        return Bichinho;

nomeBichinho = input('Qual o nome que deseja colocar no seu bichinho? ')
Bichinho = BichinhoVirtual(nome = nomeBichinho)

Bichinho.AlterarFome(+2)
Bichinho.AlterarSaude(-2)

while (Bichinho.saude > 0) and (Bichinho.fome < 100):
    Bichinho.AlterarIdade()

    print("""\n------------------------------------------\n __         __
/  \.-" "-./  \.
\    -   -    /
 |   o   o   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---`
     \n""")

    print(f'Olá meu nome é {Bichinho.nome}. O que você deseja fazer comigo agora?\n')

    Bichinho = solicitarAcao(Bichinho)
else:
    print("""\n------------------------------------------\n __         __
/  \.-" "-./  \.
\    -   -    /
 |   X   X   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---`\nVocê me deixou morrer!\n""")