#DataFlair- import modules
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
from pymongo import MongoClient


# f=open("Proj_Database",'a+')
client = MongoClient("mongodb://localhost:27017/")
db = client["shop_db"]
collection = db["items"]

root = Tk()
root.title("Shop Managment System by DataFlair")
root.configure(width=1500,height=1000,bg="#e3f4f1")
var=-1
root.minsize(800,600);

#DataFlair- function to add items

def Add_Items():
    item_name = Entry_1.get();
    item_prize = Entry_2.get();
    item_quantity = Entry_3.get();
    item_category = Entry_4.get();
    item_discount = Entry_5.get();

    if item_name:
        item = {"name": item_name, "price": int(item_prize),"quantity": int(item_quantity),"category":item_category,"discount": int(item_discount)}
        collection.insert_one(item)
    messagebox.showinfo("ADD ITEM", "ITEM ADDED SUCCESSFULLY....!!!!!")



#DataFlair- function to delete items

def Delete_Items():
    selected_item = item_list.get(tk.ACTIVE)
    if selected_item:
        item_name = selected_item.split(" - ")[0]
        collection.delete_one({"name": item_name})
        messagebox.showinfo("Success", "Item deleted!")



    


def display():
    item_list.delete(0, tk.END)
    items = collection.find()
    for item in items:
        item_list.insert(tk.END, f"{item['name']} - {item['price']} - {item['quantity']} - {item['category']} - {item['discount']}")

        

    
    
    

def update_item():
    selected_item = item_list.get(tk.ACTIVE)
    if selected_item:
        item_name = Entry_1.get()
        new_price = Entry_2.get()
        new_quantity = Entry_3.get()
        new_category = Entry_4.get()
        new_discount = Entry_5.get()




        if new_quantity.isdigit() and item_name and new_category and new_price and new_discount:
            item_name = selected_item.split(" - ")[0]
            # collection.update_one( {"name": item_name},{"$set": {"price": new_price}}, {"$set": {"quantity": int(new_quantity)}},{"$set": {"category": new_category}},{"$set": {"discount": new_discount}});
            collection.update_one({"name": item_name},{"$set": {"price": new_price}|{"quantity": int(new_quantity)}|{"category": new_category}|{"discount": new_discount}})
            messagebox.showinfo("Success", "Item quantity updated!")

def Search_Item():
    Entry_1.delete(0, END)
   



def Clear_Item():
    Entry_1.delete(0, END)
    

def Exit():
    Exit= messagebox.askyesno("Exit the System","Do you want to Exit(y/n)?")
    if Exit > 0:
        root.destroy()
        return


#All labels Entrys Button grid place
Label_0= Label(root,text="SHOP MANAGEMENT SYSTEM BY DATAFLAIR ",fg="black",font=("Times new roman", 30, 'bold'))
Label_0.grid(columnspan=6)

Label_1=Label(root,text="ENTER ITEM NAME",bg="#e8c1c7",fg="black",bd=8,font=("Times new roman", 12, 'bold'),width=25)
Label_1.grid(row=1,column=0)
Entry_1=Entry(root, font=("Times new roman", 14),bd=8,width=25)
Entry_1.grid(row=1,column=1)

Label_2=Label(root, text="ENTER ITEM PRICE",height="1",bg="#e8c1c7",bd=8,fg="black", font=("Times new roman", 12, 'bold'),width=25)
Label_2.grid(row=2,column=0)
Entry_2= Entry(root, font=("Times new roman", 14),bd=8,width=25)
Entry_2.grid(row=2,column=1)

Label_3=Label(root, text="ENTER ITEM QUANTITY",bg="#e8c1c7",bd=8,fg="black", font=("Times new roman", 12, 'bold'),width=25)
Label_3.grid(row=3,column=0)
Entry_3= Entry(root, font=("Times new roman", 14),bd=8,width=25)
Entry_3.grid(row=3,column=1)

Label_4=Label(root, text="ENTER ITEM CATEGORY",bg="#e8c1c7",bd=8,fg="black", font=("Times new roman", 12, 'bold'),width=25)
Label_4.grid(row=4,column=0)
Entry_4= Entry(root, font=("Times new roman", 14),bd=8,width=25)
Entry_4.grid(row=4,column=1)

Label_5=Label(root, text="ENTER ITEM DISCOUNT",bg="#e8c1c7",fg="black",bd=8, font=("Times new roman", 12, 'bold'),width=25)
Label_5.grid(row=5,column=0, padx=10, pady=10)
Entry_5= Entry(root, font=("Times new roman", 14),bd=8,width=25)
Entry_5.grid(row=5,column=1, padx=10, pady=10)

Label_6=Label(root, text="ENTER ITEM Update",bg="#e8c1c7",fg="black",bd=8, font=("Times new roman", 12, 'bold'),width=25)
Label_6.grid(row=6,column=0, padx=10, pady=10)
Entry_6=Entry(root, font=("Times new roman", 14),bd=8,width=25)
Entry_6.grid(row=6,column=1, padx=10, pady=10)

 
app = tk.Tk();
item_list = tk.Listbox(app, font=("Arial", 12))
item_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)



Button_1= Button(root,text="ADD ITEM",bd=8, bg="#49D810", fg="black", width=25, font=("Times new roman", 12),command=Add_Items)
Button_1.grid(row=6,column=0, padx=10, pady=10)
Button_2= Button(root, text="DELETE ITEM",bd=8, bg="#49D810", fg="black", width =25, font=("Times new roman", 12),command=Delete_Items)
Button_2.grid(row=6,column=1, padx=40, pady=10)
Button_3= Button(root, text="VIEW DATABASE",bd=8, bg="#49D810", fg="black", width =25, font=("Times new roman", 12),command=display)
Button_3.grid(row=3,column=3, padx=40, pady=10)
Button_4= Button(root, text="SEARCH ITEM",bd=8, bg="#49D810", fg="black", width =25, font=("Times new roman", 12),command=Search_Item)
Button_4.grid(row=2,column=3, padx=40, pady=10)
Button_5= Button(root, text="CLEAR SCREEN",bd=8, bg="#49D810", fg="black", width=25, font=("Times new roman", 12),command=Clear_Item)
Button_5.grid(row=4,column=3, padx=40, pady=10)


Button_6= Button(root,highlightcolor="blue",activebackground="red", text="Exit",bd=8, bg="#FF0000", fg="#EEEEF1", width=25, font=("Times", 40),command=Exit)
Button_6.place(x=310,y=450,height= 102,width=245)

Button_7= Button(root,text="UPDATE",bd=8, bg="#49D810", fg="black", width=25, font=("Times new roman", 12),command=update_item)
Button_7.place(x=620,y=337,height= 102,width=245)

Entry_6= Entry(root, font=("Times new roman", 14),justify='left',bd=8,width=25)
Entry_6.grid(row=1,column=3, padx=10, pady=10)

root.mainloop()
