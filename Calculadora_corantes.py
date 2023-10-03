while True:
    print('use ponto ao inves de virgula')
    concentração= input('qual a concentração da amostra? ')
    força= input('qual a força da amostra? (sem o %) ')
    resultado = float(força)/100
    if força != 100:
        print(float(concentração) / float(resultado))
    sair= input("voce quer sair? ").lower
    if sair== "sim" and "s":
        continue
