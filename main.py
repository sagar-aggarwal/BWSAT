#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 00:30:18 2019

@author: sagara.co@nsit.net.in, rajat.usict.101164@ipu.ac.in
"""

import Tkinter as tk
import random
import pickle
import os
import pandas as pd
import tkMessageBox as messagebox

username = "xxx"
userpart = 1
idx = 0
lines = 0
flag = 0
idxfileloc = '0'
max_entries = 0
unprocessed_idxs = 0
bucket = ""
unprocessed_idx = 0
randarr = 0

# get default path
path = os.path.dirname(os.path.abspath(__file__))
fileHandle = open(path + '/test.txt', 'w')

# get dictionary from pickle file
pickle_file = open(path + '/data/dict.pickle','rb')
word_dict = pickle.load(pickle_file)

# windpw close message  
def on_closing():
	if messagebox.askokcancel("Quit", "Do you want to quit?"):
		fileHandle.close()
		openfile = open(idxfileloc,'w')
		openfile.write(str(max(idx,0)))

		dbfile = open(path + '/files/' + username + 'unprocessed.pickle','w+')
		pickle.dump(unprocessed_idxs, dbfile)
		dbfile.close()

		main_window.destroy()

def on_complete():
	if messagebox.askokcancel("Annotations complete", "Annotations complete, Do you want to quit?"):
		fileHandle.close()
		openfile = open(idxfileloc,'w')
		openfile.write(str(max(idx,0)))
		main_window.destroy()

def fill_all():
	messagebox.showinfo("Choose right", "You can't choose none of these, choose viable option.")
	return
		
  
def meaningPressCallBack(wordMeaning):
	r = tk.Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(wordMeaning.split('-')[0])
	r.update() # now it stays on the clipboard after the window is closed


def update():
	global idx
	global lines
	global max_entries
	global bucket
	global unprocessed_idxs
	global unprocessed_idx
	global randarr


	if (idx>=max_entries-1 and len(unprocessed_idxs)==0 and var1.get()!=5 and var2.get()!=5):
		fileHandle.write(str(idx) + ',' + str(randarr[var1.get()-1]) + ',' + str(randarr[var2.get()-1]) + '\n')
		on_complete()
		return 
	
	if(flag==1):
		# add in list
		if (var1.get()==5 or var2.get()==5):

			if (bucket=="unprocessed"):
				# show pop-up
				fill_all()
				return
				
			else:
				unprocessed_idxs.append(idx)
				fileHandle.write(str(idx) + ',' + str(randarr[var1.get()-1]) + ',' + str(randarr[var2.get()-1]) + '\n')

		elif (bucket=='unprocessed'):
			fileHandle.write(str(idx) + ',' + str(randarr[var1.get()-1]) + ',' + str(randarr[var2.get()-1]) + '\n')
			unprocessed_idxs.remove(unprocessed_idx)


		else:
			fileHandle.write(str(idx) + ',' + str(randarr[var1.get()-1]) + ',' + str(randarr[var2.get()-1]) + '\n')		

		# choose index
		unprocessed_size = len(unprocessed_idxs)
		remanining_size = max_entries-1-idx
		if (remanining_size+unprocessed_size==0):
			on_complete()
		random_idx = random.randint(1,remanining_size+unprocessed_size)

		if random_idx > remanining_size:
			bucket = 'unprocessed'
			unprocessed_idx = unprocessed_idxs[random_idx - remanining_size - 1]
		else:
			bucket = 'remanining'
			idx+=1

	word = [0 for x in range(4)]

	if (bucket == 'unprocessed'):
		word[0] = lines.iloc[unprocessed_idx][0]
		word[1] = lines.iloc[unprocessed_idx][1]
		word[2] = lines.iloc[unprocessed_idx][2]
		word[3] = lines.iloc[unprocessed_idx][3]

	else :
		word[0] = lines.iloc[idx][0]
		word[1] = lines.iloc[idx][1]
		word[2] = lines.iloc[idx][2]
		word[3] = lines.iloc[idx][3]

	randarr = random.sample(range(0,4),4)

	sep = '#'
	show1 = word[randarr[0]].split(sep, 1)[0]
	show2 = word[randarr[1]].split(sep, 1)[0]
	show3 = word[randarr[2]].split(sep, 1)[0]
	show4 = word[randarr[3]].split(sep, 1)[0]

	mng1 = word_dict[word[randarr[0]]]
	mng2 = word_dict[word[randarr[1]]]
	mng3 = word_dict[word[randarr[2]]]
	mng4 = word_dict[word[randarr[3]]]


	w11.config(text=show1)
	w12.config(text=show2)
	w13.config(text=show3)
	w14.config(text=show4)
	
	w21.config(text=show1)
	w22.config(text=show2)
	w23.config(text=show3)
	w24.config(text=show4)
	
	w15.config(text='none of the above')
	w25.config(text='none of the above')
	
	meaning1.config(text = show1 + '- ' + mng1)
	meaning2.config(text = show2 + '- ' + mng2)
	meaning3.config(text = show3 + '- ' + mng3)
	meaning4.config(text = show4 + '- ' + mng4)


def raise_frame(frame):

	global username
	global userpart
	global idx
	global lines
	global fileHandle
	global flag
	global idxfileloc 
	global max_entries
	global unprocessed_idxs
	
	# get username and lowercase it and remove leading spaces
	username = Name.get().lower().lstrip()
	
	# get selected part 
	userpart = var_.get()
	lines = pd.read_csv(path + '/data/' + 'part' + str(userpart) + '.csv', 'r', encoding = 'utf-8-sig', header = None, delimiter = '\t')
	statements = lines[1:]
	max_entries = lines.shape[0]

	fileloc = path + '/files/' + username + '.txt'
	
	if (os.path.exists(fileloc) == False):
		fileHandle = open(fileloc, 'w')
		fileHandle.close()
		fileHandle = open(fileloc, 'a')
	else :
		fileHandle = open(fileloc, 'a')
	
	
	# get idx from idx file
	idxfileloc = path + '/files/' + username + 'idx.txt'
	
	if (os.path.exists(idxfileloc)):
		idxfile = open(idxfileloc)
		idxline = idxfile.readlines()
		idxfile.close()
		idx  = int(idxline[0])
	else :
		idxfile = open(idxfileloc, 'w')
		idxfile.close()
		idx = 0
	
	# get unprocessed indexes data from pickle file if present

	unprocessed_idx_file = path + '/files/' + username + 'unprocessed.pickle'

	if (os.path.exists(unprocessed_idx_file)):
		unprocessed_idx_file_pickle = open(unprocessed_idx_file,'rb')
		unprocessed_idxs =   pickle.load(unprocessed_idx_file_pickle)
	else :
		unprocessed_idx_file_pickle = open(unprocessed_idx_file,"wb")
		unprocessed_idxs = []



	update()
	flag = 1

	register_frame.destroy()
	main_frame.pack()
	frame.tkraise()
	


# main window
main_window = tk.Tk()
main_window.geometry('1080x920')

# frames
register_frame = tk.Frame(main_window)
main_frame = tk.Frame(main_window)
register_frame.pack()
	
# place label
info = tk.Label(register_frame, font=("Courier", 15), text = 'Write your name, \n choose your section and then press OK')
info.grid(row = 0, column = 0)
info.grid_propagate(0)

# place name
var = tk.StringVar()
Name = tk.Entry(register_frame, textvariable = var, width=20)
Name.grid(row = 0, column = 1)

# choose option
var_ = tk.IntVar()
op1 = tk.Radiobutton(register_frame, text='Part 1', bg = 'ivory2', value = 1, variable = var_).grid(row = 1, column = 2)
op2 = tk.Radiobutton(register_frame, text='Part 2', bg = 'ivory2', value = 2, variable = var_).grid(row = 1, column = 3)
op3 = tk.Radiobutton(register_frame, text='Part 3', bg = 'ivory2', value = 3, variable = var_).grid(row = 1, column = 4)
op4 = tk.Radiobutton(register_frame, text='Part 4', bg = 'ivory2', value = 4, variable = var_).grid(row = 1, column = 5)
op5 = tk.Radiobutton(register_frame, text='Test Part', bg = 'ivory2', value = 5, variable = var_).grid(row = 1, column = 6)

#choose OK
button = tk.Button(register_frame, height = 2, width = 4, text = 'OK', command = lambda: raise_frame(main_frame)).grid(row=4, column=1)


# frames
frm0 = tk.Frame(main_frame, width = 480, height = 100, bd=0, bg='white')
frm0.grid(row = 0, column = 0, padx=(0,4), pady=(32,0))

frm01 = tk.Frame(main_frame, width = 480, height = 100, bd=0, bg='white')
frm01.grid(row = 0, column = 1, padx=(0,4), pady=(32,0))

frm1 = tk.Frame(main_frame, width =480, height= 180, bd=10, bg='ivory2')
frm1.grid(row = 1, column = 0, padx=(0,4), pady=(32,0))
frm1.grid_propagate(0)

frm2 = tk.Frame(main_frame, width =480, height= 180, bd=10, bg='ivory2')
frm2.grid(row = 1, column = 1,padx=(4,0), pady=(32,0))
frm2.grid_propagate(0)

frm7 = tk.Frame(main_frame, width =480, height= 180, bd=10, bg='ivory2')
frm7.grid(row = 2, column = 0, pady = (32,0))
frm7.grid_propagate(0)

frm8 = tk.Frame(main_frame, width =480, height= 180, bd=10, bg='white')
frm8.grid(row = 2, column = 1, pady=(32,0))
frm8.grid_propagate(0)

# define labels
label0 = tk.Label(frm0, font=("Helvetica", 34), text = 'Please read the meanings first,')
label0.place(x=10,y=10)

label01 = tk.Label(frm01, font=("Helvetica", 34), text = 'then choose.')
label01.place(x=10,y=10)

label1 = tk.Label(frm1, font=("Courier", 16), text = 'Choose the most positive')
label1.place(x=60,y=120)

label2 = tk.Label(frm2, font=("Courier", 16), text = 'Choose the least positive')
label2.place(x=60,y=120)

meaning1 = tk.Button(frm7,font=("Courier", 14), text = 'meaningoftest1',wraplength=450, justify=tk.LEFT,
	command=lambda: meaningPressCallBack(meaning1['text']))
meaning1.pack(anchor = tk.W)

meaning2 = tk.Button(frm7,font=("Courier", 14), text = 'meaningoftest2',wraplength=450, justify=tk.LEFT,
	command=lambda: meaningPressCallBack(meaning2['text']))
meaning2.pack(anchor = tk.W)

meaning3 = tk.Button(frm7,font=("Courier", 14), text = 'meaningoftest3',wraplength=450, justify=tk.LEFT,
	command=lambda: meaningPressCallBack(meaning3['text']))
meaning3.pack(anchor = tk.W)

meaning4 = tk.Button(frm7,font=("Courier", 14), text = 'meaningoftest4',wraplength=450, justify=tk.LEFT,
	command=lambda: meaningPressCallBack(meaning4['text']))
meaning4.pack(anchor = tk.W)

# set varibles
var1 = tk.IntVar()
var2 = tk.IntVar()

# first radio button
w11 = tk.Radiobutton(frm1, text='test1', font=("Courier", 14), bg = 'ivory2', padx = 20, pady = 5, value = 1, variable = var1)
w11.grid(row = 0, column = 0)
w12 = tk.Radiobutton(frm1, text='test2', font=("Courier", 14), bg = 'ivory2', padx = 20, pady = 5, value = 2, variable = var1)
w12.grid(row = 0, column = 1)
w13 = tk.Radiobutton(frm1, text='test3', font=("Courier", 14), bg = 'ivory2', padx = 20, pady = 5, value = 3, variable = var1)
w13.grid(row = 1, column = 0)
w14 = tk.Radiobutton(frm1, text='test4', font=("Courier", 14), bg = 'ivory2', padx = 20, pady = 5, value = 4, variable = var1)
w14.grid(row = 1, column = 1)
w15 = tk.Radiobutton(frm1, text='test5', font=("Courier", 14), bg = 'ivory2', padx = 20, pady = 5, value = 5, variable = var1)
w15.grid(row = 2, column = 0)

w21 = tk.Radiobutton(frm2, text='test1', font=("Courier", 14), bg = 'ivory2', padx = 20, pady = 5, value = 1, variable = var2)
w21.grid(row = 0, column = 0)
w22 = tk.Radiobutton(frm2, text='test2', font=("Courier", 14), bg = 'ivory2', padx = 20, pady = 5, value = 2, variable = var2)
w22.grid(row = 0, column = 1)
w23 = tk.Radiobutton(frm2, text='test3', font=("Courier", 14), bg = 'ivory2', padx = 20, pady = 5, value = 3, variable = var2)
w23.grid(row = 1, column = 0)
w24 = tk.Radiobutton(frm2, text='test4', font=("Courier", 14), bg = 'ivory2', padx = 20, pady = 5, value = 4, variable = var2)
w24.grid(row = 1, column = 1)
w25 = tk.Radiobutton(frm2, text='test5', font=("Courier", 14), bg = 'ivory2', padx = 20, pady = 5, value = 5, variable = var2)
w25.grid(row = 2, column = 0)

# next and exit buttons
button = tk.Button(frm8, height = 2, width = 4, text = 'NEXT', padx=10, pady=10, command = update).pack(side = tk.LEFT)
button = tk.Button(frm8, height = 2, width = 4, text = 'EXIT', padx=10, pady=10, command = on_closing).pack(side = tk.LEFT)


main_window.protocol("WM_DELETE_WINDOW", on_closing)
main_window.resizable(width =  True, height = True)
main_window.mainloop()
	

