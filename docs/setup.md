# Zeus Setup Guide

This guide explains how to set up and run Zeus, a local AI assistant built with Python and Ollama.

## Requirements

Before running Zeus, make sure the system has:

* Linux
* Python 3
* Git
* Ollama
* A compatible Ollama model

Zeus is currently configured to use the Qwen 2.5 7B model through Ollama.

## 1. Clone the Repository

Clone the Zeus repository:

```bash
git clone https://github.com/AresCyberSec/zeus-ai.git
cd zeus-ai
```

## 2. Create a Python Virtual Environment

Create a virtual environment:

```bash
python3 -m venv ai-env
```

Activate it:

```bash
source ai-env/bin/activate
```

## 3. Install Python Dependencies

Install the required Python packages:

```bash
pip install requests
```

## 4. Install and Configure Ollama

Install Ollama using the installation method appropriate for your Linux distribution.

Verify that Ollama is available:

```bash
ollama --version
```

## 5. Download the AI Model

Pull the model used by the current Zeus implementation:

```bash
ollama pull qwen2.5:7b
```

Verify that the model is installed:

```bash
ollama list
```

## 6. Create Zeus Configuration

The repository does not include personal configuration or memory data.

Create the required directories:

```bash
mkdir -p config memory
```

Create the identity file:

```bash
nano config/identity.txt
```

Create the personality file:

```bash
nano config/personality.txt
```

These files allow each Zeus installation to define its own identity and personality.

## 7. Start Zeus

Make sure Ollama is running, then start Zeus:

```bash
python3 ai_core.py
```

Zeus should initialize and connect to the local Ollama service.

## 8. Persistent Data

Zeus can maintain local conversation history and memory.

These files are intentionally excluded from the public repository:

```text
memory/
config/
```

This prevents personal conversations, memories, and local configuration from being published.

## Troubleshooting

### Ollama is not responding

Verify that Ollama is running and available:

```bash
ollama list
```

### Model not found

Pull the required model:

```bash
ollama pull qwen2.5:7b
```

### Python dependency error

Make sure the virtual environment is activated:

```bash
source ai-env/bin/activate
```

Then install the dependency:

```bash
pip install requests
```

## Security Note

Zeus is designed as a local AI project with an emphasis on controlled access and future defensive cybersecurity capabilities.

Future versions may introduce additional permission controls, sandboxing, tool integration, and security monitoring.

Do not give Zeus access to sensitive systems or perform actions outside an authorized environment without appropriate safeguards.
