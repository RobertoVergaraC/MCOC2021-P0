import matplotlib.pylab as plt
import numpy as np

#Gráfico LLENA

#Creamos listas vacías de lo que graficaremos
Ns = []
dts_ens = []
dts_sol = []
max_ens = 0
max_sol = 0

#Abrimos los archivo
fid = open("rendimiento_E5_llena.txt","r")

#Recorremos cada línea
for linea in fid:
	sl = linea.strip("\n") #Separo string por línea
	sl = eval(sl)          #Convierto cada línea en lista de listas (ya tiene su respectivo tipo dentro)
	N = (sl[0])
	dt_ens = (sl[1])
	dt_sol = (sl[2])
	max_ens_1 = max(dt_ens)
	max_sol_1 = max(dt_sol)
	if max_ens_1>max_ens:
		max_ens = max_ens_1
	if max_sol_1>max_sol:
		max_sol = max_sol_1

	Ns.append(N)
	dts_ens.append(dt_ens)
	dts_sol.append(dt_sol)

fid.close()

#CREAR (O(N^n))
#n=0
x0_ens = [0, Ns[-1][-1]]
y0_ens = [max_ens, max_ens]
x0_sol = [0, Ns[-1][-1]]
y0_sol = [max_sol, max_sol]
#n=1
x1_ens = [Ns[-1][0], Ns[-1][-1]]
y1_ens = (max_ens/(Ns[-1][-1]**1)) * (np.array([Ns[-1][0]**1, Ns[-1][-1]**1])) 
x1_sol = [Ns[-1][0], Ns[-1][-1]]
y1_sol = (max_sol/(Ns[-1][-1]**1)) * (np.array([Ns[-1][0]**1, Ns[-1][-1]**1])) 
#n=2
x2_ens = [Ns[-1][0], Ns[-1][-1]]
y2_ens = (max_ens/(Ns[-1][-1]**2)) * (np.array([Ns[-1][0]**2, Ns[-1][-1]**2])) 
x2_sol = [Ns[-1][0], Ns[-1][-1]]
y2_sol = (max_sol/(Ns[-1][-1]**2)) * (np.array([Ns[-1][0]**2, Ns[-1][-1]**2]))
#n=3
x3_ens = [Ns[-1][0], Ns[-1][-1]]
y3_ens = (max_ens/(Ns[-1][-1]**3)) * (np.array([Ns[-1][0]**3, Ns[-1][-1]**3])) 
x3_sol = [Ns[-1][0], Ns[-1][-1]]
y3_sol = (max_sol/(Ns[-1][-1]**3)) * (np.array([Ns[-1][0]**3, Ns[-1][-1]**3]))
#n=4
x4_ens = [Ns[-1][0], Ns[-1][-1]]
y4_ens = (max_ens/(Ns[-1][-1]**4)) * (np.array([Ns[-1][0]**4, Ns[-1][-1]**4])) 
x4_sol = [Ns[-1][0], Ns[-1][-1]]
y4_sol = (max_sol/(Ns[-1][-1]**4)) * (np.array([Ns[-1][0]**4, Ns[-1][-1]**4]))


#LABELS y sus valores representativos
g1ylabel = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
g1yvalue = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600] #Tiempo

