class BichinhoVirtual:
    def __init__(self, nome):
        self.__nome = nome
        self.__fome = 20
        self.__saude = 80
        self.__idade = 1

    @property
    def nome(self):
        return self.__nome

    @property
    def saude(self):
        return self.__saude

    @property
    def fome(self):
        return self.__fome

    def alterar_nome(self, nome):
        self.__nome = nome

    def alterar_fome(self, valor_f):
        self.__fome += valor_f
        if self.__fome > 100:
            self.__fome = 100
        elif self.__fome < 0:
            self.__fome = 0

    def alterar_saude(self, valor_s):
        self.__saude += valor_s
        if self.__saude > 100:
            self.__saude = 100
        elif self.__saude < 0:
            self.__saude = 0

    def alterar_idade(self):
        self.__idade += 1

    def retornar_nome(self):
        return self.__nome

    def retornar_fome(self):
        return self.__fome

    def retornar_saude(self):
        return self.__saude

    def retornar_idade(self):
        return self.__idade

    def retornar_humor(self):
        humor = self.__saude + self.__fome
        return humor


nome_inicial = input('Qual o nome que deseja colocar no seu bichinho? ')
Bichinho = BichinhoVirtual(nome=nome_inicial)

while (Bichinho.saude > 0) and (Bichinho.fome < 100):
    Bichinho.alterar_fome(+2)
    Bichinho.alterar_saude(-2)
    Bichinho.alterar_idade()
    resposta = input(f"""\n------------------------------------------\n __         __
/  \.-" "-./  \.
\    -   -    /
 |   o   o   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---`
\nOlá meu nome é {Bichinho.nome}. O que você deseja fazer comigo agora?
1- Alimentar (-10 de fome)
2- Dormir (+10 de saúde)
3- Alterar nome
4- Visualizar humor
5- Visualizar idade
6- Visualizar fome
7- Visualizar saúde
Resposta: """)

    print('\n')

    if resposta == '1':
        Bichinho.alterar_fome(-10)
        print("-10 de fome! Obrigado!")
    elif resposta == '2':
        Bichinho.alterar_saude(+10)
        print("+10 de saúde! Obrigado!")
    elif resposta == '3':
        nome_novo = input('Qual nome deseja colocar? \n')
        Bichinho.alterar_nome(nome_novo)
    elif resposta == '4':
        print("Humor: ", Bichinho.retornar_humor())
    elif resposta == '5':
        print("Idade: ", Bichinho.retornar_idade())
    elif resposta == '6':
        print("Fome: ", Bichinho.retornar_fome())
    elif resposta == '7':
        print("Saude: ", Bichinho.retornar_saude())
    else:
        print('Escolha um número válido!')
else:
    print("""\n------------------------------------------\n __         __
/  \.-" "-./  \.
\    -   -    /
 |   X   X   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---`\nVocê me deixou morrer!\n""")
