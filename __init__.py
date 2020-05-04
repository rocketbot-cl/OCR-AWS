# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import sys
base_path  = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'OCR-AWS' + os.sep + 'libs' + os.sep
sys.path.append(cur_path )

import requests
import boto3
import csv

module = GetParams("module")

if module == "GetOCR":
    image_path = GetParams("image_path")
    csv_path = GetParams("csv_path")
    data_ = GetParams("data")
    region = GetParams("region")
    result = GetParams("result")

    if not region:
        region = "eu-west-1"


    

    try:
        with open(csv_path, newline='') as csvfile:
            credentials = csv.reader(csvfile, delimiter=',')
            position = 0
            for row in credentials:
                if position == 1:
                    aws_access_key_id = row[2]
                    aws_secret_access_key = row[3]
                position += 1


        # Read document content
        with open(image_path, 'rb') as document:
            imageBytes = bytearray(document.read())

        # Amazon Textract client
        textract = boto3.client('textract', region_name = region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

        # Call Amazon Textract
        response = textract.detect_document_text(Document={'Bytes': imageBytes})
        textAnnotation = ""
        for item in response["Blocks"]:
            if item["BlockType"] == "LINE":
                textAnnotation += item["Text"] +"\n"
        print(data_)

        if result:
            if data_:
                response["textAnnotation"] = textAnnotation
                SetVar(result, response)
            else:
                SetVar(result, textAnnotation)
    except Exception as e:
        PrintException()
        raise e
