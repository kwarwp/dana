# dana.grace.main.py
from _spy.vitollino.main import Cena, Texto, Elemento, INVENTARIO as inv
ilha = "https://gartic.com.br/imgs/mural/_v/_vorreipace_/ilha.png"
floresta_heterogenea = "https://img.elo7.com.br/product/original/12F2B86/painel-de-festa-floresta-festa-personalizada.jpg"
floresta_homogenea = "/home/todomundo/Desktop/Forest-pine-trees-sun-rays_1920x1200.jpg"
pergaminho = "https://i.pinimg.com/originals/df/6c/76/df6c765f7019656350531c4a4eff5e11.png"
habbo = "https://wydnblog.files.wordpress.com/2010/08/miss.png"
 
class criarcenas():
   def __init__(self):

       self.ilha = Cena(img=ilha)
       self.habbo = Elemento(img=habbo, style=dict, left=100, right=100, top=100, bottom=100)
       self.habbo.entra(self.ilha)
       def escreve (x):
          self.escreve=input("usando string")
          self.habbo.escreve()
       self.ilha.vai()

if __name__=="__main__":
   criarcenas()


