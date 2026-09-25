import customtkinter as ctk

from database.db import (
    clear_test_history,
    get_setting,
    save_setting
)

from ui.theme import (
    COLORS,
    FONTS,
    SPACING
)

from ui.components import (
    PageHeader,
    Card
)


class SettingsPage(ctk.CTkFrame):

    def __init__(
        self,
        parent
    ):

        super().__init__(
            parent,
            fg_color=COLORS["app_bg"]
        )

        self.grid_rowconfigure(
            0,
            weight=1
        )

        self.grid_columnconfigure(
            0,
            weight=1
        )

        self.scroll = (
            ctk.CTkScrollableFrame(
                self,
                fg_color=COLORS["app_bg"],
                corner_radius=0
            )
        )

        self.scroll.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.scroll.grid_columnconfigure(
            0,
            weight=1
        )

        self.create_header()
        self.create_preferences()
        self.create_about()

    def create_header(self):

        header = PageHeader(
            self.scroll,
            title="Settings",
            subtitle=(
                "Customize AlgoBench and "
                "view application information."
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

    def create_preferences(self):

        panel = Card(
            self.scroll
        )

        panel.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=SPACING["page_x"],
            pady=(0, 16)
        )

        ctk.CTkLabel(
            panel,
            text="Application Preferences",
            font=FONTS["section"],
            text_color=COLORS["text"]
        ).pack(
            anchor="w",
            padx=22,
            pady=(20, 3)
        )

        ctk.CTkLabel(
            panel,
            text=(
                "Manage appearance, monitoring "
                "and saved benchmark data."
            ),
            font=FONTS["small"],
            text_color=COLORS[
                "text_secondary"
            ]
        ).pack(
            anchor="w",
            padx=22,
            pady=(0, 18)
        )

        self.create_appearance_setting(
            panel
        )

        self.create_refresh_setting(
            panel
        )

        self.create_history_setting(
            panel
        )

        self.status_label = (
            ctk.CTkLabel(
                panel,
                text="",
                font=FONTS["small"],
                text_color=COLORS[
                    "text_secondary"
                ]
            )
        )

        self.status_label.pack(
            anchor="w",
            padx=22,
            pady=(0, 18)
        )

    def create_appearance_setting(
        self,
        parent
    ):

        row = self.create_setting_row(
            parent,
            "Appearance",
            "Choose the application's visual theme."
        )

        self.appearance_option = (
            ctk.CTkOptionMenu(
                row,
                values=[
                    "Dark",
                    "Light",
                    "System"
                ],
                command=self.change_appearance,
                width=155,
                height=38,
                corner_radius=8,
                fg_color=COLORS["surface"],
                button_color=COLORS["accent"],
                button_hover_color=COLORS[
                    "accent_hover"
                ],
                text_color=COLORS["text"],
                dropdown_fg_color=COLORS[
                    "surface"
                ],
                dropdown_hover_color=COLORS[
                    "surface_hover"
                ]
            )
        )

        appearance = get_setting(
            "appearance",
            "Dark"
        )

        self.appearance_option.set(
            appearance
        )

        self.appearance_option.pack(
            side="right",
            padx=16,
            pady=13
        )

    def create_refresh_setting(
        self,
        parent
    ):

        row = self.create_setting_row(
            parent,
            "Dashboard Refresh Rate",
            (
                "Control how frequently live "
                "monitoring data is refreshed."
            )
        )

        self.refresh_option = (
            ctk.CTkOptionMenu(
                row,
                values=[
                    "1 Second",
                    "2 Seconds",
                    "5 Seconds"
                ],
                command=(
                    self.change_refresh_rate
                ),
                width=155,
                height=38,
                corner_radius=8,
                fg_color=COLORS["surface"],
                button_color=COLORS["accent"],
                button_hover_color=COLORS[
                    "accent_hover"
                ],
                text_color=COLORS["text"],
                dropdown_fg_color=COLORS[
                    "surface"
                ],
                dropdown_hover_color=COLORS[
                    "surface_hover"
                ]
            )
        )

        rate = get_setting(
            "refresh_rate",
            "1"
        )

        if rate == "1":

            value = "1 Second"

        else:

            value = (
                f"{rate} Seconds"
            )

        self.refresh_option.set(
            value
        )

        self.refresh_option.pack(
            side="right",
            padx=16,
            pady=13
        )

    def create_history_setting(
        self,
        parent
    ):

        row = self.create_setting_row(
            parent,
            "Test History",
            (
                "Remove all saved benchmark "
                "records from AlgoBench."
            )
        )

        clear_button = (
            ctk.CTkButton(
                row,
                text="Clear History",
                width=155,
                height=38,
                corner_radius=8,
                command=self.clear_history,
                fg_color=COLORS["surface"],
                hover_color=COLORS[
                    "surface_hover"
                ],
                border_width=1,
                border_color=COLORS[
                    "border"
                ],
                text_color=COLORS["text"],
                font=FONTS["body_bold"]
            )
        )

        clear_button.pack(
            side="right",
            padx=16,
            pady=13
        )

    def create_setting_row(
        self,
        parent,
        title,
        description
    ):

        row = ctk.CTkFrame(
            parent,
            fg_color=COLORS[
                "surface_light"
            ],
            corner_radius=10
        )

        row.pack(
            fill="x",
            padx=22,
            pady=6
        )

        text_frame = ctk.CTkFrame(
            row,
            fg_color="transparent"
        )

        text_frame.pack(
            side="left",
            fill="x",
            expand=True,
            padx=16,
            pady=13
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
            text_color=COLORS[
                "text_secondary"
            ]
        ).pack(
            anchor="w",
            pady=(3, 0)
        )

        return row

    def create_about(self):

        panel = Card(
            self.scroll
        )

        panel.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=SPACING["page_x"],
            pady=(
                0,
                SPACING["page_x"]
            )
        )

        header = ctk.CTkFrame(
            panel,
            fg_color="transparent"
        )

        header.pack(
            fill="x",
            padx=22,
            pady=(20, 14)
        )

        icon = ctk.CTkLabel(
            header,
            text="◇",
            font=(
                "Segoe UI",
                28,
                "bold"
            ),
            text_color=COLORS["accent"]
        )

        icon.pack(
            side="left",
            padx=(0, 10)
        )

        title_area = ctk.CTkFrame(
            header,
            fg_color="transparent"
        )

        title_area.pack(
            side="left"
        )

        ctk.CTkLabel(
            title_area,
            text="About AlgoBench",
            font=FONTS["section"],
            text_color=COLORS["text"]
        ).pack(
            anchor="w"
        )

        ctk.CTkLabel(
            title_area,
            text=(
                "System Performance "
                "Benchmarking Application"
            ),
            font=FONTS["small"],
            text_color=COLORS[
                "text_secondary"
            ]
        ).pack(
            anchor="w"
        )

        self.create_description(
            panel
        )

        self.create_feature_cards(
            panel
        )

        self.create_technology_section(
            panel
        )

        self.create_project_details(
            panel
        )

    def create_description(
        self,
        parent
    ):

        card = ctk.CTkFrame(
            parent,
            fg_color=COLORS[
                "surface_light"
            ],
            corner_radius=10
        )

        card.pack(
            fill="x",
            padx=22,
            pady=(0, 14)
        )

        text = (
            "AlgoBench is an offline desktop "
            "application for monitoring and "
            "evaluating computer performance.\n\n"

            "It combines real-time system "
            "monitoring with controlled benchmark "
            "workloads to provide easy-to-understand "
            "performance measurements.\n\n"

            "The application includes CPU and memory "
            "benchmarking, processing comparison, "
            "stress testing, complete system testing, "
            "live monitoring, persistent history, "
            "and customizable preferences."
        )

        ctk.CTkLabel(
            card,
            text=text,
            font=FONTS["body"],
            text_color=COLORS[
                "text_secondary"
            ],
            justify="left",
            anchor="w",
            wraplength=1000
        ).pack(
            fill="x",
            padx=18,
            pady=16
        )

    def create_feature_cards(
        self,
        parent
    ):

        container = ctk.CTkFrame(
            parent,
            fg_color="transparent"
        )

        container.pack(
            fill="x",
            padx=22,
            pady=(0, 14)
        )

        container.grid_columnconfigure(
            (0, 1, 2),
            weight=1,
            uniform="feature_cards"
        )

        self.create_feature_card(
            container,
            0,
            "Benchmarking",
            [
                "CPU Performance",
                "Memory Performance",
                "Processing Comparison",
                "System Stress",
                "Complete Benchmark"
            ]
        )

        self.create_feature_card(
            container,
            1,
            "System Monitoring",
            [
                "CPU Usage",
                "Memory Usage",
                "Battery Status",
                "Storage Usage",
                "System Uptime"
            ]
        )

        self.create_feature_card(
            container,
            2,
            "Application",
            [
                "Offline Operation",
                "SQLite History",
                "Theme Selection",
                "Refresh Settings",
                "Desktop Interface"
            ]
        )

    def create_feature_card(
        self,
        parent,
        column,
        title,
        items
    ):

        card = ctk.CTkFrame(
            parent,
            fg_color=COLORS[
                "surface_light"
            ],
            corner_radius=10
        )

        card.grid(
            row=0,
            column=column,
            sticky="nsew",
            padx=(
                0 if column == 0 else 5,
                0 if column == 2 else 5
            )
        )

        ctk.CTkLabel(
            card,
            text=title,
            font=FONTS["body_bold"],
            text_color=COLORS["text"]
        ).pack(
            anchor="w",
            padx=15,
            pady=(14, 8)
        )

        for item in items:

            ctk.CTkLabel(
                card,
                text=f"•  {item}",
                font=FONTS["small"],
                text_color=COLORS[
                    "text_secondary"
                ]
            ).pack(
                anchor="w",
                padx=15,
                pady=2
            )

        ctk.CTkFrame(
            card,
            fg_color="transparent",
            height=10
        ).pack()

    def create_technology_section(
        self,
        parent
    ):

        card = ctk.CTkFrame(
            parent,
            fg_color=COLORS[
                "surface_light"
            ],
            corner_radius=10
        )

        card.pack(
            fill="x",
            padx=22,
            pady=(0, 14)
        )

        ctk.CTkLabel(
            card,
            text="Technology Stack",
            font=FONTS["body_bold"],
            text_color=COLORS["text"]
        ).pack(
            anchor="w",
            padx=16,
            pady=(14, 10)
        )

        chips = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        chips.pack(
            fill="x",
            padx=16,
            pady=(0, 14)
        )

        technologies = [
            "Python",
            "CustomTkinter",
            "psutil",
            "Matplotlib",
            "SQLite"
        ]

        for technology in technologies:

            chip = ctk.CTkLabel(
                chips,
                text=technology,
                font=FONTS["small"],
                text_color=COLORS["text"],
                fg_color=COLORS["surface"],
                corner_radius=8,
                padx=11,
                pady=5
            )

            chip.pack(
                side="left",
                padx=(0, 7)
            )

    def create_project_details(
        self,
        parent
    ):

        card = ctk.CTkFrame(
            parent,
            fg_color=COLORS[
                "surface_light"
            ],
            corner_radius=10
        )

        card.pack(
            fill="x",
            padx=22,
            pady=(0, 22)
        )

        ctk.CTkLabel(
            card,
            text="Project Information",
            font=FONTS["body_bold"],
            text_color=COLORS["text"]
        ).pack(
            anchor="w",
            padx=16,
            pady=(14, 8)
        )

        details = [
            (
                "Application",
                "AlgoBench"
            ),
            (
                "Version",
                "1.0"
            ),
            (
                "Application Type",
                "Offline Desktop Application"
            ),
            (
                "Local Storage",
                "SQLite Database"
            ),
            (
                "Platform",
                "Windows"
            )
        ]

        for title, value in details:

            row = ctk.CTkFrame(
                card,
                fg_color="transparent"
            )

            row.pack(
                fill="x",
                padx=16,
                pady=4
            )

            ctk.CTkLabel(
                row,
                text=title,
                font=FONTS["small"],
                text_color=COLORS[
                    "text_muted"
                ]
            ).pack(
                side="left"
            )

            ctk.CTkLabel(
                row,
                text=value,
                font=FONTS["small"],
                text_color=COLORS[
                    "text_secondary"
                ]
            ).pack(
                side="right"
            )

        ctk.CTkFrame(
            card,
            fg_color="transparent",
            height=10
        ).pack()

    def change_appearance(
        self,
        mode
    ):

        ctk.set_appearance_mode(
            mode.lower()
        )

        save_setting(
            "appearance",
            mode
        )

        self.status_label.configure(
            text=(
                f"{mode} appearance "
                "applied and saved."
            )
        )

    def change_refresh_rate(
        self,
        value
    ):

        rate = value.split()[0]

        save_setting(
            "refresh_rate",
            rate
        )

        self.status_label.configure(
            text=(
                f"Dashboard refresh rate "
                f"set to {value}."
            )
        )

    def clear_history(self):

        try:

            clear_test_history()

            self.status_label.configure(
                text=(
                    "Test history cleared "
                    "successfully."
                )
            )

        except Exception as error:

            self.status_label.configure(
                text=(
                    "Could not clear history: "
                    f"{error}"
                )
            )