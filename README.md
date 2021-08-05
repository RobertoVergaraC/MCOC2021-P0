# MCOC2021-P0

# Mi computador principal

* Marca/modelo: Asus VivoBook S15 X530UF
* Tipo: Notebook
* Año adquisición: 2019
* Procesador:
  * Marca/Modelo: Intel Core i7-8550U
  * Velocidad Base: 1.80 GHz
  * Velocidad Máxima: 4.00 GHz
  * Numero de núcleos: 4 
  * Humero de hilos (Procesadores lógicos): 8
  * Arquitectura: x86_64
  * Set de instrucciones: Intel® SSE4.1, Intel® SSE4.2, Intel® AVX2
* Tamaño de las cachés del procesador
  * L1: 256KB
  * L1: 1.0MB
  * L2: 8.0MB
* Memoria 
  * Total: 16 GB
  * Tipo memoria: DDR4
  * Velocidad 2400 MHz
  * Numero de (SO)DIMM: 2
* Tarjeta Gráfica
  * Marca / Modelo: Nvidia GeForce MX130
  * Memoria dedicada: 2048 MB GDDR5
  * Resolución: 1920 x 1080
* Disco 1: 
  * Marca: SanDisk
  * Tipo: SSD
  * Tamaño: 238GB (en teoría tiene 256GB)
  * Particiones: 3 (OS, SYSTEM, RECOVERY)
  * Sistema de archivos: NTFS (además tiene FAT32 en la partición SYSTEM)
* Disco 2: 
  * Marca: Toshiba
  * Tipo: HDD
  * Tamaño: 931GB (en teoría tiene 1TB)
  * Particiones: 1
  * Sistema de archivos: NTFS
  
* Dirección MAC de la tarjeta wifi: 20:16:B9:44:BD:A3
* Dirección IP (Interna, del router): 192.168.100.2
* Dirección IP (Externa, del ISP): 186.67.234.139
* Proveedor internet: Entel Chile S.A. (fibra óptica)

# Desempeño MATMUL

En primer lugar cabe señalar que rendimiento.txt corresponde a un archivo que es una lista de listas, en donde cada línea es considerada una nueva corrida y está ordenado de la siguiente manera : [Ns],[dts],[mems]

![Desempeño Matmul](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Desempe%C3%B1o%20MATMUL.png)

# Preguntas

* ¿Cómo difiere del gráfico del profesor/ayudante?


* ¿A qué se pueden deber las diferencias en cada corrida?


* El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?


* ¿Qué versión de python está usando?
  Python Version: 3.9.6

* ¿Qué versión de numpy está usando?
  NumPy Version: 1.21.1

* Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen (screenshot) de su uso de procesador durante alguna corrida para confirmar.

![Procesador durante corrida](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Procesador%20durante%20corrida.jpg) 





