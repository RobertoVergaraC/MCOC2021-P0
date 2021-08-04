from numpy import zeros, float16, float32, float64, logspace
from time import perf_counter
import matplotlib.pylab as plt


#Tamaño
N = 1000

Nfake = logspace(0, 4, 50).tolist()
Nfake = [int(x) for x in Nfake]
Ns = []
for i in Nfake:
    if i not in Ns:
        Ns.append(i)
Ns.sort()
#print(len(Ns)) --> 45 values
#print(Ns)

dts = []
mems = []

fid = open("rendimiento.txt","w")

for N in Ns:

	uso_memoria = 0

	A = zeros((N, N)) + 1

	#uso_memoria_teorico = 2*N*N   #bytes... float32 4bytes
	#uso_memoria_numpy = A.nbytes

	#print(f"uso_memoria_teorico = {uso_memoria_teorico}")
	#print(f"uso_memoria_numpy = {uso_memoria_numpy}")

	#exit()

	B = zeros((N, N)) + 2

	#print(f"A = {A}")
	#print(f"B = {B}")

	t1 = perf_counter()
	C = A@B
	t2 = perf_counter()

	uso_memoria_total = A.nbytes + B.nbytes + C.nbytes

	dt = t2 - t1

	dts.append(dt)
	mems.append(uso_memoria_total)

	print(f"N = {N} ; dt = {dt} seg ; mem = {uso_memoria_total} bytes ; flops = {N**3/dt} flops/s")
	fid.write(f"{N} {dt} {uso_memoria_total}\n")

fid.close()

#Python Version: 3.9.6
#NumPy Version: 1.21.1