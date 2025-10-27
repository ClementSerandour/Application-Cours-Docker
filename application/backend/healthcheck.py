import sys

MAX_CPU = 80      # seuil CPU en %
MAX_RAM = 80      # seuil RAM en %

def get_cpu_usage():
    try:
        with open("/proc/stat", "r") as f:
            line = f.readline()
        cpu_times = list(map(int, line.strip().split()[1:]))
        idle, total = cpu_times[3], sum(cpu_times)
        return 100 * (1 - idle / total)
    except:
        return 0

def get_ram_usage():
    try:
        meminfo = {}
        with open("/proc/meminfo", "r") as f:
            for line in f:
                key, value = line.split(":")
                meminfo[key.strip()] = int(value.split()[0])
        total = meminfo["MemTotal"]
        free = meminfo["MemFree"] + meminfo.get("Buffers", 0) + meminfo.get("Cached", 0)
        used_percent = 100 * (total - free) / total
        return used_percent
    except:
        return 0

if __name__ == "__main__":
    cpu = get_cpu_usage()
    ram = get_ram_usage()

    if cpu > MAX_CPU:
        print(f"High CPU usage: {cpu:.1f}%")
        sys.exit(1)
    if ram > MAX_RAM:
        print(f"High RAM usage: {ram:.1f}%")
        sys.exit(1)

    print(f"Healthy - CPU: {cpu:.1f}%, RAM: {ram:.1f}%")
    sys.exit(0)