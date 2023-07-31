# OCR AWS
  
Modulo para aplicar OCR sobre un archivo de imagen  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

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



## Overview


1. OCR AWS convertir imagen  
Extrae texto de una imagen.

2. OCR AWS Tabla a CSV  
Extrae texto y lo guarda en un archivo CSV.  




----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**boto3**](https://pypi.org/project/boto3/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)