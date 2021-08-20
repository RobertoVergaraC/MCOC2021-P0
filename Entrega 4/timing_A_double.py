from scipy import matmul, rand
from time import perf_counter
from scipy.linalg import solve, inv, eigh
from numpy import eye, ones, logspace, float32, zeros, double

def laplaciana(N, dtype):
	A = zeros((N,N), dtype = dtype)
	for i in range(N):
		A[i,i] = 2
		for j in range(max(0,i-2),i):
			if abs(i - j) == 1:
				A[i,j] = -1
				A[j,i] = -1
	return A

#Seleccionamos el tipo de dato con el que trabajaremos:
tipo = double

#Tamaño de N (finalmente serán 45 valores)
Nfake = logspace(0, 4, 50).tolist()
Nfake = [int(x) for x in Nfake]
Ns = []
for i in Nfake:
    if i not in Ns:
        Ns.append(i)
Ns.sort()
#print(len(Ns)) --> 45 values

#Ns = [1, 10, 100, 1000]

fid = open("rendimiento_caso_A_double.txt","w")





#CASO I

#Creamos listas vacías donde guardaremos la información
dts = []
for i in range(10):
	print(f"Iteración {i+1} Caso I")
	a = []
	for N in Ns:
		#Creamos matrices
		A = laplaciana(N, tipo)
		b = ones(N)

		#Medimos tiempo antes y después de inv de A
		t1 = perf_counter()
		x = inv(A)*b
		t2 = perf_counter()

		#Calculamos tiempo
		dt = t2 - t1

		#Agregamos la información a cada lista
		a.append(dt)
	dts.append(a)

promedio = []
for i in range(len(dts[0])):
	valor = 0
	for j in range(len(dts)):
		valor += dts[j][i]
		pos = j
	promedio.append(valor/len(dts))

fid.write(f"{[Ns, promedio]}\n") #fid es así: [[Ns],[dts promedio]] \n ....
print("READY CASO I \n")





#CASO II
#Creamos listas vacías donde guardaremos la información
dts = []
for i in range(10):
	print(f"Iteración {i+1} Caso II")
	a = []
	for N in Ns:
		#Creamos matrices
		A = laplaciana(N, tipo)
		b = ones(N)

		#Medimos tiempo antes y después de inv de A
		t1 = perf_counter()
		x = solve(A,b)
		t2 = perf_counter()

		#Calculamos tiempo
		dt = t2 - t1

		#Agregamos la información a cada lista
		a.append(dt)
	dts.append(a)

promedio = []
for i in range(len(dts[0])):
	valor = 0
	for j in range(len(dts)):
		valor += dts[j][i]
		pos = j
	promedio.append(valor/len(dts))

fid.write(f"{[Ns, promedio]}\n") #fid es así: [[Ns],[dts promedio]] \n ....
print("READY CASO II \n")




#CASO III
#Creamos listas vacías donde guardaremos la información
dts = []
for i in range(10):
	print(f"Iteración {i+1} Caso III")
	a = []
	for N in Ns:
		#Creamos matrices
		A = laplaciana(N, tipo)
		b = ones(N)

		#Medimos tiempo antes y después de inv de A
		t1 = perf_counter()
		x = solve(A,b, assume_a="pos")
		t2 = perf_counter()

		#Calculamos tiempo
		dt = t2 - t1

		#Agregamos la información a cada lista
		a.append(dt)
	dts.append(a)

promedio = []
for i in range(len(dts[0])):
	valor = 0
	for j in range(len(dts)):
		valor += dts[j][i]
		pos = j
	promedio.append(valor/len(dts))

fid.write(f"{[Ns, promedio]}\n") #fid es así: [[Ns],[dts promedio]] \n ....
print("READY CASO III \n")





#CASO IV
#Creamos listas vacías donde guardaremos la información
dts = []
for i in range(10):
	print(f"Iteración {i+1} Caso IV")
	a = []
	for N in Ns:
		#Creamos matrices
		A = laplaciana(N, tipo)
		b = ones(N)

		#Medimos tiempo antes y después de inv de A
		t1 = perf_counter()
		x = solve(A,b, assume_a="sym")
		t2 = perf_counter()

		#Calculamos tiempo
		dt = t2 - t1

		#Agregamos la información a cada lista
		a.append(dt)
	dts.append(a)

promedio = []
for i in range(len(dts[0])):
	valor = 0
	for j in range(len(dts)):
		valor += dts[j][i]
		pos = j
	promedio.append(valor/len(dts))

fid.write(f"{[Ns, promedio]}\n") #fid es así: [[Ns],[dts promedio]] \n ....
print("READY CASO IV \n")





#CASO V
#Creamos listas vacías donde guardaremos la información
dts = []
for i in range(10):
	print(f"Iteración {i+1} Caso V")
	a = []
	for N in Ns:
		#Creamos matrices
		A = laplaciana(N, tipo)
		b = ones(N)

		#Medimos tiempo antes y después de inv de A
		t1 = perf_counter()
		x = solve(A,b, overwrite_a=True)
		t2 = perf_counter()

		#Calculamos tiempo
		dt = t2 - t1

		#Agregamos la información a cada lista
		a.append(dt)
	dts.append(a)

promedio = []
for i in range(len(dts[0])):
	valor = 0
	for j in range(len(dts)):
		valor += dts[j][i]
		pos = j
	promedio.append(valor/len(dts))

fid.write(f"{[Ns, promedio]}\n") #fid es así: [[Ns],[dts promedio]] \n ....
print("READY CASO V \n")





#CASO VI
#Creamos listas vacías donde guardaremos la información
dts = []
for i in range(10):
	print(f"Iteración {i+1} Caso VI")
	a = []
	for N in Ns:
		#Creamos matrices
		A = laplaciana(N, tipo)
		b = ones(N)

		#Medimos tiempo antes y después de inv de A
		t1 = perf_counter()
		x = solve(A,b, overwrite_b=True)
		t2 = perf_counter()

		#Calculamos tiempo
		dt = t2 - t1

		#Agregamos la información a cada lista
		a.append(dt)
	dts.append(a)

promedio = []
for i in range(len(dts[0])):
	valor = 0
	for j in range(len(dts)):
		valor += dts[j][i]
		pos = j
	promedio.append(valor/len(dts))

fid.write(f"{[Ns, promedio]}\n") #fid es así: [[Ns],[dts promedio]] \n ....
print("READY CASO VI \n")





#CASO VII
#Creamos listas vacías donde guardaremos la información
dts = []
for i in range(10):
	print(f"Iteración {i+1} Caso VII")
	a = []
	for N in Ns:
		#Creamos matrices
		A = laplaciana(N, tipo)
		b = ones(N)

		#Medimos tiempo antes y después de inv de A
		t1 = perf_counter()
		x = solve(A,b, overwrite_a=True, overwrite_b=True)
		t2 = perf_counter()

		#Calculamos tiempo
		dt = t2 - t1

		#Agregamos la información a cada lista
		a.append(dt)
	dts.append(a)

promedio = []
for i in range(len(dts[0])):
	valor = 0
	for j in range(len(dts)):
		valor += dts[j][i]
		pos = j
	promedio.append(valor/len(dts))

fid.write(f"{[Ns, promedio]}") #fid es así: [[Ns],[dts promedio]] \n ....
print("READY CASO VII \n")


fid.close()