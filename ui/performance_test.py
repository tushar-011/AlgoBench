import threading

import customtkinter as ctk

from tests.performance_benchmark import (
    run_performance_benchmark
)

from database.db import save_test_result


DISPLAY_NAMES = {
    "Bubble Sort": "Basic Data Processing (Bubble Sort)",
    "Insertion Sort": "Sequential Data Processing (Insertion Sort)",
    "Merge Sort": "Balanced Data Processing (Merge Sort)",
    "Quick Sort": "Fast Partition Processing (Quick Sort)"
}


class PerformanceTestPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(
            (0, 1),
            weight=1
        )

        self.create_header()
        self.create_test_panel()
        self.create_results_panel()

    def create_header(self):

        title = ctk.CTkLabel(
            self,
            text="Performance Comparison",
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
                "Compare how efficiently different "
                "processing methods handle the same workload."
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
            text="Test Configuration",
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

        ctk.CTkLabel(
            panel,
            text="Workload Level"
        ).pack(
            anchor="w",
            padx=25,
            pady=(5, 5)
        )

        self.workload_option = ctk.CTkOptionMenu(
            panel,
            values=[
                "Light",
                "Medium",
                "Heavy"
            ],
            command=self.update_workload_info
        )

        self.workload_option.set(
            "Medium"
        )

        self.workload_option.pack(
            fill="x",
            padx=25,
            pady=(0, 15)
        )

        self.workload_info = ctk.CTkLabel(
            panel,
            text=(
                "Standard comparison\n"
                "3,000 items"
            ),
            text_color="gray",
            justify="left"
        )

        self.workload_info.pack(
            anchor="w",
            padx=25,
            pady=(0, 20)
        )

        self.start_button = ctk.CTkButton(
            panel,
            text="Start Performance Test",
            height=45,
            command=self.start_test
        )

        self.start_button.pack(
            fill="x",
            padx=25,
            pady=(5, 25)
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
            text="Comparison Results",
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
            pady=(5, 15)
        )

        self.result_labels = {}

        for algorithm_name, display_name in (
            DISPLAY_NAMES.items()
        ):

            frame = ctk.CTkFrame(
                panel
            )

            frame.pack(
                fill="x",
                padx=25,
                pady=5
            )

            name_label = ctk.CTkLabel(
                frame,
                text=display_name,
                anchor="w"
            )

            name_label.pack(
                side="left",
                padx=12,
                pady=12
            )

            result_label = ctk.CTkLabel(
                frame,
                text="--",
                anchor="e"
            )

            result_label.pack(
                side="right",
                padx=12
            )

            self.result_labels[
                algorithm_name
            ] = result_label

        self.fastest_label = ctk.CTkLabel(
            panel,
            text="Best Performance: --",
            font=ctk.CTkFont(
                size=17,
                weight="bold"
            ),
            wraplength=350,
            justify="center"
        )

        self.fastest_label.pack(
            pady=(20, 20)
        )

    def update_workload_info(
        self,
        workload
    ):

        descriptions = {
            "Light": (
                "Quick comparison\n"
                "1,000 items"
            ),

            "Medium": (
                "Standard comparison\n"
                "3,000 items"
            ),

            "Heavy": (
                "Intensive comparison\n"
                "6,000 items"
            )
        }

        self.workload_info.configure(
            text=descriptions[workload]
        )

    def start_test(self):

        self.start_button.configure(
            state="disabled"
        )

        self.status_label.configure(
            text="Testing..."
        )

        self.fastest_label.configure(
            text="Best Performance: --"
        )

        for label in (
            self.result_labels.values()
        ):

            label.configure(
                text="--"
            )

        workload = self.workload_option.get()

        thread = threading.Thread(
            target=self.run_test,
            args=(workload,),
            daemon=True
        )

        thread.start()

    def run_test(
        self,
        workload
    ):

        try:

            result = (
                run_performance_benchmark(
                    workload
                )
            )

            self.after(
                0,
                lambda: self.display_results(
                    result
                )
            )

        except Exception as error:

            self.after(
                0,
                lambda: self.show_error(
                    str(error)
                )
            )

    def display_results(
        self,
        result
    ):

        self.status_label.configure(
            text=(
                f"{result['workload']} "
                "test completed"
            )
        )

        results = result[
            "results"
        ]

        for item in results:

            self.result_labels[
                item["name"]
            ].configure(
                text=(
                    f"{item['time']} sec"
                )
            )

        fastest = results[0]

        fastest_name = DISPLAY_NAMES.get(
            fastest["name"],
            fastest["name"]
        )

        self.fastest_label.configure(
            text=(
                "Best Performance: "
                f"{fastest_name}"
            )
        )

        save_test_result(
            test_type="Performance Comparison",
            mode=result["workload"],
            result=fastest_name,
            details=result
        )

        self.start_button.configure(
            state="normal"
        )

    def show_error(
        self,
        error
    ):

        self.status_label.configure(
            text="Test failed"
        )

        self.fastest_label.configure(
            text=error
        )

        self.start_button.configure(
            state="normal"
        )