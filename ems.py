from customtkinter import *
from tkinter import messagebox
from PIL import Image

window  = CTk()
window.title("Employee Management System")
window.geometry('930x580')

logo = CTkImage(Image.open("empbanner.jpg"),size=(930,150))
imagelab = CTkLabel(window,image=logo,text="")
imagelab.grid(row=0,column=0,columnspan= 2)


leftframe = CTkFrame(window)
leftframe.grid(row= 1,column=0)

rightframe = CTkFrame(window)
rightframe.grid(row=1,column = 1)

#left Frame
idlabel = CTkLabel(leftframe,text="Id",font=('arial',18,'bold'))
idlabel.grid(row=0,column=0,padx=20,pady=15,sticky='w')
idEntry = CTkEntry(leftframe,font=('arial',18,'bold'),width=180)
idEntry.grid(row=0,column=1)

namelabel = CTkLabel(leftframe,text="Name",font=('arial',18,'bold'))
namelabel.grid(row=1,column=0,padx=20,pady=15,sticky='w')
nameEntry = CTkEntry(leftframe,font=('arial',18,'bold'),width=180)
nameEntry.grid(row=1,column=1)

phonelabel = CTkLabel(leftframe,text="Phone",font=('arial',18,'bold'))
phonelabel.grid(row=2,column=0,padx=20,pady=15,sticky='w')
phoneEntry = CTkEntry(leftframe,font=('arial',18,'bold'),width=180)
phoneEntry.grid(row=2,column=1)

rolelabel = CTkLabel(leftframe,text="Role",font=('arial',18,'bold'))
rolelabel.grid(row=3,column=0,padx=20,pady=15,sticky='w')
role_options =["Web Developer","Data Scientist","Python Developer","IT Consultant","ML Expert","AI Engineer"]
roleBox = CTkComboBox(leftframe,values=role_options,width=180,font=('arial',18,'bold'))
roleBox.grid(row=3,column=1)

genderLabel = CTkLabel(leftframe,text="Gender",font=('arial',18,'bold'))
genderLabel.grid(row=4,column=0,padx=20,pady=15,sticky='w')
genderBox = CTkComboBox(leftframe,values=["Male","Female"],width=180,font=('arial',18,'bold'))
genderBox.grid(row=4,column=1)

salaryLabel = CTkLabel(leftframe,text="Salary",font=('arial',18,'bold'))
salaryLabel.grid(row=5,column=0,padx=20,pady=15,sticky='w')
salaryEntry = CTkEntry(leftframe,font=('arial',18,'bold'),width=180)
salaryEntry.grid(row=5,column=1)


window.resizable(0,0)
set_appearance_mode("Light")
window.mainloop()