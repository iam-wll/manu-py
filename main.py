# print("ola mundo") 

# nome = "joão" 
# variavel que recebe o valor do input
# senha = input("digite uma senha: ")

# if senha == "abobora":
#     print("senha correta!!")

# elif senha == "chevette":
#     print("senha correta")

# else: 
#     print("senha incorreta")

print ("bem vindo a o bot da manu ;p" )
opcao = input("digite um valor de 1 a1 10: ")

match opcao:
    case "1":
        print("falar com atedente...")
        print("qual atendente voce deseja falar? SAC ou RH")
        atendente = input("digite o atendimento desejado: ")

        if atendente == "sac":
            print("voce foi direcionado ao SAC")

        elif atendente == "RH":
            print("voce foi direcionado ao RH") 

        else:
            print("esse atendimento nao existe")
    
    case "2":
        print("segunda via do boleto")
        print("falar com atndente ")
        print("deseja qual boleto ")
        boleto = input("digite o qual o boleto deseja pagar conta de gaz ou internet")

        if boleto == "conta de gaz":
            print("a conta ja foi paga boleto empresso")

        elif boleto == "a conta de internet":
            print ("a conta ja foi paga boleto empresso")

        else:
            ("essa conta nao foi registrada")

    case "4":
        print("imprimir boletin")
        print("entregar boletin ")
        print("deseja qual o boletin")
        boleto = input("digite qual o boletin o senhor deseja, o de extas ou humanas")

        if boleto == "boletin de exatas":
            print("imprimir boletin ")

        elif boleto == "boletin de humanas":
            print("imprimir boletin ")
        else:
            print ("esse boletin ja foi entregue")
    case "5":
        print("quero reenbolso")
        print("reembolsar volor")
        print("qual o valor deseja reembolsar 100? ou 500? ")
        reembolso = input("digite qual o valor de 100 exatos ou 500") 

        if reembolso == "volor de 100":
            print("valor reembolsado")

        elif reembolso == "valor de 500":
            print("valor reembolsado")

        else:
            print("esse valor nao foi registrado")

    case "6":
        print("pagamento")
        print("credito")
        print("debito ou credito")
        pagamento = input("qual o tipo de pagmento o senhor deseja debito ou credito?")

        if pagamento == "debito":
            print ("transação aceita")

        elif pagamento == "credito":
            print ("transação aceita")

        else:
            print ("nao aceitamos esse tipo de pagamento")

    case "7":
        print("voce pratica algun esporte")
        print("sim, pratico")
        print("a vezes sim")
        esporte = input("qual esporte vc pratica velei e baskete")

        if esporte == "baskete":
            print("que bom isso faz bem")

        elif esporte == "volei":
            print("quem bom isso faz bem")

        else:
            print("nao faço nenhum esporte ")

    case "8":
        print (" voce assite anime ")
        print ("assisto filme ")
        print ("assito so na tomato")
        anime = input ("mas voce assite anime bom? ")

        if anime == ("sim"):
            print("pare de assistir")
        elif anime == ("nao"):
            print("entao comece a assistir")
        else:
            print("assisto apenas filme")

    case "9":
        print ("voce vai ao cinema")
        print("sim, assiste um filme ")
        print("nao, nao curto cinema")
        cinema = input("o filme é bom? ")

        if cinema == ("sim"):
            print ("o filme é bom?")

        elif cinema == ("que dahora"):
            print("oloko qual =?")

        else:  
            print("nao")

    case _:
            print("não existe essa opção, digite um numero de 1 a 9")