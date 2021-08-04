import matplotlib.pylab as plt


Ns = []
dts = []
mems = []


fid = open("rendimiento.txt","r")

for line in fid:
	sl = line.split()
	N = int(sl[0])
	dt = float(sl[1])
	mem = int(sl[2])

	Ns.append(N)
	dts.append(dt)
	mems.append(mem)


fid.close()

g1ylabel = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
g1yvalue = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]

g2ylabel = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "10 GB"]
g2yvalue = [0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000]

xlabel = [0, 10, 21, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]

plt.figure(1)

g1 = plt.subplot(2,1,1)
plt.title("Rendimiento A@B")
plt.ylabel("Tiempo Transcurrido (s)")
plt.loglog(Ns, dts)
plt.xticks(xlabel, [], rotation = 45)
plt.grid(True)


g2 = plt.subplot(2,1,2, sharex = g1)
plt.ylabel("Uso Memoria [s]")
plt.xlabel("Tamaño Matriz N")
plt.grid(True)
plt.show()