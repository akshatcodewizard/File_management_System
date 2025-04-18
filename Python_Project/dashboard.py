from tkinter import* #package GUI application 
from PIL import Image, ImageTk #for image installation in the application
from employee import employeeClass
from supplier import supplierClass
class IMS: #class
    def __init__(self, root): 
        self.root=root
        self.root.geometry("1350x700+0+0") #for adjust the hight
        self.root.title("Inventory management system") #for title
        self.root.config(bg="white") #for background color
        
        
        #title
        self.icon_title=PhotoImage(file = "image/logo1.png")
        title=Label(self.root,text="Inventory System", image=self.icon_title, compound=LEFT, 
        font=("roboto", 30, "bold"), bg="white", fg="black", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=70) #Header title design
        
        
        #button
        btn_logout= Button(self.root, text="Logout", font=("times new roman", 15, "bold"),
        bg="black", fg="white", cursor= "hand2").place(x=1150, y=10, height=50, width=150)
        
        
        #Timer_clock
        self.lbl_clock = Label(self.root,text="Management In-Box \t\t Date: DD-MM-YYYY \t\t Time: HH:MM:SS",
        font=("roboto", 10), bg="light blue", fg="black")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30) #Management Dashboard
        
        
        #left menu
        self.MenuLogo=Image.open("image/logo2.png")
        
        self.MenuLogo=self.MenuLogo.resize((255,255),  Image.Resampling.LANCZOS) #for resiz the image 
        #(ANTIALIAS no longer in Pillow version 10.0.0. so we use Image.Resampling.LANCZOS)
        
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root, bd=2, relief=RIDGE, bg= "white")
        LeftMenu.place(x=0, y=102, width=250, height=565)
        
        lbl_menulogo=Label(LeftMenu, image=self.MenuLogo)
        lbl_menulogo.pack(side=TOP, fill=X)
        
        
        #Option Button
        lbl_menu = Label(LeftMenu, text="Management Menu",font=("roboto", 15, "bold"),bg="sky blue").pack(side=TOP, fill=X)
        
        btn_employee = Button(LeftMenu, text="Employee",anchor="w",command=self.employee
        , font=("roboto", 15, "bold"),bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X) #Button_1
        
        btn_supplier = Button(LeftMenu, text="Supplier",anchor="w", command=self.supplier
        , font=("roboto", 15, "bold"),bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X) #Button_2
        
        btn_category = Button(LeftMenu, text="Category",anchor="w"
        , font=("roboto", 15, "bold"),bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X) #Button_3
        
        btn_exit = Button(LeftMenu, text="Exit",anchor="w"
        , font=("roboto", 15, "bold"),bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X) #Button_4
        
        
        #Content
        self.lbl_employee = Label(self.root, text="Total Employee\n[ 0 ]", bd=5
       , relief=RIDGE, bg="light blue", fg="black", font=("roboto", 20, "bold"))
        self.lbl_employee.place(x=300, y=120, height=150, width=300)
        
        self.lbl_supplier = Label(self.root, text="Total Supplier\n[ 0 ]", bd=5
       , relief=RIDGE, bg="light gray", fg="black", font=("roboto", 20, "bold"))
        self.lbl_supplier.place(x=650, y=120, height=150, width=300)
        
        self.lbl_category = Label(self.root, text="Total Category\n[ 0 ]", bd=5
       , relief=RIDGE, bg="orange", fg="black", font=("roboto", 20, "bold"))
        self.lbl_category.place(x=1000, y=120, height=150, width=300)
        
        
        
        #Footer
        lbl_footer = Label(self.root,text="IMS-Inventory Management System\n By XAnanta",
        font=("roboto", 12), bg="light blue", fg="white").pack(side=BOTTOM, fill=X)

    
    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)
        
    
    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)    

        
#Object
if __name__ == "__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()    