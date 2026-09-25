import gc
import os
import random
import time
import tracemalloc

import psutil

from algorithms.sorting import merge_sort


WORKLOAD_CONFIG = {
    "Light": {
        "size": 50000
    },
    "Medium": {
        "size": 200000
    },
    "Heavy": {
        "size": 500000
    }
}


def run_memory_benchmark(workload="Medium"):

    config = WORKLOAD_CONFIG.get(
        workload,
        WORKLOAD_CONFIG["Medium"]
    )

    size = config["size"]

    process = psutil.Process(
        os.getpid()
    )

    gc.collect()

    memory_before = (
        process.memory_info().rss
        / (1024 ** 2)
    )

    tracemalloc.start()

    start_time = time.perf_counter()

    data = [
        random.randint(1, 1_000_000)
        for _ in range(size)
    ]

    sorted_data = merge_sort(data)

    end_time = time.perf_counter()

    current_memory, peak_memory = (
        tracemalloc.get_traced_memory()
    )

    tracemalloc.stop()

    memory_after = (
        process.memory_info().rss
        / (1024 ** 2)
    )

    execution_time = (
        end_time - start_time
    )

    peak_memory_mb = (
        peak_memory / (1024 ** 2)
    )

    memory_change = max(
        0,
        memory_after - memory_before
    )

    score = calculate_memory_score(
        execution_time,
        peak_memory_mb
    )

    rating = get_memory_rating(
        score
    )

    del data
    del sorted_data

    gc.collect()

    return {
        "workload": workload,
        "items": size,

        "execution_time": round(
            execution_time,
            2
        ),

        "peak_memory": round(
            peak_memory_mb,
            1
        ),

        "memory_change": round(
            memory_change,
            1
        ),

        "score": score,
        "rating": rating
    }


def calculate_memory_score(
    execution_time,
    peak_memory
):

    if execution_time <= 0:
        return 9999

    speed_component = (
        5000 / execution_time
    )

    efficiency_component = (
        50000 / max(
            peak_memory,
            1
        )
    )

    score = int(
        speed_component
        + efficiency_component
    )

    return max(
        1000,
        min(
            score,
            9999
        )
    )


def get_memory_rating(score):

    if score >= 8000:
        return "Excellent"

    if score >= 6000:
        return "Very Good"

    if score >= 4000:
        return "Good"

    if score >= 2500:
        return "Average"

    return "Basic"