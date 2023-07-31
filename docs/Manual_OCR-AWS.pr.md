# OCR AWS
  
Módulo para aplicar OCR em um arquivo de imagem  

*Read this in other languages: [English](Manual_OCR-AWS.md), [Português](Manual_OCR-AWS.pr.md), [Español](Manual_OCR-AWS.es.md)*
  
![banner](imgs/Banner_OCR-AWS.png)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  

## Obter credenciais da AWS
Para poder usar este módulo, é necessário ter credenciais da AWS, para obtê-las, você deve seguir as seguintes etapas:
1. Acesse https://console.aws.amazon.com/iam/home#/users
2. Selecione o usuário que você vai usar. Você deve ter permissões de textract:AnalyzeDocument.
3. Obtenha as credenciais de acesso e chave secreta.
4. Crie um arquivo CSV com as credenciais da seguinte maneira:
```
User name, Password, Access key ID, Secret access key, Console login link
<user-name>,<password>,<access-key-id>,<secret-access-key>,https://<account-id>.signin.aws.amazon.com/console
```
5. Salve o arquivo CSV em um caminho acessível ao módulo.

## Descrição do comando

### OCR AWS converter imagem
  
Extrair o texto de uma imagem.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Imagem|Caminho do arquivo de imagem para converter|C:/Users/Usuário/Desktop/imagem.jpg|
|Insira o CSV com suas credenciais|Caminho do CSV com as credenciais da AWS|Insira o caminho do CSV com as credenciais|
|Dados estendidos|Marque se você quiser extrair dados estendidos como textAnnotation|False|
|Insira a região|Região da AWS onde o bucket está localizado|Insira a região|
|Resultado|Variável onde o resultado da extração será armazenado|resultado|

### OCR AWS Tabela para CSV
  
Extrai texto e salva em um arquivo CSV.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Imagem|Caminho da imagem a ser processada|C:/Users/Usuario/Folder/imagem.jpg|
|Insira o csv com suas credenciais|Caminho do CSV com as credenciais|Insira o caminho do CSV com as credenciais|
|Insira a região|Região da AWS onde o bucket está localizado|Insira a região|
|Caminho do arquivo |Caminho do arquivo a ser criado|C:/User/Usuario/Folder/file.csv|
