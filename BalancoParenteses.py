while True:

    try:
        expressao = str(input())
        balanco = list()

        for char in expressao:
            if char == '(' :
                balanco.append(char)
            elif char == ')' :
                if len(balanco) > 0:
                    balanco.pop()
                else:
                    balanco.append(')')

        if balanco:
            print("incorrect")

        else:
            print("correct")

    except EOFError:
        break