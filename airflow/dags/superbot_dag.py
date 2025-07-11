from airflow import DAG
from airflow.operators.bash import BashOperator
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

[trading, dropshipping, afiliados, arbitragem] >> conteudo 