from tkinter import *
from tkinter import ttk
import uuid
import json

global my_data_list
global jsonData 
global currentRowIndex

my_data_list    = []
jsonData = [] 

root = Tk()
root.title('List of Intents')
root.geometry("1278x720")
root.configure(bg='Maroon')

photo = PhotoImage(file = "star.png")
root.iconphoto(False, photo)


input_frame = LabelFrame(root,text='Info',bg="lightgray",font=('Consolas',14))
input_frame.grid(row=0,column=0,rowspan=5,columnspan=4)


l1 = Label(input_frame,           anchor="w",           width=24,
           height=1,              relief="ridge",       text="ID",          
           font=('Consolas',14)   ).grid(row=1, column=0)

l2 = Label(input_frame,           anchor="w",           width=24, 
           height=1,              relief="ridge",       text="Tag",       
           font=('Consolas',14)   ).grid(row=2, column=0)

l3 = Label(input_frame,           anchor="w",           width=24, 
           height=1,              relief="ridge",       text="Patterns", 
           font=('Consolas',14)   ).grid(row=3, column=0) 


l4 = Label(input_frame,           anchor="w",           width=24, 
           height=1,              relief="ridge",       text="Responses", 
           font=('Consolas',14)   ).grid(row=4, column=0)

l5 = Label(input_frame,           anchor="w",           width=24, 
           height=1,              relief="ridge",       text="QR Codes", 
           font=('Consolas',14)   ).grid(row=4, column=0)



id_value = StringVar()
id_value.set(uuid.uuid4())

crm_id=Label(input_frame,           anchor="w",                 height=1,
           relief="ridge",          textvariable=id_value,      font=('Consolas',14))
crm_id.grid(row=1, column=1)

crm_tag      =Entry(input_frame,width=30,borderwidth=2,fg="black",font=('Consolas',14))
crm_tag.grid(row=2, column=1,columnspan=2)

crm_patterns      =Entry(input_frame,width=50,borderwidth=2,fg="black",font=('Consolas',14))
crm_patterns.grid(row=3, column=1,columnspan=2)

crm_responses=Entry(input_frame,width=50,borderwidth=2,fg="black",font=('Consolas',14))
crm_responses.grid(row=4, column=1,columnspan=2)

crm_qr_code=Entry(input_frame,width=30,borderwidth=2,fg="black",font=('Consolas',14))
crm_qr_code.grid(row=4, column=1,columnspan=2)






trv =ttk.Treeview(root, columns=(1,2,3,4,5),show="headings",height="16")
trv.grid(row=11,column=0, rowspan=16,columnspan=4)

trv.heading(1,text="ID", anchor="center")
trv.heading(2,text="Tag", anchor="center")
trv.heading(3,text="Patterns", anchor="center")
trv.heading(4,text="Responses", anchor="center")
trv.heading(5,text="QR Codes", anchor="center")

trv.column("#1",anchor="w",width=270, stretch=True)
trv.column("#2",anchor="w", width=140, stretch=False)
trv.column("#3",anchor="w", width=140, stretch=False)
trv.column("#4",anchor="w", width=140, stretch=False)
trv.column("#5",anchor="w", width=140, stretch=False)

# --review=s
def load_json_from_file():
    global my_data_list 
    global jsonData 
    
    with open("json_files\\eng_intents.json","r") as file_handler:
        my_data_list = json.load(file_handler) 
        jsonData = my_data_list["intents"]       
        file_handler.close
    print('file has been read and closed')


# --review=s
def save_json_to_file():
    global my_data_list
    global jsonData 

    with open("json_files\\eng_intents.json", "w") as file_handler:
        json.dump(my_data_list, file_handler, indent=4) 
    file_handler.close
    print('file has been written to and closed')



# --review=s
def remove_all_data_from_trv():
    for item in trv.get_children():
        trv.delete(item)
    

# --review=s
def load_trv_with_json():
    global my_data_list
    global jsonData 

    remove_all_data_from_trv()

    rowIndex=1

    for key in jsonData:
        guid_value = key["id"]
        tag = key["tag"]
        patterns = key["patterns"] 
        responses = key["responses"]
        qr_code = key["qr_code"]

        
        trv.insert('',index='end',iid=rowIndex,text="",
                        values=(guid_value,tag,patterns,responses,qr_code))
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
    
    if command_type == "_UPDATE_":
        row = find_row_in_my_data_list(guid_value)
        if row >= 0:

            dict = {"id":guid_value, "tag":tag, 
                    "patterns":patterns.split("//"), "responses":responses.split("//"), "qr_code":qr_code} 
            jsonData[row]=dict 

    elif command_type == "_INSERT_":

            dict = {"id":guid_value, "tag":tag, 
                "patterns":patterns.split("//"), "responses":responses.split("//"), "qr_code":qr_code} 
            jsonData.append(dict) 
        

    elif command_type == "_DELETE_":
        row = find_row_in_my_data_list(guid_value)
        if row >= 0:
            del jsonData[row]; 

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
ButtonFrame = LabelFrame(root,text='',bg="lightgray",font=('Consolas',14))
ButtonFrame.grid(row=5,column=0,columnspan=6)

##save=Button(root,text="Save",padx=20,pady=10,command=Save)
btnShow=Button(ButtonFrame,text="Print",padx=20,pady=10,command=print_all_entries)
btnShow.pack(side=LEFT)

btnAdd=Button(ButtonFrame,text="Add",padx=20,pady=10,command=add_entry)
btnAdd.pack(side=LEFT)

btnUpdate=Button(ButtonFrame,text="Update",padx=20,pady=10,command=update_entry)
btnUpdate.pack(side=LEFT)

btnDelete=Button(ButtonFrame,text="Delete",padx=20,pady=10,command=delete_entry)
btnDelete.pack(side=LEFT)


btnClear=Button(ButtonFrame,text="Cancel",padx=18,pady=10,command=cancel)
btnClear.pack(side=LEFT)

btnExit=Button(ButtonFrame,text="Exit",padx=20,pady=10,command=root.quit)
btnExit.pack(side=LEFT)


# --review=Y
load_json_from_file()
load_trv_with_json()

crm_tag.focus_set();
root.mainloop()
