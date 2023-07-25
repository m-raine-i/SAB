from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog ###
from tkinter import Listbox
import os
from os import listdir, remove
from os.path import isfile, join, dirname
import uuid
import json
import pathlib
from pathlib import Path

global my_data_list
global jsonData 
global file_path
global currentRowIndex

my_data_list = []
jsonData = [] 
file_path = ""


root = Tk()
root.title('List of Intents')
root.geometry("1000x650")
root.configure(bg='Maroon')

photo = PhotoImage(file = "..\SAB (AI Assistant)\star.png")
root.iconphoto(False, photo)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=0)


input_frame = LabelFrame(root,text='Student Assistant Bot (SAB)',bg="lightgray", font=('Consolas',14))
input_frame.grid(row=0,column=0, padx=5, pady=5, sticky="nsew")


l1 = Label(input_frame, text="ID",          
           font=('Consolas',14)   ).grid(row=0, column=0, padx=5, pady=5, sticky="w")

l2 = Label(input_frame, text="Tag",       
           font=('Consolas',14)   ).grid(row=1, column=0, padx=5, pady=5, sticky="w")

l3 = Label(input_frame, text="Patterns", 
           font=('Consolas',14)   ).grid(row=2, column=0, padx=5, pady=5, sticky="w") 


l4 = Label(input_frame,  text="Responses", 
           font=('Consolas',14)   ).grid(row=3, column=0, padx=5, pady=5, sticky="w")

l5 = Label(input_frame, text="QR Codes", 
           font=('Consolas',14)   ).grid(row=4, column=0, padx=5, pady=5, sticky="w")



id_value = StringVar()
id_value.set(uuid.uuid4())

crm_id=Label(input_frame, width=70, borderwidth=2, fg="black", textvariable=id_value, font=('Consolas',14))
crm_id.grid(row=0, column=1, padx=5, pady=5, sticky="w")

crm_tag =Entry(input_frame,width=70,borderwidth=2,fg="black",font=('Consolas',14))
crm_tag.grid(row=1, column=1, padx=5, pady=5, sticky="w")

crm_patterns =Entry(input_frame,width=70,borderwidth=2,fg="black",font=('Consolas',14))
crm_patterns.grid(row=2, column=1, padx=5, pady=5, sticky="w")

crm_responses=Entry(input_frame,width=70,borderwidth=2,fg="black",font=('Consolas',14))
crm_responses.grid(row=3, column=1, padx=5, pady=5, sticky="w")

crm_qr_code=Entry(input_frame,width=70,borderwidth=2,fg="black",font=('Consolas',14))
crm_qr_code.grid(row=4, column=1, padx=5, pady=5, sticky="w")


"""
trv=Listbox(root, width=80, height=10, font=('Consolas', 14))
trv.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")"""


trv =ttk.Treeview(root, columns=(1,2,3,4,5),show="headings", height=16)
trv.grid(row=11,column=0, rowspan=16,columnspan=4, padx=10, pady=10, sticky="nsew")

trv.heading(1,text="ID", anchor="center")
trv.heading(2,text="Tag", anchor="center")
trv.heading(3,text="Patterns", anchor="center")
trv.heading(4,text="Responses", anchor="center")
trv.heading(5,text="QR Codes", anchor="center")

trv.column("#1",anchor="w",width=30, stretch=True)
trv.column("#2",anchor="w", width=140, stretch=False)
trv.column("#3",anchor="w", width=300, stretch=False)
trv.column("#4",anchor="w", width=300, stretch=False)
trv.column("#5",anchor="w", width=200, stretch=False)

# --review=s
def load_json_from_file():
    global my_data_list 
    global jsonData 
    global file_path
    ###
    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    
    if file_path:
        try:
            with open(file_path) as file_handler:
                my_data_list = json.load(file_handler) 
                jsonData = my_data_list["intents"] 
                file_handler.close
                print('file has been read and closed')
                
        except Exception as e:
            messagebox.showerror("Error", str(e))
            


