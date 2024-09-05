from tkinter import *
from tkinter import ttk
import tkinter as tk
import csv
from typing import List

def add_adm():
    root_add_adm=Tk()
    root_add_adm.geometry("450x250")
    root_add_adm.maxsize(450,250)
    root_add_adm.minsize(450,250)
    root_add_adm.title("Add Admission Details")
    l_1=Label(root_add_adm,text="Name")
    l_2=Label(root_add_adm,text="Date of birth")
    l_3=Label(root_add_adm,text="12th aggeregate marks")
    l_4=Label(root_add_adm,text="Category (GN/SC/ST/OBC)")
    l_5=Label(root_add_adm,text="Course opted")
    l_6=Label(root_add_adm,text="Phone no.")
    l_7=Label(root_add_adm,text="e-mail ID")
    l_8=Label(root_add_adm,text="JEE(m) *")
    l_9=Label(root_add_adm,text=" '*' MEANS OPTIONAL")
    l_1.grid(row=0,column=1)
    l_2.grid(row=1,column=1)
    l_3.grid(row=2,column=1)
    l_4.grid(row=3,column=1)
    l_5.grid(row=4,column=1)
    l_6.grid(row=5,column=1)
    l_7.grid(row=6,column=1)
    l_8.grid(row=7,column=1)
    l_9.grid(row=7,column=3)
    
    e_adm1=Entry(root_add_adm)
    e_adm2=Entry(root_add_adm)
    e_adm3=Entry(root_add_adm)
    e_adm4=Entry(root_add_adm)
    e_adm5=Entry(root_add_adm)
    e_adm6=Entry(root_add_adm)
    e_adm7=Entry(root_add_adm)
    e_adm8=Entry(root_add_adm)

    e_adm1.grid(row=0,column=2)
    e_adm2.grid(row=1,column=2)
    e_adm3.grid(row=2,column=2)
    e_adm4.grid(row=3,column=2)
    e_adm5.grid(row=4,column=2)
    e_adm6.grid(row=5,column=2)
    e_adm7.grid(row=6,column=2)
    e_adm8.grid(row=7,column=2)

    def add_data():
        with open ("UNI_ADM.csv","a+") as f:
            csvw=csv.writer(f)
            csvw.writerow([e_adm1.get(),e_adm2.get(),e_adm3.get(),e_adm4.get(),e_adm5.get(),e_adm6.get(),e_adm7.get(),e_adm8.get()])
        
        e_adm1.delete(0,END)
        e_adm2.delete(0,END) 
        e_adm3.delete(0,END)
        e_adm4.delete(0,END)
        e_adm5.delete(0,END)
        e_adm6.delete(0,END)
        e_adm7.delete(0,END)
        e_adm8.delete(0,END)

    button_add_adm=Button(root_add_adm,text="SUBMIT",fg="black",relief=RAISED,command=add_data)
    button_add_adm.grid(row=10,column=2)
    root_add_adm.mainloop()


