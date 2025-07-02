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