from customtkinter import *
from tkinter import ttk,messagebox
from PIL import Image
from datetime import datetime
import database
#Functions
def add_employee():
    if idEntry.get()==''or nameEntry.get()=='' or phoneEntry.get()=='' or salaryEntry.get()=='':
        messagebox.showerror("Error","All fields are required!")
    elif database.id_exists(idEntry.get()):
        messagebox.showerror("Error","Id already exists")
    else:
        database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        messagebox.showinfo("Added","Employee added Successfully!")

#GUI 
window  = CTk()
window.title("Employee Management System")
window.geometry('930x580+100+100')
window.configure(fg_color="#17122E")

logo = CTkImage(Image.open("empbanner.jpg"),size=(930,150))
imagelab = CTkLabel(window,image=logo,text="")
imagelab.grid(row=0,column=0,columnspan= 3,)

current_date = datetime.now().strftime("%d %b %Y")
titlelabel = CTkLabel( window,text=f"Employee Management System",font=('arial', 35, 'bold'),text_color="white",fg_color="#032d88")
titlelabel.place(x=0,y=0)

dateLabel = CTkLabel( window,text=f"{current_date}",font=('arial', 30, 'bold'),text_color="white",fg_color="#032d88")
dateLabel.place(x=350,y=45)



leftframe = CTkFrame(window,fg_color="#17122E")
leftframe.grid(row= 1,column=0)

rightframe = CTkFrame(window)
rightframe.grid(row=1,column = 1) 

#left Frame
idlabel = CTkLabel(leftframe,text="Id",font=('arial',18,'bold'),text_color="white")
idlabel.grid(row=0,column=0,padx=10,pady=15,sticky='w')
idEntry = CTkEntry(leftframe,font=('arial',18,'bold'),width=180)
idEntry.grid(row=0,column=1)

namelabel = CTkLabel(leftframe,text="Name",font=('arial',18,'bold'),text_color="white")
namelabel.grid(row=1,column=0,padx=10,pady=15,sticky='w')
nameEntry = CTkEntry(leftframe,font=('arial',18,'bold'),width=180)
nameEntry.grid(row=1,column=1)

phonelabel = CTkLabel(leftframe,text="Phone",font=('arial',18,'bold'),text_color="white")
phonelabel.grid(row=2,column=0,padx=10,pady=15,sticky='w')
phoneEntry = CTkEntry(leftframe,font=('arial',18,'bold'),width=180)
phoneEntry.grid(row=2,column=1)

rolelabel = CTkLabel(leftframe,text="Role",font=('arial',18,'bold'),text_color="white")
rolelabel.grid(row=3,column=0,padx=10,pady=15,sticky='w')
role_options =["Web Developer","Data Scientist","Python Developer","IT Consultant","ML Expert","AI Engineer"]
roleBox = CTkComboBox(leftframe,values=role_options,width=180,font=('arial',18,'bold'),state='readonly')
roleBox.grid(row=3,column=1)
roleBox.set(role_options[0])

genderLabel = CTkLabel(leftframe,text="Gender",font=('arial',18,'bold'),text_color="white")
genderLabel.grid(row=4,column=0,padx=10,pady=15,sticky='w')
genderBox = CTkComboBox(leftframe,values=["Male","Female"],width=180,font=('arial',18,'bold'),state='readonly')
genderBox.grid(row=4,column=1)
genderBox.set("Male")

salaryLabel = CTkLabel(leftframe,text="Salary",font=('arial',18,'bold'),text_color="white")
salaryLabel.grid(row=5,column=0,padx=10,pady=20,sticky='w')
salaryEntry = CTkEntry(leftframe,font=('arial',18,'bold'),width=180)
salaryEntry.grid(row=5,column=1)


#Right Frame
SearchBox = CTkComboBox(rightframe,values=["Id","Name","Phone","Role","Gender"],state="readonly")
SearchBox.grid(row=0,column=0)
SearchBox.set("Search By")

SearchEntry = CTkEntry(rightframe,font=('arial',18))
SearchEntry.grid(row=0,column=1)

SearchBtn = CTkButton(rightframe,text="Search",font=('arial',18),width=100)
SearchBtn.grid(row=0,column=2)
ShowallBtn = CTkButton(rightframe,text="Show All",font=('arial',18),width=100)
ShowallBtn.grid(row=0,column=3,pady=5)

# Creating the tree view in the right frame 
tree = ttk.Treeview(rightframe)
tree.grid(row=1,column=0,columnspan=4)

tree['column'] = ('Id','Name','Phone','Role','Gender','Salary')
tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')

tree.config(show="headings")
tree.column('Id',anchor="center",width=100)
tree.column('Name',anchor="center",width=160)
tree.column('Phone',anchor="center",width=140)
tree.column('Role',anchor="center",width=190)
tree.column('Gender',anchor="center",width=100)
tree.column('Salary',anchor="center",width=100)

#Column Styling
style = ttk.Style()
style.configure('Treeview.Heading',font=('arial',15,'bold'))

#Scrollbar in treeview
scrollbar = ttk.Scrollbar(rightframe,orient=VERTICAL)
scrollbar.grid(row=1,column=4,sticky=NS)


#bottom frame
bottom = CTkFrame(window,fg_color="#17122E")
bottom.grid(row=2,column=0,columnspan=2)

#buttons
newEmp = CTkButton(bottom,text="New Employee",font=('arial',18,'bold'),width=150,corner_radius=10)
newEmp.grid(row=0,column=0,pady=10)

addEmp = CTkButton(bottom,text="Add Employee",font=('arial',18,'bold'),width=150,corner_radius=10,command=add_employee)
addEmp.grid(row=0,column=1,padx=5,pady=5)

UpdateEmp = CTkButton(bottom,text="Update Employee",font=('arial',18,'bold'),width=150,corner_radius=10)
UpdateEmp.grid(row=0,column=2,padx=5,pady=5)

DeleteEmp = CTkButton(bottom,text="Delete Employee",font=('arial',18,'bold'),width=150,corner_radius=10)
DeleteEmp.grid(row=0,column=3,padx=5,pady=5)

DeleteAllEmp = CTkButton(bottom,text="Delete All",font=('arial',18,'bold'),width=150,corner_radius=10)
DeleteAllEmp.grid(row=0,column=4,padx=5,pady=5)


window.resizable(0,0)
set_appearance_mode("Light")
window.mainloop()