import threading

import customtkinter as ctk

from tests.stress_benchmark import (
    run_stress_test
)


class StressTestPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(
            (0, 1),
            weight=1
        )

        self.stop_event = (
            threading.Event()
        )

        self.test_running = False

        self.create_header()
        self.create_test_panel()
        self.create_monitor_panel()

    def create_header(self):

        title = ctk.CTkLabel(
            self,
            text="System Stress Test",
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
                "Apply a controlled workload "
                "and monitor system stability."
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
            text="Stress Level"
        ).pack(
            anchor="w",
            padx=25,
            pady=(5, 5)
        )

        self.intensity_option = (
            ctk.CTkOptionMenu(
                panel,
                values=[
                    "Light",
                    "Medium",
                    "Heavy"
                ],
                command=self.update_info
            )
        )

        self.intensity_option.set(
            "Medium"
        )

        self.intensity_option.pack(
            fill="x",
            padx=25,
            pady=(0, 15)
        )

        ctk.CTkLabel(
            panel,
            text="Duration"
        ).pack(
            anchor="w",
            padx=25,
            pady=(5, 5)
        )

        self.duration_option = (
            ctk.CTkOptionMenu(
                panel,
                values=[
                    "10 Seconds",
                    "20 Seconds",
                    "30 Seconds"
                ]
            )
        )

        self.duration_option.set(
            "20 Seconds"
        )

        self.duration_option.pack(
            fill="x",
            padx=25,
            pady=(0, 15)
        )

        self.info_label = (
            ctk.CTkLabel(
                panel,
                text=(
                    "Standard stress workload\n"
                    "Recommended for general testing"
                ),
                text_color="gray",
                justify="left"
            )
        )

        self.info_label.pack(
            anchor="w",
            padx=25,
            pady=(0, 20)
        )

        self.start_button = (
            ctk.CTkButton(
                panel,
                text="Start Stress Test",
                height=45,
                command=self.start_test
            )
        )

        self.start_button.pack(
            fill="x",
            padx=25,
            pady=(5, 10)
        )

        self.stop_button = (
            ctk.CTkButton(
                panel,
                text="Stop Test",
                height=45,
                state="disabled",
                command=self.stop_test
            )
        )

        self.stop_button.pack(
            fill="x",
            padx=25,
            pady=(0, 25)
        )

    def create_monitor_panel(self):

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
            text="Live Monitoring",
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

        self.status_label = (
            ctk.CTkLabel(
                panel,
                text="Ready to test",
                text_color="gray"
            )
        )

        self.status_label.pack(
            pady=8
        )

        self.progress_bar = (
            ctk.CTkProgressBar(
                panel
            )
        )

        self.progress_bar.pack(
            fill="x",
            padx=30,
            pady=(10, 20)
        )

        self.progress_bar.set(0)

        self.time_label = (
            ctk.CTkLabel(
                panel,
                text="Elapsed Time: --"
            )
        )

        self.time_label.pack(
            pady=4
        )

        self.cpu_label = (
            ctk.CTkLabel(
                panel,
                text="CPU Usage: --"
            )
        )

        self.cpu_label.pack(
            pady=4
        )

        self.memory_label = (
            ctk.CTkLabel(
                panel,
                text="Memory Usage: --"
            )
        )

        self.memory_label.pack(
            pady=4
        )

        self.cycles_label = (
            ctk.CTkLabel(
                panel,
                text="Processing Cycles: --"
            )
        )

        self.cycles_label.pack(
            pady=4
        )

        self.items_label = (
            ctk.CTkLabel(
                panel,
                text="Work Processed: --"
            )
        )

        self.items_label.pack(
            pady=4
        )

        self.result_label = (
            ctk.CTkLabel(
                panel,
                text="System Stability: --",
                font=ctk.CTkFont(
                    size=18,
                    weight="bold"
                )
            )
        )

        self.result_label.pack(
            pady=(20, 10)
        )

    def update_info(
        self,
        intensity
    ):

        descriptions = {
            "Light": (
                "Light system workload\n"
                "Suitable for quick stability checks"
            ),

            "Medium": (
                "Standard stress workload\n"
                "Recommended for general testing"
            ),

            "Heavy": (
                "Intensive system workload\n"
                "Places sustained load on the system"
            )
        }

        self.info_label.configure(
            text=descriptions[
                intensity
            ]
        )

    def start_test(self):

        if self.test_running:
            return

        duration_values = {
            "10 Seconds": 10,
            "20 Seconds": 20,
            "30 Seconds": 30
        }

        duration = duration_values[
            self.duration_option.get()
        ]

        intensity = (
            self.intensity_option.get()
        )

        self.test_running = True

        self.stop_event.clear()

        self.start_button.configure(
            state="disabled"
        )

        self.stop_button.configure(
            state="normal"
        )

        self.status_label.configure(
            text="Stress test running..."
        )

        self.result_label.configure(
            text="System Stability: Testing..."
        )

        self.progress_bar.set(0)

        thread = threading.Thread(
            target=self.run_test,
            args=(
                intensity,
                duration
            ),
            daemon=True
        )

        thread.start()

    def run_test(
        self,
        intensity,
        duration
    ):

        try:

            result = run_stress_test(
                intensity,
                duration,
                self.stop_event,
                lambda data:
                self.after(
                    0,
                    lambda:
                    self.update_progress(
                        data,
                        duration
                    )
                )
            )

            self.after(
                0,
                lambda:
                self.display_result(
                    result
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

    def update_progress(
        self,
        data,
        duration
    ):

        progress = min(
            data["elapsed"]
            / duration,
            1
        )

        self.progress_bar.set(
            progress
        )

        self.time_label.configure(
            text=(
                "Elapsed Time: "
                f"{data['elapsed']:.1f} sec"
            )
        )

        self.cpu_label.configure(
            text=(
                "CPU Usage: "
                f"{data['cpu']:.1f}%"
            )
        )

        self.memory_label.configure(
            text=(
                "Memory Usage: "
                f"{data['memory']:.1f}%"
            )
        )

        self.cycles_label.configure(
            text=(
                "Processing Cycles: "
                f"{data['cycles']}"
            )
        )

        self.items_label.configure(
            text=(
                "Work Processed: "
                f"{data['processed_items']:,} items"
            )
        )

    def stop_test(self):

        self.stop_event.set()

        self.status_label.configure(
            text="Stopping test..."
        )

        self.stop_button.configure(
            state="disabled"
        )

    def display_result(
        self,
        result
    ):

        self.test_running = False

        self.start_button.configure(
            state="normal"
        )

        self.stop_button.configure(
            state="disabled"
        )

        if result["stopped"]:

            self.status_label.configure(
                text="Test stopped"
            )

        else:

            self.status_label.configure(
                text="Stress test completed"
            )

            self.progress_bar.set(1)

        self.cpu_label.configure(
            text=(
                "CPU Usage: "
                f"{result['average_cpu']}% avg / "
                f"{result['peak_cpu']}% peak"
            )
        )

        self.memory_label.configure(
            text=(
                "Memory Usage: "
                f"{result['average_memory']}% avg / "
                f"{result['peak_memory']}% peak"
            )
        )

        self.cycles_label.configure(
            text=(
                "Processing Cycles: "
                f"{result['cycles']}"
            )
        )

        self.items_label.configure(
            text=(
                "Work Processed: "
                f"{result['processed_items']:,} items"
            )
        )

        self.result_label.configure(
            text=(
                "System Stability: "
                f"{result['stability']}"
            )
        )

    def show_error(
        self,
        error
    ):

        self.test_running = False

        self.status_label.configure(
            text="Stress test failed"
        )

        self.result_label.configure(
            text=error
        )

        self.start_button.configure(
            state="normal"
        )

        self.stop_button.configure(
            state="disabled"
        )