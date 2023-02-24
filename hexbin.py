#Main code

import controller,conversor

while True:
    flag = controller.Controller.menu()

    if flag == 1:
        hexagesimal = controller.Controller.getHexExpression()
        print("\n========================")
        print("HEXADECIMAL:",hexagesimal)
        print("BINARIO:",conversor.Conversor.hexToBin(hexagesimal))
        print("==========================")

    elif flag == 2:
        
        break
