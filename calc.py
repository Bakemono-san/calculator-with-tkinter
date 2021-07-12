from tkinter import *

def btnClick(numbers):
    global operateur
    operateur = operateur + str(numbers)
    text_input.set(operateur)

def btnClear():
    global operateur
    operateur = ""
    text_input.set("")

def btnEgal():
    global operateur
    calcul = str(eval(operateur))
    text_input.set(calcul)
    operateur = ""


fenetre = Tk()
fenetre.title("calculatrice")
text_input = StringVar()
operateur = ""

ecran = Entry(fenetre, font = ('arial', 20, 'bold'), textvariable = text_input, bd = 30, insertwidth = 4, bg = 'powder blue',fg="blue", justify = 'right').grid(columnspan = 4)

btn9 = Button(fenetre,padx=16,pady=16,bd=20,bg="purple",fg="yellow",text="9",font=('arial',20,'bold'),command=lambda:btnClick(9)).grid(row=1,column=0)
btn8 = Button(fenetre,padx=16,pady=16,bd=20,bg="purple",fg="yellow",text="8",font=('arial',20,'bold'),command=lambda:btnClick(8)).grid(row=1,column=1)
btn7 = Button(fenetre,padx=16,pady=16,bd=20,bg="purple",fg="yellow",text="7",font=('arial',20,'bold'),command=lambda:btnClick(7)).grid(row=1,column=2)
division = Button(fenetre,padx=16,pady=16,bd=20,bg="purple",fg="yellow",text="/",font=('arial',20,'bold'),command=lambda:btnClick("/")).grid(row=1,column=3)

btn6 = Button(fenetre,padx=16,pady=16,bd=20,bg="purple",fg="yellow",text="6",font=('arial',20,'bold'),command=lambda:btnClick(6)).grid(row=2,column=0)
btn5 = Button(fenetre,padx=16,pady=16,bd=20,bg="purple",fg="yellow",text="5",font=('arial',20,'bold'),command=lambda:btnClick(5)).grid(row=2,column=1)
btn4 = Button(fenetre,padx=16,pady=16,bd=20,bg="purple",fg="yellow",text="4",font=('arial',20,'bold'),command=lambda:btnClick(4)).grid(row=2,column=2)
multi = Button(fenetre,padx=16,pady=16,bd=20,bg="purple",fg="yellow",text="*",font=('arial',20,'bold'),command=lambda:btnClick("*")).grid(row=2,column=3)

btn3 = Button(fenetre,padx=16,pady=16,bd=20,bg="purple",fg="yellow",text="3",font=('arial',20,'bold'),command=lambda:btnClick(3)).grid(row=3,column=0)
btn2 = Button(fenetre,padx=16,pady=16,bd=20,bg="purple",fg="yellow",text="2",font=('arial',20,'bold'),command=lambda:btnClick(2)).grid(row=3,column=1)
btn1 = Button(fenetre,padx=16,pady=16,bd=20,bg="purple",fg="yellow",text="1",font=('arial',20,'bold'),command=lambda:btnClick(1)).grid(row=3,column=2)
sous = Button(fenetre,padx=16,pady=16,bd=20,bg="purple",fg="yellow",text="-",font=('arial',20,'bold'),command=lambda:btnClick("-")).grid(row=3,column=3)

btn0 = Button(fenetre,padx=16,pady=16,bd=20,bg="purple",fg="yellow",text="0",font=('arial',20,'bold'),command=lambda:btnClick(0)).grid(row=4,column=0)
effacer = Button(fenetre,padx=16,pady=16,bd=20,bg="purple",fg="yellow",text="c",font=('arial',20,'bold'),command=btnClear).grid(row=4,column=1)
egal = Button(fenetre,padx=16,pady=16,bd=20,bg="purple",fg="yellow",text="=",font=('arial',20,'bold'),command=btnEgal).grid(row=4,column=2)
addition = Button(fenetre,padx=16,pady=16,bd=20,bg="purple",fg="yellow",text="+",font=('arial',20,'bold'),command=lambda:btnClick("+")).grid(row=4,column=3)

fenetre.mainloop()