import customtkinter as ctk

from ui.theme import (
    COLORS,
    FONTS
)


class Sidebar(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        navigation_callback
    ):
        super().__init__(
            parent,
            width=210,
            corner_radius=0,
            fg_color=COLORS["sidebar"]
        )

        self.navigation_callback = (
            navigation_callback
        )

        self.grid_propagate(False)

        self.buttons = {}

        self.create_logo()
        self.create_navigation()
        self.create_footer()

    def create_logo(self):

        logo_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        logo_frame.pack(
            fill="x",
            padx=20,
            pady=(28, 28)
        )

        icon = ctk.CTkLabel(
            logo_frame,
            text="◈",
            text_color=COLORS["accent"],
            font=("Segoe UI", 26, "bold")
        )

        icon.pack(
            side="left",
            padx=(0, 8)
        )

        logo = ctk.CTkLabel(
            logo_frame,
            text="AlgoBench",
            font=FONTS["sidebar_logo"],
            text_color=COLORS["text"]
        )

        logo.pack(
            side="left"
        )

    def create_navigation(self):

        pages = [
            ("Dashboard", "▦"),
            ("System Overview", "▣"),
            ("CPU Test", "◉"),
            ("Memory Test", "▤"),
            ("Performance Test", "⇄"),
            ("Stress Test", "⚡"),
            ("All-in-One Test", "◆"),
            ("History", "◷"),
            ("Settings", "⚙")
        ]

        for page_name, icon in pages:

            button = ctk.CTkButton(
                self,
                text=f"  {icon}   {page_name}",
                anchor="w",

                height=42,

                corner_radius=9,

                fg_color="transparent",
                hover_color=COLORS[
                    "surface_hover"
                ],

                text_color=COLORS["text_secondary"],

                font=FONTS["sidebar"],

                command=lambda name=page_name:
                self.select_page(name)
            )

            button.pack(
                fill="x",
                padx=13,
                pady=3
            )

            self.buttons[
                page_name
            ] = button

    def create_footer(self):

        footer = ctk.CTkLabel(
            self,
            text="AlgoBench  •  v1.0",
            font=FONTS["small"],
            text_color=COLORS["text_muted"]
        )

        footer.pack(
            side="bottom",
            pady=20
        )

    def select_page(
        self,
        page_name
    ):

        for name, button in (
            self.buttons.items()
        ):

            if name == page_name:

                button.configure(
                    fg_color=COLORS["accent_soft"],
                    text_color=COLORS["text"]
                )

            else:

                button.configure(
                    fg_color="transparent",
                    text_color=COLORS[
                        "text_secondary"
                    ]
                )

        self.navigation_callback(
            page_name
        )

    def set_active(
        self,
        page_name
    ):

        for name, button in (
            self.buttons.items()
        ):

            if name == page_name:

                button.configure(
                    fg_color=COLORS["accent_soft"],
                    text_color=COLORS["text"]
                )

            else:

                button.configure(
                    fg_color="transparent",
                    text_color=COLORS[
                        "text_secondary"
                    ]
                )