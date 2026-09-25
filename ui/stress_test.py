import threading

import customtkinter as ctk

from tests.stress_benchmark import (
    run_stress_test
)

from database.db import save_test_result

from ui.theme import (
    COLORS,
    FONTS,
    SPACING
)

from ui.components import (
    PageHeader,
    Card,
    StatusBadge,
    PrimaryButton
)


class StressTestPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color=COLORS["app_bg"]
        )

        self.grid_columnconfigure(
            (0, 1),
            weight=1,
            uniform="stress_columns"
        )

        self.grid_rowconfigure(
            1,
            weight=1
        )

        self.stop_event = threading.Event()

        self.test_running = False

        self.create_header()
        self.create_test_panel()
        self.create_monitor_panel()

    def create_header(self):

        header = PageHeader(
            self,
            title="System Stress Test",
            subtitle=(
                "Apply a controlled workload and "
                "monitor system stability in real time."
            )
        )

        header.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=SPACING["page_x"],
            pady=(
                SPACING["page_top"],
                20
            )
        )

    def create_test_panel(self):

        panel = Card(
            self
        )

        panel.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=(
                SPACING["page_x"],
                8
            ),
            pady=(
                0,
                SPACING["page_x"]
            )
        )

        heading = ctk.CTkLabel(
            panel,
            text="Test Configuration",
            font=FONTS["section"],
            text_color=COLORS["text"]
        )

        heading.pack(
            anchor="w",
            padx=24,
            pady=(24, 4)
        )

        subtitle = ctk.CTkLabel(
            panel,
            text=(
                "Choose the test intensity and "
                "how long the workload should run."
            ),
            font=FONTS["small"],
            text_color=COLORS["text_secondary"]
        )

        subtitle.pack(
            anchor="w",
            padx=24,
            pady=(0, 24)
        )

        ctk.CTkLabel(
            panel,
            text="Stress Level",
            font=FONTS["body_bold"],
            text_color=COLORS["text"]
        ).pack(
            anchor="w",
            padx=24,
            pady=(0, 7)
        )

        self.intensity_option = ctk.CTkOptionMenu(
            panel,
            values=[
                "Light",
                "Medium",
                "Heavy"
            ],
            command=self.update_info,
            height=42,
            corner_radius=9,
            fg_color=COLORS["surface_light"],
            button_color=COLORS["accent"],
            button_hover_color=COLORS["accent_hover"],
            text_color=COLORS["text"],
            dropdown_fg_color=COLORS["surface"],
            dropdown_hover_color=COLORS["surface_hover"]
        )

        self.intensity_option.set(
            "Medium"
        )

        self.intensity_option.pack(
            fill="x",
            padx=24,
            pady=(0, 18)
        )

        ctk.CTkLabel(
            panel,
            text="Duration",
            font=FONTS["body_bold"],
            text_color=COLORS["text"]
        ).pack(
            anchor="w",
            padx=24,
            pady=(0, 7)
        )

        self.duration_option = ctk.CTkOptionMenu(
            panel,
            values=[
                "10 Seconds",
                "20 Seconds",
                "30 Seconds"
            ],
            height=42,
            corner_radius=9,
            fg_color=COLORS["surface_light"],
            button_color=COLORS["accent"],
            button_hover_color=COLORS["accent_hover"],
            text_color=COLORS["text"],
            dropdown_fg_color=COLORS["surface"],
            dropdown_hover_color=COLORS["surface_hover"]
        )

        self.duration_option.set(
            "20 Seconds"
        )

        self.duration_option.pack(
            fill="x",
            padx=24,
            pady=(0, 18)
        )

        info_card = ctk.CTkFrame(
            panel,
            fg_color=COLORS["surface_light"],
            corner_radius=10
        )

        info_card.pack(
            fill="x",
            padx=24,
            pady=(0, 22)
        )

        self.info_title = ctk.CTkLabel(
            info_card,
            text="Standard Stress Workload",
            font=FONTS["body_bold"],
            text_color=COLORS["text"]
        )

        self.info_title.pack(
            anchor="w",
            padx=16,
            pady=(14, 3)
        )

        self.info_label = ctk.CTkLabel(
            info_card,
            text=(
                "Recommended for general "
                "stability testing."
            ),
            font=FONTS["small"],
            text_color=COLORS["text_secondary"],
            justify="left"
        )

        self.info_label.pack(
            anchor="w",
            padx=16,
            pady=(0, 14)
        )

        self.start_button = PrimaryButton(
            panel,
            text="Start Stress Test",
            command=self.start_test
        )

        self.start_button.pack(
            fill="x",
            padx=24,
            pady=(0, 10)
        )

        self.stop_button = ctk.CTkButton(
            panel,
            text="Stop Test",
            height=42,
            corner_radius=9,
            state="disabled",
            command=self.stop_test,
            fg_color=COLORS["surface_light"],
            hover_color=COLORS["surface_hover"],
            text_color=COLORS["text"],
            border_width=1,
            border_color=COLORS["border"],
            font=FONTS["body_bold"]
        )

        self.stop_button.pack(
            fill="x",
            padx=24,
            pady=(0, 24)
        )

    def create_monitor_panel(self):

        panel = Card(
            self
        )

        panel.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=(
                8,
                SPACING["page_x"]
            ),
            pady=(
                0,
                SPACING["page_x"]
            )
        )

        heading_frame = ctk.CTkFrame(
            panel,
            fg_color="transparent"
        )

        heading_frame.pack(
            fill="x",
            padx=24,
            pady=(24, 0)
        )

        heading = ctk.CTkLabel(
            heading_frame,
            text="Live Monitoring",
            font=FONTS["section"],
            text_color=COLORS["text"]
        )

        heading.pack(
            side="left"
        )

        self.status_badge = StatusBadge(
            heading_frame,
            text="READY",
            status="normal"
        )

        self.status_badge.pack(
            side="right"
        )

        self.status_label = ctk.CTkLabel(
            panel,
            text="Ready to test",
            font=FONTS["small"],
            text_color=COLORS["text_secondary"]
        )

        self.status_label.pack(
            pady=(10, 18)
        )

        metrics_frame = ctk.CTkFrame(
            panel,
            fg_color="transparent"
        )

        metrics_frame.pack(
            fill="x",
            padx=18,
            pady=(0, 18)
        )

        metrics_frame.grid_columnconfigure(
            (0, 1, 2),
            weight=1,
            uniform="stress_metrics"
        )

        self.cpu_value = self.create_metric_box(
            metrics_frame,
            0,
            "CPU",
            "--"
        )

        self.memory_value = self.create_metric_box(
            metrics_frame,
            1,
            "Memory",
            "--"
        )

        self.time_value = self.create_metric_box(
            metrics_frame,
            2,
            "Time",
            "--"
        )

        progress_frame = ctk.CTkFrame(
            panel,
            fg_color="transparent"
        )

        progress_frame.pack(
            fill="x",
            padx=24,
            pady=(0, 20)
        )

        progress_header = ctk.CTkFrame(
            progress_frame,
            fg_color="transparent"
        )

        progress_header.pack(
            fill="x",
            pady=(0, 7)
        )

        ctk.CTkLabel(
            progress_header,
            text="Test Progress",
            font=FONTS["body_bold"],
            text_color=COLORS["text"]
        ).pack(
            side="left"
        )

        self.progress_text = ctk.CTkLabel(
            progress_header,
            text="0%",
            font=FONTS["small"],
            text_color=COLORS["text_secondary"]
        )

        self.progress_text.pack(
            side="right"
        )

        self.progress_bar = ctk.CTkProgressBar(
            progress_frame,
            height=10,
            corner_radius=5,
            progress_color=COLORS["accent"],
            fg_color=COLORS["border"]
        )

        self.progress_bar.pack(
            fill="x"
        )

        self.progress_bar.set(
            0
        )

        stats_card = ctk.CTkFrame(
            panel,
            fg_color=COLORS["surface_light"],
            corner_radius=10
        )

        stats_card.pack(
            fill="x",
            padx=24,
            pady=(0, 18)
        )

        self.cycles_label = self.create_result_row(
            stats_card,
            "Processing Cycles"
        )

        self.items_label = self.create_result_row(
            stats_card,
            "Work Processed"
        )

        self.peak_cpu_label = self.create_result_row(
            stats_card,
            "Peak CPU Usage"
        )

        self.peak_memory_label = self.create_result_row(
            stats_card,
            "Peak Memory Usage"
        )

        result_card = ctk.CTkFrame(
            panel,
            fg_color=COLORS["accent_soft"],
            corner_radius=12
        )

        result_card.pack(
            fill="x",
            padx=24,
            pady=(0, 24)
        )

        ctk.CTkLabel(
            result_card,
            text="SYSTEM STABILITY",
            font=FONTS["small"],
            text_color=COLORS["text_secondary"]
        ).pack(
            pady=(14, 4)
        )

        self.result_label = ctk.CTkLabel(
            result_card,
            text="--",
            font=("Segoe UI", 20, "bold"),
            text_color=COLORS["text"]
        )

        self.result_label.pack(
            pady=(0, 14)
        )

    def create_metric_box(
        self,
        parent,
        column,
        title,
        value
    ):

        box = ctk.CTkFrame(
            parent,
            fg_color=COLORS["surface_light"],
            corner_radius=10
        )

        box.grid(
            row=0,
            column=column,
            sticky="nsew",
            padx=5
        )

        ctk.CTkLabel(
            box,
            text=title.upper(),
            font=FONTS["small"],
            text_color=COLORS["text_secondary"]
        ).pack(
            pady=(14, 4)
        )

        value_label = ctk.CTkLabel(
            box,
            text=value,
            font=("Segoe UI", 23, "bold"),
            text_color=COLORS["text"]
        )

        value_label.pack(
            pady=(0, 14)
        )

        return value_label

    def create_result_row(
        self,
        parent,
        title
    ):

        row = ctk.CTkFrame(
            parent,
            fg_color="transparent"
        )

        row.pack(
            fill="x",
            padx=14,
            pady=8
        )

        ctk.CTkLabel(
            row,
            text=title,
            font=FONTS["body"],
            text_color=COLORS["text_secondary"]
        ).pack(
            side="left"
        )

        value = ctk.CTkLabel(
            row,
            text="--",
            font=FONTS["body_bold"],
            text_color=COLORS["text"]
        )

        value.pack(
            side="right"
        )

        return value

    def update_info(
        self,
        intensity
    ):

        descriptions = {
            "Light": (
                "Light Stress Workload",
                "Suitable for quick stability checks."
            ),

            "Medium": (
                "Standard Stress Workload",
                "Recommended for general stability testing."
            ),

            "Heavy": (
                "Intensive Stress Workload",
                "Places sustained load on the system."
            )
        }

        title, description = descriptions[
            intensity
        ]

        self.info_title.configure(
            text=title
        )

        self.info_label.configure(
            text=description
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
            text="Stress test is running..."
        )

        self.status_badge.set_status(
            "RUNNING",
            "warning"
        )

        self.result_label.configure(
            text="Testing..."
        )

        self.cpu_value.configure(
            text="--"
        )

        self.memory_value.configure(
            text="--"
        )

        self.time_value.configure(
            text="0.0s"
        )

        self.cycles_label.configure(
            text="--"
        )

        self.items_label.configure(
            text="--"
        )

        self.peak_cpu_label.configure(
            text="--"
        )

        self.peak_memory_label.configure(
            text="--"
        )

        self.progress_bar.set(
            0
        )

        self.progress_text.configure(
            text="0%"
        )

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
            data["elapsed"] / duration,
            1
        )

        self.progress_bar.set(
            progress
        )

        self.progress_text.configure(
            text=f"{int(progress * 100)}%"
        )

        self.cpu_value.configure(
            text=f"{data['cpu']:.0f}%"
        )

        self.memory_value.configure(
            text=f"{data['memory']:.0f}%"
        )

        self.time_value.configure(
            text=f"{data['elapsed']:.1f}s"
        )

        self.cycles_label.configure(
            text=f"{data['cycles']:,}"
        )

        self.items_label.configure(
            text=(
                f"{data['processed_items']:,} items"
            )
        )

    def stop_test(self):

        self.stop_event.set()

        self.status_label.configure(
            text="Stopping test..."
        )

        self.status_badge.set_status(
            "STOPPING",
            "warning"
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
                text="Stress test stopped."
            )

            self.status_badge.set_status(
                "STOPPED",
                "warning"
            )

        else:

            self.status_label.configure(
                text="Stress test completed successfully."
            )

            self.status_badge.set_status(
                "COMPLETED",
                "success"
            )

            self.progress_bar.set(
                1
            )

            self.progress_text.configure(
                text="100%"
            )

        self.cpu_value.configure(
            text=f"{result['average_cpu']}%"
        )

        self.memory_value.configure(
            text=f"{result['average_memory']}%"
        )

        self.time_value.configure(
            text=f"{result['duration']}s"
        )

        self.cycles_label.configure(
            text=f"{result['cycles']:,}"
        )

        self.items_label.configure(
            text=(
                f"{result['processed_items']:,} items"
            )
        )

        self.peak_cpu_label.configure(
            text=f"{result['peak_cpu']}%"
        )

        self.peak_memory_label.configure(
            text=f"{result['peak_memory']}%"
        )

        self.result_label.configure(
            text=result["stability"]
        )

        if not result["stopped"]:

            try:

                save_test_result(
                    test_type="System Stress Test",
                    mode=result["intensity"],
                    result=result["stability"],
                    details=result
                )

            except Exception as error:

                print(
                    "Stress history save error: "
                    f"{error}"
                )

    def show_error(
        self,
        error
    ):

        print(
            f"Stress test error: {error}"
        )

        self.test_running = False

        self.status_label.configure(
            text="The stress test could not be completed."
        )

        self.status_badge.set_status(
            "FAILED",
            "danger"
        )

        self.result_label.configure(
            text="Test Failed"
        )

        self.start_button.configure(
            state="normal"
        )

        self.stop_button.configure(
            state="disabled"
        )