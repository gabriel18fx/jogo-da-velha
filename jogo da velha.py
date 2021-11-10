linhau = ['_','_','_']
linhad = ['_','_','_']
linhat = ['_','_','_']



while True:
    
    print(linhau)
    print(linhad)
    print(linhat)

    jogador_1L = int(input("jogador 1, em que linha deseja jogar: [1],[2],[3] ? "))
    jogador_1C = int(input("jogador 1, em que coluna deseja jogar: [1],[2],[3] ? "))

    if(jogador_1L == 1 and jogador_1C == 1) and linhau[0] != 'X' and linhau[0] != 'O':
        linhau[0] = 'X'
    if(jogador_1L == 1 and jogador_1C == 2) and linhau[1] != 'X' and linhau[1] != 'O':
        linhau[1] = 'X'
    if(jogador_1L == 1 and jogador_1C == 3) and linhau[2] != 'X' and linhau[2] != 'O':
        linhau[2] = 'X'
        
    if (linhau[0] == 'X' and linhau[1] == 'X' and linhau[2] == 'X'):     
        print(linhau)
        print(linhad)
        print(linhat)
        print("jogador 1 venceu")
        fim = input("Deseja jogar de novo [s], [n]?")
        if(fim == 'n'):
            print("Fim de Jogo!")
            break
        
            

    if(jogador_1L == 2 and jogador_1C == 1) and linhad[0] != 'X' and linhad[0] != 'O':
        linhad[0] = 'X'
    if(jogador_1L == 2 and jogador_1C == 2) and linhad[1] != 'X' and linhad[1] != 'O':
        linhad[1] = 'X'
    if(jogador_1L == 2 and jogador_1C == 3) and linhad[2] != 'X' and linhad[2] != 'O':
        linhad[2] = 'X'

    if (linhad[0] == 'X' and linhad[1] == 'X' and linhad[2] == 'X'):
        print(linhau)
        print(linhad)
        print(linhat)
        print("jogador 1 venceu")
        fim = input("Deseja jogar de novo [s], [n]?")
        if(fim == 'n'):
            print("Fim de Jogo!")
            break


    if(jogador_1L == 3 and jogador_1C == 1) and linhat[0] != 'X' and linhat[0] != 'O':
        linhat[0] = 'X'
    if(jogador_1L == 3 and jogador_1C == 2) and linhat[1] != 'X' and linhat[1] != 'O':
        linhat[1] = 'X'
    if(jogador_1L == 3 and jogador_1C == 3) and linhat[2] != 'X' and linhat[2] != 'O':
        linhat[2] = 'X'

    if (linhat[0] == 'X' and linhat[1] == 'X' and linhat[2] == 'X'):  
        print(linhau)
        print(linhad)
        print(linhat)
        print("jogador 1 venceu")
        fim = input("Deseja jogar de novo [s], [n]?")
        if(fim == 'n'):
            print("Fim de Jogo!")
            break



    if (linhau[0] == 'X' and linhad[1] == 'X' and linhat[2] == 'X'):
        print(linhau)
        print(linhad)
        print(linhat)
        print("jogador 1 venceu")
        fim = input("Deseja jogar de novo [s], [n]?")
        if(fim == 'n'):
            print("Fim de Jogo!")
            break


    if (linhau[2] == 'X' and linhad[1] == 'X' and linhat[0] == 'X'):
        print(linhau)
        print(linhad)
        print(linhat)
        print("jogador 1 venceu")
        fim = input("Deseja jogar de novo [s], [n]?")
        if(fim == 'n'):
            print("Fim de Jogo!")
            break


    
    if(linhau[0] == 'X' and linhad[0] == 'X' and linhat[0] == 'X'):
        print(linhau)
        print(linhad)
        print(linhat)
        print("jogador 1 venceu")
        fim = input("Deseja jogar de novo [s], [n]?")
        if(fim == 'n'):
            break


    if(linhau[1] == 'X' and linhad[1] == 'X' and linhat[1] == 'X'):
        print(linhau)
        print(linhad)
        print(linhat)
        print("jogador 1 venceu")
        fim = input("Deseja jogar de novo [s], [n]?")
        if(fim == 'n'):
            print("Fim de Jogo!")
            break


    if(linhau[2] == 'X' and linhad[2] == 'X' and linhat[2] == 'X'):
        print(linhau)
        print(linhad)
        print(linhat)
        print("jogador 1 venceu")
        fim = input("Deseja jogar de novo [s], [n]?")
        if(fim == 'n'):
            print("Fim de Jogo!")
            break





    print(linhau)
    print(linhad)
    print(linhat)

    jogador_2L = int(input("jogador 2, em que linha deseja jogar: [1],[2],[3] ? "))
    jogador_2C = int(input("jogador 2, em que coluna deseja jogar: [1],[2],[3] ? "))

    if(jogador_2L == 1 and jogador_2C == 1) and linhau[0] != 'X' and linhau[0] != 'O':
        linhau[0] = 'O'
    if(jogador_2L == 1 and jogador_2C == 2) and linhau[1] != 'X' and linhau[1] != 'O':
        linhau[1] = 'O'
    if(jogador_2L == 1 and jogador_2C == 3) and linhau[2] != 'X' and linhau[2] != 'O':
        linhau[2] = 'O'

    if (linhau[0] == 'O' and linhau[1] == 'O' and linhau[2] == 'O'):
        print(linhau)
        print(linhad)
        print(linhat)
        print("jogador 2 venceu")
        fim = input("Deseja jogar de novo [s], [n]?")
        if(fim == 'n'):
            print("Fim de Jogo!")
            break
   

    if(jogador_2L == 2 and jogador_2C == 1) and linhad[0] != 'X' and linhad[0] != 'O':
        linhad[0] = 'O'
    if(jogador_2L == 2 and jogador_2C == 2) and linhad[1] != 'X' and linhad[1] != 'O':
        linhad[1] = 'O'
    if(jogador_2L == 2 and jogador_2C == 3) and linhad[2] != 'X' and linhad[2] != 'O':
        linhad[2] = 'O'
               
    if (linhad[0] == 'O' and linhad[1] == 'O' and linhad[2] == 'O'):
        print(linhau)
        print(linhad)
        print(linhat)
        print("jogador 2 venceu")
        fim = input("Deseja jogar de novo [s], [n]?")
        if(fim == 'n'):
            print("Fim de Jogo!")
            break
        

    if(jogador_2L == 3 and jogador_2C == 1) and linhat[0] != 'X' and linhat[0] != 'O':
        linhat[0] = 'O'
    if(jogador_2L == 3 and jogador_2C == 2) and linhat[1] != 'X' and linhat[0] != 'O':
        linhat[1] = 'O'
    if(jogador_2L == 3 and jogador_2C == 3) and linhat[2] != 'X' and linhat[2] != 'O':
        linhat[2] = 'O'

    if (linhat[0] == 'O' and linhat[1] == 'O' and linhat[2] == 'O'):
        print(linhau)
        print(linhad)
        print(linhat)
        print("jogador 2 venceu")
        fim = input("Deseja jogar de novo [s], [n]?")
        if(fim == 'n'):
            print("Fim de Jogo!")
            break




    if (linhau[0] == 'O' and linhad[1] == 'O' and linhat[2] == 'O'):
        print(linhau)
        print(linhad)
        print(linhat)
        print("jogador 2 venceu")
        fim = input("Deseja jogar de novo [s], [n]?")
        if(fim == 'n'):
            print("Fim de Jogo!")
            break


    if (linhau[2] == 'O' and linhad[1] == 'O' and linhat[0] == 'O'):
        print(linhau)
        print(linhad)
        print(linhat)
        print("jogador 2 venceu")
        fim = input("Deseja jogar de novo [s], [n]?")
        if(fim == 'n'):
            print("Fim de Jogo!")
            break


    
    if(linhau[0] == 'O' and linhad[0] == 'O' and linhat[0] == 'O'):
        print(linhau)
        print(linhad)
        print(linhat)
        print("jogador 2 venceu")
        fim = input("Deseja jogar de novo [s], [n]?")
        if(fim == 'n'):
            print("Fim de Jogo!")
            break


    if(linhau[1] == 'O' and linhad[1] == 'O' and linhat[1] == 'O'):
        print(linhau)
        print(linhad)
        print(linhat)
        print("jogador 2 venceu")
        fim = input("Deseja jogar de novo [s], [n]?")
        if(fim == 'n'):
            print("Fim de Jogo!")
            break


    if(linhau[2] == 'O' and linhad[2] == 'O' and linhat[2] == 'O'):
        print(linhau)
        print(linhad)
        print(linhat)
        print("jogador 2 venceu")
        fim = input("Deseja jogar de novo [s], [n]?")
        if(fim == 'n'):
            print("Fim de Jogo!")
            break
   

