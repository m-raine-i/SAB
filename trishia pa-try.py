from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog
import os
from os import listdir, remove
from os.path import isfile, join
import uuid
import json

global queries
global file_path

queries = []
file_path = ""

def initialize_gui():
    global main_frame, left_frame, right_frame
    global crm_tag, crm_patterns, crm_responses, crm_qr_code, crm_id
    global trv, id_value

    root.title('List of Intents')
    root.geometry("1000x650")
    root.configure(bg='Maroon')

    main_frame = Frame(root, bg="Maroon")
    main_frame.pack(fill=BOTH, expand=True)

    left_frame = LabelFrame(main_frame, text='Student Assistant Bot (SAB)', bg="LightGray", font=('Consolas', 14))
    left_frame.pack(side=LEFT, padx=5, pady=5, fill=BOTH, expand=True)

    right_frame = LabelFrame(main_frame, text='', bg="Maroon", font=('Consolas', 14))
    right_frame.pack(side=RIGHT, padx=5, pady=5, fill=BOTH)

    Label(left_frame, text="ID", font=('Consolas', 14)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    Label(left_frame, text="Tag", font=('Consolas', 14)).grid(row=1, column=0, padx=5, pady=5, sticky="w")
    Label(left_frame, text="Patterns", font=('Consolas', 14)).grid(row=2, column=0, padx=5, pady=5, sticky="w")
    Label(left_frame, text="Responses", font=('Consolas', 14)).grid(row=3, column=0, padx=5, pady=5, sticky="w")
    Label(left_frame, text="QR Codes", font=('Consolas', 14)).grid(row=4, column=0, padx=5, pady=5, sticky="w")

    id_value = StringVar()
    id_value.set(str(uuid.uuid4()))
    crm_id = Label(left_frame, width=70, borderwidth=2, fg="black", textvariable=id_value, font=('Consolas', 14))
    crm_id.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    crm_tag = Entry(left_frame, width=70, borderwidth=2, fg="black", font=('Consolas', 14))
    crm_tag.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    crm_patterns = Entry(left_frame, width=70, borderwidth=2, fg="black", font=('Consolas', 14))
    crm_patterns.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    crm_responses = Entry(left_frame, width=70, borderwidth=2, fg="black", font=('Consolas', 14))
    crm_responses.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    crm_qr_code = Label(left_frame, width=70, borderwidth=2, fg="black", font=('Consolas', 14))
    crm_qr_code.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    trv = ttk.Treeview(right_frame, columns=(1, 2, 3, 4, 5), show="headings", height=16)
    trv.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    trv.heading(1, text="ID", anchor="center")
    trv.heading(2, text="Tag", anchor="center")
    trv.heading(3, text="Patterns", anchor="center")
    trv.heading(4, text="Responses", anchor="center")
    trv.heading(5, text="QR Codes", anchor="center")

    trv.column("#1", anchor="w", width=30, stretch=True)
    trv.column("#2", anchor="w", width=140, stretch=False)
    trv.column("#3", anchor="w", width=300, stretch=False)
    trv.column("#4", anchor="w", width=300, stretch=False)
    trv.column("#5", anchor="w", width=200, stretch=False)

    btnLoadJSON = Button(right_frame, text="Load JSON", width=15, height=2, font=('Consolas', 10), command=load_json_from_file)
    btnLoadJSON.pack(side=TOP, pady=5)

    btnSaveJSON = Button(right_frame, text="Save JSON", width=15, height=2, font=('Consolas', 10), command=save_json_to_file)
    btnSaveJSON.pack(side=TOP, pady=5)

    btnAdd = Button(right_frame, text="Add", width=15, height=2, font=('Consolas', 10), command=add_entry)
    btnAdd.pack(side=TOP, pady=5)

    btnUpdate = Button(right_frame, text="Update", width=15, height=2, font=('Consolas', 10), command=update_entry)
    btnUpdate.pack(side=TOP, pady=5)

    btnDelete = Button(right_frame, text="Delete", width=15, height=2, font=('Consolas', 10), command=delete_entry)
    btnDelete.pack(side=TOP, pady=5)

    btnClear = Button(right_frame, text="Clear", width=15, height=2, font=('Consolas', 10), command=clear_all_fields)
    btnClear.pack(side=TOP, pady=5)

    btnChangeJSON = Button(right_frame, text="Change JSON File", width=15, height=2, font=('Consolas', 10), command=change_json_file)
    btnChangeJSON.pack(side=TOP, pady=5)

def load_json_from_file():
    global queries, file_path
    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if file_path:
        try:
            with open(file_path) as file_handler:
                queries = json.load(file_handler)["intents"]
                file_handler.close()
                load_trv_with_json()
        except Exception as e:
            messagebox.showerror("Error", str(e))

def save_json_to_file():
    global queries, file_path
    if queries and file_path:
        try:
            with open(file_path, "w") as file_handler:
                json.dump({"intents": queries}, file_handler, indent=4)
                file_handler.close()
                messagebox.showinfo("Success", "Queries saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Warning", "No queries to save or file path not set.")

def add_entry():
    global queries
    guid_value = id_value.get()
    tag = crm_tag.get()
    patterns = crm_patterns.get()
    responses = crm_responses.get()
    qr_code_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png")])

    if len(tag) == 0:
        change_background_color("#FFB2AE")
        return

    process_request("_INSERT_", guid_value, tag, patterns, responses, qr_code_path)

def update_entry():
    global queries
    guid_value = id_value.get()
    tag = crm_tag.get()
    patterns = crm_patterns.get()
    responses = crm_responses.get()
    qr_code_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png")])

    if len(tag) == 0:
        change_background_color("#FFB2AE")
        return

    process_request("_UPDATE_", guid_value, tag, patterns, responses, qr_code_path)

def process_request(command_type, guid_value, tag, patterns, responses, qr_code_path):
    global queries

    if command_type == "_UPDATE_":
        row = find_row_in_queries(guid_value)
        if row >= 0:
            queries[row] = {
                "id": guid_value,
                "tag": tag,
                "patterns": patterns.split("//"),
                "responses": responses.split("//"),
                "qr_code": qr_code_path
            }
            crm_qr_code.delete(0, END)
            crm_qr_code.insert(0, qr_code_path)
            qr_code_label.config(text=qr_code_path)
            
    elif command_type == "_INSERT_":
        dict = {
            "id": guid_value,
            "tag": tag,
            "patterns": patterns.split("//"),
            "responses": responses.split("//"),
            "qr_code": qr_code_path
        }
        queries.append(dict)

        crm_qr_code.delete(0, END)
        crm_qr_code.insert(0, qr_code_path)
        qr_code_label.config(text=qr_code_path)

    if queries and file_path:
        try:
            with open(file_path, "w") as file_handler:
                json.dump({"intents": queries}, file_handler, indent=4)
                file_handler.close()
                load_trv_with_json()
                messagebox.showinfo("Success", "Queries saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Warning", "No queries to save or file path not set.")

def delete_entry():
    global my_data_list
    guid_value = id_value.get()
    for entry in my_data_list:
        if entry["id"] == guid_value:
            my_data_list.remove(entry)
            load_trv_with_json()
            clear_all_fields()
            break
    else:
        messagebox.showwarning("Warning", "Entry not found.")

def load_trv_with_json():
    global queries
    trv.delete(*trv.get_children())
    rowIndex = 1
    for key in queries:
        guid_value = key["id"]
        tag = key["tag"]
        patterns1 = key["patterns"]
        patterns = (*map(str, patterns1), "")
        responses1 = key["responses"]
        responses = (*map(str, responses1), "")
        qr_code = key["qr_code"]
        trv.insert('', index='end', iid=rowIndex, text="", values=(guid_value, tag, '//'.join(patterns),
                                                                  '//'.join(responses), qr_code))
        rowIndex = rowIndex + 1

def clear_all_fields():
    crm_tag.delete(0, END)
    crm_patterns.delete(0, END)
    crm_responses.delete(0, END)
    crm_qr_code.delete(0, END)
    id_value.set(str(uuid.uuid4()))

def change_json_file():
    global queries, file_path
    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if file_path:
        try:
            with open(file_path) as file_handler:
                queries = json.load(file_handler)["intents"]
                file_handler.close()
                load_trv_with_json()
        except Exception as e:
            messagebox.showerror("Error", str(e))

def main():
    initialize_gui()
    root.mainloop()

if __name__ == "__main__":
    root = Tk()
    main()
