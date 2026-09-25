import customtkinter as ctk

from database.db import (
    get_test_history,
    clear_test_history
)

from ui.theme import (
    COLORS,
    FONTS,
    SPACING
)

from ui.components import (
    PageHeader,
    Card,
    StatusBadge
)


class HistoryPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color=COLORS["app_bg"]
        )

        self.grid_columnconfigure(
            0,
            weight=1
        )

        self.grid_rowconfigure(
            2,
            weight=1
        )

        self.create_header()
        self.create_toolbar()
        self.create_history_area()

        self.refresh_history()

    def create_header(self):

        header = PageHeader(
            self,
            title="Test History",
            subtitle=(
                "Review previously completed "
                "performance tests and benchmark results."
            )
        )

        header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=SPACING["page_x"],
            pady=(
                SPACING["page_top"],
                18
            )
        )

    def create_toolbar(self):

        toolbar = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        toolbar.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=SPACING["page_x"],
            pady=(0, 14)
        )

        self.count_label = ctk.CTkLabel(
            toolbar,
            text="0 saved tests",
            font=FONTS["small"],
            text_color=COLORS["text_secondary"]
        )

        self.count_label.pack(
            side="left"
        )

        clear_button = ctk.CTkButton(
            toolbar,
            text="Clear History",
            width=120,
            height=36,
            corner_radius=8,
            command=self.clear_history,
            fg_color=COLORS["surface_light"],
            hover_color=COLORS["surface_hover"],
            border_width=1,
            border_color=COLORS["border"],
            text_color=COLORS["text"],
            font=FONTS["body_bold"]
        )

        clear_button.pack(
            side="right"
        )

        refresh_button = ctk.CTkButton(
            toolbar,
            text="Refresh",
            width=100,
            height=36,
            corner_radius=8,
            command=self.refresh_history,
            fg_color=COLORS["accent"],
            hover_color=COLORS["accent_hover"],
            font=FONTS["body_bold"]
        )

        refresh_button.pack(
            side="right",
            padx=(0, 8)
        )

    def create_history_area(self):

        self.history_frame = (
            ctk.CTkScrollableFrame(
                self,
                fg_color="transparent",
                corner_radius=0
            )
        )

        self.history_frame.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=SPACING["page_x"],
            pady=(0, SPACING["page_x"])
        )

        self.history_frame.grid_columnconfigure(
            0,
            weight=1
        )

    def refresh_history(self):

        for widget in (
            self.history_frame.winfo_children()
        ):
            widget.destroy()

        history = get_test_history()

        self.count_label.configure(
            text=(
                f"{len(history)} saved "
                f"{'test' if len(history) == 1 else 'tests'}"
            )
        )

        if not history:

            self.create_empty_state()

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

    def create_empty_state(self):

        empty_card = Card(
            self.history_frame
        )

        empty_card.pack(
            fill="x",
            pady=10
        )

        icon = ctk.CTkLabel(
            empty_card,
            text="◷",
            font=("Segoe UI", 34),
            text_color=COLORS["text_muted"]
        )

        icon.pack(
            pady=(28, 8)
        )

        title = ctk.CTkLabel(
            empty_card,
            text="No test history yet",
            font=FONTS["section"],
            text_color=COLORS["text"]
        )

        title.pack()

        subtitle = ctk.CTkLabel(
            empty_card,
            text=(
                "Complete a benchmark and "
                "its result will appear here."
            ),
            font=FONTS["small"],
            text_color=COLORS["text_secondary"]
        )

        subtitle.pack(
            pady=(5, 28)
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

        card = Card(
            self.history_frame
        )

        card.pack(
            fill="x",
            pady=6
        )

        top = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        top.pack(
            fill="x",
            padx=18,
            pady=(16, 8)
        )

        left = ctk.CTkFrame(
            top,
            fg_color="transparent"
        )

        left.pack(
            side="left",
            fill="x",
            expand=True
        )

        title = ctk.CTkLabel(
            left,
            text=test_type,
            font=FONTS["body_bold"],
            text_color=COLORS["text"]
        )

        title.pack(
            anchor="w"
        )

        mode_text = (
            mode
            if mode
            else "Standard"
        )

        meta = ctk.CTkLabel(
            left,
            text=(
                f"{mode_text}  •  {created_at}"
            ),
            font=FONTS["small"],
            text_color=COLORS["text_secondary"]
        )

        meta.pack(
            anchor="w",
            pady=(3, 0)
        )

        right = ctk.CTkFrame(
            top,
            fg_color="transparent"
        )

        right.pack(
            side="right"
        )

        badge_status = self.get_badge_status(
            result
        )

        badge = StatusBadge(
            right,
            text=str(result or "RESULT").upper(),
            status=badge_status
        )

        badge.pack(
            side="right"
        )

        if score is not None:

            score_label = ctk.CTkLabel(
                right,
                text=f"{score:,}",
                font=("Segoe UI", 20, "bold"),
                text_color=COLORS["text"]
            )

            score_label.pack(
                side="right",
                padx=(0, 14)
            )

        divider = ctk.CTkFrame(
            card,
            height=1,
            fg_color=COLORS["border"]
        )

        divider.pack(
            fill="x",
            padx=18
        )

        bottom = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        bottom.pack(
            fill="x",
            padx=18,
            pady=(10, 14)
        )

        ctk.CTkLabel(
            bottom,
            text=f"Record #{test_id}",
            font=FONTS["small"],
            text_color=COLORS["text_muted"]
        ).pack(
            side="left"
        )

        summary_text = self.get_summary_text(
            test_type,
            score,
            result
        )

        ctk.CTkLabel(
            bottom,
            text=summary_text,
            font=FONTS["small"],
            text_color=COLORS["text_secondary"]
        ).pack(
            side="right"
        )

    def get_badge_status(
        self,
        result
    ):

        text = str(
            result or ""
        ).lower()

        if (
            "excellent" in text
            or "very good" in text
            or "good" in text
            or "stable" in text
        ):
            return "success"

        if (
            "average" in text
            or "heavy" in text
            or "active" in text
        ):
            return "warning"

        if (
            "failed" in text
            or "maximum" in text
        ):
            return "danger"

        return "normal"

    def get_summary_text(
        self,
        test_type,
        score,
        result
    ):

        if score is not None:

            return (
                f"Score {score:,} • "
                f"{result or 'Completed'}"
            )

        if result:

            return str(result)

        return "Completed"

    def clear_history(self):

        try:

            clear_test_history()

            self.refresh_history()

        except Exception as error:

            print(
                f"History clear error: {error}"
            )