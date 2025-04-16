## 👂 Sistema de Ouvidoria de Caio

**Esse é um sistema básico de ouvidoria programado em **Python** com integração ao **MySQL**. Ele permite que usuários registrem, consultem e removam manifestações categorizadas por tipo como reclamações, elogios e sugestões diretamente pelo terminal.**

---

## 📋 Funcionalidades

- 📋 *Listagem de todas as manifestações*
- 🔍 *Listagem por tipo (Reclamação, Elogio ou Sugestão)*
- ✍️ *Adicionar nova manifestação*
- 📊 *Exibir quantidade total de manifestações*
- 🔢 *Pesquisar manifestação pelo código*
- ❌ *Remover manifestação por código*
- 🚪 *Sair do sistema*

---

## 💾 Pré-requisitos

- *Linguagem de programação* **Python** 
- *MySQL Server*
- *Pacote* `mysql-connector-python`
---

## ⚙️ Estrutura do Banco de Dados
**Antes de rodar o programa, crie o banco e a tabela no MySQL:**
```SQL
CREATE DATABASE ouvidoriabd;
    
USE ouvidoriabd;
    
CREATE TABLE Manifestacoes( 
  codigo INT AUTO_INCREMENT,
  nome VARCHAR(100),
  manifestacao VARCHAR(150),
  tipo VARCHAR(20),
  ouvidor VARCHAR(100) DEFAULT 'SeuNome',
  PRIMARY KEY(codigo)
);
```
---
## 📁 Estrutura do Projeto:
***├── main.py***
**Código principal com o código do sistema**

***├── menu.py***
**Arquivo com todos os métodos e o menu**

***├── operacoesbd.py***
**Funções de conexão e manipulação do banco**
***├── README.md***
**Esse arquivo**

---
## ▶️ Como executar
**1.** *Clone este repositório ou copie os arquivos para uma pasta local.*

**2.** *Certifique-se de que o MySQL esteja rodando e que você criou o banco conforme indicado.*

**3.** *Atualize as credenciais de conexão no main.py:*

```python
conn = criarConexao('127.0.0.1', 'root', 'sua_senha', 'ouvidoriabd')
```
---
## 🧠 Observações

**O arquivo operacoesbd.py deve conter as funções:**

`criarConexao`, `encerrarConexao`, `listarBancoDados`, `insertNoBancoDados`, `excluirBancoDados`.

**Essas funções lidam com a conexão e operações no MySQL.**

---
## 📌 Exemplo de uso
```
Ouvidoria de (Seu nome)

1)📋 Listagem das Manifestações
2)🔍 Listagem de Manifestações por tipo
3)✍️ Criar nova manifestação
4)📊 Exibir quantidade de Manifestações
5)🔢 Pesquisar manifestação por código
6)❌ Excluir uma Manifestação do Sistema
7)🚪 Sair do Sistema

```
---
## 📬 Contato
**Projeto desenvolvido por Caio Bruno Rodrigues de Santana para fins acadêmicos e educativos.
Sinta-se à vontade para contribuir ou modificar o código!**

---
## 🙏 Gratidão
***Muito obrigado por se interessar no meu sistema de ouvidoria, busco cada vez mais melhorar e aprender mais na área de programação, esse foi meu primeiro projeto e vou buscar cada vez mais aprender para futuramente entrar num emprego na área de programação, pois esse sempre foi meu sonho desde pequeno, agradeço pelo reconhecimento!!***
