import os.path
import random
import subprocess
import pandas as pd
import csv

import tkinter as tk
import tkinter.messagebox
from tkinter import *
from tkinter.ttk import *
import tkinter.font as font


def id_gen():
    num =random.randint(00000,10000)
    directory = "PatientData/"
    files= os.listdir(directory)
    for f in files:
        if f == str(num)+'.txt' :
            id_gen()
        return num



def signup():
	global K1
	global K2
	usr=K1.get()
	pssd=K2.get()
	if usr=='' or pssd=='':
		tkinter.messagebox.showinfo( "Error", "user name or password cannot be empty!")
	else:
		df=pd.read_csv('database.csv');
		dicti={'PiD':[''],'User':[usr],'Password':[pssd],'Edit':[1]}
		df1=pd.DataFrame.from_dict(dicti)
		df3 = pd.concat([df, df1], ignore_index = True)
		df3.to_csv('database.csv', sep=',', index= False)
		tkinter.messagebox.showinfo( "Success", "Signup successful! Login!!")
		global current_frame
		current_frame.pack_forget()
		top.pack()
		current_frame = top	


def log_in():
	global E1
	global E2
	global usr
	print("In Login")
	usr=E1.get()
	pssd=E2.get()
	print(usr)
	print(pssd)
	if usr=='' or pssd=='':
		tkinter.messagebox.showinfo( "Error", "user name or password cannot be empty!")
	else:
		check_login(str(usr),str(pssd))

def check_login(usr,pssd):
	df=pd.read_csv('database.csv');
	if df['User'].eq(usr).any():
		#print('username OK')
		if df['Password'].eq(pssd).any():
			tkinter.messagebox.showinfo( "Success", "login successful!")
			create_patientInfo_frame()
		else:
			tkinter.messagebox.showinfo( "Error", "Wrong user name or password!")
	else:
		tkinter.messagebox.showinfo( "Error", "Wrong user name or password!")

def log_in_patient():
	global E1
	global E2
	global usr
	print("In Patient Login")
	usr=E1.get()
	pssd=E2.get()
	print(usr)
	print(pssd)
	if usr=='' or pssd=='':
		tkinter.messagebox.showinfo( "Error", "user name or password cannot be empty!")
	else:
		check_login_patient(str(usr),str(pssd))

def check_login_patient(usr,pssd):
	df=pd.read_csv('database.csv');
	if df['User'].eq(usr).any():
		#print('username OK')
		if df['Password'].eq(pssd).any():
			tkinter.messagebox.showinfo( "Success", "login successful!")
			#create_patientInfo_frame()
			create_patientInfoRO_frame()
		else:
			tkinter.messagebox.showinfo( "Error", "Wrong user name or password!")
	else:
		tkinter.messagebox.showinfo( "Error", "Wrong user name or password!")



def patientInfo():
	global E3
	global usr
	global PiD
	print('In patient Info')
	PiD=E3.get()
	print(PiD)
	df=pd.read_csv('database.csv');
	if df['PiD'].eq(PiD).any():
		print('Found')
		file1 = open('PatientData/'+str(PiD)+".txt","r+")
		data=file1.read()
		file1.close()
		create_displayFrameDoctor(data)
	else:
		tkinter.messagebox.showinfo( "Error", "Wrong Patient ID")


def patientInfoRO():
	global E3
	global usr
	print('In patient Info RO')
	PiD=E3.get()
	print(PiD)
	df=pd.read_csv('database.csv');
	if df['PiD'].eq(PiD).any():
		print('Found')
		print(usr)
		file1 = open('PatientData/'+str(PiD)+".txt","r+")
		data=file1.read()
		file1.close()
		create_displayFrame(data)
	else:
		tkinter.messagebox.showinfo( "Error", "Wrong Patient ID")
	


def addpatientInfo_Old():
	global E3
	global PiD
	print('In patient Info')
	print(PiD)
	df=pd.read_csv('database.csv');
	if df['PiD'].eq(PiD).any():
		print('Patient Already Exists!!')
		tkinter.messagebox.showinfo( "Error", 'Patient Already Exists!!')
		global current_frame	
		current_frame.pack_forget()
		patientInfo_frame.pack()
		current_frame = patientInfo_frame
	else:
		addPatientFrame()

