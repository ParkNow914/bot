import time
import logging
import os
import subprocess
from datetime import datetime
from gpt4all import GPT4All

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SuperBotConteudo:
    def __init__(self):
        self.model = None
        self.output_dir = "/app/output"
        self.articles = []
        
        # Criar diretórios de saída
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "markdown"), exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "pdf"), exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "epub"), exist_ok=True)
    
    def setup_model(self):
        """Configura o modelo GPT4All"""
        try:
            # Em produção, seria um modelo real baixado
            # self.model = GPT4All("ggml-gpt4all-j-v1.3-groovy")
            
            logger.info("Modelo GPT4All configurado (simulado)")
            
        except Exception as e:
            logger.error(f"Erro ao configurar modelo: {e}")
            raise
    
    def start(self):
        """Inicia o gerador de conteúdo"""
        try:
            logger.info("Iniciando Super-Bot Conteúdo...")
            
            self.setup_model()
            
            # Loop principal
            while True:
                try:
                    # Gerar conteúdo
                    self._generate_content()
                    
                    # Converter formatos
                    self._convert_formats()
                    
                    # Aguardar 6 horas
                    time.sleep(21600)
                    
                except KeyboardInterrupt:
                    logger.info("Parando gerador de conteúdo...")
                    break
                except Exception as e:
                    logger.error(f"Erro no loop principal: {e}")
                    time.sleep(3600)
                    
        except Exception as e:
            logger.error(f"Erro ao inicializar gerador: {e}")
    
    def _generate_content(self):
        """Gera conteúdo usando IA"""
        try:
            logger.info("Gerando conteúdo...")
            
            # Tópicos para gerar artigos
            topics = [
                "Como investir em criptomoedas",
                "Dicas de dropshipping para iniciantes",
                "Estratégias de arbitragem online",
                "Marketing de afiliados em 2024",
                "Automação de negócios digitais"
            ]
            
            for topic in topics:
                try:
                    article = self._generate_article(topic)
                    self.articles.append(article)
                except Exception as e:
                    logger.error(f"Erro ao gerar artigo sobre {topic}: {e}")
            
            logger.info(f"Gerados {len(self.articles)} artigos!")
            
        except Exception as e:
            logger.error(f"Erro na geração de conteúdo: {e}")
    
    def _generate_article(self, topic):
        """Gera um artigo sobre um tópico específico"""
        try:
            logger.info(f"Gerando artigo sobre: {topic}")
            
            # Em produção, seria geração real com GPT4All
            # prompt = f"Escreva um artigo completo sobre {topic} em Markdown"
            # response = self.model.generate(prompt, max_tokens=1000)
            
            # Simular geração de conteúdo
            article_content = self._create_mock_article(topic)
            
            # Salvar artigo Markdown
            filename = f"{topic.lower().replace(' ', '_')}_{int(time.time())}.md"
            filepath = os.path.join(self.output_dir, "markdown", filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(article_content)
            
            article = {
                'topic': topic,
                'content': article_content,
                'filepath': filepath,
                'timestamp': time.time()
            }
            
            logger.info(f"Artigo salvo: {filepath}")
            return article
            
        except Exception as e:
            logger.error(f"Erro ao gerar artigo: {e}")
            return None
    
    def _create_mock_article(self, topic):
        """Cria um artigo simulado em Markdown"""
        return f"""# {topic}

## Introdução

Este é um artigo gerado automaticamente pelo Super-Bot sobre {topic}.

## Principais pontos

### 1. Conceitos básicos
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

### 2. Estratégias práticas
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

### 3. Dicas importantes
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.

## Conclusão

Este artigo foi gerado automaticamente pelo Super-Bot em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.

---
*Gerado por Super-Bot - Sistema de Automação Modular*
"""
    
    def _convert_formats(self):
        """Converte artigos para PDF e ePub"""
        try:
            logger.info("Convertendo formatos...")
            
            markdown_dir = os.path.join(self.output_dir, "markdown")
            pdf_dir = os.path.join(self.output_dir, "pdf")
            epub_dir = os.path.join(self.output_dir, "epub")
            
            for filename in os.listdir(markdown_dir):
                if filename.endswith('.md'):
                    filepath = os.path.join(markdown_dir, filename)
                    base_name = filename[:-3]  # Remove .md
                    
                    # Converter para PDF
                    self._convert_to_pdf(filepath, pdf_dir, base_name)
                    
                    # Converter para ePub
                    self._convert_to_epub(filepath, epub_dir, base_name)
            
            logger.info("Conversão de formatos concluída!")
            
        except Exception as e:
            logger.error(f"Erro na conversão de formatos: {e}")
    
    def _convert_to_pdf(self, markdown_file, output_dir, base_name):
        """Converte Markdown para PDF usando Pandoc"""
        try:
            output_file = os.path.join(output_dir, f"{base_name}.pdf")
            
            cmd = [
                'pandoc',
                markdown_file,
                '-o', output_file,
                '--pdf-engine=xelatex',
                '-V', 'geometry:margin=1in',
                '-V', 'fontsize=12pt'
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                logger.info(f"PDF gerado: {output_file}")
            else:
                logger.error(f"Erro ao gerar PDF: {result.stderr}")
                
        except Exception as e:
            logger.error(f"Erro na conversão para PDF: {e}")
    
    def _convert_to_epub(self, markdown_file, output_dir, base_name):
        """Converte Markdown para ePub usando Pandoc"""
        try:
            output_file = os.path.join(output_dir, f"{base_name}.epub")
            
            cmd = [
                'pandoc',
                markdown_file,
                '-o', output_file,
                '--toc',
                '--toc-depth=2'
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                logger.info(f"ePub gerado: {output_file}")
            else:
                logger.error(f"Erro ao gerar ePub: {result.stderr}")
                
        except Exception as e:
            logger.error(f"Erro na conversão para ePub: {e}")

if __name__ == "__main__":
    bot = SuperBotConteudo()
    bot.start() 