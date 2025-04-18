from tkinter import *  # package GUI application
from PIL import Image, ImageTk  # for image installation in the application
from tkinter import ttk, messagebox
import sqlite3

class supplierClass:  # class
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")  # for adjusting the height
        self.root.title("Inventory Management System")  # for title
        self.root.config(bg="white")  # for background color
        self.root.focus_force()

        # Variables
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        
        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()
        
 

        # Frame
        SearchFrame = LabelFrame(self.root, text="Search Employee", font=("Arial", 12, "bold"), bd=2, relief=RIDGE, bg="white")
        SearchFrame.place(x=250, y=20, width=600, height=70)

        # Search options
        lbl_search = Label(SearchFrame,text="Search by Invoice No.",bg="white",font=("Arial", 12))
        lbl_search.place(x=10, y=10)
        
        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("Arial", 15), bg="lightgray")
        txt_search.place(x=200, y=10)

        # Search Button
        btn_search = Button(SearchFrame, text="Search",command=self.search,font=("Arial", 15), bg="#4caf50", fg="white", cursor="hand2")
        btn_search.place(x=430, y=10, width=150, height=25)

        # Title
        title = Label(self.root, text="Supplier Details", font=("Arial", 15, "bold"), bg="lightblue", fg="black")
        title.place(x=50, y=100, width=1000)

        # Row 1
        lbl_supplier_invoice=Label(self.root, text="Emp ID", font=("Arial", 10), bg="white").place(x=50, y=150)
        txt_supplier_invoice=Entry(self.root, textvariable=self.var_sup_invoice, font=("Arial", 10), bg="lightyellow").place(x=150, y=150, width=180)

        # Row 2
        Label(self.root, text="Name", font=("Arial", 10), bg="white").place(x=50, y=190)
        Entry(self.root, textvariable=self.var_name, font=("Arial", 10), bg="lightyellow").place(x=150, y=190, width=180)

        # Row 3
        lbl_contact=Label(self.root, text="Contact", font=("Arial", 10), bg="white").place(x=50, y=230)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("Arial", 10), bg="lightyellow").place(x=150, y=230, width=180)

        # Row 4
        lbl_desc = Label(self.root, text="Description", font=("Arial", 10), bg="white").place(x=50, y=270)
        self.txt_decs = Text(self.root, font=("Arial", 10), bg="lightyellow")
        self.txt_decs.place(x=150, y=270, width=300, height=60)

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
        
        
        self.supplierTable = ttk.Treeview(emp_frame, columns=("invoice", "name", "contact", "desc"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        
        self.supplierTable.heading("invoice", text = "Emp ID")
        self.supplierTable.heading("name", text = "Name")
        self.supplierTable.heading("contact", text = "Contact")
        self.supplierTable.heading("desc", text = "Description")
        
        
        self.supplierTable["show"] = "headings"
        
        self.supplierTable.column("invoice", width=90)
        self.supplierTable.column("name", width=90)
        self.supplierTable.column("contact", width=90)
        self.supplierTable.column("desc", width=90)  
        self.supplierTable.pack(fill=BOTH, expand=1)
        self.supplierTable.bind("<ButtonRelease-1>", self.get_data) #event
        
        
        self.show()

#Function for database 
    
    def add(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error", "Invoice must be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?", (self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!= None:
                    messagebox.showerror("Error! Invoice no already already assignedn try different", parent=self.root)      
                else:
                    cur.execute("Insert into supplier (invoice ,name ,contact, desc) values(?,?,?,?)",
                                
                        ( self.var_sup_invoice.get(), 
                          self.var_name.get(), 
                          self.var_contact.get(), 
                          self.txt_decs.get('1.0', END)
                    ))
                    
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Addedd Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")    
    
    
    #Show
    
    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            row=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in row:
                self.supplierTable.insert('', END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)      
        
    #retrive the data chart
    def get_data(self, ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
        
        #retrive the content row by row
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_decs.delete('1.0', END)
        self.txt_decs.insert(END, row[3])
            
            
            
    
    def update(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error", "Invoice no Must be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?", (self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalide Invoice no.", parent=self.root)      
                else:
                    cur.execute("UPDATE supplier SET name=?, contact=?, desc=? WHERE invoice=?", (
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_decs.get('1.0', END),  
                        self.var_sup_invoice.get(),  
                        ))

                    con.commit()
                    messagebox.showinfo("Success", " Supplier Updated Successfully", parent=self.root)
                    self.show()
                    
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)    
            
    
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice no. Must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice = ?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                
                if row is None:
                    messagebox.showerror("Error", "Invalid Invoice no. ", parent=self.root)      
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op:
                        cur.execute("DELETE FROM supplier WHERE invoice = ?", (self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Supplier Deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    
    
    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_decs.delete('1.0', END)
        self.var_searchtxt.set("")
       
        self.show()
        
        
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
          
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error", "Search invoice no. should be required", parent=self.root)
                
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('', END,values=row)
                else:
                    messagebox.showerror("Error", "No record found !!!", parent=self.root)        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)   
            
             
# Object
if __name__ == "__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()