# --review=s
def save_json_to_file():
    global my_data_list
    global jsonData 
    global file_path
    ####
    if my_data_list and file_path:
        try:
            with open(file_path, "w") as file_handler:
                json.dump(my_data_list, file_handler, indent=4) 
                file_handler.close
                print('file has been written to and closed')
                messagebox.showinfo("Success", "Queries saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Warning", "No queries to save or file path not set.")
   # 



# --review=s
def remove_all_data_from_trv():
    for item in trv.get_children():
        trv.delete(item)
    

# --review=s
def load_trv_with_json():
    global my_data_list
    global jsonData 

   
    #qr_code = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg"), ("PNG Files", "*.png")]) ###

    remove_all_data_from_trv()

    rowIndex=1

    for key in jsonData:
        guid_value = key["id"]
        tag = key["tag"]

        patterns1 = key["patterns"] #orig 'patterns'
        patterns = (*map(str,patterns1), "") #######

        responses1 = key["responses"]
        responses = (*map(str,responses1), "") #######

        qr_code = key["qr_code"] 
        
        trv.insert('',index='end',iid=rowIndex,text="",
                        values=(guid_value,tag,'//'.join(patterns),'//'.join(responses),qr_code)) #######
        rowIndex=rowIndex+1


# --review=Y
def clear_all_fields():
    crm_tag.delete(0,END)
    crm_patterns.delete(0,END)
    crm_responses.delete(0,END)
    crm_qr_code.delete(0,END)
    crm_id.configure(text="")
    crm_tag.focus_set()
    id_value.set(uuid.uuid4())
    change_background_color("#FFFFFF")
    

# --review=Y
def find_row_in_my_data_list(guid_value):
    global jsonData 
    row     = 0
    found   = False

    for rec in jsonData: 
        if rec["id"] == guid_value:
            found = True
            break
        row = row+1

    if(found==True):
        return(row)

    return(-1)


# --review=Y
def change_background_color(new_color):
    crm_tag.config(bg=new_color)
    crm_patterns.config(bg=new_color)
    crm_responses.config(bg=new_color)
    crm_qr_code.config(bg=new_color)
 

# --review=Y
def change_enabled_state(state):

    if state == 'Edit':
        btnUpdate["state"]="normal"
        btnDelete["state"]="normal"
        btnAdd["state"]="disabled"
    elif state=='Cancel':
        btnUpdate["state"]="disabled"
        btnDelete["state"]="disabled"
        btnAdd["state"]="disabled"
    else:
        btnUpdate["state"]="disabled"
        btnDelete["state"]="disabled"
        btnAdd["state"]="normal"


# --review=Y
def load_edit_field_with_row_data(_tuple):
    if len(_tuple)==0:
        return;

    id_value.set(_tuple[0]);
    crm_tag.delete(0,END)
    crm_tag.insert(0,_tuple[1])
    crm_patterns.delete(0,END)
    crm_patterns.insert(0,_tuple[2])
    crm_responses.delete(0,END)
    crm_responses.insert(0,_tuple[3])
    crm_qr_code.delete(0,END)
    crm_qr_code.insert(0,_tuple[4])


# --review=Y
def cancel():
    clear_all_fields()
    change_enabled_state('New')


# --review=Y
def print_all_entries():
    global jsonData

    for rec in jsonData: 
        print(rec)

    crm_tag.focus_set();



# --review=Y
def add_entry():
    guid_value = id_value.get()
    tag = crm_tag.get()
    patterns = crm_patterns.get()
    responses = crm_responses.get()
    qr_code = crm_qr_code.get()


    if len(tag)==0:
        change_background_color("#FFB2AE")
        return

    process_request('_INSERT_',guid_value,tag,patterns,responses,qr_code) 


# --review=Y
def update_entry():
    guid_value = id_value.get()
    tag = crm_tag.get()
    patterns = crm_patterns.get()
    responses = crm_responses.get()
    qr_code = crm_qr_code.get()


    if len(tag)==0:
        change_background_color("#FFB2AE")
        return

    process_request('_UPDATE_',guid_value,tag,patterns,responses,qr_code)  