def up_adm():
    root_up_adm=Tk()
    root_up_adm.geometry("1050x500")
    root_up_adm.maxsize()
    root_up_adm.minsize()
    root_up_adm.title("update admission record")
    frame_u1=Frame(root_up_adm)
    frame_u1.pack(fill=X)
    up_tree=ttk.Treeview(frame_u1)
    up_tree["show"]="headings"
    up_tree["column"]=("Name","Date of birth","12th aggregate marks", "Category (GN/SC/ST/OBC)","Course opted","Phone no.","e-mail ID","JEE (m) *")
    up_tree.column("Name",width=80,minwidth=50,anchor=CENTER)
    up_tree.column("Date of birth",width=80,minwidth=50,anchor=CENTER)
    up_tree.column("12th aggregate marks",width=80,minwidth=50,anchor=CENTER)
    up_tree.column("Category (GN/SC/ST/OBC)",width=80,minwidth=50,anchor=CENTER)
    up_tree.column("Course opted",width=80,minwidth=50,anchor=CENTER)
    up_tree.column("Phone no.",width=80,minwidth=50,anchor=CENTER)
    up_tree.column("e-mail ID",width=80,minwidth=50,anchor=CENTER)
    up_tree.column("JEE (m) *",width=80,minwidth=50,anchor=CENTER)
    
    up_tree.heading("Name",text="Name",anchor=CENTER)
    up_tree.heading("Date of birth",text="Date of birth",anchor=CENTER)
    up_tree.heading("12th aggregate marks",text="12th aggregate marks",anchor=CENTER)
    up_tree.heading("Category (GN/SC/ST/OBC)",text="Category (GN/SC/ST/OBC)",anchor=CENTER)
    up_tree.heading("Course opted",text="Course opted",anchor=CENTER)
    up_tree.heading("Phone no.",text="Phone no.",anchor=CENTER)
    up_tree.heading("e-mail ID",text="e-mail ID",anchor=CENTER)
    up_tree.heading("JEE (m) *",text="JEE (m) *",anchor=CENTER)

    tree_scroll_hsb=ttk.Scrollbar(frame_u1,orient=HORIZONTAL)
    tree_scroll_hsb.configure(command=up_tree.xview)

    up_tree.configure(xscrollcommand=tree_scroll_hsb.set)
    tree_scroll_hsb.pack(fill=X,side=BOTTOM)

    tree_scroll_vsb=ttk.Scrollbar(frame_u1,orient=VERTICAL)
    tree_scroll_vsb.configure(command=up_tree.yview)

    up_tree.configure(yscrollcommand=tree_scroll_vsb.set)
    tree_scroll_vsb.pack(fill=Y,side=RIGHT)

    l_1=[]
    f=open("UNI_ADM.csv","r")
    csvr=csv.reader(f)
    for i in csvr:
        if i==[]:
            continue
        else:
            l_1.append(i)
    for values in l_1:
        up_tree.insert("",END,values=values)


    frame_u2=Frame(root_up_adm)
    frame_u2.pack()
    l_u1=Label(frame_u2,text="Name")
    l_u2=Label(frame_u2,text="Date of birth")
    l_u3=Label(frame_u2,text="12th aggregate marks")
    l_u4=Label(frame_u2,text="Category (GN/SC/ST/OBC)")
    l_u5=Label(frame_u2,text="Course opted")
    l_u6=Label(frame_u2,text="Phone no.")
    l_u7=Label(frame_u2,text="e-mail ID")
    l_u8=Label(frame_u2,text="JEE (m) *")
    l_u1.grid(row=0,column=1)
    l_u2.grid(row=0,column=2)
    l_u3.grid(row=0,column=3)
    l_u4.grid(row=0,column=4)
    l_u5.grid(row=0,column=5)
    l_u6.grid(row=0,column=6)
    l_u7.grid(row=0,column=7)
    l_u8.grid(row=0,column=8)

    e_up1=Entry(frame_u2)
    e_up2=Entry(frame_u2)
    e_up3=Entry(frame_u2)
    e_up4=Entry(frame_u2)
    e_up5=Entry(frame_u2)
    e_up6=Entry(frame_u2)
    e_up7=Entry(frame_u2)
    e_up8=Entry(frame_u2)


    e_up1.grid(row=1,column=1)
    e_up2.grid(row=1,column=2)
    e_up3.grid(row=1,column=3)
    e_up4.grid(row=1,column=4)
    e_up5.grid(row=1,column=5)
    e_up6.grid(row=1,column=6)
    e_up7.grid(row=1,column=7)
    e_up8.grid(row=1,column=8)


    l_gob=[]
    def button_select_rec():
        selected=up_tree.focus()
        values=list(up_tree.item(selected,"values"))
        e_up1.insert(0,values[0])
        e_up2.insert(0,values[1])
        e_up3.insert(0,values[2])
        e_up4.insert(0,values[3])
        e_up5.insert(0,values[4])
        e_up6.insert(0,values[5])
        e_up7.insert(0,values[6])
        e_up8.insert(0,values[7])
        l_gob.append(list(values))

    def button_update_rec():
        selected=up_tree.focus()
        up_tree.item(selected,text="",values=(e_up1.get(),e_up2.get(),e_up3.get(),e_up4.get(),e_up5.get(),e_up6.get(),e_up7.get(),e_up8.get()))
        values=list(up_tree.item(selected,"values"))

        values[0]=e_up1.get()
        values[1]=e_up2.get()
        values[2]=e_up3.get()
        values[3]=e_up4.get()
        values[4]=e_up5.get()
        values[5]=e_up6.get()
        values[6]=e_up7.get()
        values[7]=e_up8.get()

        list_up=[values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7]]
        try:
            l=[]
            f=open("UNI_ADM.csv","r")
            csvr=csv.reader(f)
            for i in csvr:
                if i==[]:
                    continue
                else:
                    l.append(i)
            for rows_l_gob in l_gob:
                for rows_l in l:
                    if rows_l_gob==rows_l:
                        l[l.index(rows_l)]=list_up

            f2=open("UNI_ADM.csv","w")
            csvw=csv.writer(f)
            for i in l:
                csvw.writerow(i)
                
        except ValueError:
            pass

        e_up1.delete(0,END)
        e_up2.delete(0,END)
        e_up3.delete(0,END)
        e_up4.delete(0,END)
        e_up5.delete(0,END)
        e_up6.delete(0,END)
        e_up7.delete(0,END)
        e_up8.delete(0,END)

    def button_delete_rec():
        l=[]
        f=open("UNI_ADM.csv","r")
        csvr=csv.reader(f)
        for i in csvr:
            if i==[]:
                continue
            else:
                l.append(i)
        for rows_l in l:
            for rows_l_1 in l_gob:
                if rows_l==rows_l_1:
                    l.remove(rows_l)
        f2=open("UNI_ADM.csv","w")           
        csvw=csv.writer(f2)
        for i in l:
            csvw.writerow(f2)

        e_up1.delete(0,END)
        e_up2.delete(0,END)
        e_up3.delete(0,END)
        e_up4.delete(0,END)
        e_up5.delete(0,END)
        e_up6.delete(0,END)
        e_up7.delete(0,END)
        e_up8.delete(0,END)

        x=up_tree.selection()
        up_tree.delete(x)

    button_select=Button(root_up_adm,text="select",width=10,command=button_select_rec)
    button_select.pack(pady=20)
    button_update=Button(root_up_adm,text="update",width=10,command=button_update_rec)
    button_update.pack(pady=10)
    button_delete=Button(root_up_adm,text="delete",width=10,command=button_delete_rec)
    button_delete.pack(pady=20)
    up_tree.pack(fill=X)
    root_up_adm.mainloop()

def dis_adm():
    root_dis_adm=Tk()
    root_dis_adm.geometry("1050x500")
    root_dis_adm.maxsize()
    root_dis_adm.minsize()
    root_dis_adm.title("update admission record")
    frame_d1=Frame(root_dis_adm)
    frame_d1.pack(fill=X)
    dis_tree=ttk.Treeview(frame_d1)
    dis_tree["show"]="headings"
    dis_tree["column"]=("Name","Date of birth","12th aggregate marks", "Category (GN/SC/ST/OBC)","Course opted","Phone no.","e-mail ID","JEE (m) *")
    dis_tree.column("Name",width=80,minwidth=50,anchor=CENTER)
    dis_tree.column("Date of birth",width=80,minwidth=50,anchor=CENTER)
    dis_tree.column("12th aggregate marks",width=80,minwidth=50,anchor=CENTER)
    dis_tree.column("Category (GN/SC/ST/OBC)",width=80,minwidth=50,anchor=CENTER)
    dis_tree.column("Course opted",width=80,minwidth=50,anchor=CENTER)
    dis_tree.column("Phone no.",width=80,minwidth=50,anchor=CENTER)
    dis_tree.column("e-mail ID",width=80,minwidth=50,anchor=CENTER)
    dis_tree.column("JEE (m) *",width=80,minwidth=50,anchor=CENTER)
    
    dis_tree.heading("Name",text="Name",anchor=CENTER)
    dis_tree.heading("Date of birth",text="Date of birth",anchor=CENTER)
    dis_tree.heading("12th aggregate marks",text="12th aggregate marks",anchor=CENTER)
    dis_tree.heading("Category (GN/SC/ST/OBC)",text="Category (GN/SC/ST/OBC)",anchor=CENTER)
    dis_tree.heading("Course opted",text="Course opted",anchor=CENTER)
    dis_tree.heading("Phone no.",text="Phone no.",anchor=CENTER)
    dis_tree.heading("e-mail ID",text="e-mail ID",anchor=CENTER)
    dis_tree.heading("JEE (m) *",text="JEE (m) *",anchor=CENTER)

    tree_scroll_hsb=ttk.Scrollbar(frame_d1,orient=HORIZONTAL)
    tree_scroll_hsb.configure(command=dis_tree.xview)

    dis_tree.configure(xscrollcommand=tree_scroll_hsb.set)
    tree_scroll_hsb.pack(fill=X,side=BOTTOM)

    tree_scroll_vsb=ttk.Scrollbar(frame_d1,orient=VERTICAL)
    tree_scroll_vsb.configure(command=dis_tree.yview)

    dis_tree.configure(yscrollcommand=tree_scroll_vsb.set)
    tree_scroll_vsb.pack(fill=Y,side=RIGHT)

    l_1=[]
    f=open("UNI_ADM.csv","r")
    csvr=csv.reader(f)
    for i in csvr:
        if i==[]:
            continue
        else:
            l_1.append(i)
    for values in l_1:
        dis_tree.insert("",END,values=values)

    dis_tree.pack(fill=X)
    root_dis_adm.mainloop()

