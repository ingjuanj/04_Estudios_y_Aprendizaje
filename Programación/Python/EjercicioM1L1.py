#La empresa tiene 5000 GB de almacenamiento de datos. El tamaño de un archivo es de 256 GB.
#La empresa recibió 20 archivos para almacenamiento no puede contener todos los datos.
#¿Cuántos archivos se pueden colocar en el almacenamiento?
#¿Cuánto espacio libre quedará?

#Escriba un programa que realice los cálculos. Dé estilos a la respuestas como se muresta en la imagen.

archivos = 20
almacenamiento_total = 5000  # en GB
tamano_archivo = 256

cantidad_archivos = almacenamiento_total // tamano_archivo  # cantidad de archivos que se pueden almacenar
quedaran = almacenamiento_total - cantidad_archivos*tamano_archivo

print('El almacenamiento puede contener', cantidad_archivos, 'archivos')
print('Quedarán', quedaran, 'GB restantes')