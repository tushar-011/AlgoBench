import threading

import customtkinter as ctk

from tests.all_in_one_benchmark import (
    run_all_in_one_benchmark
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


class AllInOnePage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color=COLORS["app_bg"]
        )

        self.grid_columnconfigure(
            (0, 1),
            weight=1,
            uniform="all_in_one_columns"
        )

        self.grid_rowconfigure(
            1,
            weight=1
        )

        self.test_running = False

        self.create_header()
        self.create_test_panel()
        self.create_result_panel()

    def create_header(self):

        header = PageHeader(
            self,
            title="Complete System Test",
            subtitle=(
                "Run a complete benchmark sequence "
                "and receive one overall system score."
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
            text="Benchmark Sequence",
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
                "AlgoBench will automatically run "
                "four performance checks."
            ),
            font=FONTS["small"],
            text_color=COLORS["text_secondary"]
        )

        subtitle.pack(
            anchor="w",
            padx=24,
            pady=(0, 20)
        )

        self.create_sequence_item(
            panel,
            "01",
            "CPU Performance",
            "Measures processor workload performance."
        )

        self.create_sequence_item(
            panel,
            "02",
            "Memory Performance",
            "Measures memory usage and processing efficiency."
        )

        self.create_sequence_item(
            panel,
            "03",
            "Processing Comparison",
            "Compares multiple data processing methods."
        )

        self.create_sequence_item(
            panel,
            "04",
            "System Stress",
            "Checks system behavior under sustained load."
        )

        info_card = ctk.CTkFrame(
            panel,
            fg_color=COLORS["surface_light"],
            corner_radius=10
        )

        info_card.pack(
            fill="x",
            padx=24,
            pady=(12, 18)
        )

        ctk.CTkLabel(
            info_card,
            text="Standard Complete Benchmark",
            font=FONTS["body_bold"],
            text_color=COLORS["text"]
        ).pack(
            anchor="w",
            padx=16,
            pady=(13, 3)
        )

        ctk.CTkLabel(
            info_card,
            text=(
                "Uses standard workloads for each test "
                "and combines the results into one score."
            ),
            font=FONTS["small"],
            text_color=COLORS["text_secondary"],
            wraplength=430,
            justify="left"
        ).pack(
            anchor="w",
            padx=16,
            pady=(0, 13)
        )

        self.start_button = PrimaryButton(
            panel,
            text="Start Complete Test",
            command=self.start_test
        )

        self.start_button.pack(
            fill="x",
            padx=24,
            pady=(0, 24)
        )

    def create_sequence_item(
        self,
        parent,
        number,
        title,
        description
    ):

        item = ctk.CTkFrame(
            parent,
            fg_color="transparent"
        )

        item.pack(
            fill="x",
            padx=24,
            pady=7
        )

        badge = ctk.CTkLabel(
            item,
            text=number,
            width=34,
            height=34,
            corner_radius=8,
            fg_color=COLORS["accent_soft"],
            text_color=COLORS["accent"],
            font=FONTS["body_bold"]
        )

        badge.pack(
            side="left"
        )

        text_frame = ctk.CTkFrame(
            item,
            fg_color="transparent"
        )

        text_frame.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(12, 0)
        )

        ctk.CTkLabel(
            text_frame,
            text=title,
            font=FONTS["body_bold"],
            text_color=COLORS["text"]
        ).pack(
            anchor="w"
        )

        ctk.CTkLabel(
            text_frame,
            text=description,
            font=FONTS["small"],
            text_color=COLORS["text_secondary"]
        ).pack(
            anchor="w",
            pady=(2, 0)
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

        ctk.CTkLabel(
            heading_frame,
            text="Overall Results",
            font=FONTS["section"],
            text_color=COLORS["text"]
        ).pack(
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
            text="Ready to run complete benchmark",
            font=FONTS["small"],
            text_color=COLORS["text_secondary"]
        )

        self.status_label.pack(
            pady=(10, 12)
        )

        self.progress_bar = ctk.CTkProgressBar(
            panel,
            height=9,
            corner_radius=5,
            progress_color=COLORS["accent"],
            fg_color=COLORS["border"]
        )

        self.progress_bar.pack(
            fill="x",
            padx=24,
            pady=(0, 6)
        )

        self.progress_bar.set(
            0
        )

        self.progress_text = ctk.CTkLabel(
            panel,
            text="0%",
            font=FONTS["small"],
            text_color=COLORS["text_muted"]
        )

        self.progress_text.pack(
            anchor="e",
            padx=24,
            pady=(0, 14)
        )

        score_card = ctk.CTkFrame(
            panel,
            fg_color=COLORS["surface_light"],
            corner_radius=12
        )

        score_card.pack(
            fill="x",
            padx=24,
            pady=(0, 18)
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
            text="Overall System Score",
            font=FONTS["small"],
            text_color=COLORS["text_secondary"]
        ).pack()

        self.rating_label = ctk.CTkLabel(
            score_card,
            text="--",
            font=("Segoe UI", 19, "bold"),
            text_color=COLORS["accent"]
        )

        self.rating_label.pack(
            pady=(8, 18)
        )

        results_card = ctk.CTkFrame(
            panel,
            fg_color="transparent"
        )

        results_card.pack(
            fill="x",
            padx=24,
            pady=(0, 12)
        )

        self.cpu_label = self.create_result_row(
            results_card,
            "CPU Score"
        )

        self.memory_label = self.create_result_row(
            results_card,
            "Memory Score"
        )

        self.processing_label = self.create_result_row(
            results_card,
            "Best Processing Method"
        )

        self.stress_label = self.create_result_row(
            results_card,
            "System Stability"
        )

    def create_result_row(
        self,
        parent,
        title
    ):

        row = ctk.CTkFrame(
            parent,
            fg_color=COLORS["surface_light"],
            corner_radius=9
        )

        row.pack(
            fill="x",
            pady=5
        )

        ctk.CTkLabel(
            row,
            text=title,
            font=FONTS["body"],
            text_color=COLORS["text_secondary"]
        ).pack(
            side="left",
            padx=14,
            pady=10
        )

        value = ctk.CTkLabel(
            row,
            text="--",
            font=FONTS["body_bold"],
            text_color=COLORS["text"],
            wraplength=250,
            justify="right"
        )

        value.pack(
            side="right",
            padx=14,
            pady=10
        )

        return value

    def start_test(self):

        if self.test_running:
            return

        self.test_running = True

        self.start_button.configure(
            state="disabled"
        )

        self.status_badge.set_status(
            "RUNNING",
            "warning"
        )

        self.status_label.configure(
            text="Preparing complete benchmark..."
        )

        self.progress_bar.set(
            0
        )

        self.progress_text.configure(
            text="0%"
        )

        self.score_label.configure(
            text="--"
        )

        self.rating_label.configure(
            text="Testing..."
        )

        self.cpu_label.configure(
            text="--"
        )

        self.memory_label.configure(
            text="--"
        )

        self.processing_label.configure(
            text="--"
        )

        self.stress_label.configure(
            text="--"
        )

        thread = threading.Thread(
            target=self.run_test,
            daemon=True
        )

        thread.start()

    def run_test(self):

        try:

            results = run_all_in_one_benchmark(
                progress_callback=self.progress_update
            )

            self.after(
                0,
                lambda: self.display_results(
                    results
                )
            )

        except Exception as error:

            self.after(
                0,
                lambda: self.show_error(
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
            lambda: self.update_progress_ui(
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

        self.progress_text.configure(
            text=f"{int(progress * 100)}%"
        )

    def display_results(
        self,
        results
    ):

        self.test_running = False

        self.start_button.configure(
            state="normal"
        )

        self.status_badge.set_status(
            "COMPLETED",
            "success"
        )

        self.status_label.configure(
            text="Complete system benchmark finished."
        )

        self.progress_bar.set(
            1
        )

        self.progress_text.configure(
            text="100%"
        )

        self.score_label.configure(
            text=f"{results['overall_score']:,}"
        )

        self.rating_label.configure(
            text=results["rating"]
        )

        self.cpu_label.configure(
            text=f"{results['cpu']['score']:,}"
        )

        self.memory_label.configure(
            text=f"{results['memory']['score']:,}"
        )

        fastest = (
            results[
                "performance"
            ][
                "results"
            ][0]
        )

        fastest_name = DISPLAY_NAMES.get(
            fastest["name"],
            fastest["name"]
        )

        self.processing_label.configure(
            text=fastest_name
        )

        self.stress_label.configure(
            text=results["stress"]["stability"]
        )

        try:

            save_test_result(
                test_type="Complete System Test",
                mode="Standard",
                score=results["overall_score"],
                result=results["rating"],
                details=results
            )

        except Exception as error:

            print(
                "Complete test history save error: "
                f"{error}"
            )

    def show_error(
        self,
        error
    ):

        print(
            f"Complete system test error: {error}"
        )

        self.test_running = False

        self.start_button.configure(
            state="normal"
        )

        self.status_badge.set_status(
            "FAILED",
            "danger"
        )

        self.status_label.configure(
            text="Complete benchmark could not be finished."
        )

        self.progress_bar.set(
            0
        )

        self.progress_text.configure(
            text="0%"
        )

        self.rating_label.configure(
            text="Test Failed"
        )