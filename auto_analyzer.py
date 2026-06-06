import os
import time

# File containing the discovered devices
input_file = "discovered_devices.txt"
# File to save final reports
output_file = "network_scan_results.txt"

print("Automated scanning system is ready...")

def analyze():
    # Check if the input file exists
    if not os.path.exists(input_file):
        print("Waiting for new device discoveries...")
        return

    # Read unique IPs to avoid redundant scans
    with open(input_file, "r") as f:
        ips = set(line.strip() for line in f)

    for ip in ips:
        print(f"Scanning discovered device: {ip}")
        # Run nmap with -Pn flag to skip host discovery (Ping)
        # Using redirection to append results to the report file
        command = f"nmap -Pn {ip} >> {output_file}"
        os.system(command)
        print(f"Report for {ip} saved to {output_file}")

# Run the analysis loop every 60 seconds
while True:
    analyze()
    time.sleep(60)
