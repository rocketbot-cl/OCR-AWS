



# OCR AWS
  
Module to apply OCR on an image file  

*Read this in other languages: [English](Manual_OCR-AWS.md), [Português](Manual_OCR-AWS.pr.md), [Español](Manual_OCR-AWS.es.md)*
  
![banner](imgs/Banner_OCR-AWS.png o jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

## Get AWS credentials
To be able to use this module it is necessary to have AWS credentials, to obtain them you must follow the following steps:
1. Go to https://console.aws.amazon.com/iam/home#/users
2. Select the user to be used. You must have textract:AnalyzeDocument permissions.
3. Get access credentials and secret key.
4. Create a CSV file with the credentials as follows:
```
User name, Password, Access key ID, Secret access key, Console login link
<user-name>,<password>,<access-key-id>,<secret-access-key>,https://<account-id>.signin.aws.amazon.com/console
```
5. Save the CSV file in a path accessible to the module.

## Description of the commands

### OCR AWS convert image file
  
Extract text from image file.
|Parameters|Description|example|
| --- | --- | --- |
|Image|Image File Path to convert|C:/Users/User/Desktop/image.jpg|
|Input csv with credentials|CSV Path with AWS credentials|Input CSV Path with credentials|
|Extended Data|Check if you want to extract extended data like textAnnotation|False|
|Input region|AWS region where the bucket is located|Input region|
|Result|Variable where the result of the extraction will be stored|result|

### OCR AWS Table to CSV
  
Extract text and saves it in a CSV file
|Parameters|Description|example|
| --- | --- | --- |
|Image|Image path to process|C:/Users/User/Folder/image.jpg|
|Input csv with credentials|CSV path with credentials|Input CSV Path with credentials|
|Input region|AWS region where the bucket is located|Input region|
|File path  |File path to create|C:/User/Usuario/Folder/file.csv|
