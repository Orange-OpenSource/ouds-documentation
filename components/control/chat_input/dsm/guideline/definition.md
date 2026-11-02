A chat input is a UI element that allows users to compose a message in a conversation. It combines a text entry area, configurable bottom actions and optional supporting messages or a helper link.

This overview documents the supplied draft: its visual variants and editable content. Message submission, validation, character counting and suggestion logic must be implemented by the product.

Chat input does not expose Voice input, AI legal notice or a content slot at its root. The microphone is an action icon, not a voice-input mode. A slot is available only inside the nested Bottom actions component.