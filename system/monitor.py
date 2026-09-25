import os
import platform
import socket
import subprocess
import time

import psutil


def get_windows_cpu_name():

    if platform.system() != "Windows":
        return platform.processor()

    try:

        command = [
            "powershell",
            "-NoProfile",
            "-Command",
            "(Get-CimInstance Win32_Processor).Name"
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        )

        cpu_name = result.stdout.strip()

        if cpu_name:
            return cpu_name

    except Exception:
        pass

    return platform.processor()


def get_processor_name():

    processor = get_windows_cpu_name()

    if processor:
        return processor

    processor = platform.processor()

    if processor:
        return processor

    return "Processor information unavailable"


def get_cpu_usage():

    return psutil.cpu_percent(
        interval=None
    )


def get_memory_usage():

    memory = psutil.virtual_memory()

    return {
        "percent": memory.percent,

        "used_gb": round(
            memory.used
            / (1024 ** 3),
            1
        ),

        "total_gb": round(
            memory.total
            / (1024 ** 3),
            1
        ),

        "available_gb": round(
            memory.available
            / (1024 ** 3),
            1
        )
    }


def get_battery_info():

    try:

        battery = (
            psutil.sensors_battery()
        )

    except Exception:

        battery = None

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

    if platform.system() == "Windows":

        system_drive = os.environ.get(
            "SystemDrive",
            "C:"
        )

        disk_path = (
            f"{system_drive}\\"
        )

    else:

        disk_path = "/"

    disk = psutil.disk_usage(
        disk_path
    )

    return {
        "percent": disk.percent,

        "used_gb": round(
            disk.used
            / (1024 ** 3),
            1
        ),

        "total_gb": round(
            disk.total
            / (1024 ** 3),
            1
        ),

        "free_gb": round(
            disk.free
            / (1024 ** 3),
            1
        )
    }


def get_system_info():

    processor = (
        get_processor_name()
    )

    physical_cores = (
        psutil.cpu_count(
            logical=False
        )
    )

    threads = (
        psutil.cpu_count(
            logical=True
        )
    )

    if physical_cores is None:
        physical_cores = 0

    if threads is None:
        threads = 0

    return {
        "device_name": (
            socket.gethostname()
        ),

        "os": (
            f"{platform.system()} "
            f"{platform.release()}"
        ),

        "processor": processor,

        "architecture": (
            platform.machine()
        ),

        "physical_cores": (
            physical_cores
        ),

        "threads": threads
    }


def get_system_uptime():

    boot_time = (
        psutil.boot_time()
    )

    uptime_seconds = int(
        time.time()
        - boot_time
    )

    days = (
        uptime_seconds
        // 86400
    )

    hours = (
        uptime_seconds
        % 86400
    ) // 3600

    minutes = (
        uptime_seconds
        % 3600
    ) // 60

    if days > 0:

        return (
            f"{days}d "
            f"{hours}h "
            f"{minutes}m"
        )

    if hours > 0:

        return (
            f"{hours}h "
            f"{minutes}m"
        )

    return f"{minutes}m"