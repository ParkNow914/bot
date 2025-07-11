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

## Como rodar (em breve)

--- 