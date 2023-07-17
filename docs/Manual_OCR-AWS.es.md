# OCR AWS
  
Modulo para aplicar OCR sobre un archivo de imagen  

*Read this in other languages: [English](Manual_OCR-AWS.md), [Português](Manual_OCR-AWS.pr.md), [Español](Manual_OCR-AWS.es.md)*
  
![banner](imgs/Banner_OCR-AWS.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### OCR AWS convertir imagen
  
Extrae texto de una imagen.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Imagen||C:/Users/Usuario/Desktop/imagen.jpg|
|Ingrese csv con sus credenciales||Ingrese ruta del CSV con las credenciales|
|Datos extendidos||False|
|Ingrese la región||Ingrese la región|
|Resultado||{resultado}|

### OCR AWS Tabla a CSV
  
Extrae texto y lo guarda en un archivo CSV.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Imagen||C:/Users/Usuario/Folder/imagen.jpg|
|Ingrese csv con sus credenciales||Ingrese ruta del CSV con las credenciales|
|Ingrese la región||Ingrese la región|
|Ruta del archivo ||C:/User/Usuario/Folder/file.csv|
