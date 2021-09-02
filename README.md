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
  * Numero de hilos (Procesadores lógicos): 8
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

En primer lugar cabe señalar que rendimiento.txt corresponde a un archivo que por cada línea es una lista de listas, en donde cada una de estas es considerada una nueva corrida y está ordenada de la siguiente manera : [[Ns],[dts],[mems]]

![Desempeño Matmul](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%202/Desempe%C3%B1o%20MATMUL.png)

### Preguntas

* **¿Cómo difiere del gráfico del profesor/ayudante?**  
  En primer lugar se puede notar como tengo una partida similar en tiempo a las del profesor/ayudante, luego las 9 siguientes tienen un tiempo de partida mayor. Luego es interesante señalar como en matrices con tamaños entre 50 y 60 de evidencia un salto en el tiempo de memoria en el cual en mi notebook es menor que el del profesor/ayudante. Por último el comportamiento final es prácticamente igual, terminando por cada partida un poco inferior a un minuto al igual que el profesor/ayudante. Otra diferencia significativa podría ser debido a la cantidad de N en el eje x que el profesor/ayudante seleccionó vs los que yo establecí (45).    
  En estricto rigor se puede evidenciar como el pc del profesor/ayudante tiene un mejor rendimiento en un inicio y en el final, mientras que mi PC tiene mejor rendimiento en los valores de N intermedios.  
  Lo anteriormente señalado ocurre debido a las distintas características de caché, RAM, y disco entre el pc del profesor/ayudante y el mio. Pero en en general, los gráficos son muy similares.


* **¿A qué se pueden deber las diferencias en cada corrida?**  
  Esto ocurre, ya que, python para el uso de memoria siempre intenta utilizar la menor cantidad de memoria posible. Además, la memoria funciona por bloques, entonces al necesitar más memoria ira en busqueda del siguiente módulo de memoria y es por esto que se producen los "saltos" en el tiempo que se observan en el gráfico, en estos cambios de memoria manda la jerarquia de memoria es decir, primero caché, luego RAM y por último el disco. Este proceso de "cambio de módulo de memoria" es muy variable y es por eso que se puede evidenciar diferencias en los tiempos de ejecución en cada corrida.  
  Otro factor que puede influir es el sistema operativo, el cual prioriza distintos procesos (hace una cosa a la vez con distintas prioridades, por lo que hacer diferentes acciones el el pc (como navegar en internet) puede influir directamente), los cuales pueden influir directamente en el tiempo de ejecución, estás pueden ser acciones que uno hace directamente, como también acciones que hace el sistema operativo reliza por detrás sin que uno se de cuenta.  
  Por último, otros factores que pueden influir son que el computador este utilizando una gran cantidad de recursos que relentice el proceso (por ejemplo que la temperatura del PC aumente).


* **El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?**  
  Esto ocurre ya que, en una multiplicación de matrices existe un número predeterminado de "acciones" por lo que la memoria utilizada en la operación siempre será la misma (es por eso que al graficar las 10 corridas sigue viendose una única gráfica). Es decir, la memoria utilizada esta establecida por la operación y el porte de las matrices y no influira si esta se desarrolla antes o después a diferencia de lo que ocurre con el tiempo.  
  Con respecto a la linealidad del gráfico, la memoria utilizada es lineal ya que si una matriz es el doble de grande simplemente utilizará el doble de memoria sin importar otros factores (lo mismo ocurre con la operación MATMUL), pero en el caso del tiempo, a medida que se multiplica una matriz con valores de N más grande, los recursos necesarios van creciendo exponencialemente (es decir una matriz el doble de grande no demorara necesariamente el doble del tiempo sino que más), esto debido a la complejidad de la operación MATMUL que va aumentando exponencialmente a medida que aumenta los valores de N.  


* **¿Qué versión de python está usando?**  
  Python Version: 3.9.6


* **¿Qué versión de numpy está usando?**  
  NumPy Version: 1.21.1


* **Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen (screenshot) de su uso de procesador durante alguna corrida para confirmar.**  

![Procesador durante corrida](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%202/Procesador%20durante%20corrida.jpg) 

