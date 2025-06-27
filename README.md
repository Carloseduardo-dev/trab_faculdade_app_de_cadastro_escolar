
# 🎓 Sistema de Login - Colégio Golden Ball

Este projeto é um sistema de login simples desenvolvido em **Python** usando a biblioteca **Tkinter**, com interface gráfica customizada para uso escolar. O sistema valida credenciais e, em caso de sucesso, executa um novo script Python (`main.py`), representando o sistema principal da aplicação.

---

## 🛠 Tecnologias Utilizadas

- **Python 3.x**
- **Tkinter** (Interface gráfica)
- **ttk** (Estilo nativo do sistema)
- **Pillow (PIL)** (Exibição de imagens)

---

## 📂 Estrutura do Projeto

```
.
├── login.py         # Código principal da interface de login
├── main.py          # Sistema principal que será aberto após login bem-sucedido
└── img-estudante-96.png  # Ícone usado no topo da janela de login
```

---

## ▶️ Como Executar

1. **Pré-requisitos**:
   - Python 3.x instalado.
   - Biblioteca Pillow instalada:
     ```bash
     pip install pillow
     ```

2. **Executar o sistema**:
   ```bash
   python login.py
   ```

---

## 🔑 Credenciais de Acesso

O sistema possui um conjunto fixo de usuários válidos (definidos em dicionário). Por padrão, o usuário e senha são:

- **Usuário**: `goldenball`
- **Senha**: `123`

Você pode adicionar mais usuários modificando a estrutura abaixo no método `fazer_login()`:

```python
usuarios_validos = {
    'goldenball': '123',
    'outro_usuario': 'senha_segura',
}
```

---

## 📌 Funcionalidades

- Interface gráfica com design personalizado.
- Validação de usuário e senha.
- Exibição de mensagens de erro e sucesso.
- Abertura automática de outro script Python após login válido.
- Opção de cancelar e sair do aplicativo com confirmação.

---

## 📷 Interface Visual

![Exemplo da Interface](img-estudante-96.png)  
*A imagem acima é usada como ícone no cabeçalho do sistema.*

---

## ❓ Dúvidas e Problemas

Caso ocorra algum erro ao tentar abrir o arquivo `main.py`, o sistema exibe uma mensagem informando o problema. Verifique se o arquivo `main.py` está presente no mesmo diretório do script de login.

---

## 📌 Observações Finais

- O design foi pensado para escolas, mas pode ser adaptado para outros contextos.
- Você pode personalizar as cores no topo do script, na seção de variáveis `co0` a `co11`.
- Recomendado centralizar a imagem `img-estudante-96.png` na pasta para correta visualização.

---

# 📘 Banco de Dados: Sistema de Cadastro Escolar

Este projeto SQL define e popula a base de dados **`cadastro`**, contemplando informações de **alunos**, **cursos**, **turmas** e **notas**.  
Ele é ideal para sistemas educacionais (escolas, faculdades, cursos técnicos) que precisam controlar matrículas, avaliações e turmas.

---

## 🗂️ Estrutura do Projeto

Arquivos `.sql` incluídos:

| Script | Descrição |
| ------ | --------- |
| `cadastro_cursos.sql` | Cria a tabela `cursos` e insere 20 registros de exemplo |
| `cadastro_turmas.sql` | Cria a tabela `turmas` e insere 20 registros, vinculando‐as aos cursos |
| `cadastro_alunos.sql` | Cria a tabela `alunos` e insere 20 alunos, associando‐os a turmas e cursos |
| `cadastro_notas.sql`  | Cria a tabela `notas` e registra as notas dos alunos |

---

## 🧱 Modelagem das Tabelas

### Tabela: `cursos`

| Coluna         | Tipo            | Descrição                           |
| -------------- | --------------- | ----------------------------------- |
| `id_curso`     | INT (PK)        | Identificador único do curso        |
| `nome_curso`   | VARCHAR(30)     | Nome do curso                       |
| `carga_horaria`| VARCHAR(100)    | Carga horária total                 |
| `preco`        | VARCHAR(100)    | Preço ou investimento               |

