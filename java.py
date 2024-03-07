import mysql.connector

mdb=mysql.connector.connect(
    host='localhost',
    username='root',
    password='abhi24ram',
    database='css',
)

mycr=mdb.cursor()
def List():
    mycr.execute("select * from data")
    r=mycr.fetchall()
    for i in r:
        print("\tName : ", i[0],"\tAge : ", i[1],"\tSalary : ", i[2])

def add():
    n_name=input("Enter Name: ")
    n_age=int(input("Enter Age: "))
    n_sal=int(input("Enter Salary: "))
    sql="insert into data values(%s, %s, %s)"
    val=(n_name,n_age,n_sal)
    mycr.execute(sql,val)
    mdb.commit()
    print("Employee added successfully!")

def edit():
    name=input("Enter the name")
    n_name=input("Enter Employee new Name: ")
    n_age=int(input("Enter Employee new Age: "))
    n_sal=int(input("Enter Employee new Salary: "))
    mycr.execute("update data set name=%s, age=%s, salary=%s where name=%s",(n_name,n_age,n_sal,name))
    mdb.commit()
    print("Employee information updated successfully!")

def delete():
    name=input("Enter the name")
    mycr.execute("delete from data where name=%s",(name,))
    mdb.commit()
    print("Employee deleted successfully!")
c=6
while c!=5:
    print("================================================================")
    c=int(input("Menu\nPlease select your input \n1.List\n2.Add\n3.Edit\n4.Delete\n5.Exit\nSelect your choice: "))
    if c==1:
        List()
    elif c==2:
        add()
    elif c==3:
        edit()
    elif c==4:
        delete()
if c==5:
    exit