from collections import UserDict
from types import MappingProxyType
from typing import Any


class Config(UserDict):

    def __init__(self, initial_config):
        self.data = initial_config or {}
        self._immutable_config = MappingProxyType(self.data)

    def __setitem__(self, key, value):
        raise TypeError("Configurações são imutáveis e não podem ser alteradas.")

    def __delitem__(self, key):
        raise TypeError("Configurações são imutáveis e não podem ser removidas.")
    
    def get_config(self):
        return self._immutable_config
    
    def add_config(self,key, value):
        if not key in self.data:
            self.data[key] = value

if __name__=='__main__':
    #Criando uma instancia
    cf = Config(
        {
            'um':1,
            'dois':2,
            'tres':3
        }
    )
    
    #Exibindo as configurações
    print(cf)

    # Testado modificar uma valor
    try:
        cf['um'] = '1'
    except TypeError as e:
        print(e) 

    # Testado deletar uma valor
    try:
        del cf['um']
    except TypeError as e:
        print(e) 

    # Pegando as informações imutaveis
    print(cf.get_config())

    # Adicionando novas configuraçoes por um metodo especial
    cf.add_config('quatro',4)
    print(cf)

    # Tentando modificar configuraçoes existentes pelo metodo especial
    cf.add_config('um','1')
    print(cf)

    # Acessando o valor de uma chave
    print(cf['dois'])

    # Pegando as informações imutaveis novamente
    print(cf.get_config())