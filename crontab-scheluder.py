import os

def schedule_task(command, schedule_time):
    """
    Função para agendar uma tarefa utilizando o crontab.
    :param command: Comando a ser executado
    :param schedule_time: Hora de execução no formato cron (ex: "0 2 * * *" para rodar às 2h)
    :return: None
    """
    cron_job = f"{schedule_time} {command}"
    with open("/etc/crontab", "a") as cron_file:
        cron_file.write(cron_job + "\n")
    print(f"Tarefa agendada para: {schedule_time}")

# Exemplo de agendamento
command = "python3 /path/to/backup_script.py"
schedule_time = "0 2 * * *"  # Executa todos os dias às 2h da manhã
schedule_task(command, schedule_time)
