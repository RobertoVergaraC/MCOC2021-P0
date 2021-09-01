from time import perf_counter
import scipy.sparse as sp
import scipy.sparse.linalg as lin
from scipy.sparse import lil_matrix
from numpy import eye, ones, logspace, float32, zeros, double

def laplaciana(N, dtype):
	return 2*sp.eye(N, dtype = dtype) - sp.eye(N, N, 1, dtype = dtype) - sp.eye(N, N, -1, dtype = dtype)

#Seleccionamos el tipo de dato con el que trabajaremos:
tipo = double

#Tamaño de N (finalmente serán 45 valores)
Nfake = logspace(0, 6, 50).tolist()
Nfake = [int(x) for x in Nfake]
Ns = []
for i in Nfake:
    if i not in Ns:
        Ns.append(i)
Ns.sort()
#Ns = [1, 10, 100, 1000]

fid = open("rendimiento_solve_dispersas.txt","w")

print("CASO 'SOLVE' DISPERSAS\n")

for i in range(10):
	print(f"Iteración {i+1} Caso II")
	#Creamos listas vacías donde guardaremos la información
	dts_ens = []
	dts_sol = []
	for N in Ns:

		t1 = perf_counter()
		#Creamos matrices
		A = laplaciana(N, double)
		b = ones(N, dtype=double)
		Acsr = sp.csr_matrix(A)

		#Medimos tiempo antes y después de inv de A
		t2 = perf_counter()
		x = lin.spsolve(Acsr,b)
		t3 = perf_counter()

		#Calculamos tiempo
		dt_e = t2 - t1
		dt_s = t3 - t2

		#Agregamos la información a cada lista
		dts_ens.append(dt_e)
		dts_sol.append(dt_s)

	fid.write(f"{[Ns, dts_ens, dts_sol]}\n") #fid es así: [[Ns1],[dts_ens1],[dts_sol1]] \n [[Ns2],[dts_ens2],[dts_sol2]] \n ....

print("READY CASO DISPERSAS \n")


fid.close()