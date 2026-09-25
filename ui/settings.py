import customtkinter as ctk

from database.db import clear_test_history


class SettingsPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(
            0,
            weight=1
        )

        self.create_header()
        self.create_settings_panel()
        self.create_about_panel()

    def create_header(self):

        title = ctk.CTkLabel(
            self,
            text="Settings",
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
            text="Customize AlgoBench preferences.",
            text_color="gray"
        )

        subtitle.grid(
            row=1,
            column=0,
            sticky="w",
            padx=30,
            pady=(0, 25)
        )

    def create_settings_panel(self):

        panel = ctk.CTkFrame(
            self,
            corner_radius=12
        )

        panel.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=30,
            pady=10
        )

        heading = ctk.CTkLabel(
            panel,
            text="Application Preferences",
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

        appearance_label = ctk.CTkLabel(
            panel,
            text="Appearance"
        )

        appearance_label.pack(
            anchor="w",
            padx=25,
            pady=(0, 5)
        )

        self.appearance_option = ctk.CTkOptionMenu(
            panel,
            values=[
                "Dark",
                "Light",
                "System"
            ],
            command=self.change_appearance
        )

        self.appearance_option.set(
            "Dark"
        )

        self.appearance_option.pack(
            fill="x",
            padx=25,
            pady=(0, 20)
        )

        refresh_label = ctk.CTkLabel(
            panel,
            text="Dashboard Refresh Rate"
        )

        refresh_label.pack(
            anchor="w",
            padx=25,
            pady=(0, 5)
        )

        self.refresh_option = ctk.CTkOptionMenu(
            panel,
            values=[
                "1 Second",
                "2 Seconds",
                "5 Seconds"
            ]
        )

        self.refresh_option.set(
            "1 Second"
        )

        self.refresh_option.pack(
            fill="x",
            padx=25,
            pady=(0, 20)
        )

        clear_button = ctk.CTkButton(
            panel,
            text="Clear Test History",
            height=42,
            command=self.clear_history
        )

        clear_button.pack(
            fill="x",
            padx=25,
            pady=(5, 10)
        )

        self.status_label = ctk.CTkLabel(
            panel,
            text="",
            text_color="gray"
        )

        self.status_label.pack(
            pady=(0, 20)
        )

    def create_about_panel(self):

        panel = ctk.CTkFrame(
            self,
            corner_radius=12
        )

        panel.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=30,
            pady=(10, 30)
        )

        heading = ctk.CTkLabel(
            panel,
            text="About AlgoBench",
            font=ctk.CTkFont(
                size=20,
                weight="bold"
            )
        )

        heading.pack(
            anchor="w",
            padx=25,
            pady=(25, 10)
        )

        description = ctk.CTkLabel(
            panel,
            text=(
                "AlgoBench is an offline system performance "
                "testing application built using Python.\n\n"
                "It provides CPU, memory, processing comparison, "
                "stress testing and complete system benchmarking."
            ),
            text_color="gray",
            justify="left",
            wraplength=700
        )

        description.pack(
            anchor="w",
            padx=25,
            pady=(0, 25)
        )

    def change_appearance(self, mode):

        ctk.set_appearance_mode(
            mode.lower()
        )

        self.status_label.configure(
            text=f"Appearance changed to {mode}"
        )

    def clear_history(self):

        try:

            clear_test_history()

            self.status_label.configure(
                text="Test history cleared successfully."
            )

        except Exception as error:

            self.status_label.configure(
                text=f"Could not clear history: {error}"
            )