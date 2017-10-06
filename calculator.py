
from Tkinter import *


def butclick(numbers):
    global operator
   
    
    operator=operator + str(numbers)
    
    text_Input.set(operator)

def cleardisplay():
    global operator
    operator=""
    text_Input.set("")

def equals():
    global operator
    
    sumup=str(eval(operator))
    text_Input.set(sumup)
    

    
cal=Tk()
cal.title("Calculator")
operator=""
text_Input=StringVar()
txtDisplay=Entry(cal,font=('calibri',15,'bold'),bg='light blue',textvariable=text_Input,bd=25,insertwidth=5,justify='center').grid(columnspan=4)


butclear=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('calibri',15,'bold'),text="C",bg='light blue',command=cleardisplay).grid(row=1,column=1)
Division=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('calibri',15,'bold'),text="/",bg='light blue',command=lambda:butclick('/')).grid(row=1,column=2)
Multiply=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('calibri',15,'bold'),text="*",bg='light blue',command=lambda:butclick('*')).grid(row=1,column=3)


but7=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('calibri',15,'bold'),text="7",bg='light blue',command=lambda:butclick('7')).grid(row=2,column=0)
but8=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('calibri',15,'bold'),text="8",bg='light blue',command=lambda:butclick('8')).grid(row=2,column=1)
but9=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('calibri',15,'bold'),text="9",bg='light blue',command=lambda:butclick('9')).grid(row=2,column=2)
Subtraction=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('calibri',15,'bold'),text="-",bg='light blue',command=lambda:butclick('-')).grid(row=2,column=3)


but4=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('calibri',15,'bold'),text="4",bg='light blue',command=lambda:butclick('4')).grid(row=3,column=0)
but5=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('calibri',15,'bold'),text="5",bg='light blue',command=lambda:butclick('5')).grid(row=3,column=1)
but6=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('calibri',15,'bold'),text="6",bg='light blue',command=lambda:butclick('6')).grid(row=3,column=2)
Addition=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('calibri',15,'bold'),text="+",bg='light blue',command=lambda:butclick('+')).grid(row=3,column=3)


but1=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('calibri',15,'bold'),text="1",bg='light blue',command=lambda:butclick('1')).grid(row=4,column=0)
but2=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('calibri',15,'bold'),text="2",bg='light blue',command=lambda:butclick('2')).grid(row=4,column=1)
but3=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('calibri',15,'bold'),text="3",bg='light blue',command=lambda:butclick('3')).grid(row=4,column=2)
butEquals=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('calibri',15,'bold'),bg='light blue',text="=",command=equals).grid(row=4,column=3)


Modulus=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('calibri',15,'bold'),text="%",bg='light blue',command=lambda:butclick('%')).grid(row=5,column=0)
but0=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('calibri',15,'bold'),text="0",bg='light blue',command=lambda:butclick('0')).grid(row=5,column=1)
Dot=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('calibri',15,'bold'),text=".",bg='light blue',command=lambda:butclick('.')).grid(row=5,column=2)
#Srt=Button(caal,padx=16,pady=16,bd=8,fg='black',font=('calibri',15,'bold'),text="sqrt( )",bg='light blue',command=lambda:butclick('sqrt( )').grid(row=5,column=3)*/

cal.mainloop()

