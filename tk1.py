from tkinter import *
count=0
ct=0
def lkm(event):
    global ct
    ct+=1
    lbl.configure(text=ct,font=f"Arial {10+ct}")
def pkm(event):
    print("Нажата ПКМ")
def koleso(event):
    global count
    if event.delta==-120:
        count-=1
    if event.delta==120:
        count+=1
    btn['text']=count
def text_to_lbl(event):
    t=ent.get()
    lbl.configure(text=t)
def to_text():
    a=var.get()
    if a==0:
        text.delete(0.0,END)
    else:
        text.insert(END,a)

    
win=Tk()
win.title("Название окна")
win.geometry("500x800")
btn=Button(win,text="Нажми \nна меня",fg="red",bg="lightblue",
           font="Arial 40", width=15)#,relief=SUNKEN)#GROOVE)#RAISED)
lbl=Label(win,text="Это надпись",fg="blue",bg="pink",height=3,font="Arial 10")
ent=Entry(win,width=15,fg="green",bd=20,font="Arial 20")
w=2
h=1
x=4
#img=PhotoImage(file="Python.png").zoom(w,h)
img=PhotoImage(file="Python.png").subsample(x)
#lbl_img=Label(win,image=img)
btn_img=Button(win,image=img,fg="red",
           font="Arial 40", width=150,height=150)
text=Text(win, width=30,height=10,wrap=WORD)
var=IntVar()
var.set(2)
r1=Radiobutton(win,text="Один",variable=var,value=1,command=to_text)
r2=Radiobutton(win,text="Два",variable=var,value=2,command=to_text)
r3=Radiobutton(win,text="Три",variable=var,value=3,command=to_text)
r4=Radiobutton(win,text="Очистить",variable=var,value=0,command=to_text)
btn.bind("<Button-1>",lkm)
btn.bind("<Button-3>",pkm)
btn.bind("<MouseWheel>",koleso)
ent.bind("<Return>",text_to_lbl)
btn.pack()
lbl.pack()
ent.pack()
btn_img.pack()
text.pack()
r1.pack(side=LEFT)
r2.pack(side=LEFT)
r3.pack(side=LEFT)
r4.pack(side=LEFT)
#lbl_img.pack()
win.mainloop()
