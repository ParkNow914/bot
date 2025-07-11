# Super-Bot

Sistema modular 100% gratuito para automação de trading, dropshipping, afiliados, arbitragem e geração de conteúdo digital.

## Arquitetura
- Microsserviços em Docker
- Orquestração: Airflow/Cron
- API Gateway: FastAPI + Nginx
- Banco de dados: PostgreSQL (Heroku Free), Redis (Upstash Free)
- Segredos: GitHub Secrets, Upstash Vault

## Módulos
- **gateway/**: API Gateway (FastAPI + Nginx)
- **trading/**: Bot de trading (Freqtrade)
- **dropshipping/**: Automação de checkout (Selenium)
- **afiliados/**: Scraper de cupons (Scrapy/BeautifulSoup)
- **arbitragem/**: Arbitragem de marketplaces (Scrapy + Selenium)
- **conteudo/**: Geração de conteúdo (GPT4All + Pandoc)
- **airflow/**: Orquestração de jobs

## Orquestração
- docker-compose.yml para todos os serviços
- Airflow define DAGs para cada módulo

## DevOps
- CI/CD: GitHub Actions, Container Registry, Ansible
- Monitoramento: Loki, Prometheus, Grafana, Alertmanager

## Monitoramento
- **Loki**: Coleta de logs centralizada (porta 3100)
- **Prometheus**: Coleta de métricas (porta 9090)
- **Grafana**: Dashboards e visualização (porta 3000, admin/admin)
- **Alertmanager**: Alertas por email/Slack (porta 9093)

### Acessos:
- **Grafana**: http://localhost:3000 (admin/admin)
- **Prometheus**: http://localhost:9090
- **Loki**: http://localhost:3100
- **Alertmanager**: http://localhost:9093

## Como rodar

### Pré-requisitos
- Docker Desktop instalado
- Git
- Mínimo 8GB de RAM (recomendado)

### Instalação
```bash
# Clone o repositório
git clone https://github.com/ParkNow914/bot.git
cd bot

# Suba todos os serviços
docker-compose up -d

# Verifique se está funcionando
docker-compose ps
```

### Testes
```bash
# Rodar testes de todos os módulos
docker-compose exec gateway pytest
docker-compose exec trading pytest
docker-compose exec dropshipping pytest
docker-compose exec afiliados pytest
docker-compose exec arbitragem pytest
docker-compose exec conteudo pytest
```

## API Documentation

### Endpoints Principais

#### Gateway (Porta 8080)
- `GET /` - Status do gateway
- `GET /health` - Health check
- `GET /system/status` - Status geral do sistema

#### Trading
- `GET /trading/status` - Status do bot de trading
- `GET /trading/trades` - Lista de trades ativos

#### Dropshipping
- `GET /dropshipping/orders` - Lista de pedidos
- `POST /dropshipping/orders` - Criar novo pedido

#### Afiliados
- `GET /afiliados/coupons` - Lista de cupons
- `GET /afiliados/coupons/{category}` - Cupons por categoria

#### Arbitragem
- `GET /arbitragem/opportunities` - Oportunidades de arbitragem
- `GET /arbitragem/opportunities/{product}` - Oportunidades por produto

#### Conteúdo
- `GET /conteudo/articles` - Lista de artigos gerados
- `GET /conteudo/articles/{topic}` - Artigos por tópico

### Exemplos de Uso

#### Verificar status do sistema:
```bash
curl http://localhost:8080/system/status
```

#### Verificar status do trading:
```bash
curl http://localhost:8080/trading/status
```

#### Criar pedido de dropshipping:
```bash
curl -X POST http://localhost:8080/dropshipping/orders \
  -H "Content-Type: application/json" \
  -d '{"product": "iPhone 15", "quantity": 1, "price": 4500.00, "status": "processing"}'
```

#### Buscar cupons de eletrônicos:
```bash
curl http://localhost:8080/afiliados/coupons/Eletrônicos
```

## Troubleshooting

### Problemas Comuns

1. **Erro de memória do Docker:**
   - Aumente a memória no Docker Desktop para 8GB
   - Ou configure o arquivo `.wslconfig` para WSL 2

2. **Porta já em uso:**
   - Verifique se não há outros serviços usando as portas
   - Use `docker-compose down` antes de subir novamente

3. **Container não inicia:**
   - Verifique os logs: `docker-compose logs [serviço]`
   - Reconstrua: `docker-compose build [serviço]`

4. **API não responde:**
   - Verifique se o gateway está rodando: `docker-compose ps`
   - Teste: `curl http://localhost:8080/health`

### Logs e Debug
```bash
# Ver logs de todos os serviços
docker-compose logs

# Ver logs de um serviço específico
docker-compose logs gateway

# Ver logs em tempo real
docker-compose logs -f trading
```

--- 

# Deploy em Railway

1. Crie uma conta gratuita em https://railway.app
2. Clique em "New Project" > "Deploy from GitHub repo"
3. Selecione este repositório e aguarde o build automático
4. Configure as variáveis de ambiente (.env) no painel Railway
5. Railway detecta automaticamente o Dockerfile/docker-compose.yml
6. Acesse a URL gerada para testar seu serviço

# Deploy em Render

1. Crie uma conta gratuita em https://render.com
2. Clique em "New Web Service" > "Connect a repository"
3. Escolha este repositório
4. Configure o ambiente para Docker
5. Adicione variáveis de ambiente conforme seu .env
6. Render faz o build e deploy automático
7. Acesse a URL gerada para testar

# Dicas Gerais
- Sempre configure as variáveis de ambiente de produção no painel da plataforma
- Para múltiplos serviços, use Railway/Render YAML ou suba cada serviço como um container separado
- Consulte a documentação oficial de cada plataforma para detalhes avançados 