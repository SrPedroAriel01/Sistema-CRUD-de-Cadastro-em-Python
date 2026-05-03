# 🧾 Sistema de Cadastro em Python (CRUD)

Projeto desenvolvido com o objetivo de praticar lógica de programação, Programação Orientada a Objetos (POO) e manipulação de dados utilizando Python.

---

## 🚀 Funcionalidades

* ✅ Cadastro de pessoas
* 📋 Listagem de registros
* 🔍 Busca por nome
* ✏️ Atualização de dados (com confirmação)
* ❌ Remoção de registros (com validação)
* 💾 Persistência de dados em arquivo JSON

---

## 🧠 Conceitos Aplicados

* Estruturas de dados (listas e dicionários)
* Programação Orientada a Objetos (POO)
* Manipulação de arquivos (`json`)
* Controle de fluxo (loops, condicionais)
* Validação de entrada de dados
* Modularização do código
* Uso de Git e GitHub

---

## 📁 Estrutura do Projeto

```
Sistema-CRUD-de-Cadastro-em-Python/
│
├── main.py          # Controle principal do sistema (menu)
├── funcoes.py       # Regras de negócio e operações (CRUD)
├── pessoa.py        # Classe Pessoa
├── dados.json       # Armazenamento dos dados
├── .gitignore       # Arquivos ignorados pelo Git
└── README.md        # Documentação do projeto
```

---

## ▶️ Como Executar

1. Certifique-se de ter o Python instalado
2. Clone o repositório:

```bash
git clone https://github.com/SrPedroAriel01/Sistema-CRUD-de-Cadastro-em-Python
```

3. Acesse a pasta do projeto:

```bash
cd Sistema-CRUD-de-Cadastro-em-Python
```

4. Execute o programa:

```bash
python main.py
```

---

## 🖥️ Exemplo de Uso

```
--- MENU ---
1 - Cadastrar
2 - Listar
3 - Buscar
4 - Atualizar
5 - Remover
0 - Sair
```

---

## 🔒 Validações Implementadas

* Nome não pode ser vazio
* Idade deve ser um número válido
* Confirmação antes de atualizar ou remover
* Tratamento para múltiplos registros com o mesmo nome

---

## 📈 Possíveis Melhorias

* Ordenação por nome ou idade
* Exportação para CSV
* Interface gráfica (GUI)
* Transformação em aplicação web (Flask)
* Banco de dados (SQLite/PostgreSQL)

---

## 👨‍💻 Autor

Desenvolvido por Pedro Ariel
📌 Projeto com foco em aprendizado e evolução em programação

---

## 📌 Observação

Este projeto faz parte do meu processo de aprendizado e evolução como desenvolvedor, com foco em construir uma base sólida em lógica e desenvolvimento de software.
