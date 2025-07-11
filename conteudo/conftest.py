import sys
from unittest.mock import MagicMock

# Mock gpt4all antes de qualquer import
class MockGPT4All:
    def __init__(self, *args, **kwargs):
        pass
    
    def generate(self, *args, **kwargs):
        return "Conteúdo simulado gerado pelo mock"

mock_gpt4all = MagicMock()
mock_gpt4all.GPT4All = MockGPT4All

# Mock também o módulo completo
sys.modules["gpt4all"] = mock_gpt4all 