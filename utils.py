import subprocess
# Get IP Address

def get_wsl_host_ip():
    try:
        return subprocess.check_output("ip route show | grep default | awk '{print $3}'", shell=True).decode().strip()
    except:
        return 'your_server_ip_or_hostname'