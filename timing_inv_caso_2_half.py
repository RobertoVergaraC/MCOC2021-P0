from time import perf_counter
from numpy import zeros, logspace
from scipy.linalg import inv
from numpy import half, single, double, longdouble
from laplaciana import laplaciana

#Tamaño de N (finalmente serán 45 valores)
Nfake = logspace(0, 4, 50).tolist()
Nfake = [int(x) for x in Nfake]
Ns = []
for i in Nfake:
    if i not in Ns:
        Ns.append(i)
Ns.sort()
#print(len(Ns)) --> 45 values

#Creamos listas vacías donde guardaremos la información
dts = []
mems = []

#Creamos el documento .txt, en donde por línea habrán 3 listas [N, dt, mem]
fid = open("rendimiento_caso_2_half.txt","w")

for i in range(10):
	print(f"Iteración {i+1}")
	dts = []
	mems = []
	for N in Ns:

		#Creamos matrices
		A = laplaciana(N, half)

		#print(f"A = {A}")

		#Medimos tiempo antes y después de inv de A
		t1 = perf_counter()
		Am1 = inv(A, overwrite_a=False)
		t2 = perf_counter()

		#Calculamos Memoria
		uso_memoria_total = A.nbytes + Am1.nbytes

		#Calculamos tiempo
		dt = t2 - t1

		#Agregamos la información a cada lista
		dts.append(dt)
		mems.append(uso_memoria_total)

		#print(f"N = {N} ; dt = {dt} seg ; mem = {uso_memoria_total} bytes ; flops = {N**3/dt} flops/s")

	#print(f"{[Ns, dts, mems]}\n")  #Se utilizó para probar que la información se guardaba de manera correcta
	
	fid.write(f"{[Ns, dts, mems]}\n") #fid es así: [[Ns1],[dts1],[mems1]] \n [[Ns2],[dts2],[mems2]] \n ....

fid.close()
print("READY")