# Função para criptografar um texto com base em um deslocamento específico
def criptografar(texto, deslocamento):
    print('cript')  # Indica que a função está criptografando
    alfa1 = 'abcdefghijklmnopqrstuvwxyzàáãâéêẽèóòôõìîĩíúùûũç!?*#$%&*+=-_/@'  # Define o alfabeto 1
    resultado = ''  # Inicializa o resultado como uma sequência vazia

    for caractere in texto:
        if caractere in alfa1:  # Verifica se o caractere está no alfabeto
            indice = alfa1.find(caractere)  # Encontra a posição do caractere no alfabeto
            indice = (indice + deslocamento) % len(alfa1)  # Calcula a nova posição com base no deslocamento
            resultado += alfa1[indice]  # Adiciona o caractere criptografado ao resultado
        else:
            resultado += caractere  # Se não for uma letra, mantém o caractere original
    return resultado  # Retorna o texto criptografado


def decriptografar(texto, deslocamento):
    print('decript')  # Indica que a função está descriptografando
    alfa2 = 'abcdefghijklmnopqrstuvwxyzàáãâéêẽèóòôõìîĩíúùûũç!?*#$%&*+=-_/@'  # Define o alfabeto 2
    resultado = ''  

    for caractere in texto:
        if caractere in alfa2:  
            indice = alfa2.find(caractere)  
            indice = (indice - deslocamento) % len(alfa2)  # Calcula a nova posição para descriptografar
            resultado += alfa2[indice] 
        else:
            resultado += caractere  
    return resultado  # Retorna o texto descriptografado

while True: # Loop principal que executa o programa até que o usuário escolha sair
    print('Escolha uma Opção: ')
    print('1 - Cript')
    print('2 - Decript')
    print('0 - Sair')
    menu = input() # Solicita ao usuário que escolha uma opção do menu e aguarda a entrada

    if menu == '1' or menu == '2': # Verifica se o usuário escolheu a opção de criptografar ou descriptografar

        mensagem = input('Escreva sua mensagem: ').lower()  # Solicita a mensagem do usuário e a converte em minúsculas
        deslocamento = int(input('Digite um número entre 1 e 61: '))  # Solicita o deslocamento

        if 1 <= deslocamento <= 61:  # Verifica se o deslocamento está no intervalo permitido
            if menu == '1':
                mensagem_criptografada = criptografar(mensagem, deslocamento)  # Chama a função de criptografia
                print(f'Mensagem criptografada: {mensagem_criptografada}') # Imprime a mensagem criptografada junto com o texto fixo

            else:
                mensagem_decriptografada = decriptografar(mensagem, deslocamento)  # Chama a função de descriptografia
                print(f'Mensagem decriptografada: {mensagem_decriptografada}')  # Imprime a mensagem decriptografada junto com o texto fixo
        else:
            print('Por favor, insira um valor entre 1 e 61.')  # Mensagem de erro para deslocamento inválido
    elif menu == '0':
        print('Encerrando....')  # Mensagem de saída do programa
        break #Sai do loop principal e encerra o programa
    else:
        print('Opção Inválida')  # Mensagem de erro para opção inválida