def ser_adm():
    root=Tk()
    root.geometry("200x200")
    root.maxsize()
    root.minsize()
    root.title("search")
    label_ser=Label(root,text="Enter Name")
    label_ser.grid(row=0,column=1)
    entry_ser=Entry(root)
    entry_ser.grid(row=0,column=2)

    def dis_ser_adm():
        root_ser_adm=Tk()
        root_ser_adm.geometry("1050x255")
        root_ser_adm.maxsize(1050,255)
        root_ser_adm.minsize(1050,255)
        root_ser_adm.title("update admission record")
        frame_s1=Frame(root_ser_adm)
        frame_s1.pack(fill=X)
        ser_tree=ttk.Treeview(frame_s1)
        ser_tree["show"]="headings"
        ser_tree["column"]=("Name","Date of birth","12th aggregate marks", "Category (GN/SC/ST/OBC)","Course opted","Phone no.","e-mail ID","JEE (m) *")
        ser_tree.column("Name",width=80,minwidth=50,anchor=CENTER)
        ser_tree.column("Date of birth",width=80,minwidth=50,anchor=CENTER)
        ser_tree.column("12th aggregate marks",width=80,minwidth=50,anchor=CENTER)
        ser_tree.column("Category (GN/SC/ST/OBC)",width=80,minwidth=50,anchor=CENTER)
        ser_tree.column("Course opted",width=80,minwidth=50,anchor=CENTER)
        ser_tree.column("Phone no.",width=80,minwidth=50,anchor=CENTER)
        ser_tree.column("e-mail ID",width=80,minwidth=50,anchor=CENTER)
        ser_tree.column("JEE (m) *",width=80,minwidth=50,anchor=CENTER)
        
        ser_tree.heading("Name",text="Name",anchor=CENTER)
        ser_tree.heading("Date of birth",text="Date of birth",anchor=CENTER)
        ser_tree.heading("12th aggregate marks",text="12th aggregate marks",anchor=CENTER)
        ser_tree.heading("Category (GN/SC/ST/OBC)",text="Category (GN/SC/ST/OBC)",anchor=CENTER)
        ser_tree.heading("Course opted",text="Course opted",anchor=CENTER)
        ser_tree.heading("Phone no.",text="Phone no.",anchor=CENTER)
        ser_tree.heading("e-mail ID",text="e-mail ID",anchor=CENTER)
        ser_tree.heading("JEE (m) *",text="JEE (m) *",anchor=CENTER)

        tree_scroll_hsb=ttk.Scrollbar(frame_s1,orient=HORIZONTAL)
        tree_scroll_hsb.configure(command=ser_tree.xview)

        ser_tree.configure(xscrollcommand=tree_scroll_hsb.set)
        tree_scroll_hsb.pack(fill=X,side=BOTTOM)

        tree_scroll_vsb=ttk.Scrollbar(frame_s1,orient=VERTICAL)
        tree_scroll_vsb.configure(command=ser_tree.yview)

        ser_tree.configure(yscrollcommand=tree_scroll_vsb.set)
        tree_scroll_vsb.pack(fill=Y,side=RIGHT)

        l_1=[]
        f=open("UNI_ADM.csv","r")
        csvr=csv.reader(f)
        for i in csvr:
            if i==[]:
                continue
            else:
                l_1.append(i)
        for values in l_1:
            if entry_ser.get() in values:
                ser_tree.insert("",END,values=values)
        ser_tree.pack(fill=X)
        root_ser_adm.mainloop()
    button_ser=Button(root,text="search",fg="black",command=dis_ser_adm)
    button_ser.grid(row=1,column=2)
    root.mainloop()

def admission():
    root_adm=Tk()
    root_adm.geometry("500x350")
    root_adm.maxsize(500,350)
    root_adm.minsize(500,350)
    root_adm.title("Admission details")
    frame_a1=Frame(root_adm,borderwidth=6,bg="red",relief=RAISED)
    button_a1=Button(frame_a1,text="apply for admission",fg="black",relief=RAISED,command=add_adm)
    button_a1.pack()
    frame_a1.pack(anchor=CENTER, pady=20)

    frame_a2=Frame(root_adm,borderwidth=6,bg="red",relief=RAISED)
    button_a2=Button(frame_a2,text="update admission record",fg="black",command=up_adm)
    button_a2.pack()
    frame_a2.pack(anchor=CENTER, pady=20)

    frame_a3=Frame(root_adm,borderwidth=6,bg="red",relief=RAISED)
    button_a3=Button(frame_a3,text="display admissison record",fg="black",command=dis_adm)
    button_a3.pack()
    frame_a3.pack(anchor=CENTER, pady=20)

    frame_a4=Frame(root_adm,borderwidth=6,bg="red",relief=RAISED)
    button_a4=Button(frame_a4,text="search for details",fg="black",command=ser_adm)
    button_a4.pack()
    frame_a4.pack(anchor=CENTER, pady=20)
    root_adm.mainloop()