xlabel1 = [0.5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
xlabel2 = [0, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]



#GRAFICAMOS
plt.figure(1)

#Gráfico 1
g1 = plt.subplot(2,1,1)
plt.title("Rendimiento A@B Matrices Llenas")          #Título
plt.ylabel("Tiempo de ensamblado") #Eje y

#Graficamos nuestros datos
for i in range(len(Ns)):
	g1.loglog(Ns[i], dts_ens[i], marker='o', markersize=4, markerfacecolor="black", color="gray", alpha=0.5)
plt.loglog(x0_ens, y0_ens, linestyle="dashed", color="blue", label = "Constante")
plt.loglog(x1_ens, y1_ens, linestyle="dashed", color="orange", label= "$\mathregular{O(N)}$")
plt.loglog(x2_ens, y2_ens, linestyle="dashed", color="green", label= "$\mathregular{O(N^2)}$")
plt.loglog(x3_ens, y3_ens, linestyle="dashed", color="red", label= "$\mathregular{O(N^3)}$")
plt.loglog(x4_ens, y4_ens, linestyle="dashed", color="purple", label= "$\mathregular{O(N^4)}$")


plt.xticks(visible = False)           #Quitamos labels de eje x
plt.yticks(g1yvalue, g1ylabel)        #Labels eje y
plt.grid(True)
plt.ylim(0.000001, 10000)

#Gráfico 2
g2 = plt.subplot(2,1,2, sharex = g1)
plt.ylabel("Tiempo de solución")
plt.xlabel("Tamaño Matriz N")

#Graficamos nuestros datos
for i in range(len(Ns)):
	g2.loglog(Ns[i], dts_sol[i], marker='o', markersize=4, markerfacecolor="black", color="gray", alpha=0.5)
plt.loglog(x0_sol, y0_sol, linestyle="dashed", color="blue", label = "Constante")
plt.loglog(x1_sol, y1_sol, linestyle="dashed", color="orange", label= "$\mathregular{O(N)}$")
plt.loglog(x2_sol, y2_sol, linestyle="dashed", color="green", label= "$\mathregular{O(N^2)}$")
plt.loglog(x3_sol, y3_sol, linestyle="dashed", color="red", label= "$\mathregular{O(N^3)}$")
plt.loglog(x4_sol, y4_sol, linestyle="dashed", color="purple", label= "$\mathregular{O(N^4)}$")

plt.yticks(g1yvalue, g1ylabel)                                              #Labels eje y
plt.xticks(xlabel1, xlabel2, rotation = 45)                                 #Labels eje x
plt.grid(True)
plt.ylim(0.000001, 10000)
plt.legend().get_frame().set_alpha(0.5)

plt.savefig("Desempeño MATMUL Matrices Llenas", dpi = 300, bbox_inches = 'tight')

plt.show()













#Gráfico DISPERSA

#Creamos listas vacías de lo que graficaremos
Ns = []
dts_ens = []
dts_sol = []
max_ens = 0
max_sol = 0

#Abrimos los archivo
fid = open("rendimiento_E5_dispersas.txt","r")

#Recorremos cada línea
for linea in fid:
	sl = linea.strip("\n") #Separo string por línea
	sl = eval(sl)          #Convierto cada línea en lista de listas (ya tiene su respectivo tipo dentro)
	N = (sl[0])
	dt_ens = (sl[1])
	dt_sol = (sl[2])
	max_ens_1 = max(dt_ens)
	max_sol_1 = max(dt_sol)
	if max_ens_1>max_ens:
		max_ens = max_ens_1
	if max_sol_1>max_sol:
		max_sol = max_sol_1

	Ns.append(N)
	dts_ens.append(dt_ens)
	dts_sol.append(dt_sol)

fid.close()

#CREAR (O(N^n))
#n=0
x0_ens = [0, Ns[-1][-1]]
y0_ens = [max_ens, max_ens]
x0_sol = [0, Ns[-1][-1]]
y0_sol = [max_sol, max_sol]
#n=1
x1_ens = [Ns[-1][0], Ns[-1][-1]]
y1_ens = (max_ens/(Ns[-1][-1]**1)) * (np.array([Ns[-1][0]**1, Ns[-1][-1]**1])) 
x1_sol = [Ns[-1][0], Ns[-1][-1]]
y1_sol = (max_sol/(Ns[-1][-1]**1)) * (np.array([Ns[-1][0]**1, Ns[-1][-1]**1])) 
#n=2
x2_ens = [Ns[-1][0], Ns[-1][-1]]
y2_ens = (max_ens/(Ns[-1][-1]**2)) * (np.array([Ns[-1][0]**2, Ns[-1][-1]**2])) 
x2_sol = [Ns[-1][0], Ns[-1][-1]]
y2_sol = (max_sol/(Ns[-1][-1]**2)) * (np.array([Ns[-1][0]**2, Ns[-1][-1]**2]))
#n=3
x3_ens = [Ns[-1][0], Ns[-1][-1]]
y3_ens = (max_ens/(Ns[-1][-1]**3)) * (np.array([Ns[-1][0]**3, Ns[-1][-1]**3])) 
x3_sol = [Ns[-1][0], Ns[-1][-1]]
y3_sol = (max_sol/(Ns[-1][-1]**3)) * (np.array([Ns[-1][0]**3, Ns[-1][-1]**3]))
#n=4
x4_ens = [Ns[-1][0], Ns[-1][-1]]
y4_ens = (max_ens/(Ns[-1][-1]**4)) * (np.array([Ns[-1][0]**4, Ns[-1][-1]**4])) 
x4_sol = [Ns[-1][0], Ns[-1][-1]]
y4_sol = (max_sol/(Ns[-1][-1]**4)) * (np.array([Ns[-1][0]**4, Ns[-1][-1]**4]))


#LABELS y sus valores representativos
g1ylabel = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
g1yvalue = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600] #Tiempo

