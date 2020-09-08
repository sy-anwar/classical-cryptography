from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk

class Gui:
	def __init__(self):
		self.window = Tk()
		self.window.title("Tugas Kecil 1 IF4020 13517139 13517140")
		self.window.geometry('540x540')

		self.label_plaintext = Label(self.window, text="Plaintext")
		self.label_plaintext.grid(column=0, row=0, sticky=W, padx=10)

		self.plaintext = scrolledtext.ScrolledText(self.window, width=65, height=10)
		self.plaintext.grid(column=0, row=1, columnspan=3, padx=5)

		self.btn_openfile_plaintext = Button(self.window, text="Open File Plaintext")
		self.btn_openfile_plaintext.grid(column=2, row=0, sticky=E, pady=5, padx=20)

		self.algorithms = ['Vigenere Cipher', 'Full Vigenere Cipher', 'Auto-key Vigenere Cipher',
						'Extended Vigenere Cipher', 'Playfair Cipher', 'Super Encription', 
						'Affine Cipher', 'Hill Cipher']

		self.label_choose_algorithm = Label(self.window, text='Algorithm :')
		self.label_choose_algorithm.grid(column=0, row=3, pady=10, padx=10, sticky=SW)

		self.combobox_algorithms = ttk.Combobox(self.window, values=self.algorithms, width=30)
		self.combobox_algorithms.grid(column=1, row=3, pady=10, sticky=SW)
		self.combobox_algorithms.current(0)
		self.combobox_algorithms.bind('<<ComboboxSelected>>', self.handler)

		self.label_key = Label(self.window, text='Key :')
		self.label_key.grid(column=0, row=4, sticky=W, padx=10)

		self.key = Entry(self.window, width=40)
		self.key.grid(column=1, row=4, sticky=W)

		self.label_n_transpotition = Label(self.window, text='n_transpotition :')
		self.n_transpotition = Entry(self.window, width=40)

		self.label_m = Label(self.window, text='m :')
		self.m = Entry(self.window, width=40)

		self.label_b = Label(self.window, text='b :')
		self.b = Entry(self.window, width=40)
		
		self.label_spaces = Label(self.window, text='Spaces :')
		self.label_spaces.grid(column=0, row=5, sticky=W, padx=10)

		self.spaces = Entry(self.window, width=40)
		self.spaces.grid(column=1, row=5, sticky=W)

		self.btn_encrypt = Button(self.window, text="Encrypt", width=15)
		self.btn_encrypt.grid(column=2, row=3, sticky='E', padx=20)

		self.btn_decrypt = Button(self.window, text="Decrypt", width=15)
		self.btn_decrypt.grid(column=2, row=4, sticky='E', padx=20)

		self.label_chipertext = Label(self.window, text="Chipertext")
		self.label_chipertext.grid(column=0, row=7, sticky=W, padx=10, pady=(20, 5))

		self.chipertext = scrolledtext.ScrolledText(self.window, width=65, height=10)
		self.chipertext.grid(column=0, row=8, columnspan=3, padx=5)

		self.btn_openfile_chipertext = Button(self.window, text="Open File Chipertext")
		self.btn_openfile_chipertext.grid(column=2, row=7, sticky=E, pady=(20, 5), padx=20)
	
	def handler(self, event):
		current = self.combobox_algorithms.current()
		if current == 0 : # Vigenere
			self.label_key.grid(column=0, row=4, sticky=W, padx=10)
			self.key.grid(column=1, row=4, sticky=W)
			
			self.label_spaces.grid(column=0, row=5, sticky=W, padx=10)
			self.spaces.grid(column=1, row=5, sticky=W)

			self.label_n_transpotition.grid_remove()
			self.n_transpotition.grid_remove()

			self.label_m.grid_remove()
			self.m.grid_remove()

			self.label_b.grid_remove()
			self.b.grid_remove()
		elif current == 1 : # Full Vigenere
			self.label_key.grid(column=0, row=4, sticky=W, padx=10)
			self.key.grid(column=1, row=4, sticky=W)

			self.label_spaces.grid(column=0, row=5, sticky=W, padx=10)
			self.spaces.grid(column=1, row=5, sticky=W)

			self.label_n_transpotition.grid_remove()
			self.n_transpotition.grid_remove()

			self.label_m.grid_remove()
			self.m.grid_remove()

			self.label_b.grid_remove()
			self.b.grid_remove()
		elif current == 2 : # Auto-key Vigenere
			self.label_key.grid(column=0, row=4, sticky=W, padx=10)
			self.key.grid(column=1, row=4, sticky=W)

			self.label_spaces.grid(column=0, row=5, sticky=W, padx=10)
			self.spaces.grid(column=1, row=5, sticky=W)

			self.label_n_transpotition.grid_remove()
			self.n_transpotition.grid_remove()

			self.label_m.grid_remove()
			self.m.grid_remove()

			self.label_b.grid_remove()
			self.b.grid_remove()
		elif current == 3 : # Extended Vigenere
			self.label_key.grid(column=0, row=4, sticky=W, padx=10)
			self.key.grid(column=1, row=4, sticky=W)

			self.label_spaces.grid(column=0, row=5, sticky=W, padx=10)
			self.spaces.grid(column=1, row=5, sticky=W)

			self.label_n_transpotition.grid_remove()
			self.n_transpotition.grid_remove()

			self.label_m.grid_remove()
			self.m.grid_remove()

			self.label_b.grid_remove()
			self.b.grid_remove()
		elif current == 4 : # Playfair
			self.label_key.grid(column=0, row=4, sticky=W, padx=10)
			self.key.grid(column=1, row=4, sticky=W)

			self.label_spaces.grid(column=0, row=5, sticky=W, padx=10)
			self.spaces.grid(column=1, row=5, sticky=W)

			self.label_n_transpotition.grid_remove()
			self.n_transpotition.grid_remove()

			self.label_m.grid_remove()
			self.m.grid_remove()

			self.label_b.grid_remove()
			self.b.grid_remove()
		elif current == 5 : # Super Encription
			self.label_key.grid(column=0, row=4, sticky=W, padx=10)
			self.key.grid(column=1, row=4, sticky=W)

			self.label_n_transpotition.grid(column=0, row=5, sticky=W, padx=10)
			self.n_transpotition.grid(column=1, row=5, sticky=W)

			self.label_spaces.grid(column=0, row=6, sticky=W, padx=10)
			self.spaces.grid(column=1, row=6, sticky=W)

			self.label_m.grid_remove()
			self.m.grid_remove()

			self.label_b.grid_remove()
			self.b.grid_remove()
		elif current == 6 : # Affine
			self.label_m.grid(column=0, row=4, sticky=W, padx=10)
			self.m.grid(column=1, row=4, sticky=W)

			self.label_b.grid(column=0, row=5, sticky=W, padx=10)
			self.b.grid(column=1, row=5, sticky=W)

			self.label_spaces.grid(column=0, row=6, sticky=W, padx=10)
			self.spaces.grid(column=1, row=6, sticky=W)

			self.label_key.grid_remove()
			self.key.grid_remove()

			self.label_n_transpotition.grid_remove()
			self.n_transpotition.grid_remove()
		elif current == 7 : # Hill
			self.label_key.grid(column=0, row=4, sticky=W, padx=10)
			self.key.grid(column=1, row=4, sticky=W)

			self.label_spaces.grid(column=0, row=5, sticky=W, padx=10)
			self.spaces.grid(column=1, row=5, sticky=W)

			self.label_n_transpotition.grid_remove()
			self.n_transpotition.grid_remove()

			self.label_m.grid_remove()
			self.m.grid_remove()

			self.label_b.grid_remove()
			self.b.grid_remove()

gui = Gui()
gui.window.mainloop()
