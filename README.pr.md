# OCR AWS
  
Módulo para aplicar OCR em um arquivo de imagem  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

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

## Overview


1. OCR AWS converter imagem  
Extrair o texto de uma imagem.

2. OCR AWS Tabela para CSV  
Extrai texto e salva em um arquivo CSV.  




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