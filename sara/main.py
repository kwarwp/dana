# dana.sara.main.py
from _spy.vitollino.main import Cena, Elemento, INVENTARIO as inv
from _spy.vitollino.main import STYLE
STYLE ["width"] = 1000
#STYLE ["min-hight"] = 600

floresta = "https://vignette.wikia.nocookie.net/reinoanimalia/images/c/c3/Bosques.png/revision/latest?cb=20150820071051&path-prefix=es"
coqueiro = "https://2.bp.blogspot.com/-QutwWEONdV0/WSA8KeAeToI/AAAAAAAAJJM/2vz0mWLvEZY-ZPc_EsWi2Nl9O39WSvUkQCLcB/s1600/coqueiro-an%25C3%25A3o-produzindo.jpg"
orvalho = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-_3_HMMVXDWcMI9dIi_BI6i3F5jV-_983RseAwJ-DpEO2RoSP"
seiva = "http://cdn.ciclovivo.com.br/wp-content/uploads/2015/009/img/noticias/1238633982_9f95150143%20(1).jpg"
cacto = "https://www.guiamuriae.com.br/wp-content/uploads/2016/01/Agua-de-cacto-Foto-Pixabay.jpg"
corda = "https://4.bp.blogspot.com/-VuqgmerQZ_8/VeX2DWsMdoI/AAAAAAAAeZU/oak3CEhkAcs/s1600/N%25C3%25A1utico%2B-%2Bcorda.png"
faca = "https://vignette.wikia.nocookie.net/left4dead/images/0/0c/Machete.png/revision/latest?cb=20101021031134"
pote = "http://rodrigorepresentacoes.com.br/imagens/produtos/902/Pote%20PP-10001.png"
pano = "http://www.stickpng.com/assets/images/5856ad664f6ae202fedf277c.png"
colher = "https://upload.wikimedia.org/wikipedia/commons/3/32/Colher.png"

class Agua():
     def __init__ (self):
      inv.inicia()
     
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
     
      self.minicoqueiro= Elemento(img=coqueiro, style=dict (left=150, top=300, height=300,width=200,bottom=200))
      self.miniorvalho= Elemento (img=orvalho, style=dict (left=200, top= 500, height=300, width=200, bottom=200))
      self.miniseiva= Elemento (img=seiva, style=dict (left=500, top= 300, height=50, width=200, bottom=200))
      self.minicacto= Elemento (img=cacto, style=dict (left=300, top= 500, height=200, width=200, bottom=200))
      
      self.floresta.meio = self.floresta
      self.floresta.vai
     
      self.minicoqueiro.entra (self.florestaCoqueiro)
      self.minicacto.entra (self.florestaCacto)
      self.miniseiva.entra (self.florestaSeiva)
      self.miniorvalho.entra (self.florestaOrvalho)
     
      #criar a funÃÂÃÂ§ÃÂÃÂ£o de abrir elemento ao clicar em elemento
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
      
      self.corda = Elemento (img=corda, tit="corda", style=dict (left=150, top=300, height=300,width=200,bottom=200))
      inv.bota (self.corda)
      self.faca = Elemento (img=faca, tit="faca", style=dict (left=150, top=300, height=300,width=200,bottom=200))
      inv.bota (self.faca)
      self.pote = Elemento (img=pote, tit="pote", style=dict (left=150, top=300, height=300,width=200,bottom=200))
      inv.bota (self.pote)
      self.pano = Elemento (img=pano, tit="pano", style=dict (left=150, top=300, height=300,width=200,bottom=200))
      inv.bota (self.pano)
      self.colher = Elemento (img=colher, tit="colher", style=dict (left=150, top=300, height=300,width=200,bottom=200))
      inv.bota (self.colher)
      
      
    
      self.floresta.vai ()
if __name__ == "__main__":
     Agua()
