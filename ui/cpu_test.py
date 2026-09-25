import threading

import customtkinter as ctk

from tests.cpu_benchmark import run_cpu_benchmark


class CPUTestPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(
            (0, 1),
            weight=1
        )

        self.create_header()
        self.create_test_panel()
        self.create_result_panel()

    def create_header(self):

        title = ctk.CTkLabel(
            self,
            text="CPU Performance Test",
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
                "Measure how quickly your system "
                "handles different processing workloads."
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

        workload_label = ctk.CTkLabel(
            panel,
            text="Workload Level"
        )

        workload_label.pack(
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
            text="Standard performance test\n400,000 total items",
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
            text="Start CPU Test",
            height=45,
            command=self.start_test
        )

        self.start_button.pack(
            fill="x",
            padx=25,
            pady=(5, 25)
        )

    def create_result_panel(self):

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
            text="Test Results",
            font=ctk.CTkFont(
                size=20,
                weight="bold"
            )
        )

        heading.pack(
            anchor="w",
            padx=25,
            pady=(25, 20)
        )

        self.status_label = ctk.CTkLabel(
            panel,
            text="Ready to test",
            text_color="gray"
        )

        self.status_label.pack(
            pady=8
        )

        self.score_label = ctk.CTkLabel(
            panel,
            text="--",
            font=ctk.CTkFont(
                size=42,
                weight="bold"
            )
        )

        self.score_label.pack(
            pady=(10, 0)
        )

        ctk.CTkLabel(
            panel,
            text="Performance Score",
            text_color="gray"
        ).pack()

        self.rating_label = ctk.CTkLabel(
            panel,
            text="--",
            font=ctk.CTkFont(
                size=20,
                weight="bold"
            )
        )

        self.rating_label.pack(
            pady=(20, 10)
        )

        self.time_label = ctk.CTkLabel(
            panel,
            text="Processing Time: --"
        )

        self.time_label.pack(
            pady=4
        )

        self.work_label = ctk.CTkLabel(
            panel,
            text="Work Completed: --"
        )

        self.work_label.pack(
            pady=4
        )

        self.rate_label = ctk.CTkLabel(
            panel,
            text="Processing Rate: --"
        )

        self.rate_label.pack(
            pady=4
        )

        self.cpu_label = ctk.CTkLabel(
            panel,
            text="Peak CPU Usage: --"
        )

        self.cpu_label.pack(
            pady=4
        )

        self.average_cpu_label = ctk.CTkLabel(
            panel,
            text="Average CPU Usage: --"
        )

        self.average_cpu_label.pack(
            pady=4
        )

    def update_workload_info(self, workload):

        descriptions = {
            "Light": (
                "Quick system check\n"
                "50,000 total items"
            ),

            "Medium": (
                "Standard performance test\n"
                "400,000 total items"
            ),

            "Heavy": (
                "Intensive processing test\n"
                "1,800,000 total items"
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

        self.score_label.configure(
            text="--"
        )

        self.rating_label.configure(
            text="Please wait"
        )

        workload = self.workload_option.get()

        thread = threading.Thread(
            target=self.run_test,
            args=(workload,),
            daemon=True
        )

        thread.start()

    def run_test(self, workload):

        try:

            result = run_cpu_benchmark(
                workload
            )

            self.after(
                0,
                lambda: self.display_result(
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

    def display_result(self, result):

        self.status_label.configure(
            text=(
                f"{result['workload']} test completed"
            )
        )

        self.score_label.configure(
            text=str(
                result["score"]
            )
        )

        self.rating_label.configure(
            text=result["rating"]
        )

        self.time_label.configure(
            text=(
                "Processing Time: "
                f"{result['execution_time']} sec"
            )
        )

        self.work_label.configure(
            text=(
                "Work Completed: "
                f"{result['total_items']:,} items"
            )
        )

        self.rate_label.configure(
            text=(
                "Processing Rate: "
                f"{result['processing_rate']:,} items/sec"
            )
        )

        self.cpu_label.configure(
            text=(
                "Peak CPU Usage: "
                f"{result['peak_cpu']}%"
            )
        )

        self.average_cpu_label.configure(
            text=(
                "Average CPU Usage: "
                f"{result['average_cpu']}%"
            )
        )

        self.start_button.configure(
            state="normal"
        )

    def show_error(self, error):

        self.status_label.configure(
            text="Test failed"
        )

        self.rating_label.configure(
            text=error
        )

        self.start_button.configure(
            state="normal"
        )