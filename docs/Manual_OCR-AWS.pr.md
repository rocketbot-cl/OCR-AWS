# OCR AWS
  
Módulo para aplicar OCR em um arquivo de imagem  

*Read this in other languages: [English](Manual_OCR-AWS.md), [Português](Manual_OCR-AWS.pr.md), [Español](Manual_OCR-AWS.es.md)*
  
![banner](imgs/Banner_OCR-AWS.png)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### OCR AWS converter imagem
  
Extrair o texto de uma imagem.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Imagem||C:/Users/Usuário/Desktop/imagem.jpg|
|Insira o CSV com suas credenciais||Insira o caminho do CSV com as credenciais|
|Dados estendidos||False|
|Insira a região||Insira a região|
|Resultado||{resultado}|

### OCR AWS Tabela para CSV
  
Extrai texto e salva em um arquivo CSV.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Imagem||C:/Users/Usuario/Folder/imagem.jpg|
|Insira o csv com suas credenciais||Insira o caminho do CSV com as credenciais|
|Insira a região||Insira a região|
|Caminho do arquivo ||C:/User/Usuario/Folder/file.csv|
