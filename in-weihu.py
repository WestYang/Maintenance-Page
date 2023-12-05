import paramiko
import sys

def start_in_ng():
    server_ip = '10.120.34.13'
    server_port = 22
    server_user = '45505/10.100.28.21/root'
    server_password = 'yangsen....1'
    command = 'sh /usr/local/nginx/tool/start_maintenance.sh oa-corp'
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(server_ip, server_port, server_user, server_password)
        print(f"Executing command: {command}")
        stdin, stdout, stderr = ssh_client.exec_command(command)
        print(stdout.read().decode('utf-8'))
        print(stderr.read().decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        ssh_client.close()

def start_nord_ng():
    server_ip = '10.120.34.13'
    server_port = 22
    server_user = '45505/10.100.28.53/root'
    server_password = 'yangsen....1'
    command = 'sh /usr/local/nginx/tool/start_maintenance.sh contract contract-mobile'
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(server_ip, server_port, server_user, server_password)
        print(f"Executing command: {command}")
        stdin, stdout, stderr = ssh_client.exec_command(command)
        print(stdout.read().decode('utf-8'))
        print(stderr.read().decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        ssh_client.close()

def start_ex_ng():
    server_ip = '10.120.34.13'
    server_port = 22
    server_user = '45505/10.100.28.29/root'
    server_password = 'yangsen....1'
    command = 'sh /usr/local/nginx/tool/start_maintenance.sh oa-corp contract contract-mobile workflow'
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(server_ip, server_port, server_user, server_password)
        print(f"Executing command: {command}")
        stdin, stdout, stderr = ssh_client.exec_command(command)
        print(stdout.read().decode('utf-8'))
        print(stderr.read().decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        ssh_client.close()


def stop_in_ng():
    server_ip = '10.120.34.13'
    server_port = 22
    server_user = '45505/10.100.28.21/root'
    server_password = 'yangsen....1'
    command = 'sh /usr/local/nginx/tool/stop_maintenance.sh oa-corp'
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(server_ip, server_port, server_user, server_password)
        print(f"Executing command: {command}")
        stdin, stdout, stderr = ssh_client.exec_command(command)
        print(stdout.read().decode('utf-8'))
        print(stderr.read().decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        ssh_client.close()

def stop_nord_ng():
    server_ip = '10.120.34.13'
    server_port = 22
    server_user = '45505/10.100.28.53/root'
    server_password = 'yangsen....1'
    command = 'sh /usr/local/nginx/tool/stop_maintenance.sh contract contract-mobile'
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(server_ip, server_port, server_user, server_password)
        print(f"Executing command: {command}")
        stdin, stdout, stderr = ssh_client.exec_command(command)
        print(stdout.read().decode('utf-8'))
        print(stderr.read().decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        ssh_client.close()

def stop_ex_ng():
    server_ip = '10.120.34.13'
    server_port = 22
    server_user = '45505/10.100.28.29/root'
    server_password = 'yangsen....1'
    command = 'sh /usr/local/nginx/tool/stop_maintenance.sh oa-corp contract contract-mobile workflow'
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(server_ip, server_port, server_user, server_password)
        print(f"Executing command: {command}")
        stdin, stdout, stderr = ssh_client.exec_command(command)
        print(stdout.read().decode('utf-8'))
        print(stderr.read().decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        ssh_client.close()


def test_in_ng():
    server_ip = '10.120.34.13'
    server_port = 22
    server_user = '45505/10.100.28.21/root'
    server_password = 'yangsen....1'
    command = 'hostname'
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(server_ip, server_port, server_user, server_password)
        print(f"Executing command: {command}")
        stdin, stdout, stderr = ssh_client.exec_command(command)
        print(stdout.read().decode('utf-8'))
        print(stderr.read().decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        ssh_client.close()

def test_ex_ng():
    server_ip = '10.120.34.13'
    server_port = 22
    server_user = '45505/10.100.28.29/root'
    server_password = 'yangsen....1'
    command = 'hostname'
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(server_ip, server_port, server_user, server_password)
        print(f"Executing command: {command}")
        stdin, stdout, stderr = ssh_client.exec_command(command)
        print(stdout.read().decode('utf-8'))
        print(stderr.read().decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        ssh_client.close()

def test_nord_ng():
    server_ip = '10.120.34.13'
    server_port = 22
    server_user = '45505/10.100.28.53/root'
    server_password = 'yangsen....1'
    command = 'hostname'
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(server_ip, server_port, server_user, server_password)
        print(f"Executing command: {command}")
        stdin, stdout, stderr = ssh_client.exec_command(command)
        print(stdout.read().decode('utf-8'))
        print(stderr.read().decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        ssh_client.close()

arg = sys.argv[1]
if arg == 'start':
    start_in_ng()
    start_nord_ng()
    start_ex_ng()
if arg == 'stop':
    stop_in_ng()
    stop_nord_ng()
    stop_ex_ng()
if arg == 'test':
    test_in_ng()
    test_ex_ng()
    test_nord_ng()
