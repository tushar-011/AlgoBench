import random
import time

import psutil

from algorithms.sorting import merge_sort


STRESS_CONFIG = {
    "Light": {
        "size": 20000,
        "pause": 0.08
    },
    "Medium": {
        "size": 50000,
        "pause": 0.04
    },
    "Heavy": {
        "size": 100000,
        "pause": 0.01
    }
}


def run_stress_test(
    intensity,
    duration,
    stop_event,
    progress_callback=None
):

    config = STRESS_CONFIG.get(
        intensity,
        STRESS_CONFIG["Medium"]
    )

    size = config["size"]
    pause = config["pause"]

    start_time = time.perf_counter()

    cpu_samples = []
    memory_samples = []

    completed_cycles = 0
    processed_items = 0

    psutil.cpu_percent(
        interval=None
    )

    while True:

        if stop_event.is_set():
            break

        elapsed = (
            time.perf_counter()
            - start_time
        )

        if elapsed >= duration:
            break

        data = [
            random.randint(
                1,
                1_000_000
            )
            for _ in range(size)
        ]

        merge_sort(data)

        completed_cycles += 1
        processed_items += size

        cpu_usage = (
            psutil.cpu_percent(
                interval=None
            )
        )

        memory_usage = (
            psutil.virtual_memory().percent
        )

        cpu_samples.append(
            cpu_usage
        )

        memory_samples.append(
            memory_usage
        )

        if progress_callback:

            progress_callback({
                "elapsed": elapsed,
                "cpu": cpu_usage,
                "memory": memory_usage,
                "cycles": completed_cycles,
                "processed_items": processed_items
            })

        time.sleep(
            pause
        )

    total_time = (
        time.perf_counter()
        - start_time
    )

    average_cpu = (
        sum(cpu_samples)
        / len(cpu_samples)
        if cpu_samples
        else 0
    )

    peak_cpu = (
        max(cpu_samples)
        if cpu_samples
        else 0
    )

    average_memory = (
        sum(memory_samples)
        / len(memory_samples)
        if memory_samples
        else 0
    )

    peak_memory = (
        max(memory_samples)
        if memory_samples
        else 0
    )

    stability = calculate_stability(
        average_cpu,
        peak_cpu
    )

    return {
        "intensity": intensity,
        "duration": round(
            total_time,
            1
        ),
        "cycles": completed_cycles,
        "processed_items": processed_items,
        "average_cpu": round(
            average_cpu,
            1
        ),
        "peak_cpu": round(
            peak_cpu,
            1
        ),
        "average_memory": round(
            average_memory,
            1
        ),
        "peak_memory": round(
            peak_memory,
            1
        ),
        "stability": stability,
        "stopped": stop_event.is_set()
    }


def calculate_stability(
    average_cpu,
    peak_cpu
):

    if peak_cpu < 60:
        return "Stable"

    if peak_cpu < 80:
        return "Good"

    if peak_cpu < 95:
        return "Under Heavy Load"

    return "Maximum Load"