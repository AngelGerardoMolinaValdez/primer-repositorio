#encriptador --> pip install cryptography
#from cryptography.fernet import Fernet

import time 

class LoginApp:

	
	def __init__(self):

		self.users = {"angel1012":"pobre$$a"}
		self.strUser = input("\n....:::: D i g i t a   t u   u s u a r i o ----> ")
		self.strPassword =  input("\n....:::: D i g i t a   t u   c o n t r a s e ñ a ----> ")


	def ValidaCredenciales(self):
	
		for clave, valor in self.users.items():
			
			if clave == self.strUser and valor == self.strPassword: 
				return True
			else: 
				return False


	def Bienvenida(self):
		print(f"\n\n\n\t\t\t\t--------> B i e n v e n i d o   {self.strUser} <--------")








