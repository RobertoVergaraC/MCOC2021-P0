import matplotlib.pylab as plt
import matplotlib.patches as mpatches
import ast
from psutil import virtual_memory

#Realizaremos 4 gráficos
#1.- Comparación de A con float
#2.- Comparación de A con double
#3.- Comparación de B con float
#4.- Comparación de B con double

#Lista de listas para cada caso, en donde cada sublista es otra opción, todas en el mismo orden del enunciado.
#Caso A float
Ns_A_float = []
dts_A_float = []

#Caso A double
Ns_A_double = []
dts_A_double = []

#Caso B float
Ns_B_float = []
dts_B_float = []

#Caso B double
Ns_B_double = []
dts_B_double = []

#Abrimos nuestros 4 archivos
fid_A_float = open("rendimiento_caso_A_float.txt","r")
fid_A_double = open("rendimiento_caso_A_double.txt","r")
fid_B_float = open("rendimiento_caso_B_float.txt","r")
fid_B_double = open("rendimiento_caso_B_double.txt","r")

#Recorremos cada archivo

#Caso A float
#Recorremos cada línea
for linea in fid_A_float:
	sl = linea.strip("\n") #Separo string por línea
	sl = eval(sl)          #Convierto cada línea en lista de listas (ya tiene su respectivo tipo dentro)
	N = (sl[0])
	dt = (sl[1])

	Ns_A_float.append(N)
	dts_A_float.append(dt)

#Caso A double
#Recorremos cada línea
for linea in fid_A_double:
	sl = linea.strip("\n") #Separo string por línea
	sl = eval(sl)          #Convierto cada línea en lista de listas (ya tiene su respectivo tipo dentro)
	N = (sl[0])
	dt = (sl[1])

	Ns_A_double.append(N)
	dts_A_double.append(dt)

#Caso B float
#Recorremos cada línea
for linea in fid_B_float:
	sl = linea.strip("\n") #Separo string por línea
	sl = eval(sl)          #Convierto cada línea en lista de listas (ya tiene su respectivo tipo dentro)
	N = (sl[0])
	dt = (sl[1])

	Ns_B_float.append(N)
	dts_B_float.append(dt)

#Caso B double
#Recorremos cada línea
for linea in fid_B_double:
	sl = linea.strip("\n") #Separo string por línea
	sl = eval(sl)          #Convierto cada línea en lista de listas (ya tiene su respectivo tipo dentro)
	N = (sl[0])
	dt = (sl[1])

	Ns_B_double.append(N)
	dts_B_double.append(dt)

#Cerramos los archivos
fid_A_float.close()
fid_A_double.close()
fid_B_float.close()
fid_B_double.close()

#Ahora que tenemos todo en listas podemos comenzar a graficar


#LABELS y sus valores representativos
g1ylabel = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
g1yvalue = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600] #Tiempo

g2ylabel = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "10 GB"]
g2yvalue = [1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000] #Memoria

