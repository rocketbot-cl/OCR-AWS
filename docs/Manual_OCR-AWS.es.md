# OCR AWS
  
Modulo para aplicar OCR sobre un archivo de imagen  

*Read this in other languages: [English](Manual_OCR-AWS.md), [Português](Manual_OCR-AWS.pr.md), [Español](Manual_OCR-AWS.es.md)*
  
![banner](imgs/Banner_OCR-AWS.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  

## Obtener credenciales de AWS
Para poder utilizar este módulo es necesario contar con credenciales de AWS, para obtenerlas se debe seguir los siguientes pasos:
1. Ingresar a https://console.aws.amazon.com/iam/home#/users
2. Seleccionar el usuario que se va a utilizar. Debe contar con permisos de textract:AnalyzeDocument.
3. Obtener las credenciales de acceso y secret key.
4. Crear un archivo CSV con las credenciales de la siguiente manera:
```
User name, Password, Access key ID, Secret access key, Console login link
<user-name>,<password>,<access-key-id>,<secret-access-key>,https://<account-id>.signin.aws.amazon.com/console
```
5. Guardar el archivo CSV en una ruta accesible para el módulo.

## Descripción de los comandos

### OCR AWS convertir imagen
  
Extrae texto de una imagen.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Imagen|Ruta de la imagen a convertir|C:/Users/Usuario/Desktop/imagen.jpg|
|Ingrese csv con sus credenciales|Ruta del CSV con las credenciales de AWS|Ingrese ruta del CSV con las credenciales|
|Datos extendidos|Marcar en caso de que se quiera extraer datos extendidos como textAnnotation|False|
|Ingrese la región|Región de AWS donde se encuentra el bucket|Ingrese la región|
|Resultado|Variable donde se almacenará el resultado de la extracción|resultado|

### OCR AWS Tabla a CSV
  
Extrae texto y lo guarda en un archivo CSV.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Imagen|Ruta de la imagen a procesar|C:/Users/Usuario/Folder/imagen.jpg|
|Ingrese csv con sus credenciales|Ruta del CSV con las credenciales|Ingrese ruta del CSV con las credenciales|
|Ingrese la región|Región de AWS donde se encuentra el bucket|Ingrese la región|
|Ruta del archivo |Ruta del archivo a crear|C:/User/Usuario/Folder/file.csv|
