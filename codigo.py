class Senha:
    def __init__(self, site, usuario, senha):
        self.site = site
        self.usuario = usuario
        self.senha = senha
        self.prox = None
        
class GerenciadorDeSenhas:
    def __init__(self):
        self.cabeca = None
        self.calda = None
        self.tamanho = 0
        
    def adicionar_senha(self, site, usuario, senha):
        nova_entrada = Senha(site, usuario, senha)
        if self.cabeca is None:
            self.cabeca = nova_entrada
            self.calda = nova_entrada
        else:
            self.calda.prox = nova_entrada
            self.calda = nova_entrada
        self.tamanho += 1
        return True
    
    def remover_senha(self, site):
        if self.tamanho == 0:
            return False
        if self.tamanho == 1:
            self.cabeca = None
            self.calda = None
            self.tamanho -= 1
            return True
        if self.tamanho >= 2:
            temp = self.cabeca
            if temp.site == site:
                self.cabeca = self.cabeca.prox
                temp.prox = None
                self.tamanho -= 1
                return True
            while temp.site != site:
                anterior = temp
                temp = temp.prox
            anterior.prox = temp.prox
            temp.prox = None
            self.tamanho -= 1
            return True  
        
    def print(self):
        temp = self.cabeca
        print("SUAS SENHAS SALVAS:")
        print("")
        while temp:
            print("Site:", temp.site)
            print("Usuário:", temp.usuario)
            print("Senha:", temp.senha)
            print("")
            temp = temp.prox


            
        
        
        
        
