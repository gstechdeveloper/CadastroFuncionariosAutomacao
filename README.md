Automação de Cadastro de Funcionários

------

Este é um projeto de automação, o mesmo é para mostrar que é possível usar uma automação para preenchimento de formulários a partir de uma planilha excel CSV.

O exemplo utilizado foi usando o site SPA desenvolvido em Vue JS:

:globe_with_meridians: https://gstechdeveloper.github.io/CadastroFuncionarios/#/

------

:blue_book:: Pré-requisitos:

- Python 3.13.x instalado na máquina(https://www.python.org/downloads/release/python-3136/)

------

:play_or_pause_button:: Como rodar?

Windows:

Com o projeto na pasta, execute install.bat (Somente para windows). Após executar, basta executar o App.py que você conseguirá visualizar a automação em andamento.

MacOS/Linux:

Abra a pasta que está o projeto em um terminal e rode:

```bash
python3 -m venv .
```

Logo após rodar este comando ative o ambiente virtual com:

```bash
source bin/activate
```

Agora instale as dependências do projeto:

```bash
pip install -r requeriments.txt
```

Finalizando, rodamos o comando para instalar os drivers do playwright no computador:

```bash
playwright install
```

Após isso só executar o arquivo App.py que você conseguirá visualizar a automação.



Versão: 1.0

Developer: Gabriel Azevedo