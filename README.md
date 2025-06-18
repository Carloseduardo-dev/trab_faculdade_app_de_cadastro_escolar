# 🎓 Sistema de Login - Colégio Golden Ball

Este projeto é um sistema de login simples desenvolvido em **Python** usando a biblioteca **Tkinter**, com interface gráfica customizada para uso escolar. O sistema valida credenciais e,
em caso de sucesso, executa um novo script Python (`main.py`), representando o sistema principal da aplicação.

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
