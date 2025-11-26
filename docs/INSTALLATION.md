# Guia de Instalação

## Instalação Rápida

### Via pip
```bash
pip install ai-code-assistant
```

### Via pipx (Recomendado)
```bash
pipx install ai-code-assistant
```

## Instalação de Desenvolvimento

```bash
git clone https://github.com/AureoManzanoJr/ai-code-assistant.git
cd ai-code-assistant
pip install -e .
```

## Configuração

### 1. Configure sua API Key

```bash
# OpenAI
ai-code config set_provider openai YOUR_API_KEY

# Anthropic
ai-code config set_provider anthropic YOUR_API_KEY

# Ollama (local, sem API key)
ai-code config set_provider ollama
```

### 2. Verifique a configuração

```bash
ai-code config show
```

## Requisitos

- Python 3.9+
- API Key (OpenAI ou Anthropic) OU Ollama instalado localmente

---

**Desenvolvido por:** [Aureo Manzano Junior](https://iadev.pro)

