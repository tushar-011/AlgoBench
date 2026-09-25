import threading

import customtkinter as ctk

from tests.all_in_one_benchmark import (
    run_all_in_one_benchmark
)

from database.db import save_test_result


DISPLAY_NAMES = {
    "Bubble Sort": "Basic Data Processing (Bubble Sort)",
    "Insertion Sort": "Sequential Data Processing (Insertion Sort)",
    "Merge Sort": "Balanced Data Processing (Merge Sort)",
    "Quick Sort": "Fast Partition Processing (Quick Sort)"
}


class AllInOnePage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(
            (0, 1),
            weight=1
        )

        self.test_running = False

        self.create_header()
        self.create_test_panel()
        self.create_results_panel()

    def create_header(self):

        title = ctk.CTkLabel(
            self,
            text="Complete System Test",
            font=ctk.CTkFont(
                size=30,
                weight="bold"
            )
        )

        title.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="w",
            padx=30,
            pady=(30, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text=(
                "Run multiple performance tests "
                "and receive one overall system score."
            ),
            text_color="gray"
        )

        subtitle.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="w",
            padx=30,
            pady=(0, 25)
        )

    def create_test_panel(self):

        panel = ctk.CTkFrame(
            self,
            corner_radius=12
        )

        panel.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=(30, 10),
            pady=10
        )

        heading = ctk.CTkLabel(
            panel,
            text="Test Sequence",
            font=ctk.CTkFont(
                size=20,
                weight="bold"
            )
        )

        heading.pack(
            anchor="w",
            padx=25,
            pady=(25, 15)
        )

        tests = [
            "CPU Performance",
            "Memory Performance",
            "Processing Comparison",
            "System Stress"
        ]

        for test in tests:

            label = ctk.CTkLabel(
                panel,
                text=f"• {test}",
                text_color="gray"
            )

            label.pack(
                anchor="w",
                padx=25,
                pady=5
            )

        self.start_button = ctk.CTkButton(
            panel,
            text="Start Complete Test",
            height=45,
            command=self.start_test
        )

        self.start_button.pack(
            fill="x",
            padx=25,
            pady=(25, 25)
        )

    def create_results_panel(self):

        panel = ctk.CTkFrame(
            self,
            corner_radius=12
        )

        panel.grid(
            row=2,
            column=1,
            sticky="nsew",
            padx=(10, 30),
            pady=10
        )

        heading = ctk.CTkLabel(
            panel,
            text="Overall Results",
            font=ctk.CTkFont(
                size=20,
                weight="bold"
            )
        )

        heading.pack(
            anchor="w",
            padx=25,
            pady=(25, 15)
        )

        self.status_label = ctk.CTkLabel(
            panel,
            text="Ready to test",
            text_color="gray"
        )

        self.status_label.pack(
            pady=(5, 10)
        )

        self.progress_bar = ctk.CTkProgressBar(
            panel
        )

        self.progress_bar.pack(
            fill="x",
            padx=30,
            pady=(5, 20)
        )

        self.progress_bar.set(0)

        self.score_label = ctk.CTkLabel(
            panel,
            text="--",
            font=ctk.CTkFont(
                size=46,
                weight="bold"
            )
        )

        self.score_label.pack(
            pady=(5, 0)
        )

        ctk.CTkLabel(
            panel,
            text="Overall System Score",
            text_color="gray"
        ).pack()

        self.rating_label = ctk.CTkLabel(
            panel,
            text="--",
            font=ctk.CTkFont(
                size=22,
                weight="bold"
            )
        )

        self.rating_label.pack(
            pady=(15, 15)
        )

        self.cpu_label = ctk.CTkLabel(
            panel,
            text="CPU Score: --"
        )

        self.cpu_label.pack(
            pady=4
        )

        self.memory_label = ctk.CTkLabel(
            panel,
            text="Memory Score: --"
        )

        self.memory_label.pack(
            pady=4
        )

        self.processing_label = ctk.CTkLabel(
            panel,
            text="Best Processing Method: --",
            wraplength=350,
            justify="center"
        )

        self.processing_label.pack(
            pady=4,
            padx=20
        )

        self.stress_label = ctk.CTkLabel(
            panel,
            text="System Stability: --"
        )

        self.stress_label.pack(
            pady=4
        )

    def start_test(self):

        if self.test_running:
            return

        self.test_running = True

        self.start_button.configure(
            state="disabled"
        )

        self.status_label.configure(
            text="Starting tests..."
        )

        self.progress_bar.set(0)

        self.score_label.configure(
            text="--"
        )

        self.rating_label.configure(
            text="Testing..."
        )

        self.cpu_label.configure(
            text="CPU Score: --"
        )

        self.memory_label.configure(
            text="Memory Score: --"
        )

        self.processing_label.configure(
            text="Best Processing Method: --"
        )

        self.stress_label.configure(
            text="System Stability: --"
        )

        thread = threading.Thread(
            target=self.run_test,
            daemon=True
        )

        thread.start()

    def run_test(self):

        try:

            results = run_all_in_one_benchmark(
                progress_callback=(
                    self.progress_update
                )
            )

            self.after(
                0,
                lambda:
                self.display_results(
                    results
                )
            )

        except Exception as error:

            self.after(
                0,
                lambda:
                self.show_error(
                    str(error)
                )
            )

    def progress_update(
        self,
        stage,
        progress
    ):

        self.after(
            0,
            lambda:
            self.update_progress_ui(
                stage,
                progress
            )
        )

    def update_progress_ui(
        self,
        stage,
        progress
    ):

        self.status_label.configure(
            text=stage
        )

        self.progress_bar.set(
            progress
        )

    def display_results(
        self,
        results
    ):

        self.test_running = False

        self.start_button.configure(
            state="normal"
        )

        self.progress_bar.set(1)

        self.status_label.configure(
            text="Complete test finished"
        )

        self.score_label.configure(
            text=str(
                results[
                    "overall_score"
                ]
            )
        )

        self.rating_label.configure(
            text=results[
                "rating"
            ]
        )

        self.cpu_label.configure(
            text=(
                "CPU Score: "
                f"{results['cpu']['score']}"
            )
        )

        self.memory_label.configure(
            text=(
                "Memory Score: "
                f"{results['memory']['score']}"
            )
        )

        fastest = (
            results[
                "performance"
            ][
                "results"
            ][0]
        )

        fastest_name = (
            DISPLAY_NAMES.get(
                fastest["name"],
                fastest["name"]
            )
        )

        self.processing_label.configure(
            text=(
                "Best Processing Method: "
                f"{fastest_name}"
            )
        )

        self.stress_label.configure(
            text=(
                "System Stability: "
                f"{results['stress']['stability']}"
            )
        )

        save_test_result(
            test_type="Complete System Test",
            mode="Standard",
            score=results[
                "overall_score"
            ],
            result=results[
                "rating"
            ],
            details=results
        )

    def show_error(
        self,
        error
    ):

        self.test_running = False

        self.start_button.configure(
            state="normal"
        )

        self.progress_bar.set(0)

        self.status_label.configure(
            text="Complete test failed"
        )

        self.rating_label.configure(
            text=error
        )

        self.cpu_label.configure(
            text="CPU Score: --"
        )

        self.memory_label.configure(
            text="Memory Score: --"
        )

        self.processing_label.configure(
            text="Best Processing Method: --"
        )

        self.stress_label.configure(
            text="System Stability: --"
        )