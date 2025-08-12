ECHO Criando o ambiente virtual...

python -m venv .

cls

ECHO Ativando ambiente virtual...
call Scripts\activate.bat

cls

ECHO Instalando os pacotes...
pip install -r requirements.txt

cls

ECHO Instalando o PlayWright...
playwright install