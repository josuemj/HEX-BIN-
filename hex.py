class Hex:

    @staticmethod
    def hexLeghtVerifier(cadena):
        if len(cadena) == 3:
            return True
        else:
            return False
    
    @staticmethod
    def isHex(cadena):
        chars = [
            "1","2","3","4","5","6","7","8","9",
            "A","B","C","D","E","F"
            ]
        
        for char in cadena:
            if char in chars:
                pass
            else:
                return False
        return True
    
