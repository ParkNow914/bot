#!/bin/bash
# Backup automático do banco PostgreSQL (container 'postgres')
# Salva o dump no diretório atual com timestamp
# Dê permissão de execução: chmod +x scripts/backup_postgres.sh

TIMESTAMP=$(date +%F-%H%M)
BACKUP_FILE="backup_superbot_$TIMESTAMP.sql"

echo "Iniciando backup do banco..."
docker exec postgres pg_dump -U postgres superbot > $BACKUP_FILE
if [ $? -eq 0 ]; then
  echo "Backup realizado com sucesso: $BACKUP_FILE"
else
  echo "Erro ao realizar backup!"
fi 