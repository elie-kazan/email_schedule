import smtplib
import time
from datetime import date
from datetime import datetime
from tkinter import *
from tkinter import ttk
c_2=str(datetime.now())

nbrsecondes=time.time()
a=date.fromtimestamp(nbrsecondes)

class Fenetre:

    def __init__(self,root):
        self.root=root
        self.c_2=str(datetime.now())
        
        
        self.frame=ttk.Frame(self.root,padding=(50,50))
        self.frame.grid()
        self.root.title("Scheduel Email sending")
        self.label1=ttk.Label(self.frame,text="Enter the content of your email")
        self.label1.grid(row=0,column=0)
        self.msg=StringVar()
        self.entrymsg=ttk.Entry(self.frame,width=100,textvariable=self.msg)
        self.entrymsg.grid(row=1,column=0)
        self.labels=ttk.Label(self.frame,text="Please enter your Gmail below")
        self.labels.grid(row=2,column=0)
        self.emails=StringVar()
        self.entrys=ttk.Entry(self.frame,width=60,textvariable=self.emails)
        self.entrys.grid(row=3,column=0)
        self.labelp=ttk.Label(self.frame,text="Please enter your Gmail password below")
        self.labelp.grid(row=4,column=0)
        self.password=StringVar()
        self.entryp=ttk.Entry(self.frame,width=20,textvariable=self.password,show="*")
        self.entryp.grid(row=5,column=0)
        self.labelr=ttk.Label(self.frame,text="Please enter the gmail of the receiver")
        self.labelr.grid(row=6,column=0)
        self.emailr=StringVar()
        self.entryr=ttk.Entry(self.frame,width=60,textvariable=self.emailr)
        self.entryr.grid(row=7,column=0)
        self.labelt=ttk.Label(self.frame,text="Enter the time ")
        self.labelt.grid(row=8,column=0)
        self.times=StringVar()
        self.timeh=StringVar()
        
        self.entryth=ttk.Entry(self.frame,width=3,textvariable=self.timeh)
        self.entryth.grid(row=9,column=0)
        self.entryt=ttk.Entry(self.frame,width=3,textvariable=self.times)
        self.entryt.grid(row=9,column=1)
        self.buttons=ttk.Button(self.frame,text="Schedule",command=self.send)
        self.buttons.grid(row=10,column=0)
    def send(self):
        self.root.destroy()
        while self.c_2[11]+self.c_2[12]!=self.timeh.get()or self.c_2[14]+self.c_2[15]!=self.times.get():
            self.c_2=str(datetime.now())
        
            
            if self.c_2[14]+self.c_2[15]==self.times.get() and self.c_2[11] +self.c_2[12]==self.timeh.get():
                server=smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login(self.emails.get(),self.password.get())
                server.sendmail(self.emails.get(),self.emailr.get(),self.msg.get())
                server.quit()
                

root=Tk()
Fenetre1=Fenetre(root)





        
        


        
    