def PatientDataEdit(data):
	create_EditdisplayFrameDoctor(data)

def patientDataUpdate():
	global L11
	global PiD
	data=L11.get('1.0', 'end-1c')
	print(data)
	file1=open('PatientData/'+str(PiD)+'.txt','w')
	file1.write(data)
	file1.close()
	tkinter.messagebox.showinfo( "Success", 'Successfully Added to Patient History!!')

def addPatientFrame():
	global E4
	global E5
	global E6
	global E7
	global PiD
	PiD=id_gen()
	Lx1=tk.Label(addpatientInfo_frame,bg="white",text='Enter Patient ID')
	Lx1['font']=myFont
	Lx1.grid(sticky = W,row=0, column=0, padx=5, pady=10)
	Ex1=tk.Text(addpatientInfo_frame,bg="white", height=1,width=20)
	Ex1['font']=myFont
	Ex1.insert("1.0", PiD)
	Ex1.grid(sticky = W,row=0, column=1, padx=5, pady=10)

	Lx2=tk.Label(addpatientInfo_frame,bg="white",text='Enter Patient User ID')
	Lx2['font']=myFont
	Lx2.grid(sticky = W,row=1, column=0, padx=5, pady=10)
	Ex2=tk.Entry(addpatientInfo_frame,bg="white", textvariable = E5, width=20)
	Ex2['font']=myFont
	Ex2.grid(sticky = W,row=1, column=1, padx=5, pady=10)
	Lx3=tk.Label(addpatientInfo_frame,bg="white",text='Enter Patient Password')
	Lx3['font']=myFont
	Lx3.grid(sticky = W,row=2, column=0, padx=5, pady=10)
	Ex3=tk.Entry(addpatientInfo_frame,bg="white", textvariable = E6, show='*', width=20)
	Ex3['font']=myFont
	Ex3.grid(sticky = W,row=2, column=1, padx=5, pady=10)
	Lx4=tk.Label(addpatientInfo_frame,bg="white",text='Enter Patient Health Data')
	Lx4['font']=myFont
	Lx4.grid(sticky = W,row=3, column=0, padx=5, pady=10)
	Ex4=tk.Entry(addpatientInfo_frame,bg="white", textvariable = E7, width=30)
	Ex4['font']=myFont
	Ex4.grid(sticky = W,row=3, column=1, padx=5, pady=10)
	Bx1=tk.Button(addpatientInfo_frame,bg="white", text="Add Details", command=lambda:addpatientInfo())
	Bx1['font']=myFont
	Bx1.grid(sticky = W,row=4, column=1, padx=5, pady=10)
	Bx2=tk.Button(addpatientInfo_frame,bg="white", text="Exit", command=closer)
	Bx2['font']=myFont
	Bx2.grid(sticky = W,row=5, column=1, padx=5, pady=10)
	global current_frame
	current_frame.pack_forget()
	addpatientInfo_frame.pack()
	current_frame = addpatientInfo_frame

def addpatientInfo():
	global E4
	global E5
	global E6
	global E7
	global PiD
	print('In add patient Info')
	PiD=PiD
	usr=E5.get()
	pssd=E6.get()
	Dt=E7.get()
	df=pd.read_csv('database.csv');
	dicti={'PiD':[PiD],'User':[usr],'Password':[pssd],'Edit':[1]}
	df1=pd.DataFrame.from_dict(dicti)
	df3 = pd.concat([df, df1], ignore_index = True)
	df3.to_csv('database.csv', sep=',', index= False)
	file1=open('PatientData/'+str(PiD)+'.txt','a+')
	file1.write("\n")
	file1.write(Dt)
	file1.close()
	tkinter.messagebox.showinfo( "Success", 'Successfully Entered Data!')
	global current_frame	
	current_frame.pack_forget()
	patientInfo_frame.pack()
	current_frame = patientInfo_frame


