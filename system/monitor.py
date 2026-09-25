import platform
import socket
import time

import psutil


def get_cpu_usage():
    return psutil.cpu_percent(interval=None)


def get_memory_usage():
    memory = psutil.virtual_memory()

    return {
        "percent": memory.percent,
        "used_gb": round(memory.used / (1024 ** 3), 1),
        "total_gb": round(memory.total / (1024 ** 3), 1)
    }


def get_battery_info():
    battery = psutil.sensors_battery()

    if battery is None:
        return {
            "percent": None,
            "charging": False,
            "available": False
        }

    return {
        "percent": battery.percent,
        "charging": battery.power_plugged,
        "available": True
    }


def get_disk_usage():
    disk = psutil.disk_usage("/")

    return {
        "percent": disk.percent,
        "used_gb": round(disk.used / (1024 ** 3), 1),
        "total_gb": round(disk.total / (1024 ** 3), 1),
        "free_gb": round(disk.free / (1024 ** 3), 1)
    }


def get_system_info():
    processor = platform.processor()

    if not processor:
        processor = "Processor information unavailable"

    return {
        "device_name": socket.gethostname(),
        "os": f"{platform.system()} {platform.release()}",
        "processor": processor,
        "architecture": platform.machine(),
        "physical_cores": psutil.cpu_count(logical=False),
        "threads": psutil.cpu_count(logical=True)
    }


def get_system_uptime():
    boot_time = psutil.boot_time()

    uptime_seconds = int(time.time() - boot_time)

    days = uptime_seconds // 86400
    hours = (uptime_seconds % 86400) // 3600
    minutes = (uptime_seconds % 3600) // 60

    if days > 0:
        return f"{days}d {hours}h {minutes}m"

    if hours > 0:
        return f"{hours}h {minutes}m"

    return f"{minutes}m"