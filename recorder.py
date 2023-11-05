import os
import time
import psutil

# Define the log file path (change it to your desired location)
log_file = '/root/logfile.txt'

# Function to get CPU temperature
def get_cpu_temperature():
    try:
        # Read CPU temperature from the thermal zone file
        with open('/sys/class/thermal/thermal_zone0/temp', 'r') as temp_file:
            temperature = int(temp_file.read()) / 1000.0  # Convert to degrees Celsius
        return temperature
    except Exception as e:
        print(f"Error reading CPU temperature: {str(e)}")
        return None

# Function to log data
def log_data():
    while True:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        cpu_temperature = get_cpu_temperature()
        cpu_percent = psutil.cpu_percent(interval=1)  # Get CPU usage percentage
        log_entry = f"{timestamp}, CPU Temp: {cpu_temperature}      C, CPU %: {cpu_percent}%"

        with open(log_file, 'a') as file:
            file.write(log_entry + '\n')

        print(log_entry)
        time.sleep(10)  # Log data every 60 seconds

if __name__ == "__main__":
    if not os.path.exists(log_file):
        open(log_file, 'w').close()  # Create the log file if it doesn't exist
    log_data()
