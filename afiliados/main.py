import time
import logging
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import os

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SuperBotAfiliados:
    def __init__(self):
        self.coupons = []
        self.output_dir = "/app/output"
        
        # Criar diretório de saída se não existir
        os.makedirs(self.output_dir, exist_ok=True)
    
    def start(self):
        """Inicia o bot de afiliados"""
        try:
            logger.info("Iniciando Super-Bot Afiliados...")
            
            # Loop principal
            while True:
                try:
                    # Executar coleta de cupons
                    self._collect_coupons()
                    
                    # Gerar HTML estático
                    self._generate_html()
                    
                    # Aguardar 1 hora
                    time.sleep(3600)
                    
                except KeyboardInterrupt:
                    logger.info("Parando bot de afiliados...")
                    break
                except Exception as e:
                    logger.error(f"Erro no loop principal: {e}")
                    time.sleep(300)
                    
        except Exception as e:
            logger.error(f"Erro ao inicializar bot: {e}")
    
    def _collect_coupons(self):
        """Coleta cupons de afiliados"""
        try:
            logger.info("Coletando cupons de afiliados...")
            
            # Simular coleta de cupons de diferentes sites
            sites = [
                "https://example-coupon-site1.com",
                "https://example-coupon-site2.com",
                "https://example-coupon-site3.com"
            ]
            
            for site in sites:
                try:
                    self._scrape_site(site)
                except Exception as e:
                    logger.error(f"Erro ao coletar de {site}: {e}")
            
            logger.info(f"Coletados {len(self.coupons)} cupons!")
            
        except Exception as e:
            logger.error(f"Erro na coleta de cupons: {e}")
    
    def _scrape_site(self, url):
        """Scrapa um site específico para cupons"""
        try:
            # Simular requisição HTTP
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            # Em produção, seria uma requisição real
            # response = requests.get(url, headers=headers)
            # soup = BeautifulSoup(response.content, 'html.parser')
            
            # Simular cupons encontrados
            mock_coupons = [
                {
                    'code': f'COUPON{i}',
                    'description': f'Desconto {i*10}%',
                    'site': url,
                    'expiry': '2024-12-31',
                    'category': 'Eletrônicos'
                }
                for i in range(1, 6)
            ]
            
            self.coupons.extend(mock_coupons)
            logger.info(f"Coletados {len(mock_coupons)} cupons de {url}")
            
        except Exception as e:
            logger.error(f"Erro ao fazer scraping de {url}: {e}")
    
    def _generate_html(self):
        """Gera HTML estático com os cupons"""
        try:
            logger.info("Gerando HTML estático...")
            
            html_content = self._create_html_template()
            
            # Salvar arquivo HTML
            output_file = os.path.join(self.output_dir, "coupons.html")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            logger.info(f"HTML gerado em: {output_file}")
            
        except Exception as e:
            logger.error(f"Erro ao gerar HTML: {e}")
    
    def _create_html_template(self):
        """Cria template HTML para os cupons"""
        html = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Super-Bot Cupons</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .coupon {{ border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 5px; }}
        .code {{ background: #f0f0f0; padding: 5px; font-family: monospace; }}
        .expiry {{ color: #666; font-size: 0.9em; }}
    </style>
</head>
<body>
    <h1>Super-Bot Cupons de Afiliados</h1>
    <p>Última atualização: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    <p>Total de cupons: {len(self.coupons)}</p>
    
    <div class="coupons">
"""
        
        for coupon in self.coupons:
            html += f"""
        <div class="coupon">
            <h3>{coupon['description']}</h3>
            <p><strong>Código:</strong> <span class="code">{coupon['code']}</span></p>
            <p><strong>Site:</strong> {coupon['site']}</p>
            <p><strong>Categoria:</strong> {coupon['category']}</p>
            <p class="expiry"><strong>Válido até:</strong> {coupon['expiry']}</p>
        </div>
"""
        
        html += """
    </div>
</body>
</html>
"""
        return html

if __name__ == "__main__":
    bot = SuperBotAfiliados()
    bot.start() 