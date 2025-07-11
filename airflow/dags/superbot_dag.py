from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'superbot',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'superbot_dag',
    default_args=default_args,
    description='Orquestração dos módulos do Super-Bot',
    schedule_interval=timedelta(hours=1),
    start_date=datetime(2024, 1, 1),
    catchup=False,
)

# Healthchecks dos microserviços
trading_health = SimpleHttpOperator(
    task_id='trading_health',
    http_conn_id='trading_service',
    endpoint='/health',
    method='GET',
    dag=dag,
)
dropshipping_health = SimpleHttpOperator(
    task_id='dropshipping_health',
    http_conn_id='dropshipping_service',
    endpoint='/health',
    method='GET',
    dag=dag,
)
afiliados_health = SimpleHttpOperator(
    task_id='afiliados_health',
    http_conn_id='afiliados_service',
    endpoint='/health',
    method='GET',
    dag=dag,
)
arbitragem_health = SimpleHttpOperator(
    task_id='arbitragem_health',
    http_conn_id='arbitragem_service',
    endpoint='/health',
    method='GET',
    dag=dag,
)
conteudo_health = SimpleHttpOperator(
    task_id='conteudo_health',
    http_conn_id='conteudo_service',
    endpoint='/health',
    method='GET',
    dag=dag,
)

trading = BashOperator(
    task_id='trading',
    bash_command='echo "Executando trading..."',
    dag=dag,
)
dropshipping = BashOperator(
    task_id='dropshipping',
    bash_command='echo "Executando dropshipping..."',
    dag=dag,
)
afiliados = BashOperator(
    task_id='afiliados',
    bash_command='echo "Executando afiliados..."',
    dag=dag,
)
arbitragem = BashOperator(
    task_id='arbitragem',
    bash_command='echo "Executando arbitragem..."',
    dag=dag,
)
conteudo = BashOperator(
    task_id='conteudo',
    bash_command='echo "Executando conteudo..."',
    dag=dag,
)

# Dependências: healthcheck -> execução
tasks = [
    (trading_health, trading),
    (dropshipping_health, dropshipping),
    (afiliados_health, afiliados),
    (arbitragem_health, arbitragem),
    (conteudo_health, conteudo),
]
for health, exec_ in tasks:
    health >> exec_

[trading, dropshipping, afiliados, arbitragem] >> conteudo 