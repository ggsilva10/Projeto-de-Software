# Projeto de Software: Sistema de Controle de Hábitos

Este é o projeto desenvolvido para a disciplina de Projeto de Software. O objetivo é criar um sistema web completo para ajudar usuários a monitorar e construir hábitos positivos, com funcionalidades de cadastro, login e gerenciamento de hábitos pessoais.

---

## 👥 Integrantes

* Gustavo Silva Gonçalves

---

## 📊 Status do Projeto

* **AC1: Fundação e CRUD de Hábitos** - ✅ Concluída
* **AC2: Sistema de Usuários e Personalização** - ✅ Concluída
* **AC3: Visualização de Dados** - ✅ Concluída
* **P3: Entrega Final e Novas Funcionalidades** - ✅ Concluída

---

## ✨ Funcionalidades Entregues

### AC1 - Fundação do Projeto
* Estrutura do projeto Flask com padrão *Application Factory* e *Blueprints*.
* Configuração do banco de dados SQLite com Flask-SQLAlchemy.
* Implementação do CRUD (Create, Read, Update, Delete) completo para Hábitos.
* Interface de usuário básica para interagir com as funcionalidades.

### AC2 - Sistema de Usuários
* Criação de modelo `User` com armazenamento seguro de senhas (hashing).
* Implementação de sistema de Cadastro, Login e Logout com `Flask-Login`.
* Proteção de rotas, permitindo que apenas usuários logados acessem a área de hábitos.
* Associação de Hábitos a Usuários, garantindo que cada usuário só possa ver e gerenciar seus próprios dados.
* Interface com navegação dinâmica, que se adapta ao status de login do usuário.

### AC3 - Visualização de Dados
* **Página de Detalhes do Hábito:** Criação de uma página dedicada para cada hábito, acessível a partir da lista principal.
* **Calendário de Progresso:** Implementação de um calendário mensal na página de detalhes, destacando visualmente os dias em que o hábito foi concluído.
* **Estatísticas Simples:** Cálculo e exibição de métricas de desempenho na página de detalhes, como "Total de Conclusões" e "Sequência Atual de Dias".
* **Refatoração Completa:** Padronização de todo o código-fonte (modelos, rotas, templates) e estrutura do banco de dados para utilizar nomes em inglês, seguindo as melhores práticas de mercado.

### P3 - Entrega Final (Prova)
* **Categorias de Hábitos (Tags):** Implementação *Full-Stack* de um sistema de categorias. O usuário pode classificar seus hábitos por áreas (ex: Saúde, Estudos) que são exibidas com etiquetas coloridas dinâmicas. Inclui a geração automática de categorias padrão para novos usuários.
* **Edição de Hábitos (Update):** Funcionalidade que permite corrigir ou alterar o nome de um hábito existente sem perder o histórico de conclusões.
* **Navegação Histórica:** Melhoria no calendário de progresso, permitindo a navegação entre meses e anos anteriores/futuros através de rotas dinâmicas.
* **Documentação Técnica:** Elaboração e inclusão de Diagramas UML (Diagrama de Classes e Diagrama de Casos de Uso) detalhando a arquitetura do sistema.

---

## 🚀 Como Rodar o Projeto

1.  Clone este repositório.
2.  Crie e ative um ambiente virtual (`python -m venv venv` e `source venv/bin/activate`).
3.  Instale as dependências: `pip install -r requirements.txt`.
4.  Crie um arquivo `.flaskenv` na raiz do projeto com o conteúdo: `FLASK_APP=run.py`.
5.  Aplique as migrações do banco de dados: `flask db upgrade`.
6.  Execute a aplicação: `python3 run.py`.

---

## 🛠️ Tecnologias
* **Back-end:** Python, Flask
* **Banco de Dados:** SQLite, Flask-SQLAlchemy, Flask-Migrate
* **Front-end:** HTML, CSS (Pico.css), Jinja2
* **Autenticação:** Flask-Login, Flask-WTF
* **Versionamento:** Git, GitHub
* **Gerenciamento:** GitHub Projects (Kanban)
