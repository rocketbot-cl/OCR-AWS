# OCR AWS
  
Module to apply OCR on an image file  

*Read this in other languages: [English](Manual_OCR-AWS.md), [Português](Manual_OCR-AWS.pr.md), [Español](Manual_OCR-AWS.es.md)*
  
![banner](imgs/Banner_OCR-AWS.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### OCR AWS convert image file
  
Extract text from image file.
|Parameters|Description|example|
| --- | --- | --- |
|Image||C:/Users/User/Desktop/image.jpg|
|Input csv with credentials||Input CSV Path with credentials|
|Extended Data||False|
|Input region||Input region|
|Result||{result}|

### OCR AWS Table to CSV
  
Extract text and saves it in a CSV file
|Parameters|Description|example|
| --- | --- | --- |
|Image||C:/Users/User/Folder/image.jpg|
|Input csv with credentials||Input CSV Path with credentials|
|Input region||Input region|
|File path  ||C:/User/Usuario/Folder/file.csv|
