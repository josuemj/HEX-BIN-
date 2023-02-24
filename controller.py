import hex

class Controller:
    
    #Internal method
    #Function: Verifies the option that user provides 
    #Return: Bool
    def menuVerifier(cadena):
        try:
            numero = int(cadena)
            if numero == 1 or numero == 2:
                return True
        except:
            return False
        
    #Function: Shows up the menu
    #return: int (menu option forced)
    @staticmethod
    def menu(): 
        while True:

            print("\nConversor de HEX -> BIN")
            print("=======================")
            print("1. Convertir")
            print("2. Salir")
            print("=======================")
            
            cadena = input("Ingresar la opcion :) -> ")

            if Controller.menuVerifier(cadena) == True:
                return int(cadena)
            else:
                print("Introduce una opcion valida :)")

    #Function: Verifies if it's a hexadecimal expression (with 3 chars and if does not have another char that does not belong to hex system)
    #Return: str (The final hex expression)
    @staticmethod
    def getHexExpression():

        while True:
            hexExpression = input("Introduce la expresion hexadecimal :) -> ")

            if hex.Hex.hexLeghtVerifier(hexExpression):

                if hex.Hex.isHex(hexExpression):

                    return hexExpression
                
                else:
                    print("La expresion contiene caracteres no hexadecimales")
            else:
                print("La cantidad esta limitada a 3 caractetes hexadecimales")