def engineering_department():
    root_ed_ac=Tk()
    root_ed_ac.geometry("280x220")
    root_ed_ac.maxsize(280,220)
    root_ed_ac.minsize(280,220)
    root_ed_ac.title("Engineering Department")
    l_ed1=Label(root_ed_ac,text="B TECH (computer science engineering)")
    l_ed2=Label(root_ed_ac,text="B TECH (civil engineering)")
    l_ed3=Label(root_ed_ac,text="B TECH (mechanical engineering)")
    l_ed4=Label(root_ed_ac,text="B TECH (communication engineering)")
    l_ed5=Label(root_ed_ac,text="B TECH (information technology)")
    l_ed6=Label(root_ed_ac,text="B TECH (electrical engineering)")
    l_ed7=Label(root_ed_ac,text="B TECH (artificial intelligence)")
    l_ed8=Label(root_ed_ac,text="B TECH (biotechnology)")
    l_ed1.grid(row=0,column=1)
    l_ed2.grid(row=1,column=1)
    l_ed3.grid(row=2,column=1)
    l_ed4.grid(row=3,column=1)
    l_ed5.grid(row=4,column=1)
    l_ed6.grid(row=5,column=1)
    l_ed7.grid(row=6,column=1)
    l_ed8.grid(row=7,column=1)

    frame_ed1=Frame(root_ed_ac)
    button_ed1=Button(frame_ed1,text="apply!",fg="black",command=add_adm)
    button_ed1.pack()
    frame_ed1.grid(row=0,column=2)    
    frame_ed2=Frame(root_ed_ac)
    button_ed2=Button(frame_ed2,text="apply!",fg="black",command=add_adm)
    button_ed2.pack()
    frame_ed2.grid(row=1,column=2)
    frame_ed3=Frame(root_ed_ac)
    button_ed3=Button(frame_ed3,text="apply!",fg="black",command=add_adm)
    button_ed3.pack()
    frame_ed3.grid(row=2,column=2)
    frame_ed4=Frame(root_ed_ac)
    button_ed4=Button(frame_ed4,text="apply!",fg="black",command=add_adm)
    button_ed4.pack()
    frame_ed4.grid(row=3,column=2)
    frame_ed5=Frame(root_ed_ac)
    button_ed5=Button(frame_ed5,text="apply!",fg="black",command=add_adm)
    button_ed5.pack()
    frame_ed5.grid(row=4,column=2)
    frame_ed6=Frame(root_ed_ac)
    button_ed6=Button(frame_ed6,text="apply!",fg="black",command=add_adm)
    button_ed6.pack()
    frame_ed6.grid(row=5,column=2)
    frame_ed7=Frame(root_ed_ac)
    button_ed7=Button(frame_ed7,text="apply!",fg="black",command=add_adm)
    button_ed7.pack()
    frame_ed7.grid(row=6,column=2)
    frame_ed8=Frame(root_ed_ac)
    button_ed8=Button(frame_ed8,text="apply!",fg="black",command=add_adm)
    button_ed8.pack()
    frame_ed8.grid(row=7,column=2)
    root_ed_ac.mainloop()
    
def medical_department():
    root_md_ac=Tk()
    root_md_ac.geometry("280x220")
    root_md_ac.maxsize(280,220)
    root_md_ac.minsize(280,220)
    root_md_ac.title("Medical Department")
    l_md1=Label(root_md_ac,text="MBBS")
    l_md2=Label(root_md_ac,text="B Sc (nursing hons)")
    l_md3=Label(root_md_ac,text="Post basic B Sc nursing")
    l_md4=Label(root_md_ac,text="B Optom")
    l_md5=Label(root_md_ac,text="B Sc (dental hygiene)")
    l_md6=Label(root_md_ac,text="B Sc (operation theatre technology)")
    l_md7=Label(root_md_ac,text="MD Pharmacy")
    l_md8=Label(root_md_ac,text="M Sc pharmacology")
    l_md1.grid(row=0,column=1)
    l_md2.grid(row=1,column=1)
    l_md3.grid(row=2,column=1)
    l_md4.grid(row=3,column=1)
    l_md5.grid(row=4,column=1)
    l_md6.grid(row=5,column=1)
    l_md7.grid(row=6,column=1)
    l_md8.grid(row=7,column=1)

    frame_md1=Frame(root_md_ac)
    button_md1=Button(frame_md1,text="apply!",fg="black",command=add_adm)
    button_md1.pack()
    frame_md1.grid(row=0,column=2)    
    frame_md2=Frame(root_md_ac)
    button_md2=Button(frame_md2,text="apply!",fg="black",command=add_adm)
    button_md2.pack()
    frame_md2.grid(row=1,column=2)
    frame_md3=Frame(root_md_ac)
    button_md3=Button(frame_md3,text="apply!",fg="black",command=add_adm)
    button_md3.pack()
    frame_md3.grid(row=2,column=2)
    frame_md4=Frame(root_md_ac)
    button_md4=Button(frame_md4,text="apply!",fg="black",command=add_adm)
    button_md4.pack()
    frame_md4.grid(row=3,column=2)
    frame_md5=Frame(root_md_ac)
    button_md5=Button(frame_md5,text="apply!",fg="black",command=add_adm)
    button_md5.pack()
    frame_md5.grid(row=4,column=2)
    frame_md6=Frame(root_md_ac)
    button_md6=Button(frame_md6,text="apply!",fg="black",command=add_adm)
    button_md6.pack()
    frame_md6.grid(row=5,column=2)
    frame_md7=Frame(root_md_ac)
    button_md7=Button(frame_md7,text="apply!",fg="black",command=add_adm)
    button_md7.pack()
    frame_md7.grid(row=6,column=2)
    frame_md8=Frame(root_md_ac)
    button_md8=Button(frame_md8,text="apply!",fg="black",command=add_adm)
    button_md8.pack()
    frame_md8.grid(row=7,column=2)
    root_md_ac.mainloop()

def management_department():
    root_mand_ac=Tk()
    root_mand_ac.geometry("280x220")
    root_mand_ac.maxsize(280,220)
    root_mand_ac.minsize(280,220)
    root_mand_ac.title("Management Department")
    l_mand1=Label(root_mand_ac,text="BBA (human resource management")
    l_mand2=Label(root_mand_ac,text="BMS")
    l_mand3=Label(root_mand_ac,text="BBA + MBA (integrated program)")
    l_mand4=Label(root_mand_ac,text="PGDM")
    l_mand5=Label(root_mand_ac,text="BBA Hons.")
    l_mand6=Label(root_mand_ac,text="Executive MBA")
    l_mand7=Label(root_mand_ac,text="B Comm. Hons.")
    l_mand8=Label(root_mand_ac,text="ePGD in advance business analytics")
    l_mand1.grid(row=0,column=1)
    l_mand2.grid(row=1,column=1)
    l_mand3.grid(row=2,column=1)
    l_mand4.grid(row=3,column=1)
    l_mand5.grid(row=4,column=1)
    l_mand6.grid(row=5,column=1)
    l_mand7.grid(row=6,column=1)
    l_mand8.grid(row=7,column=1)

    frame_mand1=Frame(root_mand_ac)
    button_mand1=Button(frame_mand1,text="apply!",fg="black",command=add_adm)
    button_mand1.pack()
    frame_mand1.grid(row=0,column=2)    
    frame_mand2=Frame(root_mand_ac)
    button_mand2=Button(frame_mand2,text="apply!",fg="black",command=add_adm)
    button_mand2.pack()
    frame_mand2.grid(row=1,column=2)
    frame_mand3=Frame(root_mand_ac)
    button_mand3=Button(frame_mand3,text="apply!",fg="black",command=add_adm)
    button_mand3.pack()
    frame_mand3.grid(row=2,column=2)
    frame_mand4=Frame(root_mand_ac)
    button_mand4=Button(frame_mand4,text="apply!",fg="black",command=add_adm)
    button_mand4.pack()
    frame_mand4.grid(row=3,column=2)
    frame_mand5=Frame(root_mand_ac)
    button_mand5=Button(frame_mand5,text="apply!",fg="black",command=add_adm)
    button_mand5.pack()
    frame_mand5.grid(row=4,column=2)
    frame_mand6=Frame(root_mand_ac)
    button_mand6=Button(frame_mand6,text="apply!",fg="black",command=add_adm)
    button_mand6.pack()
    frame_mand6.grid(row=5,column=2)
    frame_mand7=Frame(root_mand_ac)
    button_mand7=Button(frame_mand7,text="apply!",fg="black",command=add_adm)
    button_mand7.pack()
    frame_mand7.grid(row=6,column=2)
    frame_mand8=Frame(root_mand_ac)
    button_mand8=Button(frame_mand8,text="apply!",fg="black",command=add_adm)
    button_mand8.pack()
    frame_mand8.grid(row=7,column=2)
    root_mand_ac.mainloop()

