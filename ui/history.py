import customtkinter as ctk

from database.db import (
    get_test_history,
    clear_test_history
)


class HistoryPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(
            0,
            weight=1
        )

        self.grid_rowconfigure(
            2,
            weight=1
        )

        self.create_header()
        self.create_controls()
        self.create_history_area()

        self.refresh_history()

    def create_header(self):

        title = ctk.CTkLabel(
            self,
            text="Test History",
            font=ctk.CTkFont(
                size=30,
                weight="bold"
            )
        )

        title.grid(
            row=0,
            column=0,
            sticky="w",
            padx=30,
            pady=(30, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text=(
                "View previously completed "
                "performance tests."
            ),
            text_color="gray"
        )

        subtitle.grid(
            row=1,
            column=0,
            sticky="w",
            padx=30,
            pady=(0, 20)
        )

    def create_controls(self):

        controls = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        controls.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=30,
            pady=(0, 10)
        )

        self.refresh_button = (
            ctk.CTkButton(
                controls,
                text="Refresh",
                width=120,
                command=self.refresh_history
            )
        )

        self.refresh_button.pack(
            side="left"
        )

        self.clear_button = (
            ctk.CTkButton(
                controls,
                text="Clear History",
                width=120,
                command=self.clear_history
            )
        )

        self.clear_button.pack(
            side="right"
        )

    def create_history_area(self):

        self.history_frame = (
            ctk.CTkScrollableFrame(
                self,
                corner_radius=12
            )
        )

        self.history_frame.grid(
            row=3,
            column=0,
            sticky="nsew",
            padx=30,
            pady=(0, 30)
        )

        self.grid_rowconfigure(
            3,
            weight=1
        )

    def refresh_history(self):

        for widget in (
            self.history_frame.winfo_children()
        ):
            widget.destroy()

        history = get_test_history()

        if not history:

            empty_label = ctk.CTkLabel(
                self.history_frame,
                text="No test history available.",
                text_color="gray"
            )

            empty_label.pack(
                pady=40
            )

            return

        for record in history:

            (
                test_id,
                test_type,
                mode,
                score,
                result,
                created_at
            ) = record

            self.create_history_card(
                test_id,
                test_type,
                mode,
                score,
                result,
                created_at
            )

    def create_history_card(
        self,
        test_id,
        test_type,
        mode,
        score,
        result,
        created_at
    ):

        card = ctk.CTkFrame(
            self.history_frame,
            corner_radius=10
        )

        card.pack(
            fill="x",
            padx=10,
            pady=6
        )

        left = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        left.pack(
            side="left",
            padx=18,
            pady=14
        )

        title = ctk.CTkLabel(
            left,
            text=test_type,
            font=ctk.CTkFont(
                size=16,
                weight="bold"
            )
        )

        title.pack(
            anchor="w"
        )

        mode_text = (
            mode
            if mode
            else "Standard"
        )

        info = ctk.CTkLabel(
            left,
            text=(
                f"{mode_text} • "
                f"{created_at}"
            ),
            text_color="gray"
        )

        info.pack(
            anchor="w"
        )

        right = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        right.pack(
            side="right",
            padx=18,
            pady=14
        )

        if score is not None:

            score_label = ctk.CTkLabel(
                right,
                text=str(score),
                font=ctk.CTkFont(
                    size=18,
                    weight="bold"
                )
            )

            score_label.pack()

        result_label = ctk.CTkLabel(
            right,
            text=result or "--",
            text_color="gray"
        )

        result_label.pack()

    def clear_history(self):

        clear_test_history()

        self.refresh_history()