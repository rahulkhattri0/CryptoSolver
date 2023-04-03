from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkhtmlview import HTMLLabel,HTMLText
import threading
import algo
import random
from functools import partial
#main window object
root = Tk()
bgimg= ImageTk.PhotoImage(Image.open("assets/bg.jpg"))
bgLabel = Label(root,image=bgimg)
bgLabel.place(x=0,y=0,relheight=1,anchor="nw")
root.minsize(500,380)
root.title("Cryptarithmetic Problem Solver")
frame = Frame(root,bg="#c7cee8")
frame.pack(side=BOTTOM, fill="both")
# Instructions
ins =Toplevel()
ins.geometry("400x250")
insLabel = HTMLLabel(ins,html="\
                      <h3 style='text-align:center'>Instructions</h3>\
                      <ul>\
                      <li>Enter the strings in comma separated order(except the last word)</li>\
                     <li>Enter only one resultant string.</li>\
                     <li><b>Do not include special characters.</b></li>\
                     </ul>\
                     ").pack()
def validate():
    string = strings.get()
    res = resultval.get()
    string=string.upper()
    res=res.upper()
    l = string.split(sep=",")
    l2 = res.split(sep=",")
    if(string=="" or res==""):
      messagebox.showerror("Error!","Please fill out both the fields")
    elif(res.endswith(",") or string.endswith(",")):
       messagebox.showerror("Error!","Dont end the string with a comma!")
    elif(len(l2)>1):
       messagebox.showerror("Error!","Please enter only one resultant string!")
    elif(len(l)==1 and l[0]==l2[0]):
      res = messagebox.askyesno("Warning!","The entered string and the result string are the same.\nThis will generate a lot of results and can take some time.\nIf you wish to continue,press yes")
      if(res==1):
         start(l,l2)
    elif(stringCheck(l,l2)==False):
      messagebox.showerror("Error!","Strings contain something other than alphabets!")
    else:
      start(l,l2)
def stringCheck(l,l2):
   for word in l:
      for i in word:
         res = (i>='A' and i<='Z')
         if(res==False):
            return False
   for i in l2[0]:
      res = (i>='A' and i<='Z')
      if(res==False):
            return False
   return True
def start(l,l2):
   loadingLabel=Label(text="getting your result....",bg="#c7cee8")
   # starting this in a background thread coz else this will keep executing in the main thread and block it after few seconds.
   bgThread = threading.Thread(target=submit,args=(l,l2[0],loadingLabel))
   bgThread.start()

def submit(l,res,load):
   # algo object
   ob = algo.cryp()
   for widgets in frame.winfo_children():
      widgets.destroy()
   load.place(x=220,y=300)
   print(ob.isSolvable(l,res))
   for i in ob.resList:
      print(i) # debugging purposes
   load.place_forget()
   if(len(ob.resList)==1):
      Label(frame,text="The Only possible solution is:",bg="#c7cee8").pack()
      disp=""
      for i in ob.resList[0]:
         disp = disp + i + ","
      Label(frame,text=disp[0:len(disp)-1],bg="#c7cee8").pack()
   elif(len(ob.resList)==0):
      Label(frame,text="Sorry no solution possible!",bg="#c7cee8").pack()
   else:
      rand = random.choice(ob.resList)
      Label(frame,text="One of the possible solutions is:",bg="#c7cee8").pack()
      disp = ""
      for i in rand:
         disp = disp + i + ","
      Label(frame,text=disp[0:len(disp)-1],bg="#c7cee8").pack()
      getanother = Button(frame,text="Get all results!",command=partial(
    writeTofile, ob.resList)).pack(side=BOTTOM)
def writeTofile(answers):
   file = open('answers.txt', 'w')
   for answer in answers:
      toWrite =""
      for i in answer:
         toWrite = toWrite + i + ","
      toWrite = toWrite[0:len(toWrite)-1]
      toWrite += " \n"
      file.write(toWrite)

#menu bar
def abtCmd():
    about = Toplevel()
    label = HTMLLabel(about,html="\
                      <h1>About The problem</h1>\
                      <p>In the crypt-arithmetic problem, some letters are used to assign digits to it. Like ten different letters are holding digit values from 0 to 9 to perform arithmetic operations correctly. There are two words are given and another word is given an answer of addition for those two words.As an example, we can say that two words ‘BASE’ and ‘BALL’, and the result is ‘GAMES’. Now if we try to add BASE and BALL by their symbolic digits, we will get the answer GAMES.<b>There must be ten letters maximum, otherwise it cannot be solved.</b></p>\
                        <img src='assets/Example.jpg'>\
                      <br>\
                      <br>\
                     <a href='https://github.com/rahulkhattri0/Cryptarithmetic-Problem-solver'>Source Code of this Project.</a>"
                      )
    label.pack(padx=20,pady=20)

menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu)
menu.add_cascade(label="Help",menu=file_menu)
file_menu.add_command(label="About",command=abtCmd)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.destroy)
myImg = ImageTk.PhotoImage(Image.open("assets/thinking.png"))
Label(text="Cryptarithmetic Problem Solver!".upper(),bg="#c7cee8").pack()
imglabel = Label(image=myImg,padx=10,pady=20,bg="#c7cee8").place(x=220,y=30)
number = Label(root,text="Input Strings",bg="#c7cee8").place(x=100,y=150)
result = Label(root,text="Result String",bg="#c7cee8").place(x=100,y=200)
strings = StringVar()
resultval = StringVar()
numberentry = Entry(root,textvariable=strings).place(x=210,y=150)
resultentry = Entry(root,textvariable=resultval).place(x=210,y=200)
mybtn = Button(text="SUBMIT",command=validate).place(x=230,y=250)
root.mainloop()