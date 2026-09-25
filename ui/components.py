import customtkinter as ctk

from ui.theme import (
    COLORS,
    FONTS,
    SPACING
)


class PageHeader(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        title,
        subtitle
    ):
        super().__init__(
            parent,
            fg_color="transparent"
        )

        title_label = ctk.CTkLabel(
            self,
            text=title,
            font=FONTS["page_title"],
            text_color=COLORS["text"]
        )

        title_label.pack(
            anchor="w"
        )

        subtitle_label = ctk.CTkLabel(
            self,
            text=subtitle,
            font=FONTS["page_subtitle"],
            text_color=COLORS["text_secondary"]
        )

        subtitle_label.pack(
            anchor="w",
            pady=(4, 0)
        )


class Card(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        **kwargs
    ):
        super().__init__(
            parent,
            fg_color=COLORS["surface"],
            border_color=COLORS["border"],
            border_width=1,
            corner_radius=SPACING["radius"],
            **kwargs
        )


class SectionTitle(ctk.CTkLabel):

    def __init__(
        self,
        parent,
        text
    ):
        super().__init__(
            parent,
            text=text,
            font=FONTS["section"],
            text_color=COLORS["text"]
        )


class MutedLabel(ctk.CTkLabel):

    def __init__(
        self,
        parent,
        text,
        **kwargs
    ):
        super().__init__(
            parent,
            text=text,
            font=FONTS["body"],
            text_color=COLORS["text_secondary"],
            **kwargs
        )


class MetricCard(Card):

    def __init__(
        self,
        parent,
        title,
        value="--",
        subtitle=None
    ):

        super().__init__(
            parent,
            height=120
        )

        self.grid_propagate(False)

        title_label = ctk.CTkLabel(
            self,
            text=title.upper(),
            font=FONTS["small"],
            text_color=COLORS["text_secondary"]
        )

        title_label.pack(
            anchor="w",
            padx=18,
            pady=(17, 5)
        )

        self.value_label = ctk.CTkLabel(
            self,
            text=value,
            font=FONTS["metric"],
            text_color=COLORS["text"]
        )

        self.value_label.pack(
            anchor="w",
            padx=18
        )

        self.subtitle_label = None

        if subtitle:

            self.subtitle_label = ctk.CTkLabel(
                self,
                text=subtitle,
                font=FONTS["small"],
                text_color=COLORS["text_muted"]
            )

            self.subtitle_label.pack(
                anchor="w",
                padx=18,
                pady=(2, 0)
            )

    def set_value(
        self,
        value
    ):

        self.value_label.configure(
            text=value
        )


class StatusBadge(ctk.CTkLabel):

    def __init__(
        self,
        parent,
        text="READY",
        status="normal"
    ):

        self.status_colors = {
            "normal": COLORS["accent"],
            "success": COLORS["success"],
            "warning": COLORS["warning"],
            "danger": COLORS["danger"]
        }

        super().__init__(
            parent,
            text=text,
            font=("Segoe UI", 10, "bold"),
            text_color="#FFFFFF",
            corner_radius=8,
            padx=9,
            pady=3,
            fg_color=self.status_colors.get(
                status,
                COLORS["accent"]
            )
        )

    def set_status(
        self,
        text,
        status="normal"
    ):

        self.configure(
            text=text,
            fg_color=self.status_colors.get(
                status,
                COLORS["accent"]
            )
        )


class PrimaryButton(ctk.CTkButton):

    def __init__(
        self,
        parent,
        text,
        command=None,
        **kwargs
    ):

        super().__init__(
            parent,
            text=text,
            command=command,
            height=42,
            corner_radius=9,
            fg_color=COLORS["accent"],
            hover_color=COLORS["accent_hover"],
            font=FONTS["body_bold"],
            **kwargs
        )