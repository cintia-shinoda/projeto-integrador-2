# Projeto Integrador em Computação II

## Alunos

- Cintia Izumi Shinoda, 2210847 
- Cristiano Gois de Araújo, 2106038 
- Fernando Miguel Escribano Martinez, 2216189 
- Pedro Henrique Faria Cruz, 2202072 
- Rogério Gonçalves da Silva, 2231346 
- Willy Paulino de Oliveira Gomes, 2221112



## Tema do PI
Desenvolver um software com **framework web** que utilize **banco de dados**, inclua Script Web (**JavaScript**), **nuvem**, uso de **API**, **acessibilidade**, **controle de versão** e **testes**. Opcionalmente incluir análise de dados.



## Descrição do Projeto
Landing Page



## Tecnologias Utilizadas
- Back-End: Python (Django)
- Front-End: JavaScript (React)
- Banco de Dados (SQLite)



## Estrutura do Projeto

```bash
├── backend/
│   ├── backend/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │
│   ├── vouchers/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── views.py
│   │
│   ├── db.sqlite3
│   ├── manage.py
│
├── venv/
│
├── README.md
```



## Instalação, Configuração e Execução

### 0. Certificar-se de ter Python 3 instalado
para verificar a versão do Python:
#### MacOS/Linux
```bash
python3 --version
```

#### Windows
```bash
python -version
```
<br>


### 1. Clonar o projeto do GitHub
```bash
git clone <https://github.com/cintia-shinoda/projeto-integrador-2.git>

cd projeto-integrador-2
```
<br>


### 2. Criar o ambiente virtual
#### MacOS/Linux
```bash
python3 -m venv venv
```

#### Windows
```bash
python -m venv venv
```
<br>


### 3. Ativar o ambiente virtual
#### MacOS/Linux
```bash
source venv/bin/activate
```

#### Windows
```bash
venv\Scripts\activate
```
<br>


### 4. Instalar as dependências
```bash
pip install -r requirements.txt
```
<br>


### 5. Executar
```bash
cd backend
# python3 manage.py migrate
python3 manage.py runserver
```