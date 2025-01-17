# Blog com Flask 📝

Este é um projeto de estudo desenvolvido como parte do aprendizado do framework Flask, com base no tutorial oficial disponível na [documentação do Flask](https://flask.palletsprojects.com/). O objetivo principal é consolidar conhecimentos sobre o desenvolvimento de aplicações web utilizando Flask, praticando habilidades como roteamento, templates, autenticação e manipulação de banco de dados.

---

## 💡 Sobre o Projeto

O **Blog com Flask** é uma aplicação simples que permite aos usuários:  
- Registrar uma conta.  
- Fazer login/logout com autenticação de sessão.  
- Criar, visualizar, editar e excluir posts de blog.  
- Exibir os posts mais recentes ordenados por data de criação.  

Embora seja um projeto de demonstração, ele simula funcionalidades reais encontradas em muitos sistemas de blogs.

---

## ⚙️ Funcionalidades Implementadas

1. **Autenticação e Autorização**  
   - Registro de novos usuários com validação de dados.  
   - Login/logout com gerenciamento de sessão.  
   - Restrições de acesso para ações que exigem autenticação, como criar ou editar posts.  

2. **Gerenciamento de Conteúdo**  
   - Criação de posts com título e corpo.  
   - Edição e exclusão de posts apenas pelo autor.  
   - Listagem de posts organizados por data de criação.  

3. **Integração com Banco de Dados**  
   - Banco de dados SQLite para armazenar informações de usuários e posts.  
   - Manipulação de dados usando consultas SQL.  

4. **Organização de Código**  
   - Uso de Blueprints para modularidade e melhor organização.  
   - Templates Jinja2 para separar a lógica da camada de apresentação.  

---

## 📚 Tecnologias e Habilidades

Este projeto reforça as seguintes tecnologias e habilidades:  
- **Flask Framework**: Roteamento, Blueprints, Jinja2 Templates.  
- **Banco de Dados**: SQLite, manipulação com SQL puro.  
- **Autenticação**: Gerenciamento de sessão, hash de senhas com Werkzeug.  
- **HTML e CSS**: Construção de interfaces simples e responsivas.  
- **Melhores Práticas**: Organização de código, tratamento de erros e segurança básica.  

---

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/HermesSoftwareEngineer/tutorial_flask.git
   cd tutorial_flask
2. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source .venv/bin/activate  # Para Linux/Mac
   .venv\Scripts\activate     # Para Windows
3. Inicialize o banco de dados
   ```bash
   flask init-db
4. Execute o servidor:
   ```bash
   flask --app flaskr run --debug
6. Acesse a aplicação no navegador:
  http://127.0.0.1:5000/

---
## 📂 Estrutura do Projeto
  ```
  tutorial_flask/
  ├── flaskr/
  │   ├── __init__.py         # Configuração inicial da aplicação
  │   ├── auth.py             # Rotas e lógica de autenticação
  │   ├── blog.py             # Rotas e lógica do blog
  │   ├── db.py               # Funções relacionadas ao banco de dados
  │   ├── templates/          # Templates HTML (Jinja2)
  │   └── static/             # Arquivos estáticos +
  ├── instance/
  │   └── flaskr.sqlite       # Banco de dados SQLite
  └── README.md               # Documentação do projeto]
  ```

## 📬 Contato
Se tiver dúvidas ou sugestões, fique à vontade para me contatar:
- Nome: Hermes Barbosa
- LinkedIn: [Meu Perfil](https://www.linkedin.com/in/hermes-barbosa-78840118a/)
- E-mail: hermesbarbosa9@gmail.com
