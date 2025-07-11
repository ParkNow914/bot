import os
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
import time
import logging
from dotenv import load_dotenv
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import redis

# Carregar variáveis do .env
load_dotenv()

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Super-Bot API Gateway", version="1.0.0")

# Configurar Redis para rate limiting
redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
limiter = Limiter(key_func=get_remote_address, storage_uri=redis_url)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Configurar CORS
# Em produção, troque allow_origins para os domínios confiáveis
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Exemplo: ["https://seusite.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuração do JWT
class Settings(BaseModel):
    authjwt_secret_key: str = os.getenv("GATEWAY_SECRET", "supersecret")

@AuthJWT.load_config
def get_config():
    return Settings()

# Tratamento de erro JWT
@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request, exc):
    return HTTPException(status_code=exc.status_code, detail=exc.message)

# Modelos Pydantic
class TradingStatus(BaseModel):
    status: str
    active_trades: int
    total_profit: float
    last_update: str

class DropshippingOrder(BaseModel):
    product: str
    quantity: int
    price: float
    status: str

class Coupon(BaseModel):
    code: str
    description: str
    site: str
    expiry: str
    category: str

class ArbitrageOpportunity(BaseModel):
    product: str
    prices: Dict[str, float]
    min_price: float
    max_price: float
    margin: float

class Article(BaseModel):
    topic: str
    content: str
    formats: List[str]

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str
    email: str

# Dados simulados
trading_data = {
    "status": "active",
    "active_trades": 3,
    "total_profit": 1250.50,
    "last_update": time.strftime("%Y-%m-%d %H:%M:%S")
}

dropshipping_orders = [
    {"product": "iPhone 15", "quantity": 2, "price": 4500.00, "status": "processing"},
    {"product": "Samsung Galaxy", "quantity": 1, "price": 3200.00, "status": "shipped"}
]

coupons_data = [
    {"code": "SUPER10", "description": "Desconto 10%", "site": "amazon.com", "expiry": "2024-12-31", "category": "Eletrônicos"},
    {"code": "BOT20", "description": "Desconto 20%", "site": "mercadolivre.com", "expiry": "2024-11-30", "category": "Informática"}
]

arbitrage_opportunities = [
    {
        "product": "iPhone 15",
        "prices": {"Amazon": 4500, "Mercado Livre": 4200, "Americanas": 4800},
        "min_price": 4200,
        "max_price": 4800,
        "margin": 14.29
    }
]

articles_data = [
    {
        "topic": "Como investir em criptomoedas",
        "content": "Artigo sobre criptomoedas...",
        "formats": ["markdown", "pdf", "epub"]
    }
]

@app.get("/")
def root():
    return {"message": "Super-Bot API Gateway online!", "version": "1.0.0"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")}

# Trading endpoints
@app.get("/trading/status", response_model=TradingStatus)
def get_trading_status():
    """Retorna status do bot de trading"""
    return TradingStatus(**trading_data)

@app.get("/trading/trades")
def get_trading_trades():
    """Retorna trades ativos"""
    return {"trades": [], "count": 0}

# Dropshipping endpoints
@app.get("/dropshipping/orders", response_model=List[DropshippingOrder])
def get_dropshipping_orders():
    """Retorna pedidos de dropshipping"""
    return [DropshippingOrder(**order) for order in dropshipping_orders]

@app.post("/dropshipping/orders")
def create_dropshipping_order(order: DropshippingOrder):
    """Cria novo pedido de dropshipping"""
    dropshipping_orders.append(order.dict())
    return {"message": "Pedido criado com sucesso", "order": order}

# Afiliados endpoints
@app.get("/afiliados/coupons", response_model=List[Coupon])
def get_coupons():
    """Retorna cupons de afiliados"""
    return [Coupon(**coupon) for coupon in coupons_data]

@app.get("/afiliados/coupons/{category}")
def get_coupons_by_category(category: str):
    """Retorna cupons por categoria"""
    filtered_coupons = [c for c in coupons_data if c["category"].lower() == category.lower()]
    return {"coupons": filtered_coupons, "category": category}

# Arbitragem endpoints
@app.get("/arbitragem/opportunities", response_model=List[ArbitrageOpportunity])
def get_arbitrage_opportunities():
    """Retorna oportunidades de arbitragem"""
    return [ArbitrageOpportunity(**opp) for opp in arbitrage_opportunities]

@app.get("/arbitragem/opportunities/{product}")
def get_arbitrage_by_product(product: str):
    """Retorna oportunidades para um produto específico"""
    filtered_opps = [o for o in arbitrage_opportunities if product.lower() in o["product"].lower()]
    return {"opportunities": filtered_opps, "product": product}

# Conteúdo endpoints
@app.get("/conteudo/articles", response_model=List[Article])
def get_articles():
    """Retorna artigos gerados"""
    return [Article(**article) for article in articles_data]

@app.get("/conteudo/articles/{topic}")
def get_article_by_topic(topic: str):
    """Retorna artigo por tópico"""
    filtered_articles = [a for a in articles_data if topic.lower() in a["topic"].lower()]
    return {"articles": filtered_articles, "topic": topic}

# Sistema endpoints
@app.get("/system/status")
def get_system_status():
    """Retorna status geral do sistema"""
    return {
        "trading": {"status": "active", "last_check": time.strftime("%Y-%m-%d %H:%M:%S")},
        "dropshipping": {"status": "active", "orders_count": len(dropshipping_orders)},
        "afiliados": {"status": "active", "coupons_count": len(coupons_data)},
        "arbitragem": {"status": "active", "opportunities_count": len(arbitrage_opportunities)},
        "conteudo": {"status": "active", "articles_count": len(articles_data)}
    }

@app.get("/system/logs")
def get_system_logs():
    """Retorna logs do sistema"""
    return {
        "logs": [
            {"timestamp": time.strftime("%Y-%m-%d %H:%M:%S"), "level": "INFO", "message": "Sistema funcionando normalmente"},
            {"timestamp": time.strftime("%Y-%m-%d %H:%M:%S"), "level": "INFO", "message": "Todos os módulos ativos"}
        ]
    }

@app.post("/login")
def login(user: UserLogin, Authorize: AuthJWT = Depends()):
    # Exemplo simples: usuário fixo
    if user.username == "admin" and user.password == "admin":
        access_token = Authorize.create_access_token(subject=user.username)
        return {"access_token": access_token}
    raise HTTPException(status_code=401, detail="Usuário ou senha inválidos")

# Exemplo de rota protegida
from slowapi.decorator import limiter
@app.get("/usuario/me", response_model=UserOut)
@limiter.limit("10/minute")
def get_me(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    return {"username": current_user, "email": f"{current_user}@superbot.com"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80) 