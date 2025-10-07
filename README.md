# Shell Personalizado em Python

Este projeto é uma implementação de um **interpretador de comandos estilo shell**, desenvolvida para fins de **aprendizado e experimentação com sistemas baseados em linha de comando**.

A aplicação é capaz de interpretar comandos, executar programas externos e lidar com comandos internos básicos, como `cd`, `pwd` e `echo`.
O objetivo é compreender o funcionamento interno de um shell POSIX simplificado, incluindo parsing de comandos, execução de processos e gerenciamento de entrada e saída.

---

## 🚀 Funcionalidades

* Execução de comandos externos do sistema
* Suporte a comandos internos (`cd`, `pwd`, `echo`, etc.)
* Estrutura modular em Python
* Fácil extensão e personalização

---

## 🧠 Conceitos Envolvidos

* Processos e *fork/exec*
* Streams de entrada e saída
* Parsing de comandos
* Estrutura de REPL (*Read-Eval-Print Loop*)

---

## ⚙️ Como Executar

Certifique-se de ter o **Python 3** e o **pipenv** instalados.

```bash
pipenv install
./run.sh
```

O arquivo principal do projeto está localizado em `app/main.py`.

---

## 📁 Estrutura do Projeto

```
.
├── app/
│   ├── main.py          # Ponto de entrada da aplicação
│   └── ...
├── run.sh               # Script de execução
├── Pipfile              # Dependências do projeto
├── Pipfile.lock
└── README.md
```

---

## 🧩 Observações

Este projeto foi criado **para estudo e prática pessoal**, inspirado em desafios de desenvolvimento de sistemas de shell.
Todo o código é de autoria própria e pode ser livremente adaptado e expandido.

---

## 📝 Licença

Você é livre para usar e modificar este código como quiser.
