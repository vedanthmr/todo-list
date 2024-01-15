import tkinter
from tkinter import *
 
root=Tk()
root.title("To-Do List")
root.geometry("400x650+400+100")
root.resizable(False,False) 

task_list=[]
completed_task=[]

def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)
    
    if task:
        with open("./files/tasklist.txt","a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert( END, task)

def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("./files/tasklist.txt","w") as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete( ANCHOR)

def markcompleted():
    global completed_task
    global task_list
    task=str(listbox.get(ANCHOR))
    selected_task=task
    if task in task_list:
        task_list.remove(task)
        with open("./files/tasklist.txt","w") as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete( ANCHOR)
   
    if selected_task not in completed_task:
        completed_task.append(selected_task)
        listbox1.insert(END, selected_task)
        with open("./files/completedtasks.txt","w") as taskfile:
            for task in completed_task:
                taskfile.write(task+"\n")
               

def openTaskFile():
    try:
        global task_list
        global completed_task
        with open("./files/tasklist.txt","r") as taskfile:
            tasks=taskfile.readlines()
        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)

        with open("./files/completedtasks.txt","r") as taskfile:
            completed=taskfile.readlines()
            print(completed)
        for task in completed:
            if task!= '\n':
                completed_task.append(task)
                listbox1.insert(END, task)
    except:
        file=open('./files/tasklist.txt','w')
        file.close()


heading=Label(root,text="My Tasks",font="arial 20 bold",fg="white",bg="#484a4d")
heading.place(x=140,y=20)

#main
frame=Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=100)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)

button=Button(frame,text="ADD",font="arial 20 bold",width=6,bg="#484a4d",fg="#fff",bd=0,command=addTask)
button.place(x=300,y=0)


#listbox
T = tkinter.Text(root, height=1, width=100)
T.pack()
T.pack(pady=(150,0))
T.insert(tkinter.END, "Pending \n")

frame1=Frame(root,bd=3,width=700,height=280,bg="#6e6e6e")  
frame1.pack(pady=(5,0))  

listbox=Listbox(frame1,font=('arial',12),width=40,height=8,bg="#1c1c1c",fg="white",cursor="hand2",selectbackground="#5a95ff")  #height=16
listbox.pack(side= LEFT ,fill= BOTH , padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side= RIGHT ,fill= BOTH )

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

#completed
T = tkinter.Text(root, height=1, width=100)
T.pack()
T.pack(pady=(3,0))
T.insert(tkinter.END, "Completed \n")

frame2=Frame(root,bd=3,width=700,height=380,bg="#6e6e6e")  
frame2.pack(pady=(0,0))

listbox1=Listbox(frame2,font=('arial',12),width=40,height=8,bg="#1c1c1c",fg="white",cursor="hand2",selectbackground="#5a95ff")  #height=16
listbox1.pack(side= LEFT ,fill= BOTH , padx=2)
scrollbar1=Scrollbar(frame2)
scrollbar1.pack(side= RIGHT ,fill= BOTH )

listbox1.config(yscrollcommand=scrollbar1.set)
scrollbar1.config(command=listbox1.yview)

openTaskFile()

#delete
Delete_icon=PhotoImage(file="Image/delete.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM, pady=13)

#mark_complete
mark_button=Button(root,text="Mark as completed ",font="arial 10 bold",width=15,command=markcompleted)
mark_button.pack(pady=3)

root.mainloop()