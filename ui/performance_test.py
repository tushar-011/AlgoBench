import threading

import customtkinter as ctk

from tests.performance_benchmark import (
    run_performance_benchmark
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


DISPLAY_NAMES = {
    "Bubble Sort": "Basic Data Processing",
    "Insertion Sort": "Sequential Data Processing",
    "Merge Sort": "Balanced Data Processing",
    "Quick Sort": "Fast Partition Processing"
}


class PerformanceTestPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color=COLORS["app_bg"]
        )

        self.grid_columnconfigure(
            (0, 1),
            weight=1,
            uniform="performance_columns"
        )

        self.grid_rowconfigure(
            1,
            weight=1
        )

        self.result_rows = {}

        self.create_header()
        self.create_test_panel()
        self.create_result_panel()

    def create_header(self):

        header = PageHeader(
            self,
            title="Performance Comparison",
            subtitle=(
                "Compare different processing methods "
                "using the same data workload."
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
                "Choose how much data each processing "
                "method should handle."
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
            text="Workload Level",
            font=FONTS["body_bold"],
            text_color=COLORS["text"]
        ).pack(
            anchor="w",
            padx=24,
            pady=(0, 7)
        )

        self.workload_option = ctk.CTkOptionMenu(
            panel,
            values=[
                "Light",
                "Medium",
                "Heavy"
            ],
            command=self.update_workload_info,
            height=42,
            corner_radius=9,
            fg_color=COLORS["surface_light"],
            button_color=COLORS["accent"],
            button_hover_color=COLORS["accent_hover"],
            text_color=COLORS["text"],
            dropdown_fg_color=COLORS["surface"],
            dropdown_hover_color=COLORS["surface_hover"]
        )

        self.workload_option.set(
            "Medium"
        )

        self.workload_option.pack(
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

        self.workload_title = ctk.CTkLabel(
            info_card,
            text="Standard Comparison",
            font=FONTS["body_bold"],
            text_color=COLORS["text"]
        )

        self.workload_title.pack(
            anchor="w",
            padx=16,
            pady=(14, 3)
        )

        self.workload_info = ctk.CTkLabel(
            info_card,
            text="3,000 items per method",
            font=FONTS["small"],
            text_color=COLORS["text_secondary"]
        )

        self.workload_info.pack(
            anchor="w",
            padx=16,
            pady=(0, 14)
        )

        methods_card = ctk.CTkFrame(
            panel,
            fg_color="transparent"
        )

        methods_card.pack(
            fill="x",
            padx=24,
            pady=(0, 18)
        )

        ctk.CTkLabel(
            methods_card,
            text="Methods Included",
            font=FONTS["body_bold"],
            text_color=COLORS["text"]
        ).pack(
            anchor="w",
            pady=(0, 8)
        )

        for name in DISPLAY_NAMES.values():

            ctk.CTkLabel(
                methods_card,
                text=f"• {name}",
                font=FONTS["small"],
                text_color=COLORS["text_secondary"]
            ).pack(
                anchor="w",
                pady=2
            )

        self.start_button = PrimaryButton(
            panel,
            text="Start Comparison",
            command=self.start_test
        )

        self.start_button.pack(
            fill="x",
            padx=24,
            pady=(0, 24)
        )

    def create_result_panel(self):

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
            text="Comparison Results",
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
            text="Ready to compare methods",
            font=FONTS["small"],
            text_color=COLORS["text_secondary"]
        )

        self.status_label.pack(
            pady=(10, 16)
        )

        self.results_container = ctk.CTkFrame(
            panel,
            fg_color="transparent"
        )

        self.results_container.pack(
            fill="both",
            expand=True,
            padx=24
        )

        for algorithm_name in DISPLAY_NAMES:

            self.create_result_item(
                algorithm_name
            )

        self.best_card = ctk.CTkFrame(
            panel,
            fg_color=COLORS["accent_soft"],
            corner_radius=12
        )

        self.best_card.pack(
            fill="x",
            padx=24,
            pady=(18, 24)
        )

        ctk.CTkLabel(
            self.best_card,
            text="BEST PERFORMANCE IN THIS TEST",
            font=FONTS["small"],
            text_color=COLORS["text_secondary"]
        ).pack(
            pady=(14, 4)
        )

        self.best_label = ctk.CTkLabel(
            self.best_card,
            text="--",
            font=("Segoe UI", 17, "bold"),
            text_color=COLORS["text"],
            wraplength=360,
            justify="center"
        )

        self.best_label.pack(
            padx=15,
            pady=(0, 14)
        )

    def create_result_item(
        self,
        algorithm_name
    ):

        container = ctk.CTkFrame(
            self.results_container,
            fg_color=COLORS["surface_light"],
            corner_radius=10
        )

        container.pack(
            fill="x",
            pady=6
        )

        top_row = ctk.CTkFrame(
            container,
            fg_color="transparent"
        )

        top_row.pack(
            fill="x",
            padx=14,
            pady=(12, 5)
        )

        display_name = DISPLAY_NAMES[
            algorithm_name
        ]

        name_label = ctk.CTkLabel(
            top_row,
            text=display_name,
            font=FONTS["body_bold"],
            text_color=COLORS["text"]
        )

        name_label.pack(
            side="left"
        )

        time_label = ctk.CTkLabel(
            top_row,
            text="--",
            font=FONTS["body_bold"],
            text_color=COLORS["text_secondary"]
        )

        time_label.pack(
            side="right"
        )

        algorithm_label = ctk.CTkLabel(
            container,
            text=f"({algorithm_name})",
            font=FONTS["small"],
            text_color=COLORS["text_muted"]
        )

        algorithm_label.pack(
            anchor="w",
            padx=14,
            pady=(0, 6)
        )

        progress = ctk.CTkProgressBar(
            container,
            height=8,
            corner_radius=5,
            progress_color=COLORS["accent"],
            fg_color=COLORS["border"]
        )

        progress.pack(
            fill="x",
            padx=14,
            pady=(0, 12)
        )

        progress.set(0)

        self.result_rows[
            algorithm_name
        ] = {
            "time": time_label,
            "bar": progress
        }

    def update_workload_info(
        self,
        workload
    ):

        descriptions = {
            "Light": (
                "Quick Comparison",
                "1,000 items per method"
            ),

            "Medium": (
                "Standard Comparison",
                "3,000 items per method"
            ),

            "Heavy": (
                "Intensive Comparison",
                "6,000 items per method"
            )
        }

        title, info = descriptions[
            workload
        ]

        self.workload_title.configure(
            text=title
        )

        self.workload_info.configure(
            text=info
        )

    def start_test(self):

        self.start_button.configure(
            state="disabled"
        )

        self.status_label.configure(
            text="Comparing processing methods..."
        )

        self.status_badge.set_status(
            "RUNNING",
            "warning"
        )

        self.best_label.configure(
            text="--"
        )

        for row in self.result_rows.values():

            row["time"].configure(
                text="--"
            )

            row["bar"].set(
                0
            )

        workload = (
            self.workload_option.get()
        )

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

            result = run_performance_benchmark(
                workload
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
                "comparison completed."
            )
        )

        self.status_badge.set_status(
            "COMPLETED",
            "success"
        )

        results = result["results"]

        fastest = results[0]

        slowest_time = max(
            item["time"]
            for item in results
        )

        for item in results:

            row = self.result_rows[
                item["name"]
            ]

            row["time"].configure(
                text=f"{item['time']} sec"
            )

            if slowest_time > 0:

                speed_ratio = (
                    fastest["time"]
                    / item["time"]
                )

            else:

                speed_ratio = 0

            bar_value = max(
                0.05,
                min(
                    speed_ratio,
                    1
                )
            )

            row["bar"].set(
                bar_value
            )

        fastest_name = DISPLAY_NAMES.get(
            fastest["name"],
            fastest["name"]
        )

        self.best_label.configure(
            text=(
                f"{fastest_name} "
                f"({fastest['name']})"
            )
        )

        try:

            save_test_result(
                test_type="Performance Comparison",
                mode=result["workload"],
                result=fastest_name,
                details=result
            )

        except Exception as error:

            print(
                "Performance history save error: "
                f"{error}"
            )

        self.start_button.configure(
            state="normal"
        )

    def show_error(
        self,
        error
    ):

        print(
            "Performance comparison error: "
            f"{error}"
        )

        self.status_label.configure(
            text=(
                "The comparison could not "
                "be completed."
            )
        )

        self.status_badge.set_status(
            "FAILED",
            "danger"
        )

        self.best_label.configure(
            text="Test Failed"
        )

        self.start_button.configure(
            state="normal"
        )