### Tabela: `turmas`

| Coluna       | Tipo         | Descrição                          |
| ------------ | ------------ | ---------------------------------- |
| `id_turma`   | INT (PK)     | Identificador único da turma       |
| `nome_turma` | VARCHAR(30)  | Nome/identificação da turma        |
| `cursos`     | VARCHAR(50)  | Nome do curso (redundância textual)|
| `data_inicio`| DATE         | Data de início da turma            |
| `turmacurso` | INT (FK)     | Referência à tabela `cursos`       |

### Tabela: `alunos`

| Coluna            | Tipo             | Descrição                             |
| ----------------- | ---------------- | ------------------------------------- |
| `id_aluno`        | INT (PK)         | Identificador único do aluno          |
| `nome_aluno`      | VARCHAR(100)     | Nome completo                         |
| `email`           | VARCHAR(100)     | Endereço de e‑mail                    |
| `telefone`        | VARCHAR(100)     | Telefone                              |
| `cpf`             | VARCHAR(25)      | CPF do aluno                          |
| `sexo`            | ENUM('M','F')    | Sexo                                  |
| `data_nascimento` | DATE             | Data de nascimento                    |
| `turma`           | VARCHAR(20)      | Nome da turma (texto)                 |
| `cursoaluno`      | INT (FK)         | Referência à tabela `cursos`          |
| `turmaaluno`      | INT (FK)         | Referência à tabela `turmas`          |

### Tabela: `notas`

| Coluna     | Tipo          | Descrição                           |
| ---------- | ------------- | ----------------------------------- |
| `id_nota`  | INT (PK)      | Identificador único da nota         |
| `nota1`    | DECIMAL(5,2)  | Nota da 1ª avaliação                |
| `nota2`    | DECIMAL(5,2)  | Nota da 2ª avaliação                |
| `media`    | DECIMAL(5,2)  | Média calculada                     |
| `situacao` | VARCHAR(10)   | Situação (Aprovado/Reprovado)       |
| `id_aluno` | INT (FK)      | Referência à tabela `alunos`        |

#### 🔗 Relações (Foreign Keys)

- `turmacurso` → `cursos(id_curso)`
- `cursoaluno` → `cursos(id_curso)`
- `turmaaluno` → `turmas(id_turma)`
- `id_aluno` (em `notas`) → `alunos(id_aluno)`

---

## 🧪 Dados de Exemplo

Cada script insere **20 registros** fictícios para facilitar testes e demonstrações.  
Os dados incluem exemplos realistas de nomes, e‑mails, valores de nota e datas.

---

## 🚀 Como Utilizar

1. Abra seu cliente MySQL (MySQL Workbench, DBeaver, phpMyAdmin ou terminal).
2. Crie a base de dados e selecione‐a:
   ```sql
   CREATE DATABASE cadastro;
   USE cadastro;
   ```
3. Execute os scripts **nesta ordem** para manter a integridade referencial:
   1. `cadastro_cursos.sql`
   2. `cadastro_turmas.sql`
   3. `cadastro_alunos.sql`
   4. `cadastro_notas.sql`
4. Verifique as tabelas e faça consultas para garantir que tudo foi importado corretamente.

---

## 🛠️ Requisitos

- **MySQL 8.0** ou superior (ou MariaDB equivalente)
- Permissões para criar banco, tabelas e inserir dados

---

## 📄 Licença

Este projeto é de caráter educacional. Fique à vontade para **clonar, modificar e compartilhar**, desde que cite a fonte ou deixe um ⭐ no repositório.

## 👥 Desenvolvedores

[![Carlos Eduardo](https://github.com/Carloseduardo-dev.png?size=100)](https://github.com/Carloseduardo-dev)
[![Pedro Henrique](https://github.com/PedroShinro.png?size=100)](https://github.com/PedroShinro)
[![Enzo Fernandes](https://github.com/murajiro.png?size=100)](https://github.com/murajiro)
[![Ricardo Leite](https://github.com/ricardoRD95.png?size=100)](https://github.com/ricardoRD95)

