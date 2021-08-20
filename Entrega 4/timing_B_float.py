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
tipo = float

#Tamaño de N (finalmente serán aprox 20 valores)
Nfake = logspace(0, 3.61, 22).tolist()
Nfake = [int(x) for x in Nfake]
Ns = []
for i in Nfake:
    if i not in Ns:
        Ns.append(i)
Ns.sort()
#print(len(Ns)) --> 45 values
Ns.remove(1)

#Ns = [2, 10, 100, 1000]

fid = open("rendimiento_caso_B_float.txt","w")





#CASO I

#Creamos listas vacías donde guardaremos la información
dts = []
for i in range(10):
	print(f"Iteración {i+1} Caso I")
	a = []
	for N in Ns:
		#Creamos matrices
		A = laplaciana(N, tipo)

		#Medimos tiempo antes y después de inv de A
		t1 = perf_counter()
		w,h = eigh(A)       #En donde w son los valores propios y h los vectores propios 
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





#CASO II.1
#Creamos listas vacías donde guardaremos la información
dts = []
for i in range(10):
	print(f"Iteración {i+1} Caso II.1")
	a = []
	for N in Ns:
		#Creamos matrices
		A = laplaciana(N, tipo)

		#Medimos tiempo antes y después de inv de A
		t1 = perf_counter()
		w,h = eigh(A, driver="ev", overwrite_a=False)
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
print("READY CASO II.1 \n")





#CASO II.2
#Creamos listas vacías donde guardaremos la información
dts = []
for i in range(10):
	print(f"Iteración {i+1} Caso II.2")
	a = []
	for N in Ns:
		#Creamos matrices
		A = laplaciana(N, tipo)

		#Medimos tiempo antes y después de inv de A
		t1 = perf_counter()
		w,h = eigh(A, driver="ev", overwrite_a=True)
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
print("READY CASO II.2 \n")





#CASO III.1
#Creamos listas vacías donde guardaremos la información
dts = []
for i in range(10):
	print(f"Iteración {i+1} Caso III.1")
	a = []
	for N in Ns:
		#Creamos matrices
		A = laplaciana(N, tipo)

		#Medimos tiempo antes y después de inv de A
		t1 = perf_counter()
		w,h = eigh(A, driver="evd", overwrite_a=False)
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
print("READY CASO III.1 \n")





#CASO III.2
#Creamos listas vacías donde guardaremos la información
dts = []
for i in range(10):
	print(f"Iteración {i+1} Caso III.2")
	a = []
	for N in Ns:
		#Creamos matrices
		A = laplaciana(N, tipo)

		#Medimos tiempo antes y después de inv de A
		t1 = perf_counter()
		w,h = eigh(A, driver="evd", overwrite_a=True)
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
print("READY CASO III.2 \n")





#CASO IV.1
#Creamos listas vacías donde guardaremos la información
dts = []
for i in range(10):
	print(f"Iteración {i+1} Caso IV.1")
	a = []
	for N in Ns:
		#Creamos matrices
		A = laplaciana(N, tipo)

		#Medimos tiempo antes y después de inv de A
		t1 = perf_counter()
		w,h = eigh(A, driver="evr", overwrite_a=False)
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
print("READY CASO IV.1 \n")





#CASO IV.2
#Creamos listas vacías donde guardaremos la información
dts = []
for i in range(10):
	print(f"Iteración {i+1} Caso IV.2")
	a = []
	for N in Ns:
		#Creamos matrices
		A = laplaciana(N, tipo)

		#Medimos tiempo antes y después de inv de A
		t1 = perf_counter()
		w,h = eigh(A, driver="evr", overwrite_a=True)
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
print("READY CASO IV.2 \n")





#CASO V.1
#Creamos listas vacías donde guardaremos la información
dts = []
for i in range(10):
	print(f"Iteración {i+1} Caso V.1")
	a = []
	for N in Ns:
		#Creamos matrices
		A = laplaciana(N, tipo)

		#Medimos tiempo antes y después de inv de A
		t1 = perf_counter()
		w,h = eigh(A, driver="evx", overwrite_a=False)
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
print("READY CASO V.1 \n")





#CASO V.2
#Creamos listas vacías donde guardaremos la información
dts = []
for i in range(10):
	print(f"Iteración {i+1} Caso V.2")
	a = []
	for N in Ns:
		#Creamos matrices
		A = laplaciana(N, tipo)

		#Medimos tiempo antes y después de inv de A
		t1 = perf_counter()
		w,h = eigh(A, driver="evx", overwrite_a=True)
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
print("READY CASO V.2 \n")




fid.close()