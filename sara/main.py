# dana.sara.main.py
from _spy.vitollino.main import Cena, Elemento, INVENTARIO as inv
from _spy.vitollino.main import STYLE
STYLE ["width"] = 900
STYLE ["min-hight"] = 600

floresta = "https://vignette.wikia.nocookie.net/reinoanimalia/images/c/c3/Bosques.png/revision/latest?cb=20150820071051&path-prefix=es"
coqueiro = "https://2.bp.blogspot.com/-QutwWEONdV0/WSA8KeAeToI/AAAAAAAAJJM/2vz0mWLvEZY-ZPc_EsWi2Nl9O39WSvUkQCLcB/s1600/coqueiro-an%25C3%25A3o-produzindo.jpg"
orvalho = "https://st.depositphotos.com/1030956/4910/i/950/depositphotos_49103197-stock-photo-macro-tree-branch-with-raindrops.jpg"
seiva = "http://cdn.ciclovivo.com.br/wp-content/uploads/2015/009/img/noticias/1238633982_9f95150143%20(1).jpg"
cacto = "https://www.guiamuriae.com.br/wp-content/uploads/2016/01/Agua-de-cacto-Foto-Pixabay.jpg"



class Agua():
     def __init__ (self):
     
      self.floresta= Cena(img=floresta)
      self.florestaOrvalho= Cena(img=floresta)
      self.florestaCoqueiro= Cena(img=floresta)
      self.florestaSeiva= Cena(img=floresta)
      self.florestaCacto= Cena(img=floresta)

      self.floresta.direita = self.florestaCoqueiro
      self.florestaCoqueiro.esquerda = self.floresta
     
      self.floresta.esquerda = self.florestaOrvalho
      self.florestaOrvalho.direita = self.floresta
     
      self.florestaCoqueiro.direita = self.florestaCacto
      self.florestaCacto.esquerda = self.florestaCoqueiro
     
      self.florestaOrvalho.esquerda = self.florestaSeiva
      self.florestaSeiva.direita = self.florestaOrvalho     
     
      self.florestaSeiva.esquerda = self.florestaCacto
      self.florestaCacto.direita = self.florestaSeiva
     
      self.minicoqueiro= Elemento(img=coqueiro, style=dict (left=100, top= 300, height=200 ,width=200,bottom=100))
      self.miniorvalho= Elemento (img=orvalho, style=dict (left=95, top= 100, height=100, width=100, bottom=15))
      self.miniseiva= Elemento (img=seiva, style=dict (left=100, top= 100, height=100, width=100, bottom=15))
      self.minicacto= Elemento (img=cacto, style=dict (left=95, top= 100, height=100, width=100, bottom=15))
     
      self.minicoqueiro.entra (self.florestaCoqueiro)
      self.minicacto.entra (self.florestaCacto)
      self.miniseiva.entra (self.florestaSeiva)
      self.miniorvalho.entra (self.florestaOrvalho)
     
      #criar a funÃ§Ã£o de abrir elemento ao clicar em elemento
      self.cenaCoqueiro = Cena (img=coqueiro)
      self.minicoqueiro.vai = self.cenaCoqueiro.vai
      self.cenaCoqueiro.esquerda = self.florestaCoqueiro
      self.cenaCoqueiro.direita = self.florestaCoqueiro
           
      self.cenaCacto = Cena (img= cacto)
      self.minicacto.vai = self.cenaCacto.vai
      self.cenaCacto.esquerda = self.florestaCacto
      self.cenaCacto.direita = self.florestaCacto
                     
      self.cenaOrvalho = Cena (img= orvalho)
      self.miniorvalho.vai = self.cenaOrvalho.vai
      self.cenaOrvalho.esquerda = self.florestaOrvalho
      self.cenaOrvalho.direita = self.florestaOrvalho
                     
      self.cenaSeiva = Cena (img= seiva)
      self.miniseiva.vai = self.cenaSeiva.vai
      self.cenaSeiva.esquerda = self.florestaSeiva
      self.cenaSeiva.direita = self.florestaSeiva
    
     
    
      self.floresta.vai ()
if __name__ == "__main__":
     Agua()
