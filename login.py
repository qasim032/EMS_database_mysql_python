from customtkinter import *
from PIL import Image
from tkinter import messagebox
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror("Error","All fields are required")
    elif usernameEntry.get()=='root'and passwordEntry.get()=="12345":
        messagebox.showinfo("Success","Login Successful")
        root.destroy()
        import ems
    else:
        messagebox.showerror("Error","User Doesn't exists")
root = CTk()
root.geometry('930x478+100+100')
root.resizable(0,0)
root.title("Login Page")
image  = CTkImage(Image.open("banner.png"),size=(930,478))
imageLabel = CTkLabel(root,image=image,text=None)
imageLabel.place(x=0,y=0)
headingLabel = CTkLabel(root,text="Employee Management System",bg_color="#FAFAFA",font=('Goudy Old Styly',30,'bold'),text_color="Black")
headingLabel.place(x=0,y=20)
usernameEntry = CTkEntry(root,placeholder_text="Enter Your Username",font=('arial',18,'bold'),fg_color="#FAFAFA",bg_color="#FAFAFA",text_color="Black",width=200,height=40)
usernameEntry.place(x=20,y=100)
passwordEntry = CTkEntry(root,placeholder_text="Enter Your Password",font=('arial',18,'bold'),show='*',fg_color="#FAFAFA",bg_color="#FAFAFA",text_color="Black",width=200,height=40)
passwordEntry.place(x=20,y=150)
loginBtn = CTkButton(root,text="Login",cursor='hand2',command=login,fg_color="Black",bg_color="white")
loginBtn.place(x=50,y=200)
set_appearance_mode("Light")
root.mainloop()
