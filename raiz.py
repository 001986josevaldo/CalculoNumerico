# Criar a função
# Exemplo de uma função f(x)
import os
def funcao(x):
    return x**2 - 4  # Para encontrar a raiz de x^2 - 4 = 0 (raiz quadrada de 4)

def encontrar_raiz(f, a, b, tol=1e-6, nmax=100):
    N = 1
    tabela = []  # Lista para armazenar os valores da tabela
    while N <= nmax:
        xbarra = (a + b) / 2
        fxbarra = f(xbarra)
        tabela.append((N, a, b, xbarra, fxbarra))  # Adiciona os valores atuais à tabela
        if fxbarra == 0 or (b - a) / 2 < tol:
            return xbarra, tabela
        N += 1
        if fxbarra * f(a) > 0:
            a = xbarra
        else:
            b = xbarra
    return "O algoritmo falhou.", tabela
# Intervalo inicial
def inserirIntervalo():
  a = float(input("Digite o valr do intervalo a: "))
  b = float(input("Digite o valr do intervalo a: "))
  print('A= ', a, '\nB= ', b)
  return a,b

# Função para salvar os resultados em um arquivo
def salvar_resultados(nome_arquivo, raiz, tabela, a, b):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write("\nPonto inicial: {}".format(a))
        arquivo.write("\nPonto final: {}\n".format(b))
        arquivo.write("A raiz é: {}\n".format(raiz))
        arquivo.write("\nTabela de Iterações:\n")
        arquivo.write("-------------------------------------------------\n")
        arquivo.write("|  N  |    a        |    b        |    c        |   f(c)     |\n")
        arquivo.write("-------------------------------------------------\n")
        for linha in tabela:
            arquivo.write(f"|  {linha[0]:2}  |  {linha[1]:.6f}  |  {linha[2]:.6f}  |  {linha[3]:.6f}  |  {linha[4]:.6f}  |\n")
        arquivo.write("-------------------------------------------------\n")
    print("Resultados salvos em:", nome_arquivo)


# Chamada da função para inserir o intervalo inicial
a, b = inserirIntervalo()

# Chamada da função para encontrar a raiz
raiz, tabela = encontrar_raiz(funcao, a, b)

print("A raiz é: ", raiz)
print("A raiz formatada é: ", format(raiz, '.6f'))


# Imprimir a tabela de iterações
print("\nTabela de Iterações:")
print("-------------------------------------------------")
print("|  N    |        a    |    b     |    c      |   f(c)   |")
print("-------------------------------------------------")
for linha in tabela:
    print(f"|  {linha[0]:2}  |  {linha[1]:.6f}  |  {linha[2]:.6f}  |  {linha[3]:.6f}  |  {linha[4]:.6f}  |")
print("-------------------------------------------------")

salvar = input("Deseja salvar os resultados em um arquivo? (s/n): ")


if salvar.lower() == "s":
    nome_arquivo = "resultados_bissecao.txt"
    contador = 1
    while os.path.exists(nome_arquivo):
        nome_arquivo = "resultados_bissecao_{}.txt".format(contador)
        contador += 1

    salvar_resultados(nome_arquivo, raiz, tabela, a,b)
    print("Resultados salvos em:", nome_arquivo)