import matplotlib.pyplot 
# o Progama forma uma lista com dados do usuário e coloca ela em ordem crescente
while True: # O programa evita o ValueError na entrada input, esse while reinicia o programa caso haja erro
    l = []
    x = 0 #contador x 
    try: #esse comando testa o input
        z=int(input("quantos elementos quer adicionar a lista "))
    except ValueError: #caso o usuário trolle e escreva um float ou string o programa não trava mas reinicia
        print("somente valores númericos ")
    else:#se não houver erro ele sai do laço
        break 
while z>x:#essa parte pede os valores e adiciona na lista e também evita ValueError
    try:
       e = int(input("insira o elemento "))
    except ValueError:
        print("somente valores númericos ")
    else:
        l = l + [e]
        x += 1
print("a lista desordenada é: ", l) #O Restante e um algoritmo que poem o programa em ordem crescente
L = l
fim = len(l)
while fim > 1:
    troca = True
    y=0
    while y < (fim-1):
        if l[y] > l[y+1]:
            troca = False
            temp = l[y]#temp e uma variável usada na troca, ela armanezar o valor trocado e devolve ele para sua nova posição
            l[y] = l[y+1]
            l[y+1] = temp
        y+=1
    if troca: #not false = true e not true = false, ele só sai do laço quando fim for 0
        break
    fim -= 1
for e in l: #mostra a lista em ordem crescente
    print(e) 
print("a lista ordenada é:", l)
# o Progama forma uma lista com dados do usuário e coloca ela em ordem crescente
matplotlib.pyplot.plot(l, L)
matplotlib.pyplot.ylim(0, 150)
matplotlib.pyplot.show()
