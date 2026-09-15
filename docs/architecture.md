# Zeus Architecture

## Current Architecture

Zeus is designed as a locally hosted AI assistant with separate components for inference, configuration, memory, and conversation history.

```text
                         ZEUS
                           │
                    ┌──────┴──────┐
                    │             │
                 AI Core       Configuration
                    │             │
              ┌─────┴─────┐    ┌──┴──────┐
              │           │    │         │
           Ollama      Prompt  Identity Personality
              │
           Qwen 2.5
              │
         Local Inference

                    │
                    ▼

                 Memory
                    │
              ┌─────┴─────┐
              │           │
          Memories    Conversations
```

## Design Principles

### Local First

AI inference is performed locally through Ollama rather than requiring a remote AI API.

### Persistent Context

Zeus maintains information between sessions through persistent memory and conversation history.

### Configurable Behavior

Identity and personality are separated from the main Python implementation, allowing behavior to be modified without rewriting the core application.

### Controlled System Access

Future system tools will be designed around explicit permissions and controlled execution rather than unrestricted host access.

## Future Architecture

The architecture will eventually expand to include:

```text
                         ZEUS
                           │
             ┌─────────────┼─────────────┐
             │             │             │
          AI Core       Memory        Tool Manager
             │             │             │
          Ollama       Database       Permission
             │                           │
          Qwen 2.5                 ┌─────┴─────┐
                                   │           │
                                Approved    Requires
                                 Tools      Approval
                                   │
                         ┌─────────┼─────────┐
                         │         │         │
                       Linux    Security   Lab Tools
                       Tools    Monitoring
```

This architecture is intended to keep AI reasoning separate from system actions and provide a security boundary between Zeus and the host system.
