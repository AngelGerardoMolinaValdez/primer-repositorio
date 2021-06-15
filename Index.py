from Login import LoginApp
from App import Action
import os as cmd
import time as wait

strWelcomeMessage = """
			                          _________
			                     ___________________
			               ________________________________
				    _______________________________________
				   *                                      *
				   *     T u r n    O f f   M y   P C     *	
				   *______________________________________*
			               ________________________________
			                      ___________________
			                           _________
	"""
intAttempsLogin = 0


while True:

	intAttempsLogin += 1

	if intAttempsLogin <= 3:
		
		cmd.system("cls")
		print(strWelcomeMessage)

		LogIn = LoginApp()

		boolCredencialesOk = LogIn.ValidaCredenciales()

		if boolCredencialesOk:
			cmd.system("cls")
			print(strWelcomeMessage)
			LogIn.Bienvenida()
			break

	else:
		cmd.system("cls")
		print(strWelcomeMessage)
		print("\n\n\n\t\t\tSolo el titular de esta maquina puede acceder a la funcion de este script. \n\n\t\t\tSolicite los permisos correspondientes con el administrador de este sistema. \n\n\t\t\tGracias.")
		break



intAttempsAction = 0

while True:

	intAttempsAction += 1

	if intAttempsAction <= 5:

		cmd.system("cls")
		print(strWelcomeMessage)
		main = Action()
		boolOpcionOk = main.EscogeTipoTiempo()

		if boolOpcionOk:
			if boolOpcionOk == "Salir":
				cmd.system("cls")
				print(strWelcomeMessage)
				print("\n\n\n\t\tSe ha solicitado la finalizacion del sistema. \n\n\t\tGracias.")
			break

	else:
		cmd.system("cls")
		print(strWelcomeMessage)
		print("\n\n\n\t\tEl sistema solo soporta 4 posibles opciones. \n\n\t\tSi lo desea, ejecute de nuevo el script e ingrese cualquiera de las opciones mostradas en el menu. \n\n\t\tGracias.")
		break



intAttempsTimeOff = 0

while True:

	intAttempsTimeOff += 1

	cmd.system("cls")
	if intAttempsTimeOff <= 4:
		if intAttempsTimeOff > 2:
			print("\n\n\t\tSe ha introducido un valor diferente a un numero. \n\n\t\tVerifique su repuesta. \n\n\t\tGracias.")
		print(strWelcomeMessage)
		boolTiempoIngresadoOk = main.AsignaTiempo()
		
		if boolTiempoIngresadoOk:
			break

	else:
		cmd.system("cls")
		print(strWelcomeMessage)
		print("\n\n\n\t\tEl valor introducido no era un valor numerico, no fue posible programar el apagado. \n\n\t\tSi lo desea, ejecute de nuevo el script e ingresar una cantidad de tiempo valida. \n\n\t\tGracias.")
		break




cmd.system("cls")
print(strWelcomeMessage)
print("\n\n\n\t\t\t\tPrograma Finalizado. \n\n\t\t\t\tGracias.")