def artistic_department():
    root_ad_ac=Tk()
    root_ad_ac.geometry("300x220")
    root_ad_ac.maxsize(300,220)
    root_ad_ac.minsize(300,220)
    root_ad_ac.title("Artistic Department")
    l_ad1=Label(root_ad_ac,text="B Sc cinema (with diploma in acting)")
    l_ad2=Label(root_ad_ac,text="B Sc cinema (with diploma in cinematography)")
    l_ad3=Label(root_ad_ac,text="BA event management")
    l_ad4=Label(root_ad_ac,text="BJMC")
    l_ad5=Label(root_ad_ac,text="B Sc cinema (with diploma in direction)")
    l_ad6=Label(root_ad_ac,text="BA music for film and TV")
    l_ad7=Label(root_ad_ac,text="B Des. fashion design")
    l_ad8=Label(root_ad_ac,text="B Des. interior design")
    l_ad1.grid(row=0,column=1)
    l_ad2.grid(row=1,column=1)
    l_ad3.grid(row=2,column=1)
    l_ad4.grid(row=3,column=1)
    l_ad5.grid(row=4,column=1)
    l_ad6.grid(row=5,column=1)
    l_ad7.grid(row=6,column=1)
    l_ad8.grid(row=7,column=1)

    frame_ad1=Frame(root_ad_ac)
    button_ad1=Button(frame_ad1,text="apply!",fg="black",command=add_adm)
    button_ad1.pack()
    frame_ad1.grid(row=0,column=2)    
    frame_ad2=Frame(root_ad_ac)
    button_ad2=Button(frame_ad2,text="apply!",fg="black",command=add_adm)
    button_ad2.pack()
    frame_ad2.grid(row=1,column=2)
    frame_ad3=Frame(root_ad_ac)
    button_ad3=Button(frame_ad3,text="apply!",fg="black",command=add_adm)
    button_ad3.pack()
    frame_ad3.grid(row=2,column=2)
    frame_ad4=Frame(root_ad_ac)
    button_ad4=Button(frame_ad4,text="apply!",fg="black",command=add_adm)
    button_ad4.pack()
    frame_ad4.grid(row=3,column=2)
    frame_ad5=Frame(root_ad_ac)
    button_ad5=Button(frame_ad5,text="apply!",fg="black",command=add_adm)
    button_ad5.pack()
    frame_ad5.grid(row=4,column=2)
    frame_ad6=Frame(root_ad_ac)
    button_ad6=Button(frame_ad6,text="apply!",fg="black",command=add_adm)
    button_ad6.pack()
    frame_ad6.grid(row=5,column=2)
    frame_ad7=Frame(root_ad_ac)
    button_ad7=Button(frame_ad7,text="apply!",fg="black",command=add_adm)
    button_ad7.pack()
    frame_ad7.grid(row=6,column=2)
    frame_ad8=Frame(root_ad_ac)
    button_ad8=Button(frame_ad8,text="apply!",fg="black",command=add_adm)
    button_ad8.pack()
    frame_ad8.grid(row=7,column=2)
    root_ad_ac.mainloop()
    
def courses_offered():
    root_co_ac=Tk()
    root_co_ac.geometry("500x350")
    root_co_ac.maxsize(500,350)
    root_co_ac.minsize(500,350)
    root_co_ac.title("Courses Offered")
    frame_co_ac1=Frame(root_co_ac,borderwidth=6,bg="orange",relief=RAISED)
    button_co_ac1=Button(frame_co_ac1,text="Engineering Department",fg="black",command=engineering_department)
    button_co_ac1.pack()
    frame_co_ac1.pack(anchor=CENTER, pady=20)

    frame_co_ac2=Frame(root_co_ac,borderwidth=6,bg="orange",relief=RAISED)
    button_co_ac2=Button(frame_co_ac2,text="Medical Department",fg="black",command=medical_department)
    button_co_ac2.pack()
    frame_co_ac2.pack(anchor=CENTER, pady=20)

    frame_co_ac3=Frame(root_co_ac,borderwidth=6,bg="orange",relief=RAISED)
    button_co_ac3=Button(frame_co_ac3,text="Management Department",fg="black",command=management_department)
    button_co_ac3.pack()
    frame_co_ac3.pack(anchor=CENTER, pady=20)

    frame_co_ac4=Frame(root_co_ac,borderwidth=6,bg="orange",relief=RAISED)
    button_co_ac4=Button(frame_co_ac4,text="Artistic Department",fg="black",command=artistic_department)
    button_co_ac4.pack()
    frame_co_ac4.pack(anchor=CENTER, pady=20)
    root_co_ac.mainloop()

