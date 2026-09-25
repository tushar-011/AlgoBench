import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class AlgoBenchApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("AlgoBench")
        self.geometry("1200x750")
        self.minsize(1000, 650)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_sidebar()
        self.create_dashboard()

    def create_sidebar(self):
        sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_propagate(False)

        logo = ctk.CTkLabel(
            sidebar,
            text="AlgoBench",
            font=ctk.CTkFont(size=26, weight="bold")
        )
        logo.pack(pady=(30, 40))

        buttons = [
            "Dashboard",
            "System Overview",
            "CPU Test",
            "Memory Test",
            "Performance Test",
            "Stress Test",
            "All-in-One Test",
            "History",
            "Settings"
        ]

        for name in buttons:
            button = ctk.CTkButton(
                sidebar,
                text=name,
                height=40,
                anchor="w"
            )
            button.pack(fill="x", padx=20, pady=5)

    def create_dashboard(self):
        dashboard = ctk.CTkFrame(self, corner_radius=0)
        dashboard.grid(row=0, column=1, sticky="nsew")

        title = ctk.CTkLabel(
            dashboard,
            text="System Dashboard",
            font=ctk.CTkFont(size=30, weight="bold")
        )
        title.pack(anchor="w", padx=30, pady=(30, 10))

        subtitle = ctk.CTkLabel(
            dashboard,
            text="Monitor your system and run performance tests.",
            text_color="gray"
        )
        subtitle.pack(anchor="w", padx=30)

        card_container = ctk.CTkFrame(
            dashboard,
            fg_color="transparent"
        )
        card_container.pack(fill="x", padx=30, pady=30)

        for title_text, value in [
            ("CPU Usage", "--%"),
            ("Memory Usage", "--%"),
            ("Battery", "--%"),
            ("System Status", "Ready")
        ]:
            card = ctk.CTkFrame(card_container, width=200, height=120)
            card.pack(side="left", padx=(0, 15), expand=True, fill="x")

            label = ctk.CTkLabel(
                card,
                text=title_text,
                text_color="gray"
            )
            label.pack(pady=(20, 5))

            value_label = ctk.CTkLabel(
                card,
                text=value,
                font=ctk.CTkFont(size=24, weight="bold")
            )
            value_label.pack()


if __name__ == "__main__":
    app = AlgoBenchApp()
    app.mainloop()