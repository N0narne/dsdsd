from tkinter import *
n=0
def vajutamine(event):
    global n
    n+=1
    nupp.config(text="Vajutatud: "+str(n))

aken=Tk()
aken.title("Bogdan")
#aken.iconbitmap(")
aken.geometry('400x600')
nupp=Button(aken,text="Vajuta siia",height=4,width=14,bg="blue",fg="green",font="Arial 36")


nupp.pack(side=TOP)
nupp.bind('<Button-3>',vajutamine)
aken.mainloop() 
