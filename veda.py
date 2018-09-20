from tkinter import *
from tkinter import messagebox
import time
import csv
    

global count


count =0
class App():
    
        
        
    def InsertData(self):
        #global classt1_text
        Sno=self.classt_text.get()
        team=self.classt1_text.get()
        participant=self.classt2_text.get()
        phoneno=self.classt3_text.get()
        print(team)
        print(participant)
        print(phoneno)
        print(Sno)
        self.e3.delete(0,END)
        self.e4.delete(0,END)
        self.e5.delete(0,END)
        self.e6.delete(0,END)
        list=[]
        list.append(Sno)
        list.append(team)
        list.append(participant)
        list.append(phoneno)
        print(list)
        
        with open('C:\\Users\\Vijaya\\Desktop\\vedacsv.csv','a',newline='') as f:
          
            writer=csv.writer(f,dialect='excel-tab',delimiter=',')
            li=[list]
            writer.writerows(li)
        list.clear()
    

    def getdata(self):
        da=self.classt4_text.get()
        self.e7.delete(0,END)
        self.l30=Label(text='Details',height=5)
        self.l30.place(x=150,y=600)
        self.tf = Text( height=2, width=30)
        self.tf.place(x=200,y=600)
       
        with open('C:\\Users\\Vijaya\\Desktop\\vedacsv.csv','r',newline='') as f:
            for line in csv.reader(f):
                if (da == line[0]):
                    print("c")
                    self.tf.insert(END,line)
                    
    def inserttime(self):
        if len(self.e8.get())== 0:
            messagebox.showinfo("Info","Invalid")
        else:
            data1=self.classt5_text.get()
            self.e8.delete(0,END)
            tim=self.d.split(":")
            a1=tim[0]
            a2=tim[1]
            a3=(int(a1)*60)+int(a2)
            list1=[]
            list1.append(data1)
            list1.append(a3)
            with open('C:\\Users\\Vijaya\\Desktop\\vedacsv1.csv','a',newline='') as f:
                writer=csv.writer(f,dialect='excel-tab',delimiter=',')
                li1=[list1]
                writer.writerows(li1)
            list1.clear()
    def shortlist(self):
         self.listb.delete(0,END)
         data2=self.classt6_text.get()
         self.e9.delete(0,END)
         list2=[]
         with open('C:\\Users\\Vijaya\\Desktop\\vedacsv1.csv','r',newline='') as f:
             for line in csv.reader(f):
                    if line[1] not in list2:
                         list2.append(int(line[1]))     
             list2.sort()
             #print(list2)
             for i in range(0,int(data2)):
                 f.seek(0)
                 for line in csv.reader(f):
                     if line[1]==str(list2[i]):
                         self.listb.insert(END,line[0])
                     
                
                
        
    
    def reset(self):
        global count
        count=1
        self.t.set('00:00')
        
    def start(self):
        global count
        count=0
        self.start_timer()
    
    def start_timer(self):
        global count
        self.timer()
    def stop(self):
        global count
        count=1
        #print(self.d)
       
        
    def timer(self):
        global count
        if(count==0):
            self.d = str(self.t.get())
            m,s = map(int,self.d.split(":"))
            
            
            m=int(m)
            s= int(s)
            
            
            if(s<59):
                s+=1
            elif(s==59):
                s=0
                if(m<59):
                    m+=1
                
                    
            
            if(m<10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s<10):
                s=str(0)+str(s)
            else:
                s=str(s)
            
            self.d=m+":"+s
            
            
            self.t.set(self.d)
            if(count==0):
                print(self.start_timer)
                self.root.after(930,self.start_timer)
                
            
        
    def __init__(self):
        self.root=Tk()
        self.root.title("Stop Watch")
        self.root.geometry("1020x700")
        self.root.resizable(False,False)
        self.t = StringVar()
        self.t.set("00:00")
        self.lb = Label(self.root,textvariable=self.t)
        self.lb.config(font=("Courier 40 bold"))                
        self.bt1 = Button(self.root,text="Start",command=self.start,font=("Courier 12 bold"))
        self.bt2 = Button(self.root,text="Stop",command=self.stop,font=("Courier 12 bold"))
        self.bt3 = Button(self.root,text="Reset",command=self.reset,font=("Courier 12 bold"))
        self.lb.place(x=650,y=100)
        self.bt1.place(x=600,y=200)
        self.bt2.place(x=700,y=200)
        self.bt3.place(x=800,y=200)
        self.l3=Label(text='S.NO:',height=3)
        self.l3.place(x=150,y=80)
        self.classt_text=StringVar()
        self.e3=Entry(textvariable=self.classt_text)
        self.e3.place(x=250,y=100)
        self.l4=Label(text='Team_Name',height=3)
        self.l4.place(x=150,y=180)
        self.classt1_text=StringVar()
        self.e4=Entry(textvariable=self.classt1_text)
        self.e4.place(x=250,y=200)
        self.l5=Label(text='Participant',height=3)
        self.l5.place(x=150,y=280)
        self.classt2_text=StringVar()
        self.e5=Entry(textvariable=self.classt2_text)
        self.e5.place(x=250,y=300)
        self.l6=Label(text='Phone_No',height=3)
        self.l6.place(x=150,y=380)
        self.classt3_text=StringVar()
        self.e6=Entry(textvariable=self.classt3_text)
        self.e6.place(x=250,y=400)
        self.button= Button(self.root,text="Insert",command=self.InsertData,font=("Courier 12 bold"))
        self.button.place(x=150,y=450)
        self.button1= Button(self.root,text="Getdata",command=self.getdata,font=("Courier 12 bold"))
        self.button1.place(x=350,y=500)
        self.classt4_text=StringVar()
        self.e7=Entry(textvariable=self.classt4_text)
        self.e7.place(x=200,y=520)
        self.l7=Label(text='team:',height=3)
        self.l7.place(x=150,y=500)
        self.l8=Label(text='teamN:',height=3)
        self.l8.place(x=600,y=300)
        self.classt5_text=StringVar()
        self.e8=Entry(textvariable=self.classt5_text)
        self.e8.place(x=650,y=320)
        self.button2= Button(self.root,text="submit",command=self.inserttime,font=("Courier 12 bold"))
        self.button2.place(x=800,y=300)
        self.l9=Label(text='Topteams:',height=3)
        self.l9.place(x=600,y=350)
        self.classt6_text=StringVar()
        self.e9=Entry(textvariable=self.classt6_text)
        self.e9.place(x=665,y=370)
        self.button3= Button(self.root,text="shortlist",command=self.shortlist,font=("Courier 12 bold"))
        self.button3.place(x=820,y=370)
        
        self.listb=Listbox(self.root,height=6,width=50)
        self.listb.place(x=600,y=450)
        
        self.header=Label(text="Tech-Charades",font='Helvetica 30 bold')
        self.header.place(x=100,y=1)
        #self.header.config(font=("Helvetica",BOLD,18))
        








a = App()
