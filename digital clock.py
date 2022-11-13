from tkinter import *
import time
clk=Tk()
clk.title("clock")
clk.geometry("1350x700+0+0")  #width,height,x-axis,y-axis we have kept 0 because we will start from left top corner
clk.config(bg="#0c1e28")  # you can give any color you want

def clock():

    hr=str(time.strftime("%H"))
    mn=str(time.strftime("%M"))
    sc=str(time.strftime("%S"))
    print(hr,mn,sc)
    if int(hr)> 12 and int(mn)> 0:   #to convert am to pm
        lb_dn.config(text="PM")
    if int(hr)> 12:
        hr=str(int(int(hr)-12))
    lb_hr.config(text=hr)
    lb_mn.config(text=mn)
    lb_sec.config(text=sc)
 
    lb_hr.after(200,clock) # to make clock update every second


lb_hr=Label(clk,text="12",font=("times 20 bold",75,'bold'),bg="#087587",fg="white")
lb_hr.place(x=350,y=200,width=150,height=150)

lb_hr_text=Label(clk,text="HOUR",font=("Times 20 bold",20,"bold"),bg="#087587",fg="white")
lb_hr_text.place(x=350,y=360,width=150,height=50)


lb_mn=Label(clk,text="12",font=("times 20 bold",75,'bold'),bg="#008EA4",fg="white")
lb_mn.place(x=520,y=200,width=150,height=150)

lb_mn_text=Label(clk,text="minute",font=("Times 20 bold",20,"bold"),bg="#008EA4",fg="white")
lb_mn_text.place(x=520,y=360,width=150,height=50)

lb_sec=Label(clk,text="12",font=("times 20 bold",75,'bold'),bg="#06B4B8",fg="white")
lb_sec.place(x=690,y=200,width=150,height=150)

lb_sec_text=Label(clk,text="second",font=("Times 20 bold",20,"bold"),bg="#06B4B8",fg="white")
lb_sec_text.place(x=690,y=360,width=150,height=50)

lb_dn=Label(clk,text="12",font=("times 20 bold",75,'bold'),bg="#9F0646",fg="white")
lb_dn.place(x=860,y=200,width=150,height=150)

lb_dn_text=Label(clk,text="NOON",font=("Times 20 bold",20,"bold"),bg="#9F0646",fg="white")
lb_dn_text.place(x=860,y=360,width=150,height=50)

clock()
clk.mainloop()