def create_signUp_frame():
	global K1
	global K2
	print('In signup Frame')
	L1=tk.Label(signUp_frame, bg="white",text='Enter User ID:')
	L1['font']=myFont
	L1.grid(row=0, column=0, padx=0, pady=10)
	T1=tk.Entry(signUp_frame,textvariable = K1)
	T1['font']=myFont
	T1.grid(row=0, column=1, padx=0, pady=10)
	L2=tk.Label(signUp_frame, bg="white",text='Enter Password:')
	L2['font']=myFont
	L2.grid(row=1, column=0, padx=0, pady=10)
	T2=tk.Entry(signUp_frame, textvariable = K2, show='*')
	T2['font']=myFont
	T2.grid(row=1, column=1, padx=0, pady=10)
	B1=tk.Button(signUp_frame, text="Signup", command=lambda:signup())
	B1['font']=myFont
	B1.grid(row=2, column=0, padx=10, pady=10)
	B2=tk.Button(signUp_frame, text="Exit", command=closer)
	B2['font']=myFont
	B2.grid(row=2, column=1, padx=10, pady=10)
	global current_frame
	current_frame.pack_forget()
	signUp_frame.pack()
	current_frame = signUp_frame


def create_loginFrame():
	global E1
	global E2
	#########DOCTOR
	L1=tk.Label(loginFrame, bg="white",text='Enter User ID:')
	L1['font']=myFont
	L1.grid(row=0, column=0, padx=0, pady=10)
	T1=tk.Entry(loginFrame,textvariable = E1)
	T1['font']=myFont
	T1.grid(row=0, column=1, padx=0, pady=10)
	L2=tk.Label(loginFrame, bg="white",text='Enter Password:')
	L2['font']=myFont
	L2.grid(row=1, column=0, padx=10, pady=10)
	T2=tk.Entry(loginFrame, textvariable = E2, show='*')
	T2['font']=myFont
	T2.grid(row=1, column=1, padx=0, pady=10)
	B1=tk.Button(loginFrame, text="Login", command=lambda:log_in())
	B1['font']=myFont
	B1.grid(row=2, column=0, padx=10, pady=10)
	B11 = tk.Button(loginFrame, bg="white", text="Back", command=lambda: backTo_mainFrame())
	B11['font'] = myFont
	B11.grid(row=3, column=0, padx=10, pady=10)
	B3=tk.Button(loginFrame, text="SignUp", command=lambda:create_signUp_frame())
	B3['font']=myFont
	B3.grid(row=2, column=1, padx=10, pady=10)
	B2=tk.Button(loginFrame, text="Exit", command=closer)
	B2['font']=myFont
	B2.grid(row=3, column=1, padx=10, pady=10)
	global current_frame
	current_frame.pack_forget()
	loginFrame.pack()
	current_frame = loginFrame

def create_loginFrame_patient():
	global E1
	global E2
	L1=tk.Label(loginFrameRO, bg="white",text='Enter User ID:')
	L1['font']=myFont
	L1.grid(row=0, column=0, padx=0, pady=10)
	T1=tk.Entry(loginFrameRO,textvariable = E1)
	T1['font']=myFont
	T1.grid(row=0, column=1, padx=0, pady=10)
	L2=tk.Label(loginFrameRO, bg="white",text='Enter Password:')
	L2['font']=myFont
	L2.grid(row=1, column=0, padx=10, pady=10)

	T2=tk.Entry(loginFrameRO, textvariable = E2, show='*')
	T2['font']=myFont
	T2.grid(row=1, column=1, padx=0, pady=10)
	B1=tk.Button(loginFrameRO, text="Login", command=lambda:log_in_patient())
	B1['font']=myFont
	B1.grid(row=2, column=0, padx=10, pady=10)
	B11 = tk.Button(loginFrameRO, bg="white", text="Back", command=lambda: backTo_mainFrame())
	B11['font'] = myFont
	B11.grid(row=3, column=0, padx=10, pady=10)
	B2=tk.Button(loginFrameRO, text="Exit", command=closer)
	B2['font']=myFont
	B2.grid(row=2, column=1, padx=10, pady=10)
	global current_frame
	current_frame.pack_forget()
	loginFrameRO.pack()
	current_frame = loginFrameRO

