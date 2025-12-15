#!/home/austin/code/python/proj/python-helpers/ip-addr-poll/.venv/bin/python
import httpx
import os
from datetime import datetime

def append_to_file(file_path, text):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, file_path)          
    with open(full_path, 'a') as file:
        file.write(text + '\n')

def main():
    response = httpx.get('https://ipv4.icanhazip.com')
    ip_addr = response.text.strip()  
    
    response1 = httpx.get('https://icanhazip.com')
    ipv6 = response1.text.strip()  

    current_time = datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')
    
    output_string = (
        f"DateTime: {current_time} - IPv4 Address: {ip_addr}\n"
        f"{' ' * 35}IPv6 Address: {ipv6}\n\n"
    )
    
    print(output_string)
    
    append_to_file('dynamic-IP-log.txt', output_string)


if __name__ == "__main__":
    main()
    
# in the terminal, run: chmod +x main.py
# crontab -e
# */10 * * * * /home/austin/code/python/proj/python-helpers/ip-addr-poll/main.py
# --- add the above line to the end of the crontab file ---
# --- runs every 10 minutes ---
# verify with: crontab -l
# make sure cron is running: sudo systemctl status cron