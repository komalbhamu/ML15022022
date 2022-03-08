import tkinter as tkn
app=tkn.Tk()
app.title('calculator')
app.geometry('500x500')


tkn.Label(app,text='a',textvariable='a',font=('',25)).place(x=0,y=0)
tkn.Label(app,text='b',textvariable='b',font=('',25)).place(x=200,y=0)
tkn.Label(app,text='result',textvariable='res',font=('',25)).place(x=80,y=350)


a=tkn.Variable(app)
tkn.Entry(app,textvariable=a).place(x=50,y=15)
b=tkn.Variable(app)
tkn.Entry(app,textvariable=b).place(x=250,y=15)
res=tkn.Variable(app)
tkn.Entry(app,textvariable=res).place(x=200,y=350)


def calculator(op):
    res.set(eval(a.get()+op+b.get()))
    
    
tkn.Button(app,text='+',font=('',20),command=lambda:calculator('+'),bg='green').place(x=0,y=150)
tkn.Button(app,text='-',font=('',20),command=lambda:calculator('-'),bg='red').place(x=150,y=150)
tkn.Button(app,text='x',font=('',20),command=lambda:calculator('*'),bg='yellow').place(x=300,y=150)
tkn.Button(app,text='/',font=('',20),command=lambda:calculator('/'),bg='blue').place(x=450,y=150)


app.mainloop()

