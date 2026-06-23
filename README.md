# 🎒 Julyo's Backpack

Uma plataforma de ferramentas para Analistas de Dados, Cientistas de Dados e profissionais de Business Intelligence.

O **Julyo's Backpack** nasceu da necessidade de reunir em um único ambiente diversas operações comuns de preparação, validação e limpeza de dados, reduzindo o tempo gasto em tarefas repetitivas e acelerando o processo de análise.

---

## Acesse o projeto através dos Links:

Vercel (FrontEnd): https://julyos-backpack.vercel.app/

Render (BackEnd): https://julyos-backpack.onrender.com

Meu portfólio: https://jullyoo.github.io/Julyo.dev/

---

## 📖 Sobre o Projeto

Durante projetos de análise de dados, grande parte do tempo é consumida por atividades de preparação de dados:

* Tratamento de valores nulos;
* Remoção de registros duplicados;
* Correção de formatação;
* Padronização de textos;
* Validação de documentos;
* Identificação de inconsistências.

O objetivo do **Julyo's Backpack** é disponibilizar um conjunto de ferramentas que automatizam essas tarefas através de uma interface simples e intuitiva.

---

## 🚀 Funcionalidades

### 📊 Data Cleaner

Ferramenta principal da plataforma para execução de processos de ETL simplificados.

Atualmente permite:

* Remoção de registros duplicados;
* Tratamento de valores nulos;
* Limpeza de textos;
* Correção de encoding;
* Formatação de datas;
* Identificação de outliers;
* Exportação dos dados processados.

---

### 🧾 Validação de Documentos

Ferramentas para validação automática de documentos brasileiros.

#### CPF Validator

* Verificação dos dígitos verificadores;
* Identificação de CPFs inválidos.

#### CNPJ Validator

* Verificação estrutural;
* Validação dos dígitos verificadores.

#### CEP Validator

* Validação de formato;
* Verificação de consistência.

---

### 📈 Data Preview

Visualização rápida dos dados antes da execução das transformações.

Permite:

* Inspeção das colunas;
* Conferência dos registros carregados;
* Verificação preliminar da qualidade dos dados.

---

## 🏗️ Arquitetura

```text
Frontend (React + Vite)
          │
          ▼
      API REST
          │
          ▼
Backend (Flask)
          │
          ▼
Módulos de Processamento
          │
          ▼
Arquivo Tratado
```

O projeto utiliza uma arquitetura modular que facilita a criação de novas ferramentas e a manutenção do código.

---

## 🛠️ Tecnologias Utilizadas

### Frontend

* React
* Vite
* JavaScript
* CSS3

### Backend

* Python
* Flask
* Pandas
* NumPy
* OpenPyXL

### Controle de Versão

* Git
* GitHub

### Deploy

* Render
* Vercel (opcional para frontend)

---

## 📂 Estrutura do Projeto

```text
backend/
├── core/
├── modules/
├── routes/
├── services/
├── outputs/
└── app.py

frontend/
├── src/
│   ├── assets/
│   ├── components/
│   ├── pages/
│   ├── services/
│   └── styles/
├── package.json
└── vite.config.js
```

---

## ⚙️ Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/julyos-backpack.git
```

### 2. Backend

```bash
cd backend

pip install -r requirements.txt

python app.py
```

Servidor disponível em:

```text
http://localhost:5000
```

---

### 3. Frontend

```bash
cd frontend

npm install

npm run dev
```

Aplicação disponível em:

```text
http://localhost:5173
```

---

## 🎯 Objetivos do Projeto

Este projeto foi desenvolvido com foco em:

* Automatização de tarefas de preparação de dados;
* Aplicação prática de conceitos de ETL;
* Desenvolvimento Full Stack;
* Criação de ferramentas voltadas para a área de Dados;
* Construção de portfólio profissional.

---

## 🔮 Próximas Evoluções

Funcionalidades planejadas para futuras versões:

* Data Profiling;
* Relatórios automáticos de qualidade dos dados;
* Dashboard de métricas do dataset;
* Sugestões inteligentes de tratamento;
* Integração com bancos de dados;
* Exportação para múltiplos formatos.

---

## 👨‍💻 Autor

**Julio**

Analista de Dados e Desenvolvedor focado em soluções para automação, análise e visualização de dados.

GitHub: https://github.com/Jullyoo
