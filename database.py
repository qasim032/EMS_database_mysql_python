import pymysql
from tkinter import messagebox
def connectdatabase(password):
    global mycursor,conn
    try:
        conn = pymysql.connect(host='localhost',user='root',password=password)
        mycursor = conn.cursor()
    except:
        messagebox.showerror("Error","Something Went wrong.Please open mysql database before running again")
        return
    mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
    mycursor.execute('USE employee_data')
    mycursor.execute('CREATE TABLE IF NOT EXISTS data (Id varchar(20),Name varchar(50),Phone varchar(15),Role varchar(50),Gender varchar(10),Salary decimal(10,2))')
    return True

def insert(id,name,phone,role,gender,salary):
    mycursor.execute('INSERT INTO data VALUES (%s,%s,%s,%s,%s,%s)',(id,name,phone,role,gender,salary))
    conn.commit()
def id_exists(id):
    mycursor.execute('SELECT COUNT(*) FROM data WHERE id=%s',id)
    result = mycursor.fetchone()
    return result[0]>0
def fetch_employees():
    mycursor.execute('SELECT * FROM data')
    result = mycursor.fetchall()
    return result
def search(searchby,data):
    if searchby=="Id":
        mycursor.execute('SELECT * FROM data WHERE Id=%s',(data,))
    elif searchby=="Name":
        mycursor.execute('SELECT * FROM data WHERE Name=%s',(data,))
    elif searchby=="Phone":
        mycursor.execute('SELECT * FROM data WHERE Phone=%s',(data,))
    elif searchby=="Role":
        mycursor.execute('SELECT * FROM data WHERE Role=%s',(data,))
    elif searchby=="Gender":
        mycursor.execute('SELECT * FROM data WHERE Gender=%s',(data,))
    elif searchby=="Salary":
        mycursor.execute('SELECT * FROM data WHERE Salary=%s',(data,))
    result = mycursor.fetchall()    
    return result
def updatedata(id,name,phone,role,gender,salary):
    mycursor.execute("UPDATE data SET Name = %s,Phone = %s,Role = %s,Gender = %s,Salary = %s WHERE Id = %s", (name, phone, role, gender, salary, id))
    conn.commit()
def delete(id):
    mycursor.execute('DELETE FROM data WHERE Id=%s',id)
    mycursor.fetchall()
    conn.commit()
def deleteall():
    mycursor.execute('Truncate table data')
    mycursor.fetchall()
    conn.commit()