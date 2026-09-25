import threading

import customtkinter as ctk

from tests.memory_benchmark import run_memory_benchmark
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


class MemoryTestPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color=COLORS["app_bg"]
        )

        self.grid_columnconfigure(
            (0, 1),
            weight=1,
            uniform="memory_columns"
        )

        self.grid_rowconfigure(
            1,
            weight=1
        )

        self.create_header()
        self.create_test_panel()
        self.create_result_panel()

    def create_header(self):

        header = PageHeader(
            self,
            title="Memory Performance Test",
            subtitle=(
                "Measure how efficiently your system "
                "handles memory-intensive workloads."
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
                "Select the amount of memory "
                "processing to perform."
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
            text="Standard Memory Test",
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
            text="200,000 items",
            font=FONTS["small"],
            text_color=COLORS["text_secondary"]
        )

        self.workload_info.pack(
            anchor="w",
            padx=16,
            pady=(0, 14)
        )

        description = ctk.CTkLabel(
            panel,
            text=(
                "The test creates and processes a large "
                "data workload while measuring execution "
                "time and memory usage."
            ),
            font=FONTS["small"],
            text_color=COLORS["text_muted"],
            justify="left",
            wraplength=420
        )

        description.pack(
            anchor="w",
            padx=24,
            pady=(0, 22)
        )

        self.start_button = PrimaryButton(
            panel,
            text="Start Memory Test",
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
            text="Test Results",
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
            pady=(10, 14)
        )

        score_card = ctk.CTkFrame(
            panel,
            fg_color=COLORS["surface_light"],
            corner_radius=12
        )

        score_card.pack(
            fill="x",
            padx=24,
            pady=(0, 20)
        )

        self.score_label = ctk.CTkLabel(
            score_card,
            text="--",
            font=FONTS["metric_large"],
            text_color=COLORS["text"]
        )

        self.score_label.pack(
            pady=(18, 0)
        )

        ctk.CTkLabel(
            score_card,
            text="Memory Score",
            font=FONTS["small"],
            text_color=COLORS["text_secondary"]
        ).pack()

        self.rating_label = ctk.CTkLabel(
            score_card,
            text="--",
            font=(
                "Segoe UI",
                18,
                "bold"
            ),
            text_color=COLORS["accent"]
        )

        self.rating_label.pack(
            pady=(8, 18)
        )

        results_frame = ctk.CTkFrame(
            panel,
            fg_color="transparent"
        )

        results_frame.pack(
            fill="x",
            padx=24,
            pady=(0, 12)
        )

        self.time_label = self.create_result_row(
            results_frame,
            "Processing Time"
        )

        self.work_label = self.create_result_row(
            results_frame,
            "Work Completed"
        )

        self.peak_label = self.create_result_row(
            results_frame,
            "Peak Memory"
        )

        self.change_label = self.create_result_row(
            results_frame,
            "Memory Increase"
        )

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
            pady=8
        )

        name_label = ctk.CTkLabel(
            row,
            text=title,
            font=FONTS["body"],
            text_color=COLORS["text_secondary"]
        )

        name_label.pack(
            side="left"
        )

        value_label = ctk.CTkLabel(
            row,
            text="--",
            font=FONTS["body_bold"],
            text_color=COLORS["text"]
        )

        value_label.pack(
            side="right"
        )

        return value_label

    def update_workload_info(
        self,
        workload
    ):

        descriptions = {
            "Light": (
                "Quick Memory Check",
                "50,000 items"
            ),

            "Medium": (
                "Standard Memory Test",
                "200,000 items"
            ),

            "Heavy": (
                "Intensive Memory Test",
                "500,000 items"
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
            text="Running memory benchmark..."
        )

        self.status_badge.set_status(
            "RUNNING",
            "warning"
        )

        self.score_label.configure(
            text="--"
        )

        self.rating_label.configure(
            text="Please wait"
        )

        self.reset_result_rows()

        workload = (
            self.workload_option.get()
        )

        thread = threading.Thread(
            target=self.run_test,
            args=(workload,),
            daemon=True
        )

        thread.start()

    def reset_result_rows(self):

        self.time_label.configure(
            text="--"
        )

        self.work_label.configure(
            text="--"
        )

        self.peak_label.configure(
            text="--"
        )

        self.change_label.configure(
            text="--"
        )

    def run_test(
        self,
        workload
    ):

        try:

            result = run_memory_benchmark(
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

    def display_result(
        self,
        result
    ):

        self.status_label.configure(
            text=(
                f"{result['workload']} "
                "workload completed successfully."
            )
        )

        self.status_badge.set_status(
            "COMPLETED",
            "success"
        )

        self.score_label.configure(
            text=f"{result['score']:,}"
        )

        self.rating_label.configure(
            text=result["rating"]
        )

        self.time_label.configure(
            text=(
                f"{result['execution_time']} sec"
            )
        )

        self.work_label.configure(
            text=(
                f"{result['items']:,} items"
            )
        )

        self.peak_label.configure(
            text=(
                f"{result['peak_memory']} MB"
            )
        )

        self.change_label.configure(
            text=(
                f"{result['memory_change']} MB"
            )
        )

        try:

            save_test_result(
                test_type="Memory Performance",
                mode=result["workload"],
                score=result["score"],
                result=result["rating"],
                details=result
            )

        except Exception as error:

            print(
                "Memory history save error: "
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
            f"Memory test error: {error}"
        )

        self.status_label.configure(
            text="The memory test could not be completed."
        )

        self.status_badge.set_status(
            "FAILED",
            "danger"
        )

        self.rating_label.configure(
            text="Test Failed"
        )

        self.start_button.configure(
            state="normal"
        )