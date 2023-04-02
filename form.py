from tkinter import *
from tkinter import messagebox
import smtplib
from colorama import init,Fore
init(autoreset=True)

red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
lightblue = Fore.LIGHTBLUE_EX


class SendMail:

    def __init__(self):

        ##Root conf
        self.root = Tk()
        self.root.geometry('500x350')
        self.root.resizable(False,False)
        self.root.title("Send Mail")
        ##From conf
        self.fromlbl = Label(self.root, text="FROM...",width=20,font=("bold", 20))
        self.fromlbl.place(x=-50,y=53)
        self.fromtxt = Entry(self.root)
        self.fromtxt.place(x=200,y=60)
        #Gmailpass conf
        self.gpasslbl = Label(self.root, text="G-Mail Pass...",width=20,font=("bold", 15))
        self.gpasslbl.place(x=-10,y=100)
        self.gpasstxt = Entry(self.root,show="*")
        self.gpasstxt.place(x=200,y=100)    
        ##To conf
        self.tolbl = Label(self.root, text="TO...",width=20,font=("bold", 20))
        self.tolbl.place(x=-50,y=130)
        self.totxt = Entry(self.root,state=DISABLED)
        self.totxt.place(x=200,y=137)
        ##Msg conf
        self.msglbl = Label(self.root, text="MSG...",width=20,font=("bold", 20))
        self.msglbl.place(x=-50,y=203)
        self.msgtxt = Text(self.root,width=30,height=7,state=DISABLED)
        self.msgtxt.place(x=200,y=214)
        self.msgs = Scrollbar(self.root)
        self.msgs.pack(side=RIGHT,fill=Y)
        self.msgs.config(command=self.msgtxt.yview)
        self.msgtxt.config(yscrollcommand=self.msgs.set)
        ##Sendbtn conf
        self.sendbtn = Button(self.root,text="Send Mail...",command=self.sendmail_f,state=DISABLED)
        self.sendbtn.place(x=60,y=290)
        ##Loginbtn con
        self.loginbtn = Button(self.root,text="Login...",command=self.checkinputs)
        self.loginbtn.place(x=400,y=55)
        ##Logoutbtn con
        self.logoutbtn = Button(self.root,text="LogOut...",state=DISABLED,command=self.logout)
        self.logoutbtn.place(x=395,y=100)
        self.root.mainloop()

    def logout(self):
        self.server.quit()
        messagebox.showerror("Quit","SuccessFully LogedOut")
        print(f"{green}SuccessFully LogedOut")
        self.logoutbtn["state"] = "disabled"
        self.loginbtn["state"] = "normal"
        self.gpasstxt["state"] = "normal"
        self.fromtxt["state"] = "normal"
        self.totxt["state"] = "disabled"
        self.msgtxt["state"] = "disabled"
        self.sendbtn["state"] = "disabled"
        self.gpasstxt.delete(0,END)
        self.fromtxt.delete(0,END)
    def checkinputs(self):
        
        if self.fromtxt.get() == "":
            messagebox.showerror("Error!!","Please Fill...")
            print(f"{red}Error!")
        else:
            if self.gpasstxt.get() == "":
                messagebox.showerror("Error!!","Please Fill...")
                print(f"{red}Error!")
            else:
                self.fromtxt["state"] = "disabled"
                self.gpasstxt["state"] = "disabled"
                self.loginbtn["state"] = "disabled"
                print(f"{lightblue}G-Mail: " , f"{red}{self.fromtxt.get()}")
                print(f"{lightblue}G-Mail Pass: " , f"{red}Secret..")
                messagebox.showwarning("Trying...","Please Wait...")
                print(f"{yellow}Please Wait...")
                self.login()
    def login(self):
        self.gmailurl = self.fromtxt.get()
        self.gmailpassword = self.gpasstxt.get()
        try:
            Host = 'smtp.gmail.com'
            Port = 587
            print(f"{yellow}Connecting To Server")
            self.server = smtplib.SMTP(Host, Port)
            self.server.ehlo()
            self.server.starttls()
            self.server.login(self.gmailurl, self.gmailpassword)
            messagebox.showinfo("Info!!","SuccessFully LogedIn")
            print(f"{green}SuccessFully LogedIn")
            self.logoutbtn["state"] = "normal"
            self.totxt["state"] = "normal"
            self.sendbtn["state"] = "normal"
            self.msgtxt["state"] = "normal"
        except Exception as e:
            messagebox.showerror("Error!!","SomeThing Is Wrong!!![Try Again]")
            print(f"{red}Error!")
            self.loginbtn["state"] = "normal"
            self.gpasstxt["state"] = "normal"
            self.fromtxt["state"] = "normal"
            self.gpasstxt.delete(0,END)
            self.fromtxt.delete(0,END)
    def sendmail_f(self):

            if self.t == "":
                print(f"{red}Please Fill TO...")
                print(f"{red}Error!")
            else:
                print(f"{green}Okay!")
                try:
                    print(f"{lightblue}msg: [{self.msg}]")
                    self.server.sendmail(self.fromtxt.get(), self.totxt.get(), self.msgtxt.get("1.0","end-1c"))
                    print(f"{green}SuccessFully Sent!")
                    messagebox.showinfo("Sent!!","SuccessFulyy Sent!!")
                    self.msgtxt.delete("1.0","end-1c")
                except Exception as e:
                    messagebox.showerror("Error!!","SomeThing Is Wrong")
                    



def main():
    sm = SendMail()

if __name__ == "__main__":
    main()
