import matplotlib.pylab as plt
import matplotlib.patches as mpatches
import ast
from psutil import virtual_memory

#Creamos listas vacías de lo que graficaremos
#Caso half
Ns_caso_half = []
dts_caso_half = []
mems_caso_half = []

#Caso single
Ns_caso_single = []
dts_caso_single = []
mems_caso_single = []

#Caso double
Ns_caso_double = []
dts_caso_double = []
mems_caso_double = []

#Caso longdouble
Ns_caso_longdouble = []
dts_caso_longdouble = []
mems_caso_longdouble = []

#Abrimos los archivos
dic_archivos = {}
for i in range(3):
	dic_archivos[f"caso_{i+1}_half"] = open(f"rendimiento_caso_{i+1}_half.txt","r")
	dic_archivos[f"caso_{i+1}_single"] = open(f"rendimiento_caso_{i+1}_single.txt","r")
	dic_archivos[f"caso_{i+1}_double"] = open(f"rendimiento_caso_{i+1}_double.txt","r")
	dic_archivos[f"caso_{i+1}_longdouble"] = open(f"rendimiento_caso_{i+1}_longdouble.txt","r")

#Recorremos cada caso_X_dtpye
for linea in dic_archivos:
	if linea == "caso_1_half" or linea == "caso_2_half" or linea == "caso_3_half":
		sl = dic_archivos[linea].read().split("\n")              #Separo string por línea

		for i in sl:
			if len(i)>0:
				a = ast.literal_eval(i)                          #Convierto cada línea en lista de listas (ya tiene su respectivo tipo dentro)
			                        
				Ns_caso_half.append(a[0])
				dts_caso_half.append(a[1])
				mems_caso_half.append(a[2])
			elif sl == ['']:                                     #Este caso solo existe para que el programa pueda ser genérico
				for j in range(10):
					Ns_caso_half.append([])
					dts_caso_half.append([])
					mems_caso_half.append([])

	elif linea == "caso_1_single" or linea == "caso_2_single" or linea == "caso_3_single":
		sl = dic_archivos[linea].read().split("\n")              #Separo string por línea

		for i in sl:
			if len(i)>0:
				a = ast.literal_eval(i)                          #Convierto cada línea en lista de listas (ya tiene su respectivo tipo dentro)
			                        
				Ns_caso_single.append(a[0])
				dts_caso_single.append(a[1])
				mems_caso_single.append(a[2])
			elif sl == ['']:                                     #Este caso solo existe para que el programa pueda ser genérico
				for j in range(10):
					Ns_caso_single.append([])
					dts_caso_single.append([])
					mems_caso_single.append([])

	elif linea == "caso_1_double" or linea == "caso_2_double" or linea == "caso_3_double":
		sl = dic_archivos[linea].read().split("\n")              #Separo string por línea

		for i in sl:
			if len(i)>0:
				a = ast.literal_eval(i)                          #Convierto cada línea en lista de listas (ya tiene su respectivo tipo dentro)
			                        
				Ns_caso_double.append(a[0])
				dts_caso_double.append(a[1])
				mems_caso_double.append(a[2])
			elif sl == ['']:                                     #Este caso solo existe para que el programa pueda ser genérico
				for j in range(10):
					Ns_caso_double.append([])
					dts_caso_double.append([])
					mems_caso_double.append([])

	elif linea == "caso_1_longdouble" or linea == "caso_2_longdouble" or linea == "caso_3_longdouble":
		sl = dic_archivos[linea].read().split("\n")              #Separo string por línea

		for i in sl:
			if len(i)>0:
				a = ast.literal_eval(i)                          #Convierto cada línea en lista de listas (ya tiene su respectivo tipo dentro)
			                        
				Ns_caso_longdouble.append(a[0])
				dts_caso_longdouble.append(a[1])
				mems_caso_longdouble.append(a[2])
			elif sl == ['']:                                     #Este caso solo existe para que el programa pueda ser genérico
				for j in range(10):
					Ns_caso_longdouble.append([])
					dts_caso_longdouble.append([])
					mems_caso_longdouble.append([])

#Cerramos archivos
for i in range(3):
	dic_archivos[f"caso_{i+1}_half"].close()
	dic_archivos[f"caso_{i+1}_single"].close()
	dic_archivos[f"caso_{i+1}_double"].close()
	dic_archivos[f"caso_{i+1}_longdouble"].close()