Tal como se evidencia en la imágen, durante la ejecución del código se utilizan 8 procesadores, los cuales corresponden a todos los de mi CPU.  
El hecho de que utilice los 8 procesadores (y con tanto %uso), es ya que el código necesita demasiados recursos y de esta manera utiliza demasiada CPU a tal punto de necesitar el 100% de su capacidad.

# Desempeño de INV

Se realizan 12 archivos .txt, uno por cada tipo en cada uno de los tres casos. Es importante señalar que tanto el tipo half y longdouble en el caso 1 (usando librería numpy) no se logran realizar, ya que son tipos que linalg de numpy no soportan.

A continuación se muestrán las comparaciones de los casos por cada tipo de dato:

**DTYPE: HALF**
![HALF](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%203/Desempe%C3%B1o%20INV%20CASO%20HALF.png)

**DTYPE: SINGLE**
![SINGLE](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%203/Desempe%C3%B1o%20INV%20CASO%20SINGLE.png)

**DTYPE: DOUBLE**
![DOUBLE](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%203/Desempe%C3%B1o%20INV%20CASO%20DOUBLE.png)

**DTYPE: LONGDOUBLE**
![LONGDOUBLE](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%203/Desempe%C3%B1o%20INV%20CASO%20LONGDOUBLE.png)


Además tanto el desempeño del procesador como de la memoria en todos los casos que los códigos funcionaron los resultado fueron prácticamente idénticos, es decir el procesador usando casi todos sus recursos (todos incluso), mientras que la memoria prácticamente no cambiaba y si lo hacía era muy leve. Si hubo alguna diferencia fue prácticamente imperceptible.

**Procesador durante corridas:**
![CPU_INV](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%203/CPU%20DURANTE%20CORRIDA%20INV.jpg)

**Memoria durante corridas:**
![MEMORIA_INV](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%203/MEMORIA%20DURANTE%20CORRIDA%20INV.jpg)  
  

### Preguntas

* **¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)? Justifique claramente su respuesta.**  
  **NumPy**: numpy.linalg.inv(A) lo que hace es llamar a la función numpy.linalg.solve(A,I) (esta función realiza Ax = I, en donde x correspondería en este caso a la matriz inversa de A), en donde I correpsonde a la matriz identidad, y luego mediante lapack's LU factorization (paquete de Descomposición LU) resuleve el sistema de solve. Esto significa que finalmente ocupa eliminación Gaussiana en donde la ortogonalidad no se detecta por default. Cabe destacar que este método aumenta el error si el array dado no es cuadrado o la inversión falla.  
  **SciPy**: Muy parecido a NumPy, lo que hace Scipy (scipy.linalg.inv(A)) es llamar directamente a los paquetes LAPACK (get_lapack_funcs("función que se quiere")) y desde ahí mediante descomposición LU realiza la inversión de la matriz. Es importante señalar que la opción overwrite_a lo que realiza es reemplazar los valores de la matriz (los va descartando), es por eso que esta opción en True podría incrementar el rendimiento.  
  Importante decir que se puede notar que scipy realiza en general el proceso más rápido ya que llama directamente a los paquetes para realizar la descomposición Lu, en cambio, numpy.linalg.inv() llama a numpy.linalg.solve(), y es esta función la que llama al mismo paquete, es decir "utiliza un paso más"

* **¿Cómo incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? Justifique su comentario en base al uso de procesadores y memoria observado durante las corridas.**  
La lógica del paralelismo es realizar varias tareas al mismo tiempo, para esto el computador divide el procesador en "mini procesadores" que cada uno realiza diferentes acciones.   Sabiendo esto, al correr el programa con datos como half vs longdouble el procesador con half ("menos información"), trabaja de mejor manera con estos "mini procesadores", ya que esa tarea puede distribuirla mejor entre ellos sin tener que colapsar los caché, en cambio con longdouble el procesador necesita usar mayores recursos destinando más cantidad de "mini procesadores" y así dificulta y alarga más el tiempo de ejecución, ya que estos estarán entregando mayor rendimeinto con un tamaño de caché al máximo.  
Es importante señalar que en mi caso, para todos los tipos de datos el tiempo de corrida fue similar, levemente los datos más pequeños fueron un poco más rápido, pero es de manera prácticamente imperceptible. Esto quiere decir que mi pc, para poder correr datos de half utiliza varios de estos "mini procesadores" y con la capacidad de los caché si no es al máximo, muy cercano, en el caso de un dato más grande como longdouble, probablemente este usando todo los recursos.  
Por último, para el caso de la memoria, al tener una gran cantidad y con mucho desuso no significó un gran problema para todos los tipos de datos, sin embargo con datos pequeños esta trabajo leve e imperciptiblemente menos que con datos más grandes.

