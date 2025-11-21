import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

# Establish connection to MySQL
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Aryu@118',
            database='Garhwali_Dict'
        )
        print("Connected to database successfully!")
        return connection
    except Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")
        return None

# Function to search for a word
def find_entry():
    word = entry_word.get()
    if not word:
        messagebox.showwarning("Input Error", "Please enter a word!")
        return

    connection = create_connection()
    if not connection:
        return
    
    cursor = connection.cursor()
    query = "SELECT * FROM dictionary WHERE English_word = %s"
    cursor.execute(query, (word,))
    output = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    if output:
        result = f"Hindi: {output[0][2]}\nGarhwali: {output[0][1]}"
        label_result.config(text=result)
    else:
        messagebox.showinfo("Not Found", f"No entry found for '{word}'.")

# Function to add a word
def add_word():
    Gword = entry_garhwali.get()
    Hword = entry_hindi.get()
    Eword = entry_english.get()

    if not (Gword and Hword and Eword):
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    connection = create_connection()
    if not connection:
        return

    cursor = connection.cursor()
    query = "INSERT INTO dictionary(Garhwali_Word, Hindi_Word, English_Word) VALUES (%s, %s, %s)"
    
    try:
        cursor.execute(query, (Gword, Hword, Eword))
        connection.commit()
        messagebox.showinfo("Success", "Word added successfully!")
    except Error as e:
        messagebox.showerror("Error", f"Failed to add word: {e}")
    
    cursor.close()
    connection.close()

# Function to remove a word
def remove_word():
    Rword = entry_word.get()
    if not Rword:
        messagebox.showwarning("Input Error", "Enter a word to remove!")
        return

    connection = create_connection()
    if not connection:
        return

    cursor = connection.cursor()
    query = "DELETE FROM dictionary WHERE English_word = %s"
    
    try:
        cursor.execute(query, (Rword,))
        connection.commit()
        messagebox.showinfo("Success", "Entry removed successfully!")
    except Error as e:
        messagebox.showerror("Error", f"Failed to remove entry: {e}")
    
    cursor.close()
    connection.close()

# Create the GUI Window
root = tk.Tk()
root.title("Garhwali Dictionary")
root.geometry("400x400")

# Search section
tk.Label(root, text="Search English Word:").pack()
entry_word = tk.Entry(root)
entry_word.pack()
tk.Button(root, text="Find Word", command=find_entry).pack()

# Result Label
label_result = tk.Label(root, text="", fg="blue")
label_result.pack()

# Add new word section
tk.Label(root, text="Add New Word").pack()
tk.Label(root, text="Garhwali:").pack()
entry_garhwali = tk.Entry(root)
entry_garhwali.pack()

tk.Label(root, text="Hindi:").pack()
entry_hindi = tk.Entry(root)
entry_hindi.pack()

tk.Label(root, text="English:").pack()
entry_english = tk.Entry(root)
entry_english.pack()

tk.Button(root, text="Add Word", command=add_word).pack()

# Remove word section
tk.Button(root, text="Remove Word", command=remove_word, fg="red").pack()

# Run the GUI
root.mainloop()
