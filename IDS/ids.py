import psutil
import time
import datetime

# Function to check for suspicious behavior (you can add more checks here)
def is_suspicious(proc):
    # Example check: high CPU usage
    if proc.cpu_percent(interval=1) > 80:
        return "High CPU usage"
    # Add other checks (e.g., suspicious process names, network activity, etc.)
    if check_network_activity(proc):
    	return "Unexpected Network Activity"
    
    if check_high_memory_usage(proc):
    	return "High Memory Usage"

    return None

def check_high_memory_usage(proc, memory_threshold=100000000):  # 100 MB threshold
    try:
        memory_usage = proc.memory_info().rss  # Resident Set Size
        if memory_usage > memory_threshold:
            return True
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass
    return False


def check_network_activity(proc):
    try:
        connections = proc.connections(kind='inet')
        if connections:
            return True
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass
    return False

# Function to calculate process age
def get_process_age(proc):
    try:
        start_time = proc.create_time()
        now = time.time()
        age_seconds = now - start_time
        return str(datetime.timedelta(seconds=int(age_seconds)))
    except Exception:
        return "Unknown"

# Main loop to check all processes
for proc in psutil.process_iter(['pid', 'name', 'username', 'create_time']):
    try:
        reason = is_suspicious(proc)
        if reason:
            print(f"Flagged Process: {proc.info['name']} (PID: {proc.info['pid']}, "
                  f"Age: {get_process_age(proc)}, Owner: {proc.info['username']}, "
                  f"Flagged for: {reason})")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        continue
