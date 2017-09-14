#Inicia entrada de dados pelo usuário
valor = float(input("Digite um número: "))
#Monta o menu de seleções
print("Selecione uma das opções abaixo: ")
print("1. Converter para escala Celsius (ºC)")
print("2. Converter para escala Farenheit (ºF)")
#Recebe o valor selecionado no menu anterior
opcao = int(input(("Digite o número de uma opção acima: ")))
#Checa se a opção 1 foi selecionada
if opcao == 1:
#Realiza a conversão do valor digitado para ºC
    C = (valor - 32) / 1.8
#Escreve na tela o resultado
    print("Temperatura na escala Celsius (ºC) ", C)
#Senão checa se a opção 2 foi selecionada
elif opcao == 2:
#Realiza a conversão do valor digitado para ºF
    F = round(((1.8 * valor) + 32),2)
#Escreve na tela o resultado
    print("Temperatura na escala Farenheit (ºF) ", F)
#Se nenhuma das 2 condições acimas forem satisfeitas, imprime na tela a mensagem de erro e encerra o programa
else:
    print("Valor inválido")
