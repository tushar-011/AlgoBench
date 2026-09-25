import random
import time

import psutil

from algorithms.sorting import merge_sort


WORKLOAD_CONFIG = {
    "Light": {
        "size": 25000,
        "repetitions": 2
    },
    "Medium": {
        "size": 100000,
        "repetitions": 4
    },
    "Heavy": {
        "size": 300000,
        "repetitions": 6
    }
}


def run_cpu_benchmark(workload="Medium"):

    config = WORKLOAD_CONFIG.get(
        workload,
        WORKLOAD_CONFIG["Medium"]
    )

    size = config["size"]
    repetitions = config["repetitions"]

    total_items = size * repetitions

    cpu_samples = []

    start_time = time.perf_counter()

    for _ in range(repetitions):

        data = [
            random.randint(1, 1_000_000)
            for _ in range(size)
        ]

        cpu_samples.append(
            psutil.cpu_percent(interval=None)
        )

        merge_sort(data)

        cpu_samples.append(
            psutil.cpu_percent(interval=None)
        )

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    processing_rate = (
        total_items / execution_time
        if execution_time > 0
        else 0
    )

    peak_cpu = (
        max(cpu_samples)
        if cpu_samples
        else 0
    )

    average_cpu = (
        sum(cpu_samples) / len(cpu_samples)
        if cpu_samples
        else 0
    )

    score = calculate_score(
        processing_rate
    )

    rating = get_performance_rating(
        score
    )

    return {
        "workload": workload,
        "execution_time": round(
            execution_time,
            2
        ),
        "peak_cpu": round(
            peak_cpu,
            1
        ),
        "average_cpu": round(
            average_cpu,
            1
        ),
        "score": score,
        "rating": rating,
        "total_items": total_items,
        "processing_rate": int(
            processing_rate
        )
    }


def calculate_score(processing_rate):

    score = int(
        processing_rate / 40
    )

    return min(
        score,
        9999
    )


def get_performance_rating(score):

    if score >= 8000:
        return "Excellent"

    if score >= 6000:
        return "Very Good"

    if score >= 4000:
        return "Good"

    if score >= 2000:
        return "Average"

    return "Basic"