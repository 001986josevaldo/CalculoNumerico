# Função para encontrar a raiz de f(x) = x^2 - 4
import os
import os

# Função para encontrar a raiz de f(x) = x^2 - 4
def funcao(x):
    return x**2 - 4  # Para encontrar a raiz de x^2 - 4 = 0 (raiz quadrada de 4)

def encontrar_raiz(f, a, b, tol=1e-6, nmax=100):
    N = 1
    tabela = []  # Lista para armazenar os valores da tabela
    while N <= nmax:
        fa = f(a)
        fb = f(b)
        xbarra = (a * fb - b * fa) / (fb - fa)
        fxbarra = f(xbarra)
        tabela.append((N, a, fa, b, fb, xbarra, fxbarra))  # Adiciona os valores atuais à tabela
        if abs(fxbarra) < tol:
            return xbarra, tabela
        N += 1
        if fxbarra * fa > 0:
            a = xbarra
        else:
            b = xbarra
    return "O algoritmo falhou.", tabela

# Função para inserir o intervalo inicial
def inserirIntervalo():
    a = float(input("Digite o valor do intervalo a: "))
    b = float(input("Digite o valor do intervalo b: "))
    print('A = ', a, '\nB = ', b)
    return a, b

# Função para salvar os resultados em um arquivo
def salvar_resultados(nome_arquivo, raiz, tabela, a, b):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write("Ponto inicial: {}\n".format(a))
        arquivo.write("Ponto final: {}\n".format(b))
        arquivo.write("A raiz é: {}\n".format(raiz))
        arquivo.write("\nTabela de Iterações:\n")
        arquivo.write("-----------------------------------------------------------------\n")
        arquivo.write("|  N  |    a        |   f(a)      |    b        |   f(b)      |    c        |   f(c)     |\n")
        arquivo.write("-----------------------------------------------------------------\n")
        for linha in tabela:
            arquivo.write(f"|  {linha[0]:2}  |  {linha[1]:.6f}  |  {linha[2]:.6f}  |  {linha[3]:.6f}  |  {linha[4]:.6f}  |  {linha[5]:.6f}  |  {linha[6]:.6f}  |\n")
        arquivo.write("-----------------------------------------------------------------\n")
    print("Resultados salvos em:", nome_arquivo)

# Chamada da função para inserir o intervalo inicial
a, b = inserirIntervalo()

# Chamada da função para encontrar a raiz
raiz, tabela = encontrar_raiz(funcao, a, b)

# Imprimir a raiz com 6 casas decimais

print("A raiz é: ", raiz)
print("A raiz formatada é: ", format(raiz, '.6f'))

# Imprimir a tabela de iterações
print("\nTabela de Iterações:")
print("-----------------------------------------------------------------")
print("|  N  |    a        |   f(a)      |    b        |   f(b)      |    c        |   f(c)     |")
print("-----------------------------------------------------------------")
for linha in tabela:
    print(f"|  {linha[0]:2}  |  {linha[1]:.6f}  |  {linha[2]:.6f}  |  {linha[3]:.6f}  |  {linha[4]:.6f}  |  {linha[5]:.6f}  |  {linha[6]:.6f}  |")
print("-----------------------------------------------------------------")

# Perguntar ao usuário se deseja salvar o arquivo

salvar = input("Deseja salvar os resultados em um arquivo? (s/n): ")
if salvar.lower() == 's':
#nome_arquivo = input("Digite o nome do arquivo para salvar (com a extensão .txt): ")
    nome_arquivo = "resultados_falsa_posicao"
    if os.path.exists(nome_arquivo):
        contador = 1
        while os.path.exists(nome_arquivo):
            nome_arquivo = f"resultados_falsa_posicao_{contador}.txt"
            contador += 1
    salvar_resultados(nome_arquivo, raiz, tabela, a, b)
    print("Resultados salvos em:", nome_arquivo)