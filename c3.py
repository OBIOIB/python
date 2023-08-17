import tkinter

FNT=('Times New Roman',30)

class GameCharacter:
    def __init__(self,job,life,imgfile):
        self.job=job
        self.life=life
        self.img=tkinter.PhotoImage(file=imgfile)
        
    def draw(self):
        canvas.create_image(200,280,image=self.img)
        canvas.create_text(300,400,text=self.job,font=FNT,fill='red')
        canvas.create_text(300,480,text=self.job,font=FNT,fill='blue')
warrior=GameCharacter('戦士',100)
warrior.info()
