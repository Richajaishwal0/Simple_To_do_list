from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
def insert():
    id=e_id.get()
    name=e_name.get()
    phone=e_phone.get()
    if (id=="" or name=="" or phone ==""):
        MessageBox.showinfo("Status", "All fields are required")
    else:
        con=mysql.connect(host="localhost", user="root", password="#####", database="py_tkinter")
        cur=con.cursor()
        cur.execute("insert into Flight values('"+ id +"','"+ name +"','"+ phone +"')")
        cur.execute("commit");
        e_id.delete(0, 'end')
        e_name.delete(0,'end')
        e_phone.delete(0, 'end')
        show()
        MessageBox.showinfo("Status","Inserted succesfully");
        con.close();
def delete():
    if (e_id.get()== ""):
        MessageBox.showinfo("Status","no id given")
    else:
        con=mysql.connect(host="localhost", user="root", password="#####", database="py_tkinter")
        cur=con.cursor()
        cur.execute("delete from Flight where id ='"+ e_id.get() +"'")
        cur.execute("commit");
        e_id.delete(0, 'end')
        e_name.delete(0,'end')
        e_phone.delete(0, 'end')
        show()
        MessageBox.showinfo("Status","Deleted succesfully");
        con.close();
def update():
    id=e_id.get()
    name=e_name.get()
    phone=e_phone.get()
    if (id=="" or name=="" or phone ==""):
        MessageBox.showinfo("Status", "All fields are required")
    else:
        con=mysql.connect(host="localhost", user="root", password="#####", database="py_tkinter")
        cur=con.cursor()
        cur.execute("update Flight set name='"+name+"',phone='"+phone+"',id='"+id+"'")
        cur.execute("commit");
        e_id.delete(0, 'end')
        e_name.delete(0,'end')
        e_phone.delete(0, 'end')
        show()
        MessageBox.showinfo("Status","Updated successfully succesfully");
        con.close();
def get():
    if (e_id.get()== ""):
        MessageBox.showinfo("Status","no id given")
    else:
        con=mysql.connect(host="localhost", user="root", password="#####", database="py_tkinter")
        cur=con.cursor()
        cur.execute("select * from  Flight where id ='"+ e_id.get() +"'")
        rows=cur.fetchall()
        MessageBox.showinfo("Status","processing succesfully");
        con.close();
        for row in rows:
            e_name.insert(0,row[1])
            e_phone.insert(0,row[2])
def show():
     con=mysql.connect(host="localhost", user="root", password="#####", database="py_tkinter")
     cur=con.cursor()
     cur.execute("select * from Flight ")
     rows=cur.fetchall()
     list.delete(0,list.size())

     for row in rows:
         insertData=str(row[0])+ "           "+row[1]
         list.insert(list.size()+1, insertData)
     con.close()
    
root = Tk()
root.geometry("600x400")
root.title("Flight")
id = Label(root,text="Enter id", font=('bold', 10))
id.place(x=20, y=30);
id = Label(root,text="Enter name", font=('bold', 10))
id.place(x=20, y=60);
id = Label(root,text="Enter phone number", font=('bold', 10))
id.place(x=20, y=90);
e_id=Entry()
e_id.place(x=150, y=30);
e_name=Entry()
e_name.place(x=150, y=60);
e_phone=Entry()
e_phone.place(x=150, y=90);

insert=Button(root, text="Insert", font=("italic", 10), bg="white", command=insert)
insert.place(x=20, y=140);

get=Button(root, text="get", font=("italic", 10), bg="white", command=get)
get.place(x=70, y=140);

update=Button(root, text="Update", font=("italic", 10), bg="white", command=update)
update.place(x=120, y=140);

delete=Button(root, text="Delete", font=("italic", 10), bg="white", command=delete)
delete.place(x=190, y=140);

list=Listbox(root)
list.place(x=290, y=30)
show()
root.mainloop()