def create_patientInfo_frame():
	global current_frame
	global E3
	print('In create Patient Into Frame')
	print('PiD:',PiD)
	L1=tk.Label(patientInfo_frame, bg="white",text='Enter Patient ID:')
	L1['font']=myFont
	L1.grid(row=0, column=0, padx=0, pady=10)
	T1=tk.Entry(patientInfo_frame,  bg="white",  textvariable = E3)
	T1['font']=myFont
	T1.grid(row=0, column=1, padx=10, pady=10)
	B1=tk.Button(patientInfo_frame,  bg="white", text="Get Details", command=lambda:patientInfo())
	B1['font']=myFont
	B1.grid(row=2, column=1, padx=10, pady=10)
	B2=tk.Button(patientInfo_frame,  bg="white", text="Add New Patient Details", command=lambda:addPatientFrame())
	B2['font']=myFont
	B2.grid(row=4, column=0, padx=10, pady=10)
	B3=tk.Button(patientInfo_frame,  bg="white", text="Exit", command=closer)
	B3['font']=myFont
	B3.grid(row=4, column=1, padx=10, pady=10)
	current_frame.pack_forget()
	patientInfo_frame.pack()
	current_frame = patientInfo_frame

def create_patientInfoRO_frame():
	global current_frame
	global E3
	print('In create_patientInfoRO_frame')
	L1=tk.Label(patientInfoRO_frame, bg="white",text='Enter Patient ID:')
	L1['font']=myFont
	L1.grid(row=0, column=0, padx=0, pady=10)
	T1=tk.Entry(patientInfoRO_frame,  bg="white", textvariable = E3)
	T1['font']=myFont
	T1.grid(row=0, column=1, padx=10, pady=10)
	B1=tk.Button(patientInfoRO_frame,  bg="white", text="Get Details", command=lambda:patientInfoRO())
	B1['font']=myFont
	B1.grid(row=2, column=1, padx=10, pady=10)
	B3=tk.Button(patientInfoRO_frame,  bg="white", text="Exit", command=closer)
	B3['font']=myFont
	B3.grid(row=4, column=1, padx=10, pady=10)
	current_frame.pack_forget()
	patientInfoRO_frame.pack()
	current_frame = patientInfoRO_frame

def backTo_patientInfoRO_frame():
	global current_frame
	global flag
	global L11
	if flag=='1':
		L11.config(text=" ")
		flag='0'
	global current_frame	
	current_frame.pack_forget()
	patientInfoRO_frame.pack()
	current_frame = patientInfoRO_frame

def backTo_patientInfo_frame():
	global current_frame
	global L11
	global flag
	if flag=='1':
		L11.config(text=" ")
		flag='0'

	current_frame.pack_forget()
	patientInfo_frame.pack()
	current_frame = patientInfo_frame

def backTo_mainFrame():
	global current_frame
	global L11
	global flag
	if flag=='1':
		L11.config(text=" ")
		flag='0'

	current_frame.pack_forget()
	create_mainFrame.pack()
	current_frame = create_mainFrame

def create_displayFrame(data):
	print('In display Frame',data)
	global flag
	flag='1'
	L11=tk.Label(displayFrame, bg="white",text=str(data))
	L11['font']=myFont
	L11.grid(row=0, column=0, padx=0, pady=10)
	B8=tk.Button(displayFrame,  bg="white", text="Back", command=lambda:backTo_patientInfoRO_frame())
	B8['font']=myFont
	B8.grid(row=1, column=0, padx=10, pady=10)
	B3=tk.Button(displayFrame,  bg="white", text="Exit", command=closer)
	B3['font']=myFont
	B3.grid(row=1, column=1, padx=10, pady=10)
	global current_frame
	current_frame.pack_forget()
	displayFrame.pack()
	current_frame = displayFrame

def create_displayFrameDoctor(data):
	print('In Doctor display Frame',data)
	global L11
	global flag
	flag='1'
	L11=tk.Label(displayFrameDoctor, bg="white",text=str(data))
	L11['font']=myFont
	L11.grid(row=0, column=0, padx=0, pady=10)
	B11=tk.Button(displayFrameDoctor,  bg="white", text="Back", command=lambda:backTo_patientInfo_frame())
	B11['font']=myFont
	B11.grid(row=2, column=0, padx=10, pady=10)
	B9=tk.Button(displayFrameDoctor,  bg="white", text="Edit", command=lambda:PatientDataEdit(data))
	B9['font']=myFont
	B9.grid(row=2, column=1, padx=10, pady=10)
	#B10=tk.Button(displayFrameDoctor,  bg="white", text="save", command=lambda:patientDataUpdate())
	#B10['font']=myFont
	#B10.grid(row=3, column=0, padx=10, pady=10)
	B12=tk.Button(displayFrameDoctor,  bg="white", text="Exit", command=closer)
	B12['font']=myFont
	B12.grid(row=3, column=1, padx=10, pady=10)
	global current_frame
	current_frame.pack_forget()
	displayFrameDoctor.pack()
	current_frame = displayFrameDoctor	

