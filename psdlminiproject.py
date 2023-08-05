from tkinter import *
import math,random
from tkinter import messagebox

root=Tk() 
scroll_text= StringVar()
msg2 = "THANK YOU FOR VISITING US..."
text2 = ""
n=0
class Bill_App:

    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("RESTARANT")
        bg_color="thistle3"
        title=Label(self.root,text="WORLD OF VEG",bd=10,relief=GROOVE,bg=bg_color,fg="black",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #=====var====
        #====starter======
        self.Veg_Crispy=IntVar()
        self.Honey_Chilli_potato=IntVar()
        self.spinach_roll=IntVar()
        self.alfredo_pasta=IntVar()
        self.veg_manchurian=IntVar()
        self.kabab=IntVar()

        #=====main course====
        self.palak_paneer=IntVar()
        self.kaju_masala=IntVar()
        self.veg_kofta=IntVar()
        self.jeera_rice=IntVar()
        self.naan=IntVar()
        self.dal_tadka=IntVar()

        #=====Dessert====
        self.brownie=IntVar()
        self.icecream=IntVar()
        self.cheesecake=IntVar()
        self.pancake=IntVar()
        self.waffles=IntVar()
        self.pudding=IntVar()

        #=====Total Price=====
        self.starter_price=StringVar()
        self.main_course_price=StringVar()
        self.dessert_price=StringVar()

        #=======Tax price======
        self.starter_tax=StringVar()
        self.main_course_tax=StringVar()
        self.dessert_tax=StringVar()

        #====name of customer=====
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill=StringVar()
        a=random.randint(1000,9999)
        self.bill.set(str(a))
        self.search_bill=StringVar()

        #===========cust Detail========
        F1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),bg=bg_color,fg="#191970")#
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Name Of Customer",bg=bg_color,fg="#003151",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=20,textvariable=self.c_name,font="arial 10",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)

        cphn_lbl=Label(F1,text="Phone Number",bg=bg_color,fg="#003151",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=20,textvariable=self.c_phon,font="arial 10",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=5,pady=10)

      
        #======Starter Frame=======
        F2=LabelFrame(self.root,text="Starter",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="#191970",bg=bg_color)
        F2.place(x=5,y=180,width=335,height=380)

        Veg_Crispy_lbl1=Label(F2,text="Veg Crispy(Rs.180)",font=("times new roman",13,"bold"),bg=bg_color,fg="#003151").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Veg_Crispy_txt=Entry(F2,width=7,textvariable=self.Veg_Crispy,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
     
        Honey_Chilli_potato_lbl1=Label(F2,text="Honey chilli potato(Rs.200)",font=("times new roman",13,"bold"),bg=bg_color,fg="#003151").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Honey_Chilli_potato_txt=Entry(F2,width=7,textvariable=self.Honey_Chilli_potato,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        alfredo_pasta_lbl1=Label(F2,text="Alfredo Pasta(Rs.250)",font=("times new roman",13,"bold"),bg=bg_color,fg="#003151").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        alfredo_pasta_txt=Entry(F2,width=7,textvariable=self.alfredo_pasta,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        veg_manchurian_lbl1=Label(F2,text="Veg Manchurian(Rs.190)",font=("times new roman",13,"bold"),bg=bg_color,fg="#003151").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        veg_manchurian_txt=Entry(F2,width=7,textvariable=self.veg_manchurian,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
       
        spinach_roll_lbl1=Label(F2,text="Spinach Roll(Rs.175)",font=("times new roman",13,"bold"),bg=bg_color,fg="#003151").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        spinach_roll_txt=Entry(F2,width=7,textvariable=self.spinach_roll,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        kabab_lbl1=Label(F2,text="Kabab(Rs.150)",font=("times new roman",13,"bold"),bg=bg_color,fg="#003151").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        kabab_txt=Entry(F2,width=7,textvariable=self.kabab,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #  =======main course Frame=======

        F3=LabelFrame(self.root,text="Main Course",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="#191970",bg=bg_color)
        F3.place(x=345,y=180,width=335,height=380)

        palak_paneer_lbl1=Label(F3,text="Palak Paneer(Rs.285)",font=("times new roman",13,"bold"),bg=bg_color,fg="#003151").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        palak_paneer_txt=Entry(F3,width=7,textvariable=self.palak_paneer,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
     
        kaju_masala_lbl1=Label(F3,text="Kaju masala(Rs.300)",font=("times new roman",13,"bold"),bg=bg_color,fg="#003151").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        kaju_masala_txt=Entry(F3,width=7,textvariable=self.kaju_masala,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        veg_kofta_lbl1=Label(F3,text="Veg Kofta(Rs.290)",font=("times new roman",13,"bold"),bg=bg_color,fg="#003151").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        veg_kofta_txt=Entry(F3,width=7,textvariable=self.veg_kofta,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        jeera_rice_lbl1=Label(F3,text="Jeera Rice(Rs.200)",font=("times new roman",13,"bold"),bg=bg_color,fg="#003151").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        jeera_rice_txt=Entry(F3,width=7,textvariable=self.jeera_rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
       
        naan_lbl1=Label(F3,text="Naan(Rs.50)",font=("times new roman",13,"bold"),bg=bg_color,fg="#003151").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        naan_txt=Entry(F3,width=7,textvariable=self.naan,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        dal_tadka_lbl1=Label(F3,text="Daal Tadka(Rs.190)",font=("times new roman",13,"bold"),bg=bg_color,fg="#003151").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        dal_tadka_txt=Entry(F3,width=7,textvariable=self.dal_tadka,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        #========Dessert Frame============

        F4=LabelFrame(self.root,text="Dessert",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="#191970",bg=bg_color)
        F4.place(x=679,y=180,width=325,height=380)

        brownie_lbl1=Label(F4,text=" Brownie(Rs.120)",font=("times new roman",13,"bold"),bg=bg_color,fg="#003151").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        brownie_txt=Entry(F4,width=10,textvariable=self.brownie,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
     
        icecream_lbl1=Label(F4,text="Icecream(Rs.50)",font=("times new roman",13,"bold"),bg=bg_color,fg="#003151").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        icecream_txt=Entry(F4,width=10,textvariable=self.icecream,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        cheesecake_lbl1=Label(F4,text="Cheese Cake(Rs.280)",font=("times new roman",13,"bold"),bg=bg_color,fg="#003151").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        cheesecake_txt=Entry(F4,width=10,textvariable=self.cheesecake,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        pancake_lbl1=Label(F4,text="Pancake(Rs.200)",font=("times new roman",13,"bold"),bg=bg_color,fg="#003151").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        pancake_txt=Entry(F4,width=10,textvariable=self.pancake,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
       
        waffles_lbl1=Label(F4,text="Waffles(Rs.240)",font=("times new roman",13,"bold"),bg=bg_color,fg="#003151").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        waffles_txt=Entry(F4,width=10,textvariable=self.waffles,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        pudding_lbl1=Label(F4,text="Pudding(Rs.210)",font=("times new roman",13,"bold"),bg=bg_color,fg="#003151").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        pudding_txt=Entry(F4,width=10,textvariable=self.pudding,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        
        # Bill

        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=520,height=380)
        bill=Label(F5,text="BILL",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #=======Button=======
        F6=LabelFrame(self.root,text="Bill Menu",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="#191970",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)

        a1_lbl1=Label(F6,text="Total Starter Price",bg=bg_color,fg="#003151",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        a1_txt=Entry(F6,width=18,textvariable=self.starter_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        a2_lbl1=Label(F6,text="Total Main Course Price",bg=bg_color,fg="#003151",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        a2_txt=Entry(F6,width=18,textvariable=self.main_course_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        a3_lbl1=Label(F6,text="Total Dessert Price",bg=bg_color,fg="#003151",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        a3_txt=Entry(F6,width=18,textvariable=self.dessert_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        
        b1_lbl1=Label(F6,text="Starter Tax",bg=bg_color,fg="#003151",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        b1_txt=Entry(F6,width=18,textvariable=self.starter_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        b2_lbl1=Label(F6,text="Main Course Tax",bg=bg_color,fg="#003151",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        b2_txt=Entry(F6,width=18,textvariable=self.main_course_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        b3_lbl1=Label(F6,text="Dessert Tax",bg=bg_color,fg="#003151",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        b3_txt=Entry(F6,width=18,textvariable=self.dessert_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_A=Frame(F6,bd=7,relief=GROOVE)
        btn_A.place(x=750,width=570,height=105)

        

        total=Button(btn_A,command=self.total,text="Total",bg="#03C04A",fg="White",bd=5,pady=15,width=11,font="arial 13 bold").grid(row=0,column=0,padx=5,pady=5)
        Generate_bill=Button(btn_A,command=self.bill_area,text="Generate Bill",bg="#03C04A",fg="White",bd=5,pady=15,width=11,font="arial 13 bold").grid(row=0,column=1,padx=5,pady=5)
        clear=Button(btn_A,text="Clear",command=self.clear_data,bg="#03C04A",fg="White",bd=5,pady=15,width=11,font="arial 13 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit=Button(btn_A,text="Exit",command=self.Exit_app,bg="#03C04A",fg="White",bd=5,pady=15,width=11,font="arial 13 bold").grid(row=0,column=3,padx=5,pady=5)
        
        self.welcome_bill()

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,fg="#191970",bg=bg_color)
        F6.place(x=0,y=690,relwidth=1,height=110)


         #============scroll text=============
        
        def display():
            global text2, n, msg2
            for t in range(len(msg2)):
                for k in range(t):
                    text2 += ' '
                for g in range(len(msg2) - t):
                    text2 += msg2[g]
                
                F6.update()
                F6.after(200)
                text2 = text2.strip()
                scroll_text.set('')
                scroll_text.set(text2)
                text2 = ''
            scroll_text.set('')
            txtscroll.after(200,display)
        
        txtscroll=Entry(F6,textvariable=scroll_text, font=('arial',50,'bold'), fg='#003151', bd=10, bg=bg_color, width=150)
        txtscroll.grid(row=0, column=0, columnspan=4)
        display()

    def total(self):
        self.palak_paneer_price=285
        self.kaju_masala_price=300
        self.veg_kofta_price=290
        self.jeera_rice_price=200
        self.naan_price=50
        self.dal_tadka_price=190
        self.c_l_p=(self.palak_paneer.get()*self.palak_paneer_price)
        self.c_d_p=(self.kaju_masala.get()*self.kaju_masala_price)
        self.c_p_p=(self.veg_kofta.get()*self.veg_kofta_price)
        self.c_pe_p=(self.jeera_rice.get()*self.jeera_rice_price)
        self.c_ku_p=(self.naan.get()*self.naan_price)
        self.c_w_p=(self.dal_tadka.get()*self.dal_tadka_price)
        self.total_main_course_price=float(
                                self.c_l_p+
                                self.c_d_p+
                                self.c_p_p+
                                self.c_pe_p+
                                self.c_ku_p+
                                self.c_w_p
                                )
        self.main_course_price.set("Rs. "+str(self.total_main_course_price))
        self.cs_tax=round((self.total_main_course_price*0.1),2)
        self.main_course_tax.set("Rs. "+str(self.cs_tax))

        self.Veg_Crispy_price=180
        self.Honey_Chilli_potato_price=200
        self.alfredo_pasta_price=250
        self.veg_manchurian_price=190
        self.spinach_roll_price=175
        self.kabab_price=150
        self.j_s_p= (self.Veg_Crispy.get()*self.Veg_Crispy_price)
        self.j_t_p=(self.Honey_Chilli_potato.get()*self.Honey_Chilli_potato_price)
        self.j_c_p=(self.alfredo_pasta.get()*self.alfredo_pasta_price)
        self.j_sv_p=(self.veg_manchurian.get()*self.veg_manchurian_price)
        self.j_d_p=(self.spinach_roll.get()*self.spinach_roll_price)
        self.j_m_p=(self.kabab.get()*self.kabab_price)
        self.total_starter_price=float(
                                self.j_s_p+
                                self.j_t_p+
                                self.j_c_p+
                                self.j_sv_p+
                                self.j_d_p+
                                self.j_m_p
                                )
        self.starter_price.set("Rs. "+str(self.total_starter_price))
        self.s_tax=round((self.total_starter_price*0.05),2)
        self.starter_tax.set("Rs. "+str(self.s_tax))

        self.brownie_price=120
        self.icecream_price=50
        self.cheesecake_price=280
        self.pancake_price=200
        self.waffles_price=240
        self.pudding_price=210
        self.c_s_p=(self.brownie.get()*self.brownie_price)
        self.c_t_p=(self.icecream.get()*self.icecream_price)
        self.c_k_p=(self.cheesecake.get()*self.cheesecake_price)
        self.c_sr_p=(self.pancake.get()*self.pancake_price)
        self.c_st_p=(self.waffles.get()*self.waffles_price)
        self.c_f_p=(self.pudding.get()*self.pudding_price)
        self.total_dessert_price=float(
                                self.c_s_p+
                                self.c_t_p+
                                self.c_k_p+
                                self.c_sr_p+
                                self.c_st_p+
                                self.c_f_p
                                )
        self.dessert_price.set("Rs. "+str(self.total_dessert_price))
        self.ch_tax=round((self.total_dessert_price*0.15),2)
        self.dessert_tax.set("Rs. "+str(self.ch_tax))
    
        self.Total_bill=float(self.total_main_course_price+
                            self.total_dessert_price+
                            self.total_starter_price+
                            self.cs_tax+
                            self.s_tax+
                            self.ch_tax
                            )   

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t\t\tWELCOME FOOD RETAIL\n")
        self.txtarea.insert(END,f"\n BILL NUMBER : {self.bill.get()}")
        self.txtarea.insert(END,f"\n CUSTOMER NAME : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n PHONE NUMBER : {self.c_phon.get()}")
        self.txtarea.insert(END,f"\n===========================================================")
        self.txtarea.insert(END,f"\n PRODUCTS\t\tQUANTITY\t\tPRICE\t\tTOTAL PRICE")
        self.txtarea.insert(END,f"\n===========================================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer Detais are Required")
        elif self.starter_price.get()=="Rs. 0.0" and self.main_course_price.get()=="Rs. 0.0" and self.chocolate_price.get()=="Rs. 0.0":
             messagebox.showerror("Error","Products Not selected")
        else:
            self.welcome_bill()

            #====starter bill generate======
            if self.Veg_Crispy.get()!=0:
                self.txtarea.insert(END,f"\n Veg_Crispy\t\t{self.Veg_Crispy.get()}\t\t{self.Veg_Crispy_price}\t\t{self.j_s_p}")
            if self.Honey_Chilli_potato.get()!=0:
                self.txtarea.insert(END,f"\n Honey chilli potato\t\t{self.Honey_Chilli_potato.get()}\t\t{self.Honey_Chilli_potato_price}\t\t{self.j_t_p}")
            if self.alfredo_pasta.get()!=0:
                self.txtarea.insert(END,f"\n alfredo_pasta\t\t{self.alfredo_pasta.get()}\t\t{self.alfredo_pasta_price}\t\t{self.j_c_p}")
            if self.veg_manchurian.get()!=0:
                self.txtarea.insert(END,f"\n veg_manchurian \t\t{self.veg_manchurian.get()}\t\t{self.veg_manchurian_price}\t\t{self.j_sv_p}")
            if self.spinach_roll.get()!=0:
                self.txtarea.insert(END,f"\n spinach_roll\t\t{self.spinach_roll.get()}\t\t{self.spinach_roll_price}\t\t{self.j_d_p}")
            if self.kabab.get()!=0:
                self.txtarea.insert(END,f"\n Kabab\t\t{self.kabab.get()}\t\t{self.kabab_price}\t\t{self.j_m_p}")
                
            #=========main course bill generate======    
            if self.palak_paneer.get()!=0:
                self.txtarea.insert(END,f"\n Palak Paneer\t\t{self.palak_paneer.get()}\t\t{self.palak_paneer_price}\t\t{self.c_l_p}")
            if self.kaju_masala.get()!=0:
                self.txtarea.insert(END,f"\n Kaju Masala\t\t{self.kaju_masala.get()}\t\t{self.kaju_masala_price}\t\t{self.c_d_p}")
            if self.veg_kofta.get()!=0:
                self.txtarea.insert(END,f"\n Veg Kofta\t\t{self.veg_kofta.get()}\t\t{self.veg_kofta_price}\t\t{self.c_p_p}")
            if self.jeera_rice.get()!=0:
                self.txtarea.insert(END,f"\n Jeera Rice\t\t{self.jeera_rice.get()}\t\t{self.jeera_rice_price}\t\t{self.c_pe_p}")
            if self.naan.get()!=0:
                self.txtarea.insert(END,f"\n Naan\t\t{self.naan.get()}\t\t{self.naan_price}\t\t{self.c_ku_p}")
            if self.dal_tadka.get()!=0:
                self.txtarea.insert(END,f"\n Dal Tadka\t\t{self.dal_tadka.get()}\t\t{self.dal_tadka_price}\t\t{self.c_w_p}")

            #=========dessert bill generate=====
            if self.brownie.get()!=0:
                self.txtarea.insert(END,f"\n Brownie\t\t{self.brownie.get()}\t\t{self.brownie_price}\t\t{self.c_s_p}")
            if self.icecream.get()!=0:
                self.txtarea.insert(END,f"\n Icecream\t\t{self.icecream.get()}\t\t{self.icecream_price}\t\t{self.c_t_p}")
            if self.cheesecake.get()!=0:
                self.txtarea.insert(END,f"\n Cheese Cake\t\t{self.cheesecake.get()}\t\t{self.cheesecake_price}\t\t{self.c_k_p}")
            if self.pancake.get()!=0:
                self.txtarea.insert(END,f"\n Pancake\t\t{self.pancake.get()}\t\t{self.pancake_price}\t\t{self.c_sr_p}")
            if self.waffles.get()!=0:
                self.txtarea.insert(END,f"\n Waffles\t\t{self.waffles.get()}\t\t{self.waffles_price}\t\t{self.c_st_p}")
            if self.pudding.get()!=0:
                self.txtarea.insert(END,f"\n Pudding\t\t{self.pudding.get()}\t\t{self.pudding_price}\t\t{self.c_f_p}")
            
            self.txtarea.insert(END,f"\n-----------------------------------------------------------")
            if self.starter_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Starter Tax\t\t\t\t\t\t{self.starter_tax.get()}")
            if self.main_course_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Main Course Tax\t\t\t\t\t\t{self.main_course_tax.get()}")
            if self.dessert_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n chocolate Tax\t\t\t\t\t\t{self.dessert_tax.get()}")
            
            self.txtarea.insert(END,f"\n TOTAL BILL\t\t\t\t\t\tRs. {str(self.Total_bill)}")
            self.txtarea.insert(END,f"\n-----------------------------------------------------------")
            self.save_bill()
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("D:\\Python_code\\Python_Project\\bills"+str(self.bill.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No :{self.bill.get()} Saved Succeddfully")
        else:
            return
   
    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you want to clear?")
        if op>0:
            self.Veg_Crispy.set(0)
            self.Honey_Chilli_potato.set(0)
            self.alfredo_pasta.set(0)
            self.veg_manchurian.set(0)
            self.spinach_roll.set(0)
            self.kabab.set(0)

            #=====Main course=====
            self.palak_paneer.set(0)
            self.kaju_masala.set(0)
            self.veg_kofta.set(0)
            self.jeera_rice.set(0)
            self.naan.set(0)
            self.dal_tadka.set(0)

            #=====Dessert====
            self.brownie.set(0)
            self.icecream.set(0)
            self.cheesecake.set(0)
            self.pancake.set(0)
            self.waffles.set(0)
            self.pudding.set(0)

            #=====Total Price=====
            self.starter_price.set("")
            self.main_course_price.set("")
            self.dessert_price.set("")

            #=======Tax price======
            self.starter_tax.set("")
            self.main_course_tax.set("")
            self.dessert_tax.set("")

            #====name of customer=====
            self.c_name.set("")
            self.c_phon.set("")
            self.bill.set("")
            a=random.randint(1000,9999)
            self.bill.set(str(a))
            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op>0:
            self.root.destroy()
  
obj=Bill_App(root)
root.configure(bg="#87CEEB")
root.mainloop()