def UDL_mar():
    root_udl_mar=tk.Toplevel()
    root_udl_mar.geometry("810x455")
    root_udl_mar.maxsize(810,455)
    root_udl_mar.minsize(810,455)
    root_udl_mar.title("University Of DENISELAND - Marseille")
    label_mar=Label(root_udl_mar,text="""We doubt the critics, reject the status quo and see opportunity in dissatisfaction.
    Our campus, faculty and students are driven by optimism. It is not naïve; it is essential. 
    And it has fueled every accomplishment, allowing us to redefine what's possible, time after time.
    This can-do perspective has brought us 14 Nobel Prizes, 14 faculty MacArthur Fellows, 118 NCAA titles and more Olympic medals than most nations. 
    Our faculty and alumni helped create the Internet and pioneered reverse osmosis. 
    And more than 140 companies have been created based on technology developed at UDL - Marseille.
    What inspires MacArthur Fellows and Rhodes Scholars? 
    What gave Jackie Robinson the courage to become the first African American in Major League Baseball? 
    What was the catalyst that spurred Vint Cerf and Leonard Kleinrock's dream of the Internet?
    Here, at UDL- Marseille""",bg="black",fg="white")
    label_mar.pack(anchor=CENTER)
    label_mar2=Label(root_udl_mar,text="total no. of seats at UDL - marseille = 4,500 seats", bg="white", fg="black")
    label_mar2.pack(anchor=CENTER)
    label_mar3=Label(root_udl_mar,text="total no. of faculties = 350",bg="white",fg="black")
    label_mar3.pack(anchor=CENTER)
    frame_photo1=Frame(root_udl_mar)
    photo_2=PhotoImage(file="UDL-marseillelol.png")
    label_photo_2=Label(frame_photo1,image=photo_2)
    frame_photo1.pack()
    label_photo_2.pack()     

    root_udl_mar.mainloop()

def UDL_lyon():
    root_udl_lyon=tk.Toplevel()
    root_udl_lyon.geometry("810x480")
    root_udl_lyon.maxsize(810,480)
    root_udl_lyon.minsize(810,480)
    root_udl_lyon.title("University Of DENISELAND - Lyon")
    label_lyon=Label(root_udl_lyon,text="""UDL - Lyon, officially Leland Stanford Junior University,is a private research university in Lyon, Deniseland. 
    UDL - Lyon was founded in 1885 by Leland and Jane lyon in memory of their only child, Leland lyon Jr.
    who had died of typhoid fever at age 15 the previous year.
    University Of Deniseland - Lyon, is ranked among the best universities in the world by academic publications.
    It is also one of the top fundraising institutions in the country, becoming the first school to raise more than one billion dollars in a year.""",bg="black",fg="white")
    label_lyon.pack(anchor=CENTER)
    label_lyon2=Label(root_udl_lyon,text="total no. of seats at UDL - Lyon = 6,550 seats", bg="white", fg="black")
    label_lyon2.pack(anchor=CENTER)
    label_lyon3=Label(root_udl_lyon,text="total no. of faculties = 710",bg="white",fg="black")
    label_lyon3.pack(anchor=CENTER)
    frame_photo1=Frame(root_udl_lyon)
    photo_2=PhotoImage(file="uni-lyon.png")
    label_photo_2=Label(frame_photo1,image=photo_2)
    frame_photo1.pack()
    label_photo_2.pack()     

    root_udl_lyon.mainloop()


def UDL_bor():
    root_udl_bor=tk.Toplevel()
    root_udl_bor.geometry("840x500")
    root_udl_bor.maxsize(840,500)
    root_udl_bor.minsize(840,500)
    root_udl_bor.title("University Of DENISELAND - Bordeaux")
    label_bor=Label(root_udl_bor,text="""University of Deniseland - Bordeaux is a private Ivy League research university in Bordeaux, Deniseland. 
    Established in 1636 and named for its first benefactor, clergyman John Harvard, UDL - Bordeaux, is the oldest institution of higher learning in the Deniseland.
    And among the most prestigious in the world""",bg="black",fg="white")
    label_bor.pack(anchor=CENTER)
    label_bor2=Label(root_udl_bor,text="total no. of seats at UDL - Bordeaux = 4,100 seats", bg="white", fg="black")
    label_bor2.pack(anchor=CENTER)
    label_bor3=Label(root_udl_bor,text="total no. of faculties = 500+ ",bg="white",fg="black")
    label_bor3.pack(anchor=CENTER)
    frame_photo1=Frame(root_udl_bor)
    photo_2=PhotoImage(file="uni-bor.png")
    label_photo_2=Label(frame_photo1,image=photo_2)
    frame_photo1.pack()
    label_photo_2.pack()     

    root_udl_bor.mainloop()

def UDL_nice():
    root_udl_nice=tk.Toplevel()
    root_udl_nice.geometry("1080x385")
    root_udl_nice.maxsize(1080,385)
    root_udl_nice.minsize(1080,385)
    root_udl_nice.title("University Of DENISELAND - Nice")
    label_nice=Label(root_udl_nice,text="""The University of Deniseland - Nice is the five-campus public university system and the only public research system in the Commonwealth of deniseland. 
    The university system includes five campuses (Amherst, Boston, Dartmouth, Lowell, and a medical school in Worcester), and a satellite campus, with system administration in Boston and Shrewsbury.
    The system is accredited by the Deniseland Association of Schools and Colleges and across its campuses enrolls 73,000 students""",bg="black",fg="white")
    label_nice.pack(anchor=CENTER)
    label_nice2=Label(root_udl_nice,text="total no. of seats at UDL - Nice = 73,000 seats", bg="white", fg="black")
    label_nice2.pack(anchor=CENTER)
    label_nice3=Label(root_udl_nice,text="total no. of faculties = 11,000",bg="white",fg="black")
    label_nice3.pack(anchor=CENTER)
    frame_photo1=Frame(root_udl_nice)
    photo_2=PhotoImage(file="uni-nice.png")
    label_photo_2=Label(frame_photo1,image=photo_2)
    frame_photo1.pack()
    label_photo_2.pack()     

    root_udl_nice.mainloop()

def UDL_nan():
    root_udl_nan=tk.Toplevel()
    root_udl_nan.geometry("900x415")
    root_udl_nan.maxsize(900,415)
    root_udl_nan.minsize(900,415)
    root_udl_nan.title("University Of DENISELAND - Nantes")
    label_nan=Label(root_udl_nan,text="""Amongst Top 4 Private Engineering colleges in Deniseland by The Week 2020. Multicultural Campus. No. 1 Pvt University in deniseland by Education World 2020. 
    Get Placed in Top Companies. 600 Acre Green Campus. World-class Laboratories. 33000+ Students.""",bg="black",fg="white")
    label_nan.pack(anchor=CENTER)
    label_nan2=Label(root_udl_nan,text="total no. of seats at UDL - Nantes = 33,500 seats", bg="white", fg="black")
    label_nan2.pack(anchor=CENTER)
    label_nan3=Label(root_udl_nan,text="total no. of faculties = 4500",bg="white",fg="black")
    label_nan3.pack(anchor=CENTER)
    frame_photo1=Frame(root_udl_nan)
    photo_2=PhotoImage(file="uni-nan.png")
    label_photo_2=Label(frame_photo1,image=photo_2)
    frame_photo1.pack()
    label_photo_2.pack()     

    root_udl_nan.mainloop()

