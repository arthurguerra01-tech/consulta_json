# Projeto_Desenvolvimento_Web
Projeto de desenvolvimento de aplicação da disciplina de Programas de Desenvolvimento WEB (1° Semestre) / 2025

O presente Projeto de aplicação consiste na criação de uma aplicação FullStack na qual permite ao usuário Administrador criar cadastros para médicos bem como suas
especialidades. Ademais, outra funcionalidade da aplicação permite um Usuário se cadastrar através de Nome e CPF , selecionar o médico e especialidade desejada, escolher
a data e horário da consulta bem como excluir esse agendamento.

# Acessando os Arquivos do repositório

Opção 01
1. Realizar o Download (Arquivo.rar) desse repositório;
2. Após o Download descompactar esse arquivo em uma pasta de preferência;
3. Abrir Algum editor de código, no caso dessa aplicação , fora utilizado o programa nativo do Windows,
VS CODE;
4. Ao abrir o Editor selecionar a opção Open Folder e abrir a pasta com o Repositório no Ambiente de desenvolvimento.

# Configuração do Ambiente do editor de Código
No terminal do VS CODE Será necessário criar uma máquina virtual e instalar as dependências (Biliotecas Python)

1. Para acessar a pasta, insira no Terminal :
```
 cd (nome_da_sua_pasta)
```
3. Após acessada , inicie um ambiente virtual :
 ```
 python3 -m venv venv
```
3. Para iniciar o ambiente virtual :
```
source ./venv/bin/activate
```
5. Para instalar as dependências da aplicação :
```
 pip install -r requirements.txt
```
# Configuração para acessar o Servidor e ativar o Banco de dados Padrão do DJANGO(SQlite)
1. Ativando o banco de dados : *SOMENTE PARA PROJETO SQLITE
```
python manage.py makemigrations
python manage.py migrate
```
3. Criando o usuário Admin : *SOMENTE PARA PROJETO SQLITE
```
python manage.py createsuperuser 
```
5. Inserir nome , email e senha (Criar uma nova) *SOMENTE PARA PROJETO SQLITE
6. Iniciando o Servidor : 
```
python manage.py runserver
```
8. O domínio para acesso da aplicação será :
```
http://127.0.0.1:8000/
http://127.0.0.1:8000/admin-panel/ (PARA ARQUIVO JSON)
```
9. Para desligar o Servidor após o uso :
```
ctrl + c (No terminal da aplicação)
```
