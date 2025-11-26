# 🤖 AI Code Assistant CLI

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/AureoManzanoJr/ai-code-assistant?style=social)](https://github.com/AureoManzanoJr/ai-code-assistant)
[![Forks](https://img.shields.io/github/forks/AureoManzanoJr/ai-code-assistant?style=social)](https://github.com/AureoManzanoJr/ai-code-assistant)
[![Issues](https://img.shields.io/github/issues/AureoManzanoJr/ai-code-assistant)](https://github.com/AureoManzanoJr/ai-code-assistant/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**A ferramenta CLI mais poderosa para assistência de código com IA**

[Features](#-funcionalidades) • [Instalação](#-instalação-rápida) • [Uso](#-como-usar) • [Documentação](#-documentação) • [Contribuir](#-contribuindo)

[![Demo](https://img.shields.io/badge/🎬-Ver%20Demo-blue)](https://github.com/AureoManzanoJr/ai-code-assistant#-demonstração)
[![Website](https://img.shields.io/badge/🌐-iadev.pro-blue)](https://iadev.pro)
[![Email](https://img.shields.io/badge/📧-Contato-blue)](mailto:aureomanzano@icloud.com)

</div>

---

## 🚀 O que é?

**AI Code Assistant CLI** é uma ferramenta de linha de comando revolucionária que utiliza Inteligência Artificial para transformar completamente sua experiência de desenvolvimento. Gere código, refatore, explique, teste e muito mais - tudo diretamente do terminal.

### ⚡ Por que usar?

- 🎯 **Múltiplos Modelos de IA** - OpenAI, Anthropic Claude, Ollama (local), e mais
- 🔥 **10+ Funcionalidades Poderosas** - Geração, refatoração, testes, documentação, e muito mais
- 💻 **CLI Intuitivo** - Interface simples e poderosa
- 🌐 **Interface Web Opcional** - Dashboard moderno e interativo
- 🎨 **Syntax Highlighting** - Código colorido e formatado
- 📚 **Documentação Completa** - Exemplos e guias detalhados
- 🚀 **Rápido e Eficiente** - Otimizado para performance
- 🔒 **Privacidade** - Suporte para modelos locais (Ollama)

---

## ✨ Funcionalidades

### 🎨 Geração de Código
```bash
ai-code generate "função que calcula fibonacci em Python"
ai-code generate "componente React com hooks"
```

### 🔧 Refatoração Inteligente
```bash
ai-code refactor arquivo.py --improve-performance
ai-code refactor src/ --apply-best-practices
```

### 📖 Explicação de Código
```bash
ai-code explain arquivo.py
ai-code explain "função complexa" --detailed
```

### 🧪 Geração de Testes
```bash
ai-code test arquivo.py --framework pytest
ai-code test src/ --coverage
```

### 🌍 Tradução entre Linguagens
```bash
ai-code translate arquivo.py --to javascript
ai-code translate src/ --to typescript
```

### 🐛 Correção de Bugs
```bash
ai-code fix arquivo.py
ai-code fix src/ --auto-apply
```

### 📝 Documentação Automática
```bash
ai-code docs arquivo.py
ai-code docs src/ --format markdown
```

### 🔍 Análise de Código
```bash
ai-code analyze arquivo.py
ai-code analyze src/ --suggest-improvements
```

### 💬 Chat Interativo
```bash
ai-code chat
# Inicia um chat interativo com IA
```

### 🎯 Code Review
```bash
ai-code review arquivo.py
ai-code review pr/ --detailed
```

---

## 📦 Instalação Rápida

### Via pip
```bash
pip install ai-code-assistant
```

### Via pipx (recomendado)
```bash
pipx install ai-code-assistant
```

### Desenvolvimento
```bash
git clone https://github.com/AureoManzanoJr/ai-code-assistant.git
cd ai-code-assistant
pip install -e .
```

---

## 🎬 Demonstração

### Geração de Código
```bash
$ ai-code generate "função que valida email em Python"

def validate_email(email: str) -> bool:
    """
    Valida um endereço de email usando regex.
    
    Args:
        email: Endereço de email a ser validado
        
    Returns:
        True se o email é válido, False caso contrário
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
```

### Refatoração
```bash
$ ai-code refactor old_code.py --improve-performance

✨ Refatorando código...
✅ Código otimizado com sucesso!
📊 Melhorias aplicadas:
   - Redução de complexidade: 45%
   - Melhoria de performance: 30%
   - Legibilidade: +60%
```

### Explicação de Código
```bash
$ ai-code explain complex_function.py

📖 Explicação do código:

Esta função implementa um algoritmo de ordenação quicksort...
[Explicação detalhada]
```

---

## 🛠️ Como Usar

### Configuração Inicial

1. **Configure sua API Key:**
```bash
ai-code config set openai_key YOUR_API_KEY
# ou
ai-code config set anthropic_key YOUR_API_KEY
# ou use Ollama local (sem API key necessário)
ai-code config set provider ollama
```

2. **Verifique a configuração:**
```bash
ai-code config show
```

### Exemplos de Uso

#### Geração de Código
```bash
# Gera código a partir de descrição
ai-code generate "classe User com autenticação"

# Gera código em arquivo específico
ai-code generate "API REST em Flask" --output app.py

# Gera com contexto
ai-code generate "função de busca" --context "usando MongoDB"
```

#### Refatoração
```bash
# Refatora um arquivo
ai-code refactor main.py

# Refatora com melhorias específicas
ai-code refactor src/ --improve-performance --apply-best-practices

# Refatora mantendo estilo
ai-code refactor code.py --preserve-style
```

#### Explicação
```bash
# Explica código simples
ai-code explain function.py

# Explicação detalhada
ai-code explain complex.py --detailed

# Explica função específica
ai-code explain file.py --function calculate_total
```

#### Testes
```bash
# Gera testes para arquivo
ai-code test calculator.py

# Testes com framework específico
ai-code test api.py --framework pytest

# Testes com cobertura
ai-code test src/ --coverage
```

#### Tradução
```bash
# Traduz Python para JavaScript
ai-code translate app.py --to javascript

# Traduz para TypeScript
ai-code translate src/ --to typescript

# Traduz mantendo comentários
ai-code translate code.py --to go --preserve-comments
```

---

## ⚙️ Configuração

### Modelos Suportados

- **OpenAI**: `gpt-4`, `gpt-4-turbo`, `gpt-3.5-turbo`
- **Anthropic**: `claude-3-opus`, `claude-3-sonnet`, `claude-3-haiku`
- **Ollama** (Local): `llama2`, `codellama`, `mistral`, `neural-chat`

### Arquivo de Configuração

Crie `~/.ai-code/config.yaml`:

```yaml
provider: openai  # openai, anthropic, ollama
model: gpt-4-turbo
api_key: your-api-key-here
temperature: 0.7
max_tokens: 2000
default_language: python
theme: dark
```

---

## 🌐 Interface Web

Inicie o servidor web para uma experiência visual:

```bash
ai-code web
```

Acesse `http://localhost:8080` para:
- Editor de código interativo
- Chat com IA
- Visualização de resultados
- Histórico de comandos
- Configurações visuais

---

## 📚 Documentação Completa

- [Guia de Instalação](docs/INSTALLATION.md)
- [Guia de Uso](docs/USAGE.md)
- [API Reference](docs/API.md)
- [Exemplos](examples/)
- [FAQ](docs/FAQ.md)
- [Contribuindo](CONTRIBUTING.md)

---

## 🎯 Casos de Uso

### Desenvolvimento Rápido
```bash
# Gera estrutura completa de projeto
ai-code generate "API REST em FastAPI com autenticação JWT" --output api/

# Gera testes automaticamente
ai-code test api/ --framework pytest

# Gera documentação
ai-code docs api/ --format markdown
```

### Refatoração de Código Legado
```bash
# Analisa código antigo
ai-code analyze legacy_code/ --suggest-improvements

# Refatora mantendo funcionalidade
ai-code refactor legacy_code/ --preserve-functionality
```

### Aprendizado
```bash
# Explica código complexo
ai-code explain algorithm.py --detailed

# Traduz entre linguagens para aprender
ai-code translate python_code.py --to rust
```

---

## 🏗️ Arquitetura

```
ai-code-assistant/
├── cli/              # Interface CLI
├── core/              # Lógica principal
│   ├── providers/     # Integrações com IA
│   ├── processors/    # Processadores de código
│   └── utils/        # Utilitários
├── web/               # Interface web
├── tests/             # Testes
└── docs/              # Documentação
```

---

## 🤝 Contribuindo

Contribuições são muito bem-vindas! Veja [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes.

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📊 Estatísticas

- ⚡ **10+ Funcionalidades** poderosas
- 🎯 **3+ Modelos de IA** suportados
- 🌍 **20+ Linguagens** suportadas
- 📦 **Fácil instalação** com pip
- 🚀 **Rápido** e otimizado

---

## 👨‍💻 Autor

**Aureo Manzano Junior**

Desenvolvedor apaixonado por criar ferramentas que transformam a experiência de desenvolvimento.

- 🌐 **Website:** [iadev.pro](https://iadev.pro)
- 📧 **Email:** [aureomanzano@icloud.com](mailto:aureomanzano@icloud.com)
- 💼 **GitHub:** [@AureoManzanoJr](https://github.com/AureoManzanoJr)
- 🚀 **Portfólio:** [iadev.pro](https://iadev.pro)

### Entre em Contato

Tem uma ideia, sugestão ou quer trabalhar junto?

- 📧 Email: [aureomanzano@icloud.com](mailto:aureomanzano@icloud.com)
- 🌐 Website: [iadev.pro](https://iadev.pro)
- 💬 Issues: [GitHub Issues](https://github.com/AureoManzanoJr/ai-code-assistant/issues)

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja [LICENSE](LICENSE) para mais detalhes.

---

## ⭐ Suporte

Se este projeto foi útil para você:

- ⭐ **Dê uma estrela** no GitHub
- 🍴 **Faça um fork**
- 🐛 **Reporte bugs**
- 💡 **Sugira funcionalidades**
- 📢 **Compartilhe com amigos**

---

## 🙏 Agradecimentos

Obrigado por usar o AI Code Assistant CLI! Se você gostou do projeto, considere dar uma estrela ⭐ e compartilhar com outros desenvolvedores.

---

<div align="center">

**Desenvolvido com ❤️ por [Aureo Manzano Junior](https://iadev.pro)**

*Transformando desenvolvimento com Inteligência Artificial*

[![Website](https://img.shields.io/badge/🌐-iadev.pro-blue)](https://iadev.pro)
[![Email](https://img.shields.io/badge/📧-aureomanzano@icloud.com-blue)](mailto:aureomanzano@icloud.com)

</div>

