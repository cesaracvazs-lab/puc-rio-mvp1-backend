# TODO adaptar README
Em ambos os repositórios deve existir um arquivo README.md contendo as seguintes
informações:

● Título e uma breve descrição do projeto;
● Instruções de Instalação, tais como:
    ○ descrever as etapas necessárias para que os usuários possam
    configurar o ambiente local,
    ○ instalar dependências,
    ○ comandos de inicialização, etc;
● Certifique-se de que o arquivo README.md seja formatado de forma clara e
use cabeçalhos, listas e formatação de texto para tornar a documentação fácil
de ler.


# Minha API

Este pequeno projeto faz parte do material diático da Disciplina **Desenvolvimento Full Stack Básico** 

O objetivo aqui é ilutsrar o conteúdo apresentado ao longo das três aulas da disciplina.

---
## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
