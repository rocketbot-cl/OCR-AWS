# OCR AWS
  
Module to apply OCR on an image file  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

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

## Overview


1. OCR AWS convert image file  
Extract text from image file.

2. OCR AWS Table to CSV  
Extract text and saves it in a CSV file  




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