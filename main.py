import socket
import requests

TOKEN = "6164402442:AAHCi6reHElgVXukVa4hdIBswWDQqUaza-w"
ID = "290714995"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

ip_list = {
    "MIWISH": "192.168.100.234",
    "Domo_Belgrano": "192.168.100.74",
    "INTERNET": "8.8.8.8",
    "Domo_Apaza": "192.168.100.70"
}

flag = True
faill_ips = []

for name, ip_address in ip_list.items():
  s = socket.socket()
  s.settimeout(1)
  try:
    s.connect((ip_address, 80))
    print(f"Success >> {ip_address} {name}")
  except:
    print(f"Fail >> {ip_address} {name}")
    faill_ips.append(name)
    flag = False

  s.close()

if not flag:
  message = f"Dish [FAILL] > {' '.join(faill_ips)}"
  payload = {"chat_id": ID, "text": message}
  requests.post(url=url, params=payload)
else:
  message = "Dish [OK]"
  payload = {"chat_id": ID, "text": message}
  requests.post(url=url, params=payload)
