from playsound import playsound
import keyboard
import tkinter
from tkinter import *
from PIL import Image
from PIL import ImageTk


path='Music_Notes/'

root = Tk()
root.title("Piano_By_RAKi")
root.geometry('1366x760')
root.config(bg = '#000000')

###########################
canvas = Canvas(root, bg="black", width=1366, height=760)
canvas.place(x=-2,y=0)
###########################

img = Image.open("bg.jpg")
img = img.resize((1366,760))
photoImg =  ImageTk.PhotoImage(img)
#Image_label = Label(root,image=photoImg)
#Image_label.pack()
canvas.create_image(680, 380, image=photoImg,anchor=CENTER)


img1 = Image.open("Raki.png")
img1 = img1.resize((100,40))
photoImg1 =  ImageTk.PhotoImage(img1)
canvas.create_image(677, 330, image=photoImg1)
#Image_label1 = Label(root,image=photoImg1)
#Image_label1.place()
#ℜakëรђ
#text = Label(root, text="",font=("", 10),fg='green',bg='black')
#text.place(x=0,y=700,width = 100,height = 30)

def Press(Str1):
    playsound(path+Str1+'.wav')


C = Button(root,text = "C",font = ('',16),bg = 'white',command = lambda :Press("C"))
C.place(x=270,y=350,width = 75,height = 300)

D = Button(root,text = "D",font = ('',16),bg = 'white',command = lambda :Press("D"))
D.place(x=345,y=350,width = 75,height = 300)

E = Button(root,text = "E",font = ('',16),bg = 'white',command = lambda :Press("E"))
E.place(x=420,y=350,width = 75,height = 300)

F = Button(root,text = "F",font = ('',16),bg = 'white',command = lambda :Press("F"))
F.place(x=495,y=350,width = 75,height = 300)

G = Button(root,text = "G",font = ('',16),bg = 'white',command = lambda :Press("G"))
G.place(x=570,y=350,width = 75,height = 300)

A = Button(root,text = "A",font = ('',16),bg = 'white',command = lambda :Press("A"))
A.place(x=645,y=350,width = 75,height = 300)

B = Button(root,text = "B",font = ('',16),bg = 'white',command = lambda :Press("B"))
B.place(x=720,y=350,width = 75,height = 300)

C1 = Button(root,text = "C1",font = ('',16),bg = 'white',command = lambda :Press("C1"))
C1.place(x=795,y=350,width = 75,height = 300)

D1 = Button(root,text = "D1",font = ('',16),bg = 'white',command = lambda :Press("D1"))
D1.place(x=870,y=350,width = 75,height = 300)

E1 = Button(root,text = "E1",font = ('',16),bg = 'white',command = lambda :Press("E1"))
E1.place(x=945,y=350,width = 75,height = 300)

F1 = Button(root,text = "F1",font = ('',16),bg = 'white',command = lambda :Press("F1"))
F1.place(x=1020,y=350,width = 75,height = 300)




Cs = Button(root,text = "C#",font = ('',16),fg='white',bg = 'black',command = lambda :Press("C_s"))
Cs.place(x=320,y=350,width = 50,height = 188)

Ds = Button(root,text = "D#",font = ('',16),fg='white',bg = 'black',command = lambda :Press("D_s"))
Ds.place(x=395,y=350,width = 50,height = 188)

Fs = Button(root,text = "F#",font = ('',16),fg='white',bg = 'black',command = lambda :Press("F_s"))
Fs.place(x=545,y=350,width = 50,height = 188)

Gs = Button(root,text = "G#",font = ('',16),fg='white',bg = 'black',command = lambda :Press("G_s"))
Gs.place(x=620,y=350,width = 50,height = 188)

As = Button(root,text = "A#",font = ('',16),fg='white',bg = 'black',command = lambda :Press("A_s"))
As.place(x=695,y=350,width = 50,height = 188)

C1s = Button(root,text = "C1#",font = ('',16),fg='white',bg = 'black',command = lambda :Press("C_s1"))
C1s.place(x=845,y=350,width = 50,height = 188)

D1s = Button(root,text = "D1#",font = ('',16),fg='white',bg = 'black',command = lambda :Press("D_s1"))
D1s.place(x=920,y=350,width = 50,height = 188)



###########################################################
#Only got these sounds From here ALL DUMMY KEYS
#NO SOUND KEYS
###########################################################


F = Button(root,text = "-",font = ('',16),bg = 'white')#,command = lambda :Press("F"))
F.place(x=-30,y=350,width = 75,height = 300)

G = Button(root,text = "-",font = ('',16),bg = 'white')#,command = lambda :Press("G"))
G.place(x=45,y=350,width = 75,height = 300)

A = Button(root,text = "-",font = ('',16),bg = 'white')#,command = lambda :Press("A"))
A.place(x=120,y=350,width = 75,height = 300)

B = Button(root,text = "-",font = ('',16),bg = 'white')#,command = lambda :Press("B"))
B.place(x=195,y=350,width = 75,height = 300)

G = Button(root,text = "-",font = ('',16),bg = 'white')#,command = lambda :Press("G"))
G.place(x=1095,y=350,width = 75,height = 300)

A = Button(root,text = "-",font = ('',16),bg = 'white')#,command = lambda :Press("A"))
A.place(x=1170,y=350,width = 75,height = 300)

B = Button(root,text = "-",font = ('',16),bg = 'white')#,command = lambda :Press("B"))
B.place(x=1245,y=350,width = 75,height = 300)

C = Button(root,text = "-",font = ('',16),bg = 'white')#,command = lambda :Press("C"))
C.place(x=1320,y=350,width = 75,height = 300)



Fs = Button(root,text = "-",font = ('',16),fg='white',bg = 'black')#,command = lambda :Press("F_s"))
Fs.place(x=20,y=350,width = 50,height = 188)

Gs = Button(root,text = "-",font = ('',16),fg='white',bg = 'black')#,command = lambda :Press("G_s"))
Gs.place(x=95,y=350,width = 50,height = 188)

As = Button(root,text = "-",font = ('',16),fg='white',bg = 'black')#,command = lambda :Press("A_s"))
As.place(x=170,y=350,width = 50,height = 188)

Fs = Button(root,text = "-",font = ('',16),fg='white',bg = 'black')#,command = lambda :Press("F_s"))
Fs.place(x=1070,y=350,width = 50,height = 188)

Gs = Button(root,text = "-",font = ('',16),fg='white',bg = 'black')#,command = lambda :Press("G_s"))
Gs.place(x=1145,y=350,width = 50,height = 188)

As = Button(root,text = "-",font = ('',16),fg='white',bg = 'black')#,command = lambda :Press("A_s"))
As.place(x=1220,y=350,width = 50,height = 188)





root.mainloop()