def UDL_ren():
    root_udl_ren=tk.Toplevel()
    root_udl_ren.geometry("1050x415")
    root_udl_ren.maxsize(1050,415)
    root_udl_ren.minsize(1050,415)
    root_udl_ren.title("University Of DENISELAND - Rennes")
    label_ren=Label(root_udl_ren,text="""We value the rich heritage and rich culture of Deniseland, and we belive that each band every child is capable of changing the world.
    with the best faculty, infrastructure and placements UDL - Rennes tops as one the best medical college, fully affiliated under the government of Deniseland.
    one of the top surgeons and medical professionals in the history have earned their degree from our prestiged institue and we look forward in creating more.
    giving the best medical support and interaction for over 100+ years and rated grade "A++" by the AIFE Branch Of Education we move forward in a path to give our best to humanity.
    """,bg="black",fg="white")
    label_ren.pack(anchor=CENTER)
    label_ren2=Label(root_udl_ren,text="total no. of seats at UDL - Rennes = 19,500 seats", bg="white", fg="black")
    label_ren2.pack(anchor=CENTER)
    label_ren3=Label(root_udl_ren,text="total no. of faculties = 7800",bg="white",fg="black")
    label_ren3.pack(anchor=CENTER)
    frame_photo1=Frame(root_udl_ren)
    photo_2=PhotoImage(file="uni-ren.png")
    label_photo_2=Label(frame_photo1,image=photo_2)
    frame_photo1.pack()
    label_photo_2.pack()     

    root_udl_ren.mainloop()

def UDL_bes():
    root_udl_bes=tk.Toplevel()
    root_udl_bes.geometry("1050x505")
    root_udl_bes.maxsize(1050,505)
    root_udl_bes.minsize(1050,505)
    root_udl_bes.title("University Of DENISELAND - Rennes")
    label_bes=Label(root_udl_bes,text="""Deniseland is known for its rich aesthetic and a safe and lovely invironment, as a university its our job to put those values into our future generation.
    with the growing inductry the young brains of Deniseland are working their best to stand out in this fast growing world.
    University of Deniseland - Besançon tries its best to provide the best work life exposure in the world, and have produced so many brilliant CEO 's which are running the world.
    great infrastructure and lush green campus spread within 200 acres we provide the best Management knowledge in the whole wide world.
    living the dream is not just an expression for us, we make it come true here at UDL - Besançon.
    """,bg="black",fg="white")
    label_bes.pack(anchor=CENTER)
    label_bes2=Label(root_udl_bes,text="total no. of seats at UDL - Rennes = 19,500 seats", bg="white", fg="black")
    label_bes2.pack(anchor=CENTER)
    label_bes3=Label(root_udl_bes,text="total no. of faculties = 7800",bg="white",fg="black")
    label_bes3.pack(anchor=CENTER)
    frame_photo1=Frame(root_udl_bes)
    photo_2=PhotoImage(file="uni-bes.png")
    label_photo_2=Label(frame_photo1,image=photo_2)
    frame_photo1.pack()
    label_photo_2.pack()     

    root_udl_bes.mainloop()
    

def list_aff_inst():
    root_aff=Tk()
    root_aff.geometry("200x195")
    root_aff.maxsize(200,195)
    root_aff.minsize(200,195)
    root_aff.title("List of Affiliated Institues")
    l_aff1=Label(root_aff,text="UDL Marseille")
    l_aff2=Label(root_aff,text="UDL Lyon")
    l_aff3=Label(root_aff,text="UDL Bordeaux")
    l_aff4=Label(root_aff,text="UDL Nice")
    l_aff5=Label(root_aff,text="UDL Nantes")
    l_aff6=Label(root_aff,text="UDL Rennes")
    l_aff7=Label(root_aff,text="UDL Besançon")
    l_aff1.grid(row=0,column=1)
    l_aff2.grid(row=1,column=1)
    l_aff3.grid(row=2,column=1)
    l_aff4.grid(row=3,column=1)
    l_aff5.grid(row=4,column=1)
    l_aff6.grid(row=5,column=1)
    l_aff7.grid(row=6,column=1)

    frame_aff1=Frame(root_aff)
    button_aff1=Button(frame_aff1,text="about?",fg="black",command=UDL_mar)
    button_aff1.pack()
    frame_aff1.grid(row=0,column=2)    
    frame_aff2=Frame(root_aff)
    button_aff2=Button(frame_aff2,text="about?",fg="black",command=UDL_lyon)
    button_aff2.pack()
    frame_aff2.grid(row=1,column=2)
    frame_aff3=Frame(root_aff)
    button_aff3=Button(frame_aff3,text="about?",fg="black",command=UDL_bor)
    button_aff3.pack()
    frame_aff3.grid(row=2,column=2)
    frame_aff4=Frame(root_aff)
    button_aff4=Button(frame_aff4,text="about?",fg="black",command=UDL_nice)
    button_aff4.pack()
    frame_aff4.grid(row=3,column=2)
    frame_aff5=Frame(root_aff)
    button_aff5=Button(frame_aff5,text="about?",fg="black",command=UDL_nan)
    button_aff5.pack()
    frame_aff5.grid(row=4,column=2)
    frame_aff6=Frame(root_aff)
    button_aff6=Button(frame_aff6,text="about?",fg="black",command=UDL_ren)
    button_aff6.pack()
    frame_aff6.grid(row=5,column=2)
    frame_aff7=Frame(root_aff)
    button_aff7=Button(frame_aff7,text="about?",fg="black",command=UDL_bes)
    button_aff7.pack()
    frame_aff7.grid(row=6,column=2)
    root_aff.mainloop()

def officers():
    root_off=Tk()
    root_off.geometry("300x157")
    root_off.maxsize(300,157)
    root_off.minsize(300,157)
    root_off.title("Officers")
    label_off=Label(root_off,text="""1) Rita Ora   -    ritaorabbr@gmail.com
    2) Nadia Trainor   -   trainornadia.88@hotmail.com
    3) Prince Naveen   -   prince00@yahoo.com
    4) McLane Laura    -   mslauranusiness@gmail.com
    5) Louis Tomilson  -   tlouisjr@hotmail.com
    6) Rayn Dorothy    -   ryandsnr@yahoo.com
    7) Mr. M. Fletcher -   marcohfletcher0020@gmail.com
    8) Dr. Mira Patel  -   drmirapatel.1@gmail.com
    9) Mrs. Fu Haan Shao   -   fuhaan@hotmail.com
    10) Alexander Moore -   mrmoorealex7878@gmail.com""", bg= "white", fg="black", relief=RAISED)
    label_off.pack()
    root_off.mainloop()

