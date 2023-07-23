# Django - Aprendendo Autenticação

 Este repositório contém um projeto Django em que estou aprendendo sobre autenticação no Django. Aqui, vou compartilhar meus conhecimentos sobre como configurar a autenticação de usuários em uma aplicação Django usando o Django REST framework.

## Pré-requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas em seu ambiente de desenvolvimento:

- Python
- Django
- Django REST framework

## Criar Ambiente Virtual
``` py -m venv <nome-do-seu-ambiente>  ```

## Configuração do Ambiente Virtual

- Para começar, ative seu ambiente virtual usando o seguinte comando:

```
<name-do-seu-ambiente>\Scripts\activate
```
## Instalação das Dependências
- Instale as dependências necessárias para este projeto usando os seguintes comandos:
```
pip install markdown -opcional
pip install django-filter -opcional
pip install djangorestframework
```
## Iniciando o Projeto
- Primeiro, crie um novo projeto Django usando o seguinte comando:
```
django-admin startproject main
cd main
```
### Em seguida, crie um novo aplicativo dentro do projeto:
```
manage.py startapp app
```
## Para registrar sua pasta app coloque isto dentro da pasta ```settings.py ```

```
INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    :
    'rest_framework',
    'app',
    :

]
```

### Contribuição
Se você quiser contribuir para este projeto, sinta-se à vontade para fazer um fork do repositório e enviar um pull request com suas melhorias.

### Licença
Este projeto é licenciado sob a MIT License.
