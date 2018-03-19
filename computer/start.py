import os
import json
from pathlib import Path
from dotenv import load_dotenv
import socket
import paramiko
import time
import subprocess
import http.server
import socketserver

# Source the environment variables
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

sensor_count = int(os.getenv('NUMBER_SENSORS'))
pi_username = os.getenv('PI_USERNAME')
pi_password = os.getenv('PI_PASSWORD')
computer_ip = socket.gethostbyname(socket.gethostname())
server_port = int(os.getenv('SERVER_PORT'))

# Query the router for the connected devices.
# This is specific to the Card-King AC 1200M Wireless Router
# It's worth noticing that I can do this so long as I'm on the network.
os.system('mkdir -p tmp')
os.system("curl 'http://192.168.0.1/protocol.csp?fname=system&opt=main&function=get' -X POST -H 'Content-Length: 0' --compressed > tmp/systemMainData.json")
data = json.load(open('tmp/systemMainData.json'))
os.system('rm -rf tmp')

# Prune the devices to be those currently on the network
terminals = list(filter(lambda x: len(x['ip']) != 0, data['terminals']))

# Make sure all the connected devices are on the network
if len(data['terminals']) != sensor_count + 1:
	raise Exception(f"Detected {len(terminals) - 1} of {sensor_count} sensor(s).")

# We have the requisite number of devices, get the ips for the sensors
sensor_ips = list(filter(lambda x: x!= computer_ip, map(lambda x: x['ip'], terminals)))

# Handler = http.server.SimpleHTTPRequestHandler
# with socketserver.TCPServer(("", server_port), Handler) as httpd:
# 	print("serving at port", server_port)
# 	httpd.serve_forever()

# 	time.sleep(1)
# 	# SSH into each of the pis and get them ready to stream data
# 	for sensor in sensor_ips:
# 		ssh = paramiko.SSHClient()
# 		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 		ssh.connect(sensor, username=pi_username, password=pi_password)
# 		ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f'curl http://{computer_ip}:{server_port}')
print(sensor_ips)