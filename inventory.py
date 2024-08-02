import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["inventory_db"]
collection = db["items"]

def add_item():
    item_name = name_entry.get()
    item_quantity = quantity_entry.get()

    if item_name and item_quantity:
        item = {"name": item_name, "quantity": int(item_quantity)}
        collection.insert_one(item)
        name_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
        display_items()
        messagebox.showinfo("Success", "Item added to inventory!")

def update_item():
    selected_item = item_list.get(tk.ACTIVE)
    if selected_item:
        new_quantity = updated_quantity_entry.get()
        if new_quantity and new_quantity.isdigit():
            item_name = selected_item.split(" - ")[0]
            collection.update_one({"name": item_name}, {"$set": {"quantity": int(new_quantity)}})
            display_items()
            messagebox.showinfo("Success", "Item quantity updated!")

def delete_item():
    selected_item = item_list.get(tk.ACTIVE)
    if selected_item:
        item_name = selected_item.split(" - ")[0]
        collection.delete_one({"name": item_name})
        display_items()
        messagebox.showinfo("Success", "Item deleted!")

def display_items():
    item_list.delete(0, tk.END)
    items = collection.find()
    for item in items:
        item_list.insert(tk.END, f"{item['name']} - {item['quantity']}")

app = tk.Tk()
app.title("Inventory Management System")

# Set the window size and background color
app.geometry("800x500")
app.configure(bg="lightblue")  # Set the background color

# Create a style for buttons with rounded corners
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10, relief=tk.RAISED, borderwidth=5, bordercolor="gray")
style.map("TButton", foreground=[("active", "black")])

name_label = ttk.Label(app, text="Item Name", font=("Arial", 12))
name_label.pack(pady=10)
name_entry = ttk.Entry(app, font=("Arial", 12))
name_entry.pack(pady=5)

quantity_label = ttk.Label(app, text="Quantity", font=("Arial", 12))
quantity_label.pack()
quantity_entry = ttk.Entry(app, font=("Arial", 12))
quantity_entry.pack(pady=5)

add_button = ttk.Button(app, text="Add Item", command=add_item)
add_button.pack(pady=10)

display_button = ttk.Button(app, text="Display Items", command=display_items)
display_button.pack()

update_label = ttk.Label(app, text="Update Quantity", font=("Arial", 12))
update_label.pack(pady=10)
updated_quantity_entry = ttk.Entry(app, font=("Arial", 12))
updated_quantity_entry.pack(pady=5)

update_button = ttk.Button(app, text="Update Item", command=update_item)
update_button.pack(pady=10)

delete_button = ttk.Button(app, text="Delete Item", command=delete_item)
delete_button.pack()

item_list = tk.Listbox(app, font=("Arial", 12))
item_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

app.mainloop()
