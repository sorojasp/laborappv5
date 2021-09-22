import json
from typing import Final
class Encrypt:
    """[summary]
    """

    position_move:Final = 1  # la clave es el número que se aumenta al ascii de cada carácter del string a encriptar
    __change_msg=''
    
    def __init__(self):
        pass
        
        
    """
    """    
    def __change_strings_characters(self, operation:str,
                                str_of_characters:str)->str:
        if operation=='+':
            
            for character in str_of_characters:
                self.__change_msg=chr(ord(character)+self.position_move)+self.__change_msg
        else:
            for character in str_of_characters:
                self.__change_msg=chr(ord(character)-self.position_move)+self.__change_msg
        
        return self.__change_msg
    

    def encrypt_msg(self,msg)->str:
        
        return self.__change_strings_characters('+',msg)
    
    def decrypt_msg(self,msg)->str:
        
        return self.__change_strings_characters('-',msg)
    
    
encryp:Encrypt=Encrypt()

dict_str=json.dumps(
    {
        'name':'Stiven ',
        'lastName':'Rojas Pulido'
    }
)
print(encryp.encrypt_msg(dict_str))
