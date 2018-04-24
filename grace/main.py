# dana.grace.main.py
from _spy.vitollino.main import Cena,Elemento, Texto
from _spy.vitollino.main import INVENTARIO as inv

ilha = "https://gartic.com.br/imgs/mural/_v/_vorreipace_/ilha.png"
floresta_heterogenea = "https://img.elo7.com.br/product/original/12F2B86/painel-de-festa-floresta-festa-personalizada.jpg"
floresta_homogenea = "/home/todomundo/Desktop/Forest-pine-trees-sun-rays_1920x1200.jpg"
pergaminho = "https://i.pinimg.com/originals/df/6c/76/df6c765f7019656350531c4a4eff5e11.png"
habbo = "https://wydnblog.files.wordpress.com/2010/08/miss.png"
 
class criarcenas():
   def __init__(self):

     self.ilha = Cena(img=ilha)
     self.habbo = Elemento(img=habbo, tit="voce perdido", style = dict( left = 90,
                                                                        height = 200,
                                                                        width = 60, 
                                                                        top = 100))
     self.pergaminho = Elemento(img=pergaminho, = dict ( left = 90,height = 200, width = 60,    top = 100))
                                                                                      
                                                                                        
                                                                                         
     self.instrucao = texto(self.pergaminho,"água,fogo,abrigo,comida")  
      
      
      self.habbo.entra(self.ilha)
      self.pergaminho.entra(self.ilha)
      self.pergaminho.vai = self.intrucao.vai
      
      self.ilha.vai()
   
if __name__ == "__main__":
     criarcenas()