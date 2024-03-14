
 #primeiro criamos a variavel do nome do arquivo para então pedir que o programa leia em "rb' para ler em binario 
import sys
try:
    arqname =(input("diretorio do arquivo junto de seu nome e sua extensão e origem OBS: caso esteja executando este programa na pasta do seu arquivo desejado n é necessario seu caminho completo  "))
    
    if not arqname:
        sys.exit("nada foi digitado")

    ##aqui criamos o arquivo e pede se o conteudo do arquivo em lista 
    with open(arqname,"rb") as arquivo:
        conteudo=list(arquivo.read())

    x = 0
    p = input("digite a palavra passe desejada:")
    ##aqui atualizasse a variavel em p  com ord para fazer uma lista de inteiros 
    p = [ord(l) for l in p]



    ##aqui é feita a operação XOR para se codificar os dados ja que transformamos "conteudo" e "p" em uma lista de inteiros a operação fica mais facil de ser aplicada
    for i in range(len(conteudo)):
        conteudo[i] = conteudo[i] ^ p[x]
        x=x+1
        if x==len(p):
            x=0

    ##aqui transformamos o resultados em bytes para depois salvar o novo arquivo         
    resultado = bytes(conteudo)

   
    arquivo_salvo = input("escolha o nome,diretorio  e adicione a extensão do seu arquivo criptografado :")
    

    ##aqui se faz um if para verificar se o nome do novo arquivo n é igual a o antigo  se o nome não for igual o novo arquivo é gerado 
    if not arquivo_salvo:
        sys.exit('voce não digitou o nome do seu arquivo')
    if arquivo_salvo == arqname:
        sys.exit('este nome ja é o do arquivo original  isso ira sobreescrever os seus dados a operação n pode ser concluida')
    if arquivo_salvo and arquivo_salvo != arqname:
        with open(arquivo_salvo,"wb") as novoarquivo:
            novoarquivo.write(resultado)
except FileNotFoundError:
    print('o arquivo não foi encontrado ')