# Desempeño de SOLVE y EIGH

Se realizaron 4 archivos .py (uno para todos los puntos del caso A, otro para todos los puntos del caso B y esto por cada tipo de dato), además de estos se obtuvieron 4 archivos .txt los cuales por línea contienen los subcasos de A y B, pero solo los valores promedios de las 10 corridas por subcaso (son del tipo [[Ns],[dts]]).    

A continuación se muestra una tabla con los desempeños del procesador y la memoria por cada caso (subcaso) realizado.

| CASO | PROCESADOR (CPU) | MEMORIA (RAM) |
| ------------- | ------------- | ------------- |
| A.I (float) (```x = Am1 x b```) | ![A.I (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(float)/CPU%20CASO%20A.I%20(float).jpg)  | ![A.I (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(float)/MEMORIA%20CASO%20A.I%20(float).jpg) |
| A.II (float) (```scipy.linalg.solve``` by default) | ![A.II (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(float)/CPU%20CASO%20A.II%20(float).jpg)  | ![A.II (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(float)/MEMORIA%20CASO%20A.II%20(float).jpg) |
| A.III (float) (using ```assume_a='pos'```) | ![A.III (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(float)/CPU%20CASO%20A.III%20(float).jpg)  | ![A.III (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(float)/MEMORIA%20CASO%20A.III%20(float).jpg) |
| A.IV (float) (using ```assume_a='sym'```) | ![A.IV (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(float)/CPU%20CASO%20A.IV%20(float).jpg)  | ![A.IV (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(float)/MEMORIA%20CASO%20A.IV%20(float).jpg) |
| A.V (float) (using ```overwrite_a=True```) | ![A.V (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(float)/CPU%20CASO%20A.V%20(float).jpg)  | ![A.V (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(float)/MEMORIA%20CASO%20A.V%20(float).jpg) |
| A.VI (float) (using ```overwrite_b=True```) | ![A.VI (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(float)/CPU%20CASO%20A.VI%20(float).jpg)  | ![A.VI (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(float)/MEMORIA%20CASO%20A.VI%20(float).jpg) |
| A.VII (float) (using ```overwrite_a=True``` and ```overwrite_b=True```| ![A.VII (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(float)/CPU%20CASO%20A.VII%20(float).jpg)  | ![A.VII (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(float)/MEMORIA%20CASO%20A.VII%20(float).jpg) |
| A.I (double) (```x = Am1 x b```) | ![A.I (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(double)/CPU%20CASO%20A.I%20(double).jpg)  | ![A.I (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(double)/MEMORIA%20CASO%20A.I%20(double).jpg) |
| A.II (double) (```scipy.linalg.solve``` by default) | ![A.II (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(double)/CPU%20CASO%20A.II%20(double).jpg)  | ![A.II (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(double)/MEMORIA%20CASO%20A.II%20(double).jpg) |
| A.III (double) (using ```assume_a='pos'```) | ![A.III (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(double)/CPU%20CASO%20A.III%20(double).jpg)  | ![A.III (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(double)/MEMORIA%20CASO%20A.III%20(double).jpg) |
| A.IV (double) (using ```assume_a='sym'```) | ![A.IV (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(double)/CPU%20CASO%20A.IV%20(double).jpg)  | ![A.IV (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(double)/MEMORIA%20CASO%20A.IV%20(double).jpg) |
| A.V (double) (using ```overwrite_a=True```) | ![A.V (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(double)/CPU%20CASO%20A.V%20(double).jpg)  | ![A.V (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(double)/MEMORIA%20CASO%20A.V%20(double).jpg) |
| A.VI (double) (using ```overwrite_b=True```) | ![A.VI (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(double)/CPU%20CASO%20A.VI%20(double).jpg)  | ![A.VI (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(double)/MEMORIA%20CASO%20A.VI%20(double).jpg) |
| A.VII (double) (using ```overwrite_a=True``` and ```overwrite_b=True```| ![A.VII (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(double)/CPU%20CASO%20A.VII%20(double).jpg)  | ![A.VII (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20A%20(double)/MEMORIA%20CASO%20A.VII%20(double).jpg) |
| B.I (float) (```scipy.linalg.eigh``` by default) | ![B.I (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(float)/CPU%20CASO%20B.I%20(float).jpg) | ![B.I (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(float)/MEMORIA%20CASO%20B.I%20(float).jpg) |
| B.II.1 (float) (```driver='ev'``` and ```overwrite_a=False```) | ![B.II.1 (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(float)/CPU%20CASO%20B.II.1%20(float).jpg) | ![B.II.1 (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(float)/MEMORIA%20CASO%20B.II.1%20(float).jpg) |
| B.II.2 (float) (```driver='ev'``` and ```overwrite_a=True```) | ![B.II.2 (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(float)/CPU%20CASO%20B.II.2%20(float).jpg) | ![B.II.2 (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(float)/MEMORIA%20CASO%20B.II.2%20(float).jpg) |
| B.III.1 (float) (```driver='evd'``` and ```overwrite_a=False```) | ![B.III.1 (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(float)/CPU%20CASO%20B.III.1%20(float).jpg) | ![B.III.1 (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(float)/MEMORIA%20CASO%20B.III.1%20(float).jpg) |
| B.III.2 (float) (```driver='evd'``` and ```overwrite_a=True```) | ![B.III.2 (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(float)/CPU%20CASO%20B.III.2%20(float).jpg) | ![B.III.2 (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(float)/MEMORIA%20CASO%20B.III.2%20(float).jpg) |
| B.VI.1 (float) (```driver='evr'``` and ```overwrite_a=False```) | ![B.IV.1 (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(float)/CPU%20CASO%20B.IV.1%20(float).jpg) | ![B.IV.1 (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(float)/MEMORIA%20CASO%20B.IV.1%20(float).jpg) |
| B.VI.2 (float) (```driver='evr'``` and ```overwrite_a=True```) | ![B.IV.2 (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(float)/CPU%20CASO%20B.IV.2%20(float).jpg) | ![B.IV.2 (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(float)/MEMORIA%20CASO%20B.IV.2%20(float).jpg) |
| B.V.1 (float) (```driver='evx'``` and ```overwrite_a=False```) | ![B.V.1 (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(float)/CPU%20CASO%20B.V.1%20(float).jpg) | ![B.V.1 (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(float)/MEMORIA%20CASO%20B.V.1%20(float).jpg) |
| B.V.2 (float) (```driver='evx'``` and ```overwrite_a=True```) | ![B.V.2 (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(float)/CPU%20CASO%20B.V.2%20(float).jpg) | ![B.V.2 (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(float)/MEMORIA%20CASO%20B.V.2%20(float).jpg) |
| B.I (double) (```scipy.linalg.eigh``` by default) | ![B.I (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(double)/CPU%20CASO%20B.I%20(double).JPG) | ![B.I (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(double)/MEMORIA%20CASO%20B.I%20(double).JPG) |
| B.II.1 (double) (```driver='ev'``` and ```overwrite_a=False```) | ![B.II.1 (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(double)/CPU%20CASO%20B.II.1%20(double).JPG) | ![B.II.1 (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(double)/MEMORIA%20CASO%20B.II.1%20(double).JPG) |
| B.II.2 (double) (```driver='ev'``` and ```overwrite_a=True```) | ![B.II.2 (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(double)/CPU%20CASO%20B.II.2%20(double).JPG) | ![B.II.2 (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(double)/MEMORIA%20CASO%20B.II.2%20(double).JPG) |
| B.III.1 (double) (```driver='evd'``` and ```overwrite_a=False```) | ![B.III.1 (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(double)/CPU%20CASO%20B.III.1%20(double).JPG) | ![B.III.1 (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(double)/MEMORIA%20CASO%20B.III.1%20(double).JPG) |
| B.III.2 (double) (```driver='evd'``` and ```overwrite_a=True```) | ![B.III.2 (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(double)/CPU%20CASO%20B.III.2%20(double).JPG) | ![B.III.2 (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(double)/MEMORIA%20CASO%20B.III.2%20(double).JPG) |
| B.IV.1 (double) (```driver='evr'``` and ```overwrite_a=False```) | ![B.IV.1 (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(double)/CPU%20CASO%20B.IV.1%20(double).JPG) | ![B.IV.1 (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(double)/MEMORIA%20CASO%20B.IV.1%20(double).JPG) |
| B.IV.2 (double) (```driver='evr'``` and ```overwrite_a=True```) | ![B.IV.2 (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(double)/CPU%20CASO%20B.IV.2%20(double).JPG) | ![B.IV.2 (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(double)/MEMORIA%20CASO%20B.IV.2%20(double).JPG) |
| B.V.1 (double) (```driver='evx'``` and ```overwrite_a=False```) | ![B.V.1 (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(double)/CPU%20CASO%20B.V.1%20(double).JPG) | ![B.V.1 (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(double)/MEMORIA%20CASO%20B.V.1%20(double).JPG) |
| B.V.2 (double) (```driver='evx'``` and ```overwrite_a=True```) | ![B.V.2 (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(double)/CPU%20CASO%20B.V.2%20(double).JPG) | ![B.V.2 (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Fotos%20Caso%20B%20(double)/MEMORIA%20CASO%20B.V.2%20(double).JPG) |  

Se puede evidenciar que en general en las corridas el procesadro alcanza su máximo en los puntos con mayores valores de N, y es en esos casos que la memoria ram tiende a subir un poco, para ayudar a procesar la información. Otro aspecto interesante a señalar, que para el caso B opción II y V el procesador no usaba en promedio ni el 50% y la memoria nunca se vio afectada, lo curioso es que estos casos fueron los que más tiempo demoraron en ejecutarse (esto explica mejor su tiempo de duración ya que al utilizar menos recursos su tiempo de realización es más lento, quizas esto puede deberse a que la operación no tenía una dificultad tan grande pero si un proceso extenso).  

A continuación se muestran los gráficos encontrados:

| **CASO A (float)** | **CASO A (double)** |
| ------------- | ------------- |
| ![A (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Comparaci%C3%B3n%20Caso%20A%20(float).png) | ![A (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Comparaci%C3%B3n%20Caso%20A%20(double).png) |

| **CASO B (float)** | **CASO B (double)** |
| ------------- | ------------- |
| ![B (float)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Comparaci%C3%B3n%20Caso%20B%20(float).png) | ![B (double)](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%204/Comparaci%C3%B3n%20Caso%20B%20(double).png) |  

De los gráficos para el caso A, se puede apreciar que son muy similares entre ellos, casi no hay diferencias, y si las hay no tienen un claro patrón hasta el final (es decir hasta los valores más grandes de N), queda claro que la opción de calcular la inversa y luego multiplicar esta por la matriz b es la manera más lenta de realizar la operación, mientrás que la más rápida es utilizando scipy.linalg.solve asumiento una matriz A positiva (```assume_a='pos'```). Es importante señalar que los resultados entre el caso A usando datos de tipo float vs usando datos de tipo double son prácticamente idénticos.  

Por otro lado, observando lo ocurrido en el caso B, se puede apreciar que si existen mayores diferencias entre las diferentes opciones, en donde las opciones II.1, II.2, V.1 y V.2 (```driver='ev y driver=evx```) son evidentemente más lentas, mientras que todas las demás tienen tiempos prácticamente iguales obteniendo un mejor rendimiento. Al igual que el caso anterior, la diferencia entre el tipo de dato double y float es prácticamente imperceptible.  


### Preguntas  

* **Haga un comentario completo respecto de todo lo que ve en términos de desempeño en cada problema.**  

Tal como se menciona antes se puede apreciar como en el caso A son todos los casos muy parecidos, siendo el método de utilizar la inversa el más lento, mientras que el más rápido es asumiendo que la matriz A es positiva.  
Para el caso B, usar ```driver='ev y driver=ev``` relentizan considerablemente el proceso, mientras que los demás trabajan de manera más eficiente.  
(Más comentarios debajo de los gráficos...).  

* **¿Como es la variabilidad del tiempo de ejecucion para cada algoritmo?**  

En el caso A se puede evidenciar que no hay tanta variabilidad de tiempo, pero que para valores de N entre aproximandamente 60 y 220 el caso más optimo será asumir una matriz A simétrica, mientras que para los todos los demás casos de N (menores y mayores), el tiempo de ejecución de usar scipy.linalg.solve asumiento una matriz positiva es mejor.  
Para el caso B utilizando scipy.linalg.eigh, claramente hay una diferencia notable de tiempo entre los subcasos con ```driver='ev y driver=evx```, los cuales serán siempre más lentos, mientras que todos los demás casos tienen un comportamiento casi identico con un tiempo de ejecución considerablemente mejor.  

Cabe agregar que el método scipy.linal.solve es evidentemente más rápido que scipy.linalg.eigh.  

* **¿Qué algoritmo gana (en promedio) en cada caso?**  

En el caso A en promedio el algoritmo más rápido es scipy.linalg.solve(assume_a='pos').  
En el caso B en promedio el algoritmo más rápido es scipy.linalg.eigh(driver="evd", overwrite_a=True) --> Es levemente más rápido, prácticamente imperceptible.  

* **¿Depende del tamaño de la matriz?**  

Para el caso A, si es influyente el tamaño de la matriz, porque como ya mencioné antes el subcaso IV tiene mejor rendimiento que cualquiera con matrices de tamaño entre 60<N<220.  
Para el caso B, el porte de la matriz no es un factor influyente, siempre existe el mismo comportamiento (si hay diferencias es prácticamente imperceptible).  

* **¿A que se puede deber la superioridad de cada opción?**  

La superioridad de cada opción tanto en el caso A como en el caso B, se debe plenamente a los paquetes y el proceso que reliza "por detrás" los diferentes métodos con sus diferentes parámetros. Por ejemplo, si se utiliza un argumento overwrite_a=True, se utilizarían menos recursos, ya que no se esta creando una nueva matriz, sino que se está reescribiendo la misma, otros ejemplos podrían ser que al asumirla de un tipo (positiva o simétrica), en donde el cálculo es más fácil, y el paquete al estar informado, realiza "trucos" de resolución más óptimos.  

* **¿Su computador usa más de un proceso por cada corrida?**  

Tal como se evidencia en las imagenes del procesador, este utiliza los 8 procesadores lógicos para la mayoria de los casos, hay un par de excepciones en donde utiliza 2 al máximo y los demás en mitad del rendimiento, pero en estricto rigor siempre esta utilizando cerca del 100% de la memoria de la CPU en los casos con N altos. Que el computador utilice más de un proceso significa que esta realizando muchas acciones diferentes simultaneamente y esto viene definido en parte por el computador (por que decide usar), pero también por las librerías y paquetes que se utilicen, los cuales puden requerir de hacer varias acciones en simultáneo para hacerlas de manera más eficiente.  

* **¿Que hay del uso de memoria (como crece)?**  

En mi caso, la memoria se vio muy poco afectada, ya que mi procesador es bastante potente, solo cambiaba levemente cuando el procesador sobrepasaba el 100% de su rendimiento, y cuando lo hacía de todas maneras lo que cambiaba la memoria era muy poco. Probablemente esto haya ocurrido para los valores de N que eran más grandes.  
Todo lo anteriormente señalado, ocurre por la jerarquización de la memoria en los computadores.  

# Matrices dispersas y complejidad computacional

Se realizó un archivo .py, el cual desarrollaba la operación MATMUL tanto con matrices llenas como con dispersas, se puede notar que tanto el tiempo de ensamblaje de matrices laplacianas, tanto como resolver la operación, era infinitamente más rápido usando matrices dispersas, es más, para poder notar el gráfico, para las matrices dispersas se tuvo que utilizas un Nmax = 1.000.000.  

### Ensamblaje

Para realizar el ensamblaje tanto de las matrices dispersas como de las llenas, se definieron las siguientes funciones para poder desarrollarlas:  

**Función Laplaciana Matrices Llenas**
```python
def matriz_laplaciana_llena(N, dtype):
	A = zeros((N,N), dtype = dtype)
	for i in range(N):
		A[i,i] = 2
		for j in range(max(0,i-2),i):
			if abs(i - j) == 1:
				A[i,j] = -1
				A[j,i] = -1
	return A  
```  

**Función Laplaciana Matrices Dispersas**
```python
def matriz_laplaciana_dispersa(N, dtype):
	return 2*sparse.eye(N, dtype = dtype) - sparse.eye(N, N, 1, dtype = dtype) - sparse.eye(N, N, -1, dtype = dtype)
```                            
   
Para las matrices llenas no se pudo utilizar el método eye, ya que para el tipo de dato double no lo soportaba, mientras que para el caso de matrices dispersas si.  

### Solución

Para la solución simplemente se uso el método matmul (@), pero es importante para el caso de las matrices dispersas antes de realizar la operación, tanto las matrices A como B se transformaron a una matriz de tipo CSR.  

### Gráficos

A continuación se muestran los gráficos encontrados:  

| **Gráfico Caso Matrices Llenas** | **Gráfico Caso Matrices Dispersas** |
| ------------- | ------------- |
| ![Matrices Llenas](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%205/Desempe%C3%B1o%20MATMUL%20Matrices%20Llenas.png) | ![Matrices Dispersas](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%205/Desempe%C3%B1o%20MATMUL%20Matrices%20Dispersas.png) |  

Es importante descatacar que para poder desarrollar los gráficos representativos de complejidad computacional, se tuvo que trabajar pensando que se tenia un gráfico doblemente logarítmico, es decir del tipo ![Eq1](https://latex.codecogs.com/png.latex?%5Cinline%20log%28y%29%20%3D%20k%20%5Ccdot%20log%28x%29%20&plus;%20log%28a%29) que otra manera de representarlo sería ![Eq2](https://latex.codecogs.com/png.latex?%5Cinline%20y%20%3D%20a%20%5Ccdot%20x%5E%7Bk%7D). De esta manera de despejan los distintos niveles de complejidad, ya que se conoce un punto (el máximo) y su pendiente, quedando de la siguiente manera: ![Eq3](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cdisplaystyle%20%5Cfrac%7By_%7Bmax%7D%7D%7BN_%7Bmax%7D%5E%7Bk%7D%7D%20%5Ccdot%20N_%7Bvalues%7D%5E%7Bk%7D).  

Luego se puede interpretar como para el caso de las matrices llenas para el caso del ensamblaje tiene un nivel de complejidad máxima de ![n2](https://latex.codecogs.com/png.latex?%5Cinline%20O%28N%5E%7B2%7D%29) y para la solución de MATMUL en la parte final casi de ![n4](https://latex.codecogs.com/png.latex?%5Cinline%20O%28N%5E%7B4%7D%29).  
Para el caso de las matrices dispersas tuvieron que agregarse más valores ya que osino no se podía ver que hubiera una complejidad dada. Finalmente se puede notar que para el ensamblaje existe una complejidad máxima de ![n2](https://latex.codecogs.com/png.latex?%5Cinline%20O%28N%5E%7B2%7D%29) y para el caso de la solución de ![n2](https://latex.codecogs.com/png.latex?%5Cinline%20O%28N%5E%7B2%7D%29).  

# Matrices dispersas y complejidad computacional (parte 2)  

Para esta entrega se realizaron 4 archivos .py, los cuales corresponden a los dos métodos a utilizar para matrices llenas y para dispersas. Para las matrices llenas se optó por usar las versiones más eficientes utilizando así el método de la inversa (caso con ```overwrite_a=True```) y de solve (```assume_a='pos'```), para así compararlo con las matrices dispersas, que en todo caso, siempre lograron una mejor eficiencia.  

### Solución  

**Inversa:** Para la solución simplemente se uso el método inv de scipy.linalg, pero es importante que para el caso de las matrices dispersas antes de realizar la operación, la matriz 'A' es necesaria tranformarla al tipo CSC, ya que de está manera el método consigue la mejor eficiencia.  
**Solve:** Al igual que en el caso pasado, para el caso de matrices llenas se utilizo el método solve de scipy.linalg, mientras que para las matrices dispersas se utilizó el método spsolve de scipy.sparse.linalg, en donde la matriz 'A' (laplaciana) es transformada al tipo CSR, mientras que la matriz 'b', al ser una matriz compuesta de solo unos, no es necesario realizar ningún tipo de transformación.  

### Gráficos  

A continuación se muestran los gráficos encontrados:  

#### **CASO INVERSA**  

| **Gráfico Caso Matrices Llenas (```overwrite_a=True```)** | **Gráfico Caso Matrices Dispersas** |
| ------------- | ------------- |
| ![Matrices Llenas INV](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%206/Desempe%C3%B1o%20INV%20Matrices%20Llenas.png) | ![Matrices Dispersas INV](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%206/Desempe%C3%B1o%20INV%20Matrices%20Dispersas.png) |  

	
#### **CASO SOLVE**  

| **Gráfico Caso Matrices Llenas (```assume_a='pos'```)** | **Gráfico Caso Matrices Dispersas** |
| ------------- | ------------- |
| ![Matrices Llenas SOLVE](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%206/Desempe%C3%B1o%20SOLVE%20Matrices%20Llenas.png) | ![Matrices Dispersas SOLVE](https://github.com/RobertoVergaraC/MCOC2021-P0/blob/main/Entrega%206/Desempe%C3%B1o%20SOLVE%20Matrices%20Dispersas.png) |  

### Ensamblaje Laplaciana  
	
**Función Laplaciana Matrices Llenas**  
```python
def laplaciana(N, dtype):
	A = zeros((N,N), dtype = dtype)
	for i in range(N):
		A[i,i] = 2
		for j in range(max(0,i-2),i):
			if abs(i - j) == 1:
				A[i,j] = -1
				A[j,i] = -1
	return A
```  

**Función Laplaciana Matrices Dispersas**  
```python
def laplaciana(N, dtype):
	return 2*sp.eye(N, dtype = dtype) - sp.eye(N, N, 1, dtype = dtype) - sp.eye(N, N, -1, dtype = dtype)
```   

* **Comente cómo esta elección se ve reflejada en el desempeño y complejidad algorítmica mostrada.**  
En primer lugar, se puede notar como en el caso de la laplaciana de matrices dispersas el rendimiento es mucho mejor, esto puede deberse principalmente a dos factores:  
1.- El uso de la función 'eye' es mucho más eficiente que reemplazar lso elementos de una lista (caso laplaciana dispersas vs caso laplaciana llenas).  
2.- Utilizar el método scipy.sparse procesa los datos mucho más rápido.  
Debido a todo lo aprendido se puede deducir que en general la opción 2 será más siginficante, ya que matrices dispersas son mucho más eficientes que las llenas.  
Cabe señalar que la manera de almacenar los datos de las matrices llenas, tal como indica el nombre, es guardando toda la información y por ende al momento de realizar oepraciones, muchos procesos que realiza son reiterativos e innecesarios, al contrario de las matrices dispersas que solo guarda los valores importantes y los demás los da conocidos por teória (guarda los numeros y los 0 no, por lo que por ejemplo multiplicaciones por 0 no los toma en consideración). Por lo anteriormente señalado, lógicamente, la manera que trabaja scipy.sparse vs scipy será mucho más eficiente obteniendo un rendimeinto mucho mejor (sobretodo en una matriz laplaciana la cual contiene muchos '0').  
Por último, podemos argumentar que la complejidad algorítmica mostrada es directamente proporcional al valor de N, pero utilizando un mismo valor de N, las matrices llenas tienen una complejidad mayor a las de las dispersas. Para obtener la misma complejidad entre estos dos tipos de matrices se necesita un valor de N muy superior en el caso de las matrices dispersas para poder igualar la complejidad de las matrices llenas.

### Preguntas

* **Comente las diferencias que ve en el comportamiento de los algoritmos en el caso de matrices llenas y dispersas.**  

* **¿Cual parece la complejidad asintótica (para N→∞)  para el ensamblado y solución en ambos casos y porqué?**  

* **¿Como afecta el tamaño de las matrices al comportamiento aparente?**  

* **¿Qué tan estables son las corridas (se parecen todas entre si siempre, nunca, en un rango)?**  
