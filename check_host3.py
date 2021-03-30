import subprocess
import concurrent.futures
import time

# waktu awal
T1 = time.perf_counter()

# list ip
hosts = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '8.8.8.8', '8.8.4.4']

# fungsi cek host
def check_host(ip):
    status, result = subprocess.getstatusoutput("ping -c1 " + ip)
    if (status == 0):
        return f'Host {ip} is UP'
    else:
        return f'Host {ip} is DOWN'

# proses multi processing
with concurrent.futures.ProcessPoolExecutor() as executor:
    results = executor.map(check_host, hosts)
    for results in results:
        print(results)

T2 = time.perf_counter()

# cetak total waktu
print(f"selesai dalam : {round(T2 - T1, 2)} detik")