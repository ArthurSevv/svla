def interpretador():
    variaveis = {}

    linhas = codigo.splitlines()

    for linha in linhas:
        partes = linha.split()

        if len(partes) != 0:
            if partes[0] == "print":
                
                #VALOR CASO SEJE VARIAVEL
                if partes[1] in variaveis:
                    print(variaveis[partes[1]])

                #TIPOS DE VALORES
                #STRINGS + REMOVE ASPAS
                elif partes[1][0] == "'":
                    print(partes[1].replace("'",""))
                elif partes[1][0] == '"':
                    print(partes[1].replace('"','')) 
                #INTEIROS
                else:
                    print(int(partes[1]))

            elif partes[0] == "let":

                #STRINGS + REMOVE ASPAS
                if partes[3][0] == "'":
                    variaveis[partes[1]] = partes[3].replace("'","")
                elif partes[3][0] == '"':
                    variaveis[partes[1]] = partes[3].replace('"','')
                #INTEIROS
                else:
                    variaveis[partes[1]] = int(partes[3])


codigo = """
    let nome = 'Arthur'
    let idade = 20

    print nome
    print idade
"""

interpretador()