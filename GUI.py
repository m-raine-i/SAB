import json
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

queries = []
file_path = ""

def load_queries():
    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if file_path:
        try:
            with open(file_path) as f:
                data = json.load(f)
                return data, file_path
        except Exception as e:
            messagebox.showerror("Error", str(e))

def save_queries():
    if queries and file_path:
        try:
            with open(file_path, "w") as f:
                json.dump(queries, f, indent=4)
                messagebox.showinfo("Success", "Queries saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Warning", "No queries to save or file path not set.")

def add_query():
    query = query_entry.get()
    response = response_entry.get()
    qr_code_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg"), ("PNG Files", "*.png")])
    
    if query and response:
        query_data = {"query": query, "response": response}
        if qr_code_path:
            query_data["qr_code_path"] = qr_code_path
        queries.append(query_data)
        update_listbox()

def update_listbox():
    query_listbox.delete(0, tk.END)
    for query_data in queries:
        query_listbox.insert(tk.END, query_data["query"])

    query_listbox.bind("<<ListboxSelect>>", select_query)

def select_query(event):
    selected_index = query_listbox.curselection()
    if selected_index:
        selected_query = query_listbox.get(selected_index)
        for query_data in queries:
            if query_data["query"] == selected_query:
                query_entry.delete(0, tk.END)
                response_entry.delete(0, tk.END)
                query_entry.insert(tk.END, query_data["query"])
                response_entry.insert(tk.END, query_data["response"])
                qr_code_path_label_value.configure(text=query_data.get("qr_code_path", ""))
                break

def update_query():
    selected_query = query_listbox.get(tk.ACTIVE)
    new_query = query_entry.get()
    new_response = response_entry.get()
    if selected_query and new_query and new_response:
        for query_data in queries:
            if query_data["query"] == selected_query:
                query_data["query"] = new_query
                query_data["response"] = new_response
                if "qr_code_path" in query_data:
                    qr_code_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
                    if qr_code_path:
                        query_data["qr_code_path"] = qr_code_path
                break
        update_listbox()

def delete_query():
    selected_query = query_listbox.get(tk.ACTIVE)
    if selected_query:
        for query_data in queries:
            if query_data["query"] == selected_query:
                queries.remove(query_data)
                break
        update_listbox()
        query_entry.delete(0, tk.END)
        response_entry.delete(0, tk.END)
        qr_code_path_label.configure(text="")

def change_json_file():
    global queries, file_path
    queries, file_path = load_queries()
    if not queries:
        queries = []
    update_listbox()

def initialize_gui():
    global queries, file_path, query_listbox, query_entry, response_entry, qr_code_path_label, qr_code_path_label_value

    queries, file_path = load_queries()
    if not queries:
        queries = []

    root = tk.Tk()
    root.title('List of Queries')
    root.geometry("800x480")
    root.configure(bg='Maroon')

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=0)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=0)

    input_frame = LabelFrame(root, text='Student Assistant Bot (SAB)', bg="lightgray", font=('Consolas', 14))
    input_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    query_label = Label(input_frame, text="Query", font=('Consolas', 14))
    query_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    query_entry = Entry(input_frame, width=40, borderwidth=2, fg="black", font=('Consolas', 14))
    query_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    response_label = Label(input_frame, text="Response", font=('Consolas', 14))
    response_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    response_entry = Entry(input_frame, width=40, borderwidth=2, fg="black", font=('Consolas', 14))
    response_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    qr_code_path_label = Label(input_frame, text="QR Code \n File Path", font=('Consolas', 12))
    qr_code_path_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    qr_code_path_label_value = Label(input_frame, text="", font=('Consolas', 10))
    qr_code_path_label_value.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    query_listbox = tk.Listbox(root, width=80, height=10, font=('Consolas', 14))
    query_listbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    button_frame = Frame(root, bg="Maroon")
    button_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

    add_button = tk.Button(button_frame, text="Add Query", width=15, height=2, font=('Consolas', 10), command=add_query)
    add_button.pack(side="top", pady=5)

    update_button = tk.Button(button_frame, text="Update Query", width=15, height=2, font=('Consolas', 10), command=update_query)
    update_button.pack(side="top", pady=5)

    delete_button = tk.Button(button_frame, text="Delete Query", width=15, height=2, font=('Consolas', 10), command=delete_query)
    delete_button.pack(side="top", pady=5)

    save_button = tk.Button(button_frame, text="Save Queries", width=15, height=2, font=('Consolas', 10), command=save_queries)
    save_button.pack(side="top", pady=5)

    change_json_button = tk.Button(button_frame, text="Change JSON File", width=15, height=2, font=('Consolas', 10), command=change_json_file)
    change_json_button.pack(side="top", pady=5)

    update_listbox()

    root.mainloop()
    
    
if __name__ == '__main__':
    initialize_gui()
