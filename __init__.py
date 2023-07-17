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

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'OCR-AWS' + os.sep + 'libs' + os.sep

cur_path_x64 = os.path.join(cur_path, 'Windows' + os.sep +  'x64' + os.sep)
cur_path_x86 = os.path.join(cur_path, 'Windows' + os.sep +  'x86' + os.sep)

if sys.maxsize > 2**32 and cur_path_x64 not in sys.path:
    sys.path.append(cur_path_x64)
elif sys.maxsize <= 2**32 and cur_path_x86 not in sys.path:
    sys.path.append(cur_path_x86)

import requests
import boto3
import csv

class Textract_AWS:
    def __init__(self, region, aws_access_key_id, aws_secret_access_key, path_):
        self.region = region
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.path_ = path_
    
    def get_rows_columns_map(self, table_result, blocks_map):
        rows = {}
        for relationship in table_result['Relationships']:
            if relationship['Type'] == 'CHILD':
                for child_id in relationship['Ids']:
                    cell = blocks_map[child_id]
                    if cell['BlockType'] == 'CELL':
                        row_index = cell['RowIndex']
                        col_index = cell['ColumnIndex']
                        if row_index not in rows:
                            # create new row
                            rows[row_index] = {}
                            
                        # get the text value
                        rows[row_index][col_index] = self.get_text(cell, blocks_map)
        return rows

    def get_text(self, result, blocks_map):
        text = ''
        if 'Relationships' in result:
            for relationship in result['Relationships']:
                if relationship['Type'] == 'CHILD':
                    for child_id in relationship['Ids']:
                        word = blocks_map[child_id]
                        if word['BlockType'] == 'WORD':
                            text += word['Text'] + ' '
                        if word['BlockType'] == 'SELECTION_ELEMENT':
                            if word['SelectionStatus'] =='SELECTED':
                                text +=  'X '    
        return text
    
    def get_table_csv_results(self, file_name):
        import boto3


        with open(file_name, 'rb') as file:
            img_test = file.read()
            bytes_test = bytearray(img_test)


        # process using image bytes
        # get the results

        client = boto3.client('textract', region_name = self.region, aws_access_key_id=self.aws_access_key_id, aws_secret_access_key=self.aws_secret_access_key)

        
        response = client.analyze_document(Document={'Bytes': bytes_test}, FeatureTypes=['TABLES'])

        # Get the text blocks
        blocks=response['Blocks']


        blocks_map = {}
        table_blocks = []
        for block in blocks:
            blocks_map[block['Id']] = block
            if block['BlockType'] == "TABLE":
                table_blocks.append(block)

        if len(table_blocks) <= 0:
            return "<b> NO Table FOUND </b>"

        csv = ''
        for index, table in enumerate(table_blocks):
            csv += self.generate_table_csv(table, blocks_map, index +1)
            csv += '\n\n'

        return csv
    
    def generate_table_csv(self, table_result, blocks_map, table_index):
        rows = self.get_rows_columns_map(table_result, blocks_map)

        table_id = 'Table_' + str(table_index)
        
        # get cells.
        csv = 'Table: {0}\n\n'.format(table_id)

        for row_index, cols in rows.items():
            
            for col_index, text in cols.items():
                csv += '{}'.format(text) + ","
            csv += '\n'
            
        csv += '\n\n\n'
        return csv
    
    def main(self, file_name):
        table_csv = self.get_table_csv_results(file_name)

        output_file = self.path_

        # replace content
        with open(output_file, "wt") as fout:
            fout.write(table_csv)

    

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
                    if len(row) > 3:
                        aws_access_key_id = row[2]
                        aws_secret_access_key = row[3]
                    else:
                        aws_access_key_id = row[0]
                        aws_secret_access_key = row[1]
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


        if result:
            if data_:
                response["textAnnotation"] = textAnnotation
                SetVar(result, response)
            else:
                SetVar(result, textAnnotation)
    except Exception as e:
        PrintException()
        raise e

if module == "GetCSV":
    image_path = GetParams("image_path")
    csv_path = GetParams("csv_path")
    region = GetParams("region")
    path_ = GetParams("path")
    
    path_ = path_.replace("\\", "/")
    
    try:
        if not region:
            region = "eu-west-1"
        
        
        with open(csv_path, newline='') as csvfile:
            credentials = csv.reader(csvfile, delimiter=',')
            position = 0
            for row in credentials:
                if position == 1:
                    if len(row) > 3:
                        aws_access_key_id = row[2]
                        aws_secret_access_key = row[3]
                    else:
                        aws_access_key_id = row[0]
                        aws_secret_access_key = row[1]
                position += 1
        
        
        csvv = Textract_AWS(region, aws_access_key_id, aws_secret_access_key, path_)
        
        csvv.main(image_path)
  
    except Exception as e:
        PrintException()
        raise e