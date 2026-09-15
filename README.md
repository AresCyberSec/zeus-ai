# Zeus AI 🤖

A locally hosted AI assistant built with Python and Ollama.

Zeus is an ongoing personal project focused on exploring local AI, persistent memory, controlled system interaction, and cybersecurity-oriented assistance.

## 🧠 Overview

Zeus runs locally rather than relying on a cloud-hosted AI service.

The project currently uses:

* Python
* Ollama
* Qwen 2.5
* JSON-based memory
* Local conversation history
* Linux

The goal is to develop Zeus into a capable local AI assistant while maintaining clear boundaries around system access and user control.

## 🏗️ Current Architecture

```text
                    ZEUS
                     │
              ┌──────┴──────┐
              │             │
          AI Core         Memory
              │             │
              │       ┌─────┴─────┐
              │       │           │
           Ollama  Memories   Conversations
              │
          Qwen 2.5
```

## ✨ Current Features

* Local AI inference through Ollama
* Persistent memory
* Conversation history
* Configurable identity
* Configurable personality
* Python-based AI core
* Local Linux deployment

## 🔐 Security Philosophy

Zeus is being developed with security and user control as core design principles.

The long-term architecture is intended to use controlled permissions for system interaction rather than giving the AI unrestricted access to the host machine.

Potentially sensitive or irreversible actions should require appropriate authorization.

## 🚧 Development Status

**Active Development**

Zeus is still an experimental project. Features and architecture are expected to change as development continues.

### Planned Development

* Improved memory architecture
* Better conversation continuity
* Controlled system tools
* Permission and authorization layer
* Security monitoring integration
* Sandboxed tool execution
* Improved error handling
* Voice interface
* Expanded cybersecurity capabilities

## 🛠️ Project Goals

The long-term goal is to create a powerful local AI assistant that can operate alongside a cybersecurity laboratory while maintaining strong isolation, transparency, and user control.

## ⚠️ Disclaimer

Zeus is an educational and experimental project.

Users are responsible for how they configure and deploy the software. Security-related capabilities should only be used on systems and networks where the user has appropriate authorization.