def create_EditdisplayFrameDoctor(data):
	global flag
	global L11
	flag='0'
	print('In Edit Doctor display Frame',data)
	L11=tk.Text(editdisplayFrameDoctor, bg="white", height=10, width=30)
	L11['font']=myFont
	L11.grid(row=0, column=0, padx=10, pady=10)
	L11.insert("1.0", data)
	B11=tk.Button(editdisplayFrameDoctor,  bg="white", text="Back", command=lambda:backTo_patientInfo_frame())
	B11['font']=myFont
	B11.grid(row=2, column=0, padx=10, pady=10)
	B10=tk.Button(editdisplayFrameDoctor,  bg="white", text="save", command=lambda:patientDataUpdate())
	B10['font']=myFont
	B10.grid(row=3, column=0, padx=10, pady=10)
	B12=tk.Button(editdisplayFrameDoctor,  bg="white", text="Exit", command=closer)
	B12['font']=myFont
	B12.grid(row=2, column=1, padx=10, pady=10)
	global current_frame
	current_frame.pack_forget()
	editdisplayFrameDoctor.pack()
	current_frame = editdisplayFrameDoctor


def closer():
	exit()

def create_mainFrame():
	global current_frame
	T1=tk.Label(top, bg="pink",fg="Green",text='Health Card')
	T1['font']=myFont1
	T1.pack(padx=5, pady=15)
	bt1=tk.Button(top, text="Login (Doctor)", bg="white", command=lambda:create_loginFrame())
	bt1['font']=myFont
	bt1.pack(padx=5, pady=15)#,anchor = 'center')
	bt4=tk.Button(top, text="Login (Patient)", bg="white", command=lambda:create_loginFrame_patient())
	bt4['font']=myFont
	bt4.pack(padx=5, pady=15)#,anchor = 'center')
	bt3=tk.Button(top, text="Exit",  bg="white",command=closer)
	bt3['font']=myFont
	bt3.pack(padx=5, pady=15)#,anchor = 'center')
	T2=tk.Label(top, bg="pink",text='Project By: ')
	T2['font']=myFont
	T2.pack(padx=5, pady=15)
	T3=tk.Label(top, bg="pink",text='Mihir Ghatage, Anish Sangavkar, Aarya Gabale,')
	T3['font']=myFont
	T3.pack(padx=5, pady=15)
	T4=tk.Label(top, bg="pink",text=' Naveli Nikam, Atharvraj Shivudkar')
	T4['font']=myFont
	T4.pack(padx=5, pady=15)
	top.pack()

root = tk.Tk()
w = 700 # width for the Tk root
h = 500 # height for the Tk root
# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
#root.geometry("100x200")
myFont = font.Font(size=16)
myFont1 = font.Font(size=20)

top = tk.Frame(root, width=10,height=10, bg='pink')
loginFrame = tk.Frame(root, width=10,height=10,bg='pink')
loginFrameRO = tk.Frame(root, width=10,height=10,bg='pink')
signUp_frame = tk.Frame(root, width=10,height=10,bg='pink')
patientInfo_frame=tk.Frame(root, width=30,height=30,bg='pink')
addpatientInfo_frame=tk.Frame(root, width=30,height=30,bg='pink')
patientInfoRO_frame=tk.Frame(root, width=30,height=30,bg='pink')
displayFrame=tk.Frame(root, width=30,height=30,bg='pink')
displayFrameDoctor=tk.Frame(root, width=30,height=30,bg='pink')
editdisplayFrameDoctor=tk.Frame(root, width=30,height=30,bg='pink')
# set weights to the frame so when you resize the window the frame size changes
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.configure(bg='pink')
usr=StringVar()
E1=StringVar()
E2=StringVar()
E3=StringVar()
E4=StringVar()
E5=StringVar()
E6=StringVar()
E7=StringVar()
DT11=StringVar()
L11=StringVar()
flag=StringVar()
PiD=StringVar()
K1=StringVar()
K2=StringVar()
Cleaner=StringVar()

L11=''

current_frame = top
create_mainFrame()


root.mainloop()

