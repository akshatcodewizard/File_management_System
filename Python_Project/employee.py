from tkinter import *  # package GUI application
from PIL import Image, ImageTk  # for image installation in the application
from tkinter import ttk, messagebox
import sqlite3
class employeeClass:  # class
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")  # for adjusting the height
        self.root.title("Inventory Management System")  # for title
        self.root.config(bg="white")  # for background color
        self.root.focus_force()

        # Variables
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()

        # Frame
        SearchFrame = LabelFrame(self.root, text="Search Employee", font=("Arial", 12, "bold"), bd=2, relief=RIDGE, bg="white")
        SearchFrame.place(x=250, y=20, width=600, height=70)

        # Search options
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby,
                                  values=("Select", "Email", "Name", "Contact"),
                                  state='readonly', justify=CENTER, font=("Arial", 12))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("Arial", 15), bg="lightgray")
        txt_search.place(x=200, y=10)

        # Search Button
        btn_search = Button(SearchFrame, text="Search" ,command=self.search,font=("Arial", 15), bg="#4caf50", fg="white", cursor="hand2")
        btn_search.place(x=430, y=10, width=150, height=25)

        # Title
        title = Label(self.root, text="Employee Details", font=("Arial", 15, "bold"), bg="lightblue", fg="black")
        title.place(x=50, y=100, width=1000)

        # Row 1
        Label(self.root, text="Emp ID", font=("Arial", 10), bg="white").place(x=50, y=150)
        Label(self.root, text="Gender", font=("Arial", 10), bg="white").place(x=350, y=150)
        Label(self.root, text="Contact", font=("Arial", 10), bg="white").place(x=750, y=150)

        Entry(self.root, textvariable=self.var_emp_id, font=("Arial", 10), bg="lightyellow").place(x=150, y=150, width=180)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender,
                                  values=("Select", "Male", "Female", "Other"),
                                  state='readonly', justify=CENTER, font=("Arial", 12))
        cmb_gender.place(x=500, y=150, width=180)
        cmb_gender.current(0)
        Entry(self.root, textvariable=self.var_contact, font=("Arial", 10), bg="lightyellow").place(x=850, y=150, width=180)

        # Row 2
        Label(self.root, text="Name", font=("Arial", 10), bg="white").place(x=50, y=190)
        Label(self.root, text="D.O.B", font=("Arial", 10), bg="white").place(x=350, y=190)
        Label(self.root, text="D.O.J", font=("Arial", 10), bg="white").place(x=750, y=190)

        Entry(self.root, textvariable=self.var_name, font=("Arial", 10), bg="lightyellow").place(x=150, y=190, width=180)
        Entry(self.root, textvariable=self.var_dob, font=("Arial", 10), bg="lightyellow").place(x=500, y=190, width=180)
        Entry(self.root, textvariable=self.var_doj, font=("Arial", 10), bg="lightyellow").place(x=850, y=190, width=180)

        # Row 3
        lbl_email=Label(self.root, text="Email", font=("Arial", 10), bg="white").place(x=50, y=230)
        lbl_password=Label(self.root, text="Password", font=("Arial", 10), bg="white").place(x=350, y=230)
        lbl_utype=Label(self.root, text="User Type", font=("Arial", 10), bg="white").place(x=750, y=230)

        txt_email = Entry(self.root, textvariable=self.var_email, font=("Arial", 10), bg="lightyellow").place(x=150, y=230, width=180)
        txt_pass  = Entry(self.root, textvariable=self.var_password, font=("Arial", 10), bg="lightyellow", show='*').place(x=500, y=230, width=180)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=("Admin", "Employee"),
                                 state='readonly', justify=CENTER, font=("Arial", 12))
        cmb_utype.place(x=850, y=230, width=180)
        cmb_utype.current(0)

        # Row 4
        lbl_address = Label(self.root, text="Address", font=("Arial", 10), bg="white").place(x=50, y=270)
        lbl_salary = Label(self.root, text="Salary", font=("Arial", 10), bg="white").place(x=500, y=270)

        self.txt_address = Text(self.root, font=("Arial", 10), bg="lightyellow")
        self.txt_address.place(x=150, y=270, width=300, height=60)
        txt_salary = Entry(self.root, textvariable=self.var_salary, font=("Arial", 10), bg="lightyellow").place(x=600, y=270, width=180)

        # Buttons
        btn_add = Button(self.root, text="Save" ,command=self.add ,font=("Arial", 15), bg="blue", fg="white", cursor="hand2")
        btn_add.place(x=500, y=305, width=110, height=28)

        btn_update = Button(self.root, text="Update",command=self.update,font=("Arial", 15), bg="green", fg="white", cursor="hand2")
        btn_update.place(x=620, y=305, width=110, height=28)

        btn_delete = Button(self.root, text="Delete",command=self.delete, font=("Arial", 15), bg="red", fg="white", cursor="hand2")
        btn_delete.place(x=740, y=305, width=110, height=28)

        btn_clear = Button(self.root, text="Clear" ,command=self.clear ,font=("Arial", 15), bg="gray", fg="white", cursor="hand2")
        btn_clear.place(x=860, y=305, width=110, height=28)
        
        
        #employee chart
        
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=150)
        
        scrolly = Scrollbar(emp_frame,orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)
        
        
        self.EmployeeTable = ttk.Treeview(emp_frame, columns=("eid", "name", "email", "gender", "contact", "dob", "doj","pass", "utype", "address", "salary"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        
        self.EmployeeTable.heading("eid", text = "EMP ID")
        self.EmployeeTable.heading("name", text = "NAME")
        self.EmployeeTable.heading("email", text = "EMAIL")
        self.EmployeeTable.heading("gender", text = "GENDER")
        self.EmployeeTable.heading("contact", text = "CONTACT")
        self.EmployeeTable.heading("dob", text = "DOB")
        self.EmployeeTable.heading("doj", text = "DOJ")
        self.EmployeeTable.heading("pass", text = "PASSWORD")
        self.EmployeeTable.heading("utype", text = "USER TYPE")
        self.EmployeeTable.heading("address", text = "ADDRESS")
        self.EmployeeTable.heading("salary", text = "SALARY")
        
        
        
        self.EmployeeTable["show"] = "headings"
        
        self.EmployeeTable.column("eid", width=90)
        self.EmployeeTable.column("name", width=90)
        self.EmployeeTable.column("email", width=90)
        self.EmployeeTable.column("gender", width=90)
        self.EmployeeTable.column("contact", width=90)
        self.EmployeeTable.column("dob", width=90)
        self.EmployeeTable.column("doj", width=90)
        self.EmployeeTable.column("pass", width=90)
        self.EmployeeTable.column("utype", width=90)
        self.EmployeeTable.column("address", width=90)
        self.EmployeeTable.column("salary",width=90)
        
        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data) #event
        
        
        self.show()

#Function for database 
    
    def add(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error", "Employee ID Must be required", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?", (self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!= None:
                    messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)      
                else:
                    cur.execute("Insert into employee (eid ,name ,email, gender ,contact ,dob ,doj ,pass ,utype ,address ,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                            self.var_emp_id.get(),
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),

                            self.var_dob.get(),
                            self.var_doj.get(),
                            
                            self.var_password.get(),
                            self.var_utype.get(),
                            self.txt_address.get('1.0', END),
                            self.var_salary.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Addedd Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")    
    
    
    #Show
    
    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            row=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in row:
                self.EmployeeTable.insert('', END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)      
        
    #retrive the data chart
    def get_data(self, ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        
        #retrive the content row by row
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
                            
        self.var_password.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[9])
        self.var_salary.set(row[10])
            
            
            
    
    def update(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error", "Employee ID Must be required", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?", (self.var_emp_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalide Employee ID", parent=self.root)      
                else:
                    cur.execute("UPDATE employee SET name=?, email=?, gender=?, contact=?, dob=?, doj=?, pass=?, utype=?, address=?, salary=? WHERE eid=?", (
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_password.get(),
                        self.var_utype.get(),
                        self.txt_address.get('1.0', END),  
                        self.var_salary.get(),
                        self.var_emp_id.get(),  
                        ))

                    con.commit()
                    messagebox.showinfo("Success", " Employee Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")    
            
    
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID Must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                
                if row is None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)      
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op:
                        cur.execute("DELETE FROM employee WHERE eid = ?", (self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Employee Deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    
    
    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
                            
        self.var_password.set("")
        self.var_utype.set("Admin")
        self.txt_address.delete('1.0', END)
        self.var_salary.set("")           
        
        self.show()
        
        
    
    def search(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select Search By option", parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error", "Search intput will be required", parent=self.root)
                
            else:
                query = f"SELECT * FROM employee WHERE {self.var_searchby.get()} LIKE ?"
                cur.execute(query, ('%' + self.var_searchtxt.get() + '%',))
                row=cur.fetchall()
                if len(row)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in row:
                        self.EmployeeTable.insert('', END,values=row)
                else:
                    messagebox.showerror("Error", "No record found !!!", parent=self.root)        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)   
            
             
# Object
if __name__ == "__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()
