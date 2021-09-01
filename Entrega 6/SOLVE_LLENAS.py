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
#Ns = [1, 10, 100, 1000]

fid = open("rendimiento_solve_llenas.txt","w")

print("CASO 'SOLVE' LLENAS\n")

#ESCOGEMOS EL MEJOR CASO

#CASO III
for i in range(10):
	print(f"Iteración {i+1} Caso III")
	#Creamos listas vacías donde guardaremos la información
	dts_ens = []
	dts_sol = []
	for N in Ns:

		t1 = perf_counter()
		#Creamos matrices
		A = laplaciana(N, tipo)
		b = ones(N)

		#Medimos tiempo antes y después de inv de A
		t2 = perf_counter()
		x = solve(A,b, assume_a="pos")
		t3 = perf_counter()

		#Calculamos tiempo
		dt_e = t2 - t1
		dt_s = t3 - t2

		#Agregamos la información a cada lista
		dts_ens.append(dt_e)
		dts_sol.append(dt_s)

	fid.write(f"{[Ns, dts_ens, dts_sol]}\n") #fid es así: [[Ns1],[dts_ens1],[dts_sol1]] \n [[Ns2],[dts_ens2],[dts_sol2]] \n ....

print("READY CASO III \n")

fid.close()