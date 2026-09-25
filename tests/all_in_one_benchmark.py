import threading

from tests.cpu_benchmark import run_cpu_benchmark
from tests.memory_benchmark import run_memory_benchmark
from tests.performance_benchmark import run_performance_benchmark
from tests.stress_benchmark import run_stress_test


def run_all_in_one_benchmark(
    progress_callback=None
):

    results = {}

    if progress_callback:
        progress_callback(
            "CPU Test",
            0.10
        )

    cpu_result = run_cpu_benchmark(
        "Medium"
    )

    results["cpu"] = cpu_result

    if progress_callback:
        progress_callback(
            "Memory Test",
            0.35
        )

    memory_result = run_memory_benchmark(
        "Medium"
    )

    results["memory"] = memory_result

    if progress_callback:
        progress_callback(
            "Performance Test",
            0.60
        )

    performance_result = (
        run_performance_benchmark(
            "Medium"
        )
    )

    results["performance"] = (
        performance_result
    )

    if progress_callback:
        progress_callback(
            "Stress Test",
            0.80
        )

    stop_event = threading.Event()

    stress_result = run_stress_test(
        intensity="Medium",
        duration=8,
        stop_event=stop_event
    )

    results["stress"] = stress_result

    if progress_callback:
        progress_callback(
            "Calculating Results",
            0.95
        )

    overall_score = calculate_overall_score(
        cpu_result,
        memory_result,
        performance_result,
        stress_result
    )

    rating = get_overall_rating(
        overall_score
    )

    results["overall_score"] = (
        overall_score
    )

    results["rating"] = rating

    if progress_callback:
        progress_callback(
            "Completed",
            1.0
        )

    return results


def calculate_overall_score(
    cpu_result,
    memory_result,
    performance_result,
    stress_result
):

    cpu_score = cpu_result[
        "score"
    ]

    memory_score = memory_result[
        "score"
    ]

    performance_score = (
        calculate_performance_score(
            performance_result
        )
    )

    stress_score = (
        calculate_stress_score(
            stress_result
        )
    )

    overall = (
        cpu_score * 0.35
        +
        memory_score * 0.30
        +
        performance_score * 0.20
        +
        stress_score * 0.15
    )

    return int(
        min(
            overall,
            9999
        )
    )


def calculate_performance_score(
    performance_result
):

    results = performance_result[
        "results"
    ]

    fastest_time = results[0][
        "time"
    ]

    if fastest_time <= 0:
        return 9999

    score = int(
        7000 / (
            1 + fastest_time
        )
    )

    return max(
        1000,
        min(
            score,
            9999
        )
    )


def calculate_stress_score(
    stress_result
):

    stability = stress_result[
        "stability"
    ]

    stability_scores = {
        "Stable": 8500,
        "Good": 7500,
        "Under Heavy Load": 6000,
        "Maximum Load": 4500
    }

    return stability_scores.get(
        stability,
        5000
    )


def get_overall_rating(
    score
):

    if score >= 8000:
        return "Excellent"

    if score >= 6500:
        return "Very Good"

    if score >= 5000:
        return "Good"

    if score >= 3500:
        return "Average"

    return "Basic"