xlabel1 = [0.5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
xlabel2 = [0, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]

#GRÁFICO CASO A FLOAT
plt.title("Comparación Caso A (float)")          #Título
plt.ylabel("Tiempo Transcurrido (s)")            #Eje y

#Graficamos nuestros datos
for i in range(len(Ns_A_float)):
	#plt.scatter(Ns_A_float[i], dts_A_float[i], s=10)
	plt.loglog(Ns_A_float[i], dts_A_float[i], marker='o', markersize=4)

plt.legend(["Option I (x = Am1*b)", "Option II (solve by default)", "Option III (using assume_a='pos')", "Option IV (using assume_a='sym')", "Option V (using overwrite_a=True)", "Option VI (using overwrite_b=True)", "Option VII (using verwrite_a=True and overwrite_b=True)"], prop={'size': 8.5})
plt.yticks(g1yvalue, g1ylabel)                   #Labels eje y
plt.xticks(xlabel1, xlabel2, rotation = 45)      #Labels eje x
plt.grid(True)

plt.savefig("Comparación Caso A (float)", dpi = 300, bbox_inches = 'tight')
plt.show()

#GRÁFICO CASO A DOUBLE
plt.title("Comparación Caso A (double)")         #Título
plt.ylabel("Tiempo Transcurrido (s)")            #Eje y

#Graficamos nuestros datos
for i in range(len(Ns_A_double)):
	#plt.scatter(Ns_A_double[i], dts_A_double[i], s=10)
	plt.loglog(Ns_A_double[i], dts_A_double[i], marker='o', markersize=4)

plt.legend(["Option I (x = Am1*b)", "Option II (solve by default)", "Option III (using assume_a='pos')", "Option IV (using assume_a='sym')", "Option V (using overwrite_a=True)", "Option VI (using overwrite_b=True)", "Option VII (using verwrite_a=True and overwrite_b=True)"], prop={'size': 8.5})
plt.yticks(g1yvalue, g1ylabel)                   #Labels eje y
plt.xticks(xlabel1, xlabel2, rotation = 45)      #Labels eje x
plt.grid(True)

plt.savefig("Comparación Caso A (double)", dpi = 300, bbox_inches = 'tight')
plt.show()

#GRÁFICO CASO B FLOAT
plt.title("Comparación Caso B (float)")          #Título
plt.ylabel("Tiempo Transcurrido (s)")            #Eje y

#Graficamos nuestros datos
for i in range(len(Ns_B_float)):
	#plt.scatter(Ns_B_float[i], dts_B_float[i], s=10)
	plt.loglog(Ns_B_float[i], dts_B_float[i], marker='o', markersize=4)

plt.legend(["Option I (eigh by default)", "Option II.1 (driver='ev' and overwrite_a=False)", "Option II.2 (driver='ev' and overwrite_a=True)", "Option III.1 (driver='evd' and overwrite_a=False)", "Option III.2 (driver='evd' and overwrite_a=True)", "Option IV.1 (driver='evr' and overwrite_a=False)", "Option IV.2 (driver='evr' and overwrite_a=True)", "Option V.1 (driver='evx' and overwrite_a=False)", "Option V.2 (driver='evx' and overwrite_a=True)"], prop={'size': 8.5})
plt.yticks(g1yvalue, g1ylabel)                   #Labels eje y
plt.xticks(xlabel1, xlabel2, rotation = 45)      #Labels eje x
plt.grid(True)

plt.savefig("Comparación Caso B (float)", dpi = 300, bbox_inches = 'tight')
plt.show()

#GRÁFICO CASO B DOUBLE
plt.title("Comparación Caso B (double)")          #Título
plt.ylabel("Tiempo Transcurrido (s)")            #Eje y

#Graficamos nuestros datos
for i in range(len(Ns_B_double)):
	#plt.scatter(Ns_B_double[i], dts_B_double[i], s=10)
	plt.loglog(Ns_B_double[i], dts_B_double[i], marker='o', markersize=4)

plt.legend(["Option I (eigh by default)", "Option II.1 (driver='ev' and overwrite_a=False)", "Option II.2 (driver='ev' and overwrite_a=True)", "Option III.1 (driver='evd' and overwrite_a=False)", "Option III.2 (driver='evd' and overwrite_a=True)", "Option IV.1 (driver='evr' and overwrite_a=False)", "Option IV.2 (driver='evr' and overwrite_a=True)", "Option V.1 (driver='evx' and overwrite_a=False)", "Option V.2 (driver='evx' and overwrite_a=True)"], prop={'size': 8.5})
plt.yticks(g1yvalue, g1ylabel)                   #Labels eje y
plt.xticks(xlabel1, xlabel2, rotation = 45)      #Labels eje x
plt.grid(True)

plt.savefig("Comparación Caso B (double)", dpi = 300, bbox_inches = 'tight')
plt.show()
