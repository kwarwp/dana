# dana.libby.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE, Codigo as Code, INVENTARIO, NS
from browser import html
STYLE["width"] = 800
class Foto:
    SPG= "https://imgur.com/TPGqQ7k.png"
    IN01="https://imgur.com/Lqx1fWA.png"
    MIL0="https://imgur.com/ojAlOFl.png"
    PFOR="https://imgur.com/dbFMO8W.png"
    FORE="https://imgur.com/Ac9gSDD.png"
    SBCC="https://imgur.com/6vaIIR1.png"
    SPPT="https://imgur.com/EUjDgk2.png"
    KWOP="https://imgur.com/yfL0EFR.png"
    MAN0="https://imgur.com/RJ4dNv9.png"
    MAN1="https://imgur.com/Vx6zqTS.png"
    MAN2="https://imgur.com/rYPXyYM.png"
    SPGG="https://imgur.com/yAAFXJd.png"
    SPCC="https://imgur.com/6vWvrAW.png"
    SPGF="https://imgur.com/EjW4X9B.png"
    SPGE="https://imgur.com/UZHl9z3.png"
    SPGP="https://imgur.com/WIJiQ0A.png"
    SPGU="https://imgur.com/KoLkTix.png"
    SPGC="https://imgur.com/7ezi6zF.png"
    SGVI="https://www.youtube.com/embed/LsRdPQ8Stq8"
    SGVE='<iframe width="560" height="315" src="https://www.youtube.com/embed/LsRdPQ8Stq8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    
class Codigo(Code):
    def __init__(self, codigo="", topo="", cena=INVENTARIO, img="", vai=None, style=NS):
        Code.__init__(self, codigo=codigo, topo=topo, cena=cena, img=img, vai=vai, style=style)
        a = html.A("×", href="#", style=dict(position="absolute", top="0px", right="10px",
        fontSize="30px", fontWeight="bold"))  
        a.onclick = self._close
        self.elt<=a
        self._close()
        #self.elt.style = {"visibility": "hidden", "opacity": 0}
    def _close(self, *_):
        self.elt.style = {"visibility": "hidden", "opacity": 0}
        self.cena._code_=self

class Video(Elemento):
    def __init__(self,source, width, height, top, left):
        Elemento.__init__(self,style=dict(position="absolute", top=top,left=left))
        video=html.VIDEO(width=width, height=height,autoplay=True, style=dict(position="absolute", top=top,
        left=left))
        video<=html.SOURCE(src=source)
        video.onclick = self._close
        self.elt<=video

    def _close(self, *_):
        self.elt.style = {"visibility": "hidden", "opacity": 0}
        self.cena._video_=self

class Embed(Elemento):
    def __init__(self,source, width, height, top, left):
        Elemento.__init__(self,style=dict(position="absolute", top=top,left=left))
        video=html.IFRAME(src=source, width=width, height=height, frameborder="0",
        allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture")
        video.onclick = self._close
        self.elt<=video

    def _close(self, *_):
        self.elt.style = {"visibility": "hidden", "opacity": 0}
        self.cena._video_=self
    
c = Cena(Foto.SPG)
e = Elemento(Foto.MIL0, style=dict(left=100, top=100, width="100px", height="120px"))
e.entra(c)
v = Embed(Foto.SGVI, 600, 400, 100, 100)
v.entra(c)
c.vai()
