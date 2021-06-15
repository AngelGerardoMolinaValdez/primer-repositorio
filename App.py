import os as cmd

class Action:

	def __init__(self):
		print("\nSaludos cordiales. \n\nSelecciona el formato de tiempo en el que deseas introducir el tiempo de espera para apagar tu maquina:")
		print("\n\n\t\t\t1.-Horas.")
		print("\n\n\t\t\t2.-Minutos.")
		print("\n\n\t\t\t3.-Segundos.")
		print("\n\n\t\t\t0.-Salir del sistema.")

	def EscogeTipoTiempo(self):
		self.intTipoTiempo = input("\n..:: Selecciona el formato --> ")

		if self.intTipoTiempo.isnumeric():

			self.intTipoTiempo = int(self.intTipoTiempo)
			
			if self.intTipoTiempo >= 0 and self.intTipoTiempo <= 3:
				
				if self.intTipoTiempo == 0:
					return "Salir"
				else:
					return True
			else:
				return False
		else:
			return False
		

	def AsignaTiempo(self):
		intTiempoTotal = 0
		strParametrosTurnOff = "shutdown -s -t "

		#horas
		if self.intTipoTiempo == 1:
			intHorasEnSegundos = 3600
			print("\n\n\t\t\tFormato seleccionado --> ...::: H o r a s :::... <--")
		#minutos
		if self.intTipoTiempo == 2:
			intMinutosEnSegundos = 60
			print("\n\n\t\t\tFormato seleccionado --> ...::: M i n u t o s :::... <--")

		if self.intTipoTiempo == 3:
			print("\n\n\t\t\tFormato seleccionado --> ...::: S e g u n d o s :::... <--")


		self.intTiempo = input("\n..:: ¿En cuanto tiempo se apagara la maquina? --> ")

		if self.intTiempo.isnumeric():

			self.intTiempo = int(self.intTiempo)

			if self.intTipoTiempo == 1:
				intTiempoTotal = self.intTiempo * intHorasEnSegundos
				strScriptTurnOff = strParametrosTurnOff + str(intTiempoTotal)

			if self.intTipoTiempo == 2:
				intTiempoTotal = self.intTiempo * intMinutosEnSegundos
				strScriptTurnOff = strParametrosTurnOff + str(intTiempoTotal)

			if self.intTipoTiempo == 3:
				intTiempoTotal = self.intTiempo
				strScriptTurnOff = strParametrosTurnOff + str(intTiempoTotal)

			cmd.system(strParametrosTurnOff)
			return True














'''
#validar despues we gogog 
import time

listValuesAscii = []
for i in "B i e n v e n i d o":
	listValuesAscii.append(ord(i))



for i in listValuesAscii:
	time.sleep(1)
	print(chr(i), end="")

'''








"""
print("Apagado automatizado con Python!!\n\n Por: Angel\n")

intSegundos = int(input("Digita el tiempo en segundos para apagar tu computadora -->"))


strApagadoAutomatico = "shutdown -s -t {}".format(intSegundos)

os.system(strApagadoAutomatico)
"""