# En este punto tenemos 4 grupos de listas armadas 1 por cada caso, cada grupo con N, dt y mem, y cada uno de estás con 30 listas, cada 10 listas corresponde grupo diferente (se armo en orden asique se sabe que están en orden)
# Procederemos a graficar 4 situaciones por cada tipo de dato, comparando cada caso

# PARTE GRAFICOS 
#LABELS y sus valores representativos
g1ylabel = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
g1yvalue = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600] #Tiempo

g2ylabel = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "10 GB"]
g2yvalue = [1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000] #Memoria

xlabel1 = [0.5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
xlabel2 = [0, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]







#GRAFICO CASO HALF
plt.figure(1)

#Gráfico 1
g1 = plt.subplot(2,1,1)
plt.title("Rendimiento Am1 Caso half")          #Título
plt.ylabel("Tiempo Transcurrido (s)") #Eje y

#Graficamos nuestros datos
for i in range(len(Ns_caso_half)):
	if 0<=i<=9:
		g1.scatter(Ns_caso_half[i], dts_caso_half[i], color ="steelblue", label = "Caso 1", s=10)
		g1.loglog(Ns_caso_half[i], dts_caso_half[i], color = "steelblue", label = "Caso 1")

		plt.xticks(visible = False)           #Quitamos labels de eje x
		plt.yticks(g1yvalue, g1ylabel)        #Labels eje y
		plt.grid(True)
	elif 10<=i<=19:
		g1.scatter(Ns_caso_half[i], dts_caso_half[i], color ="green", label = "Caso 2", s=10)
		g1.loglog(Ns_caso_half[i], dts_caso_half[i], color = "green", label = "Caso 2")

		plt.xticks(visible = False)           #Quitamos labels de eje x
		plt.yticks(g1yvalue, g1ylabel)        #Labels eje y
		plt.grid(True)
	elif 20<=i<=29:
		g1.scatter(Ns_caso_half[i], dts_caso_half[i], color ="red", label = "Caso 3", s=10)
		g1.loglog(Ns_caso_half[i], dts_caso_half[i], color = "red", label = "Caso 3")

		plt.xticks(visible = False)           #Quitamos labels de eje x
		plt.yticks(g1yvalue, g1ylabel)        #Labels eje y
		plt.grid(True)
		caso1 = mpatches.Patch(color = "steelblue", label="Caso 1")
		caso2 = mpatches.Patch(color = "green", label="Caso 2")
		caso3 = mpatches.Patch(color = "red", label="Caso 3")
		plt.legend(handles = [caso1, caso2, caso3])

#Gráfico 2
g2 = plt.subplot(2,1,2, sharex = g1)
plt.ylabel("Uso Memoria (s)")
plt.xlabel("Tamaño Matriz N")

#Graficamos nuestros datos
for i in range(len(Ns_caso_half)):
	if 0<=i<=9:
		g2.scatter(Ns_caso_half[i], mems_caso_half[i], color ="steelblue", label = "Caso 1", s=10)
		g2.loglog(Ns_caso_half[i], mems_caso_half[i], color = "steelblue")

		plt.yticks(g2yvalue, g2ylabel)                                              #Labels eje y
		plt.xticks(xlabel1, xlabel2, rotation = 45)                                 #Labels eje x
		plt.axhline(y = virtual_memory().total, linestyle = '--', color = "black")  #Memoria RAM
		plt.grid(True)
	elif 10<=i<=19:
		g2.scatter(Ns_caso_half[i], mems_caso_half[i], color ="green", label = "Caso 2", s=10)
		g2.loglog(Ns_caso_half[i], mems_caso_half[i], color = "green")

		plt.yticks(g2yvalue, g2ylabel)                                              #Labels eje y
		plt.xticks(xlabel1, xlabel2, rotation = 45)                                 #Labels eje x
		plt.axhline(y = virtual_memory().total, linestyle = '--', color = "black")  #Memoria RAM
		plt.grid(True)
	elif 20<=i<=29:
		g2.scatter(Ns_caso_half[i], mems_caso_half[i], color ="red", label = "Caso 3", s=10)
		g2.loglog(Ns_caso_half[i], mems_caso_half[i], color = "red")

		plt.yticks(g2yvalue, g2ylabel)                                              #Labels eje y
		plt.xticks(xlabel1, xlabel2, rotation = 45)                                 #Labels eje x
		plt.axhline(y = virtual_memory().total, linestyle = '--', color = "black")  #Memoria RAM
		plt.grid(True)
		caso1 = mpatches.Patch(color = "steelblue", label="Caso 1")
		caso2 = mpatches.Patch(color = "green", label="Caso 2")
		caso3 = mpatches.Patch(color = "red", label="Caso 3")
		plt.legend(handles = [caso1, caso2, caso3])

#Guardamos imagenes
plt.savefig("Desempeño INV CASO HALF", dpi = 300, bbox_inches = 'tight')
plt.show()








#GRAFICO CASO SINGLE
plt.figure(1)

#Gráfico 1
g1 = plt.subplot(2,1,1)
plt.title("Rendimiento Am1 Caso single")          #Título
plt.ylabel("Tiempo Transcurrido (s)") #Eje y

#Graficamos nuestros datos
for i in range(len(Ns_caso_single)):
	if 0<=i<=9:
		g1.scatter(Ns_caso_single[i], dts_caso_single[i], color ="steelblue", label = "Caso 1", s=10)
		g1.loglog(Ns_caso_single[i], dts_caso_single[i], color = "steelblue", label = "Caso 1")

		plt.xticks(visible = False)           #Quitamos labels de eje x
		plt.yticks(g1yvalue, g1ylabel)        #Labels eje y
		plt.grid(True)
	elif 10<=i<=19:
		g1.scatter(Ns_caso_single[i], dts_caso_single[i], color ="green", label = "Caso 2", s=10)
		g1.loglog(Ns_caso_single[i], dts_caso_single[i], color = "green", label = "Caso 2")

		plt.xticks(visible = False)           #Quitamos labels de eje x
		plt.yticks(g1yvalue, g1ylabel)        #Labels eje y
		plt.grid(True)
	elif 20<=i<=29:
		g1.scatter(Ns_caso_single[i], dts_caso_single[i], color ="red", label = "Caso 3", s=10)
		g1.loglog(Ns_caso_single[i], dts_caso_single[i], color = "red", label = "Caso 3")

		plt.xticks(visible = False)           #Quitamos labels de eje x
		plt.yticks(g1yvalue, g1ylabel)        #Labels eje y
		plt.grid(True)
		caso1 = mpatches.Patch(color = "steelblue", label="Caso 1")
		caso2 = mpatches.Patch(color = "green", label="Caso 2")
		caso3 = mpatches.Patch(color = "red", label="Caso 3")
		plt.legend(handles = [caso1, caso2, caso3])

#Gráfico 2
g2 = plt.subplot(2,1,2, sharex = g1)
plt.ylabel("Uso Memoria (s)")
plt.xlabel("Tamaño Matriz N")

#Graficamos nuestros datos
for i in range(len(Ns_caso_single)):
	if 0<=i<=9:
		g2.scatter(Ns_caso_single[i], mems_caso_single[i], color ="steelblue", label = "Caso 1", s=10)
		g2.loglog(Ns_caso_single[i], mems_caso_single[i], color = "steelblue")

		plt.yticks(g2yvalue, g2ylabel)                                              #Labels eje y
		plt.xticks(xlabel1, xlabel2, rotation = 45)                                 #Labels eje x
		plt.axhline(y = virtual_memory().total, linestyle = '--', color = "black")  #Memoria RAM
		plt.grid(True)
	elif 10<=i<=19:
		g2.scatter(Ns_caso_single[i], mems_caso_single[i], color ="green", label = "Caso 2", s=10)
		g2.loglog(Ns_caso_single[i], mems_caso_single[i], color = "green")

		plt.yticks(g2yvalue, g2ylabel)                                              #Labels eje y
		plt.xticks(xlabel1, xlabel2, rotation = 45)                                 #Labels eje x
		plt.axhline(y = virtual_memory().total, linestyle = '--', color = "black")  #Memoria RAM
		plt.grid(True)
	elif 20<=i<=29:
		g2.scatter(Ns_caso_single[i], mems_caso_single[i], color ="red", label = "Caso 3", s=10)
		g2.loglog(Ns_caso_single[i], mems_caso_single[i], color = "red")

		plt.yticks(g2yvalue, g2ylabel)                                              #Labels eje y
		plt.xticks(xlabel1, xlabel2, rotation = 45)                                 #Labels eje x
		plt.axhline(y = virtual_memory().total, linestyle = '--', color = "black")  #Memoria RAM
		plt.grid(True)
		caso1 = mpatches.Patch(color = "steelblue", label="Caso 1")
		caso2 = mpatches.Patch(color = "green", label="Caso 2")
		caso3 = mpatches.Patch(color = "red", label="Caso 3")
		plt.legend(handles = [caso1, caso2, caso3])

#Guardamos imagenes
plt.savefig("Desempeño INV CASO SINGLE", dpi = 300, bbox_inches = 'tight')
plt.show()







#GRAFICO CASO DOUBLE
plt.figure(1)

#Gráfico 1
g1 = plt.subplot(2,1,1)
plt.title("Rendimiento Am1 Caso double")          #Título
plt.ylabel("Tiempo Transcurrido (s)") #Eje y

#Graficamos nuestros datos
for i in range(len(Ns_caso_double)):
	if 0<=i<=9:
		g1.scatter(Ns_caso_double[i], dts_caso_double[i], color ="steelblue", label = "Caso 1", s=10)
		g1.loglog(Ns_caso_double[i], dts_caso_double[i], color = "steelblue", label = "Caso 1")

		plt.xticks(visible = False)           #Quitamos labels de eje x
		plt.yticks(g1yvalue, g1ylabel)        #Labels eje y
		plt.grid(True)
	elif 10<=i<=19:
		g1.scatter(Ns_caso_double[i], dts_caso_double[i], color ="green", label = "Caso 2", s=10)
		g1.loglog(Ns_caso_double[i], dts_caso_double[i], color = "green", label = "Caso 2")

		plt.xticks(visible = False)           #Quitamos labels de eje x
		plt.yticks(g1yvalue, g1ylabel)        #Labels eje y
		plt.grid(True)
	elif 20<=i<=29:
		g1.scatter(Ns_caso_double[i], dts_caso_double[i], color ="red", label = "Caso 3", s=10)
		g1.loglog(Ns_caso_double[i], dts_caso_double[i], color = "red", label = "Caso 3")

		plt.xticks(visible = False)           #Quitamos labels de eje x
		plt.yticks(g1yvalue, g1ylabel)        #Labels eje y
		plt.grid(True)
		caso1 = mpatches.Patch(color = "steelblue", label="Caso 1")
		caso2 = mpatches.Patch(color = "green", label="Caso 2")
		caso3 = mpatches.Patch(color = "red", label="Caso 3")
		plt.legend(handles = [caso1, caso2, caso3])

#Gráfico 2
g2 = plt.subplot(2,1,2, sharex = g1)
plt.ylabel("Uso Memoria (s)")
plt.xlabel("Tamaño Matriz N")

#Graficamos nuestros datos
for i in range(len(Ns_caso_double)):
	if 0<=i<=9:
		g2.scatter(Ns_caso_double[i], mems_caso_double[i], color ="steelblue", label = "Caso 1", s=10)
		g2.loglog(Ns_caso_double[i], mems_caso_double[i], color = "steelblue")

		plt.yticks(g2yvalue, g2ylabel)                                              #Labels eje y
		plt.xticks(xlabel1, xlabel2, rotation = 45)                                 #Labels eje x
		plt.axhline(y = virtual_memory().total, linestyle = '--', color = "black")  #Memoria RAM
		plt.grid(True)
	elif 10<=i<=19:
		g2.scatter(Ns_caso_double[i], mems_caso_double[i], color ="green", label = "Caso 2", s=10)
		g2.loglog(Ns_caso_double[i], mems_caso_double[i], color = "green")

		plt.yticks(g2yvalue, g2ylabel)                                              #Labels eje y
		plt.xticks(xlabel1, xlabel2, rotation = 45)                                 #Labels eje x
		plt.axhline(y = virtual_memory().total, linestyle = '--', color = "black")  #Memoria RAM
		plt.grid(True)
	elif 20<=i<=29:
		g2.scatter(Ns_caso_double[i], mems_caso_double[i], color ="red", label = "Caso 3", s=10)
		g2.loglog(Ns_caso_double[i], mems_caso_double[i], color = "red")

		plt.yticks(g2yvalue, g2ylabel)                                              #Labels eje y
		plt.xticks(xlabel1, xlabel2, rotation = 45)                                 #Labels eje x
		plt.axhline(y = virtual_memory().total, linestyle = '--', color = "black")  #Memoria RAM
		plt.grid(True)
		caso1 = mpatches.Patch(color = "steelblue", label="Caso 1")
		caso2 = mpatches.Patch(color = "green", label="Caso 2")
		caso3 = mpatches.Patch(color = "red", label="Caso 3")
		plt.legend(handles = [caso1, caso2, caso3])

#Guardamos imagenes
plt.savefig("Desempeño INV CASO DOUBLE", dpi = 300, bbox_inches = 'tight')
plt.show()







#GRAFICO CASO LONGDOUBLE
plt.figure(1)

#Gráfico 1
g1 = plt.subplot(2,1,1)
plt.title("Rendimiento Am1 Caso longdouble")          #Título
plt.ylabel("Tiempo Transcurrido (s)") #Eje y

#Graficamos nuestros datos
for i in range(len(Ns_caso_longdouble)):
	if 0<=i<=9:
		g1.scatter(Ns_caso_longdouble[i], dts_caso_longdouble[i], color ="steelblue", label = "Caso 1", s=10)
		g1.loglog(Ns_caso_longdouble[i], dts_caso_longdouble[i], color = "steelblue", label = "Caso 1")

		plt.xticks(visible = False)           #Quitamos labels de eje x
		plt.yticks(g1yvalue, g1ylabel)        #Labels eje y
		plt.grid(True)
	elif 10<=i<=19:
		g1.scatter(Ns_caso_longdouble[i], dts_caso_longdouble[i], color ="green", label = "Caso 2", s=10)
		g1.loglog(Ns_caso_longdouble[i], dts_caso_longdouble[i], color = "green", label = "Caso 2")

		plt.xticks(visible = False)           #Quitamos labels de eje x
		plt.yticks(g1yvalue, g1ylabel)        #Labels eje y
		plt.grid(True)
	elif 20<=i<=29:
		g1.scatter(Ns_caso_longdouble[i], dts_caso_longdouble[i], color ="red", label = "Caso 3", s=10)
		g1.loglog(Ns_caso_longdouble[i], dts_caso_longdouble[i], color = "red", label = "Caso 3")

		plt.xticks(visible = False)           #Quitamos labels de eje x
		plt.yticks(g1yvalue, g1ylabel)        #Labels eje y
		plt.grid(True)
		caso1 = mpatches.Patch(color = "steelblue", label="Caso 1")
		caso2 = mpatches.Patch(color = "green", label="Caso 2")
		caso3 = mpatches.Patch(color = "red", label="Caso 3")
		plt.legend(handles = [caso1, caso2, caso3])

#Gráfico 2
g2 = plt.subplot(2,1,2, sharex = g1)
plt.ylabel("Uso Memoria (s)")
plt.xlabel("Tamaño Matriz N")

#Graficamos nuestros datos
for i in range(len(Ns_caso_longdouble)):
	if 0<=i<=9:
		g2.scatter(Ns_caso_longdouble[i], mems_caso_longdouble[i], color ="steelblue", label = "Caso 1", s=10)
		g2.loglog(Ns_caso_longdouble[i], mems_caso_longdouble[i], color = "steelblue")

		plt.yticks(g2yvalue, g2ylabel)                                              #Labels eje y
		plt.xticks(xlabel1, xlabel2, rotation = 45)                                 #Labels eje x
		plt.axhline(y = virtual_memory().total, linestyle = '--', color = "black")  #Memoria RAM
		plt.grid(True)
	elif 10<=i<=19:
		g2.scatter(Ns_caso_longdouble[i], mems_caso_longdouble[i], color ="green", label = "Caso 2", s=10)
		g2.loglog(Ns_caso_longdouble[i], mems_caso_longdouble[i], color = "green")

		plt.yticks(g2yvalue, g2ylabel)                                              #Labels eje y
		plt.xticks(xlabel1, xlabel2, rotation = 45)                                 #Labels eje x
		plt.axhline(y = virtual_memory().total, linestyle = '--', color = "black")  #Memoria RAM
		plt.grid(True)
	elif 20<=i<=29:
		g2.scatter(Ns_caso_longdouble[i], mems_caso_longdouble[i], color ="red", label = "Caso 3", s=10)
		g2.loglog(Ns_caso_longdouble[i], mems_caso_longdouble[i], color = "red")

		plt.yticks(g2yvalue, g2ylabel)                                              #Labels eje y
		plt.xticks(xlabel1, xlabel2, rotation = 45)                                 #Labels eje x
		plt.axhline(y = virtual_memory().total, linestyle = '--', color = "black")  #Memoria RAM
		plt.grid(True)
		caso1 = mpatches.Patch(color = "steelblue", label="Caso 1")
		caso2 = mpatches.Patch(color = "green", label="Caso 2")
		caso3 = mpatches.Patch(color = "red", label="Caso 3")
		plt.legend(handles = [caso1, caso2, caso3])

#Guardamos imagenes
plt.savefig("Desempeño INV CASO LONGDOUBLE", dpi = 300, bbox_inches = 'tight')
plt.show()