# --review=Y
def delete_entry():
    guid_value = id_value.get()
    process_request('_DELETE_',guid_value,None,None,None,None)
 


# --review=Y
def process_request(command_type,guid_value,tag,patterns,responses,qr_code):
    global jsonData 
    global file_path

    path = os.path.dirname(file_path) + '/'   #goes to dir of json file
    ext=['checkpoint', '*.pickle', '*.data-00000-of-00001', '*.index', '*.meta', '*.txt']
    allfiles = [f for f in listdir(path) if isfile(join(path, f))]

    """folder = pathlib.Path(file_path)
    files = [Path("folder\\checkpoint"), Path("folder\\data.pickle"), Path("folder\\model.tflearn.*")]"""
    #qr_code_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg"), ("PNG Files", "*.png")])####

    
    if command_type == "_UPDATE_":
        
        """for f in listdir(path):
            if f.endswith(tuple(ext)):
                try:
                    os.remove(path+f)
                except:
                    print("Failed With:", e.strerror)
                    print("Failed With:", e.code)"""

        row = find_row_in_my_data_list(guid_value)

        if row >= 0:

            dict = {"id":guid_value, "tag":tag, 
                    "patterns":patterns.split("//"), "responses":responses.split("//"), "qr_code":qr_code} 
            jsonData[row]=dict 

            for f in allfiles:
              if f in ext:
                try:
                  os.remove(path+f)
                except:
                  continue


                
            #for filename in files:
                #filename.unlink()



    elif command_type == "_INSERT_":

            dict = {"id":guid_value, "tag":tag, 
                "patterns":patterns.split("//"), "responses":responses.split("//"), "qr_code":qr_code} 
            jsonData.append(dict)
            
            for f in listdir(path):
              if f.endswith(tuple(ext)):
                os.remove(path+f)
        
            """for f in allfiles:
              if f in list1:
                try:
                  remove(path+f)
                except:
                  continue"""
            ##
            #for filename in files:
                #filename.unlink()
  

    elif command_type == "_DELETE_":
        row = find_row_in_my_data_list(guid_value)
        if row >= 0:
            del jsonData[row]; 

            for f in listdir(path):
              if f.endswith(tuple(ext)):
                os.remove(path+f)
            ###
            #for filename in files:
                #filename.unlink()


    save_json_to_file();
    load_trv_with_json();
    clear_all_fields();


# --review=Y
def MouseButtonUpCallBack(event):
    currentRowIndex = trv.selection()[0]
    lastTuple = (trv.item(currentRowIndex,'values'))
    load_edit_field_with_row_data(lastTuple)

    change_enabled_state('Edit')


# --review=Y
trv.bind("<ButtonRelease>",MouseButtonUpCallBack)


# --review=
ButtonFrame = LabelFrame(root,text='',bg="maroon",font=('Consolas',14))
ButtonFrame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

##save=Button(root,text="Save",padx=20,pady=10,command=Save)
#btnShow=Button(ButtonFrame,text="Print",width=15, height=2,  font=('Consolas', 10), command=print_all_entries)
#btnShow.pack(side="top", pady=5)

btnAdd=Button(ButtonFrame,text="Add",width=15, height=2,  font=('Consolas', 10), command=add_entry)
btnAdd.pack(side="top", pady=5)

btnUpdate=Button(ButtonFrame,text="Update",width=15, height=2,  font=('Consolas', 10), command=update_entry)
btnUpdate.pack(side="top", pady=5)

btnDelete=Button(ButtonFrame,text="Delete",width=15, height=2,  font=('Consolas', 10), command=delete_entry)
btnDelete.pack(side="top", pady=5)


btnClear=Button(ButtonFrame,text="Cancel",width=15, height=2, font=('Consolas', 10), command=cancel)
btnClear.pack(side="top", pady=5)

btnExit=Button(ButtonFrame,text="Exit",width=15, height=2,command=root.quit)
btnExit.pack(side="top", pady=5)


# --review=Y
load_json_from_file()
load_trv_with_json()

crm_tag.focus_set();
root.mainloop()