def ann_sports():
    root_ann_sp=tk.Toplevel()
    root_ann_sp.geometry("670x350")
    root_ann_sp.maxsize()
    root_ann_sp.minsize()
    root_ann_sp.title("ANNUAL SPORTS MEET")
    frame_photo1=Frame(root_ann_sp)
    photo_2=PhotoImage(file="ann-sp.png")
    label_photo_2=Label(frame_photo1,image=photo_2)
    frame_photo1.pack()
    label_photo_2.pack()

    label_ann_sp=Label(root_ann_sp,text=""" 
    THE GRAND ANNUAL DENISELAND SPORTS FEST
    """, bg="black", fg="white")
    label_ann_sp.pack()
    label_ann_sp1=Label(root_ann_sp,text="""" 
    Deniseland, have always been the land of awesome minds, spectacular physique, undefinable knowledge and much more
    The young generations have tried their best to never let the holy name of Deniseland ever down.
    with all pride we try to innovate the future in our prestegious university of deniseland.
    With the great Athletes of all times, we commence the departure of the GRAND ANNUAL SPORTS MEET.
    """, bg="white", fg="black")
    label_ann_sp1.pack()
    root_ann_sp.mainloop()


def sports():
    root_sp=Tk()
    root_sp.geometry("500x350")
    root_sp.maxsize()
    root_sp.minsize()
    root_sp.title("Sports and Cultural Activities")
    lsp1=Label(root_sp,text="ANNUAL SPORTS MEET")
    lsp2=Label(root_sp,text="ANNUAL CULTURAL MEET")
    lsp1.grid(row=0,column=1)
    lsp2.grid(row=1,column=1)

    frame_sp1=Frame(root_sp)
    button_sp1=Button(frame_sp1,text="Click to know more",fg="black",command=ann_sports)
    button_sp1.pack()
    frame_sp1.grid(row=0,column=2)    
    frame_sp2=Frame(root_sp)
    button_sp2=Button(frame_sp2,text="click to know more",fg="black")
    button_sp2.pack()
    frame_sp2.grid(row=1,column=2)
    
    root_sp.mainloop()



def affiliated_institutes():
    root_ai=Tk()
    root_ai.geometry("500x350")
    root_ai.maxsize()
    root_ai.minsize()
    root_ai.title("Affiliated Institutes")
    frame_ai1=Frame(root_ai,borderwidth=6,bg="pink",relief=RAISED)
    button_ai1=Button(frame_ai1,text="List of Affiliated Institutes",fg="black",command=list_aff_inst)
    button_ai1.pack()
    frame_ai1.pack(anchor=CENTER, pady=20)

    frame_ai2=Frame(root_ai,borderwidth=6,bg="pink",relief=RAISED)
    button_ai2=Button(frame_ai2,text="Officers",fg="black",command=officers)
    button_ai2.pack()
    frame_ai2.pack(anchor=CENTER, pady=20)

    frame_ai3=Frame(root_ai,borderwidth=6,bg="pink",relief=RAISED)
    button_ai3=Button(frame_ai3,text="Sports and Cultural Activities",fg="black",command=sports)
    button_ai3.pack()
    frame_ai3.pack(anchor=CENTER, pady=20)
    
    root_ai.mainloop()



def academics():
    root_ac=Tk()
    root_ac.geometry("500x350")
    root_ac.maxsize(500,350)
    root_ac.minsize(500,350)
    root_ac.title("Academics")
    frame_ac1=Frame(root_ac,borderwidth=6,bg="blue",relief=RAISED)
    button_ac1=Button(frame_ac1,text="Courses Offered",fg="black",command=courses_offered)
    button_ac1.pack()
    frame_ac1.pack(anchor=CENTER, pady=20)

    frame_ac2=Frame(root_ac,borderwidth=6,bg="blue",relief=RAISED)
    button_ac2=Button(frame_ac2,text="Affiliated Institutes",fg="black",command=affiliated_institutes)
    button_ac2.pack()
    frame_ac2.pack(anchor=CENTER, pady=20)

    frame_ac3=Frame(root_ac,borderwidth=6,bg="blue",relief=RAISED)
    button_ac3=Button(frame_ac3,text="Scheme/Syllabus",fg="black")
    button_ac3.pack()
    frame_ac3.pack(anchor=CENTER, pady=20)

    frame_ac4=Frame(root_ac,borderwidth=6,bg="blue",relief=RAISED)
    button_ac4=Button(frame_ac4,text="International Affairs",fg="black")
    button_ac4.pack()
    frame_ac4.pack(anchor=CENTER, pady=20)
    root_ac.mainloop()

def main():
    root=Tk() 
    root.geometry("800x630")
    root.maxsize(800,630)
    root.minsize(800,630)
    root.title("University Of DENISELAND")
    
    photo_1=PhotoImage(file="unimain.png")
    label_photo_1=Label(root,image=photo_1)
    label_photo_1.pack()

    frame_1=Frame(root,borderwidth=2,bg="maroon",relief=FLAT)
    button_1=Button(frame_1,text="Admission",fg="black",command=admission)
    
    button_1.pack()
    frame_1.pack(anchor=CENTER, pady=20)

    frame_2=Frame(root,borderwidth=2,bg="maroon",relief=FLAT)
    button_2=Button(frame_2,text="Academics",fg="black",command=academics)
    button_2.pack()
    frame_2.pack(anchor=CENTER, pady=20)

    frame_3=Frame(root,borderwidth=2,bg="maroon",relief=FLAT)
    button_3=Button(frame_3,text="Students & Alumini",fg="black")
    button_3.pack()
    frame_3.pack(anchor=CENTER,pady=20)

    frame_4=Frame(root,borderwidth=2,bg="maroon",relief=FLAT)
    button_4=Button(frame_4,text="about?",fg="black")
    button_4.pack()
    frame_4.pack(anchor=CENTER, pady=20)

    frame_photo1=Frame(root)
    photo_2=PhotoImage(file="dd2.png")
    label_photo_2=Label(frame_photo1,image=photo_2)
    frame_photo1.pack(side=LEFT)
    label_photo_2.grid(row=0,column=1)

    frame_photo2=Frame(root)
    photo_3=PhotoImage(file="vp2.png")
    label_photo_3=Label(frame_photo2,image=photo_3)
    frame_photo2.pack(side=RIGHT)
    label_photo_3.grid(row=0,column=1)

    label_text1=Label(frame_photo1,text="Director of UDL - Meme Gurl")
    label_text1.grid(row=1,column=1)

    label_text2=Label(frame_photo2,text="Vice Principal of UDL - Wants Boobs")
    label_text2.grid(row=1,column=1)

    root.mainloop()
if __name__=="__main__":
    main()