xlabel1 = [0.5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 250000,500000, 1000000]
xlabel2 = [0, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 250000,500000, 1000000]


#GRAFICAMOS
plt.figure(1)

#Gráfico 1
g1 = plt.subplot(2,1,1)
plt.title("Rendimiento A@B Matrices Dispersas")          #Título
plt.ylabel("Tiempo de ensamblado") #Eje y

#Graficamos nuestros datos
for i in range(len(Ns)):
	g1.loglog(Ns[i], dts_ens[i], marker='o', markersize=4, markerfacecolor="black", color="gray", alpha=0.5)
plt.loglog(x0_ens, y0_ens, linestyle="dashed", color="blue", label = "Constante")
plt.loglog(x1_ens, y1_ens, linestyle="dashed", color="orange", label= "$\mathregular{O(N)}$")
plt.loglog(x2_ens, y2_ens, linestyle="dashed", color="green", label= "$\mathregular{O(N^2)}$")
plt.loglog(x3_ens, y3_ens, linestyle="dashed", color="red", label= "$\mathregular{O(N^3)}$")
plt.loglog(x4_ens, y4_ens, linestyle="dashed", color="purple", label= "$\mathregular{O(N^4)}$")

plt.xticks(visible = False)           #Quitamos labels de eje x
plt.yticks(g1yvalue, g1ylabel)        #Labels eje y
plt.grid(True)
plt.ylim(0.000001, 10000)


#Gráfico 2
g2 = plt.subplot(2,1,2, sharex = g1)
plt.ylabel("Tiempo de solución")
plt.xlabel("Tamaño Matriz N")

#Graficamos nuestros datos
for i in range(len(Ns)):
	g2.loglog(Ns[i], dts_sol[i], marker='o', markersize=4, markerfacecolor="black", color="gray", alpha=0.5)
plt.loglog(x0_sol, y0_sol, linestyle="dashed", color="blue", label = "Constante")
plt.loglog(x1_sol, y1_sol, linestyle="dashed", color="orange", label= "$\mathregular{O(N)}$")
plt.loglog(x2_sol, y2_sol, linestyle="dashed", color="green", label= "$\mathregular{O(N^2)}$")
plt.loglog(x3_sol, y3_sol, linestyle="dashed", color="red", label= "$\mathregular{O(N^3)}$")
plt.loglog(x4_sol, y4_sol, linestyle="dashed", color="purple", label= "$\mathregular{O(N^4)}$")

plt.yticks(g1yvalue, g1ylabel)                                              #Labels eje y
plt.xticks(xlabel1, xlabel2, rotation = 45)                                 #Labels eje x
plt.grid(True)
plt.ylim(0.000001, 10000)
plt.legend().get_frame().set_alpha(0.5)

plt.savefig("Desempeño MATMUL Matrices Dispersas", dpi = 300, bbox_inches = 'tight')

plt.show()