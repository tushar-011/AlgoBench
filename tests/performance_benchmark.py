import random
import time

from algorithms.sorting import (
    bubble_sort,
    insertion_sort,
    merge_sort,
    quick_sort
)


ALGORITHMS = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort
}


WORKLOAD_CONFIG = {
    "Light": 1000,
    "Medium": 3000,
    "Heavy": 6000
}


def run_performance_benchmark(
    workload="Medium"
):

    size = WORKLOAD_CONFIG.get(
        workload,
        WORKLOAD_CONFIG["Medium"]
    )

    original_data = [
        random.randint(
            1,
            100000
        )
        for _ in range(size)
    ]

    results = []

    for name, algorithm in (
        ALGORITHMS.items()
    ):

        data = original_data.copy()

        start_time = (
            time.perf_counter()
        )

        algorithm(data)

        end_time = (
            time.perf_counter()
        )

        execution_time = (
            end_time
            -
            start_time
        )

        results.append({
            "name": name,
            "time": execution_time
        })

    fastest_time = min(
        result["time"]
        for result in results
    )

    for result in results:

        result["relative_speed"] = (
            fastest_time
            /
            result["time"]
            *
            100
        )

        result["time"] = round(
            result["time"],
            4
        )

        result["relative_speed"] = (
            round(
                result[
                    "relative_speed"
                ],
                1
            )
        )

    results.sort(
        key=lambda item:
        item["time"]
    )

    return {
        "workload": workload,
        "items": size,
        "results": results
    }