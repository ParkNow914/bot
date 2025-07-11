import sys
from unittest.mock import MagicMock

# Mock requests para evitar chamadas HTTP reais
mock_requests = MagicMock()
mock_requests.get = MagicMock()
mock_requests.post = MagicMock()
mock_requests.put = MagicMock()
mock_requests.delete = MagicMock()

sys.modules["requests"] = mock_requests 