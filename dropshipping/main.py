import os
import time
import logging
from fastapi import FastAPI
import threading
from prometheus_fastapi_instrumentator import Instrumentator

# Configurar logging para arquivo e stdout
log_dir = '/app/logs'
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, 'dropshipping.log')
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# FastAPI para healthcheck
app = FastAPI(title="Dropshipping Service", version="1.0.0")

# Instrumentação Prometheus
Instrumentator().instrument(app).expose(app, include_in_schema=False, should_gzip=True)

@app.get("/health")
def health():
    return {"status": "healthy", "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")}

# Exemplo de lógica principal
class DropshippingBot:
    def start(self):
        while True:
            try:
                logger.info("Dropshipping rodando...")
                time.sleep(60)
            except Exception as e:
                logger.error(f"Erro no bot: {e}")
                time.sleep(30)

def start_api():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    api_thread = threading.Thread(target=start_api, daemon=True)
    api_thread.start()
    bot = DropshippingBot()
    bot.start() 