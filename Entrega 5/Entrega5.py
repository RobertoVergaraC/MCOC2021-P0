# PARTE MATRIZ LLENA
from numpy import zeros, double, logspace, eye
from time import perf_counter

def matriz_laplaciana_llena(N, dtype):
	A = zeros((N,N), dtype = dtype)
	for i in range(N):
		A[i,i] = 2
		for j in range(max(0,i-2),i):
			if abs(i - j) == 1:
				A[i,j] = -1
				A[j,i] = -1
	return A

#Tamaño de N
Nfake = logspace(0, 4.1, 50).tolist()
Nfake = [int(x) for x in Nfake]
Ns = []
for i in Nfake:
    if i not in Ns:
        Ns.append(i)
Ns.sort()

#Creamos listas vacías donde guardaremos la información
dts_ens = []
dts_sol = []

#Creamos el documento .txt, en donde por línea habrán 3 listas [N, dt, mem]
fid = open("rendimiento_E5_llena.txt","w")


#Creamos nuestras listas a partir de los valores de N
for i in range(10):
	print(f"Iteración {i+1}")
	dts_ens = []
	dts_sol = []
	for N in Ns:
		#Medimos tiempo de ensamblaje (t2-t1) y de solución (t3-t2)
		t1 = perf_counter()

		A = matriz_laplaciana_llena(N, double)		
		B = matriz_laplaciana_llena(N, double)

		t2 = perf_counter()

		C = A@B
		t3 = perf_counter()

		#Calculamos tiempo
		dt_en = t2 - t1
		dt_sol = t3 - t2

		#Agregamos la información a cada lista
		dts_ens.append(dt_en)
		dts_sol.append(dt_sol)

	
	fid.write(f"{[Ns, dts_ens, dts_sol]}\n") #fid es así: [[Ns1] [dts_en_1] [dts_sol_1]] \n [[Ns2] [dts_en_2] [dts_sol_2]] \n ....

fid.close()
print("Parte Matrices Llenas LISTO!\n")





# PARTE MATRIZ SPARSE
import numpy as np
import scipy.sparse as sparse
import scipy.sparse.linalg as lin

def matriz_laplaciana_dispersa(N, dtype):
	return 2*sparse.eye(N, dtype = dtype) - sparse.eye(N, N, 1, dtype = dtype) - sparse.eye(N, N, -1, dtype = dtype)

#Tamaño de N
Nfake = np.logspace(0, 6, 50).tolist()
Nfake = [int(x) for x in Nfake]
Ns = []
for i in Nfake:
    if i not in Ns:
        Ns.append(i)
Ns.sort()

#Creamos listas vacías donde guardaremos la información
dts_ens = []
dts_sol = []

#Creamos el documento .txt, en donde por línea habrán 3 listas [N, dt, mem]
fid = open("rendimiento_E5_dispersas.txt","w")


#Creamos nuestras listas a partir de los valores de N
for i in range(10):
	print(f"Iteración {i+1}")
	dts_ens = []
	dts_sol = []
	for N in Ns:
		#Medimos tiempo de ensamblaje (t2-t1) y de solución (t3-t2)
		t1 = perf_counter()

		A = matriz_laplaciana_dispersa(N, np.double)		
		B = matriz_laplaciana_dispersa(N, np.double)

		Acsr = sparse.csr_matrix(A)
		Bcsr = sparse.csr_matrix(B)

		t2 = perf_counter()

		C = Acsr@Bcsr
		
		t3 = perf_counter()

		#Calculamos tiempo
		dt_en = t2 - t1
		dt_sol = t3 - t2

		#Agregamos la información a cada lista
		dts_ens.append(dt_en)
		dts_sol.append(dt_sol)
	
	fid.write(f"{[Ns, dts_ens, dts_sol]}\n") #fid es así: [[Ns1] [dts_en_1] [dts_sol_1]] \n [[Ns2] [dts_en_2] [dts_sol_2]] \n ....

fid.close()
print("Parte Matrices Dispersas LISTO!")