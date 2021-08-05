import matplotlib.pylab as plt
from psutil import virtual_memory

#Creamos listas vacías de lo que graficaremos
Ns = []
dts = []
mems = []

#Abrimos el archivo
fid = open("rendimiento.txt","r")

#Recorremos cada línea
for linea in fid:
	sl = linea.strip("\n") #Separo string por línea
	sl = eval(sl)          #Convierto cada línea en lista de listas (ya tiene su respectivo tipo dentro)
	N = (sl[0])
	dt = (sl[1])
	mem = (sl[2])

	Ns.append(N)
	dts.append(dt)
	mems.append(mem)

fid.close()

#LABELS y sus valores representativos
g1ylabel = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
g1yvalue = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600] #Tiempo

g2ylabel = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "10 GB"]
g2yvalue = [1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000] #Memoria

xlabel1 = [0.5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
xlabel2 = [0, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]


#GRAFICAMOS
plt.figure(1)

#Gráfico 1
g1 = plt.subplot(2,1,1)
plt.title("Rendimiento A@B")          #Título
plt.ylabel("Tiempo Transcurrido (s)") #Eje y

#Graficamos nuestros datos
for i in range(len(Ns)):
	g1.scatter(Ns[i], dts[i])
	g1.loglog(Ns[i], dts[i])

plt.xticks(visible = False)           #Quitamos labels de eje x
plt.yticks(g1yvalue, g1ylabel)        #Labels eje y
plt.grid(True)


#Gráfico 2
g2 = plt.subplot(2,1,2, sharex = g1)
plt.ylabel("Uso Memoria (s)")
plt.xlabel("Tamaño Matriz N")

#Graficamos nuestros datos
for i in range(len(Ns)):
	g2.scatter(Ns[i], mems[i], color ="steelblue")
	g2.loglog(Ns[i], mems[i], color = "steelblue")

plt.yticks(g2yvalue, g2ylabel)                                              #Labels eje y
plt.xticks(xlabel1, xlabel2, rotation = 45)                                 #Labels eje x
plt.axhline(y = virtual_memory().total, linestyle = '--', color = "black")  #Memoria RAM
plt.grid(True)

plt.show()