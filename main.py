import customtkinter as ctk

from system.monitor import (
    get_cpu_usage,
    get_memory_usage,
    get_battery_info,
    get_disk_usage
)


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

        self.update_system_stats()

    def create_sidebar(self):
        sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0
        )

        sidebar.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        sidebar.grid_propagate(False)

        logo = ctk.CTkLabel(
            sidebar,
            text="AlgoBench",
            font=ctk.CTkFont(
                size=26,
                weight="bold"
            )
        )

        logo.pack(
            pady=(30, 40)
        )

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

            button.pack(
                fill="x",
                padx=20,
                pady=5
            )

    def create_dashboard(self):
        self.dashboard = ctk.CTkFrame(
            self,
            corner_radius=0
        )

        self.dashboard.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        title = ctk.CTkLabel(
            self.dashboard,
            text="System Dashboard",
            font=ctk.CTkFont(
                size=30,
                weight="bold"
            )
        )

        title.pack(
            anchor="w",
            padx=30,
            pady=(30, 10)
        )

        subtitle = ctk.CTkLabel(
            self.dashboard,
            text="Monitor your system and run performance tests.",
            text_color="gray"
        )

        subtitle.pack(
            anchor="w",
            padx=30
        )

        card_container = ctk.CTkFrame(
            self.dashboard,
            fg_color="transparent"
        )

        card_container.pack(
            fill="x",
            padx=30,
            pady=30
        )

        self.cpu_value = self.create_card(
            card_container,
            "CPU Usage"
        )

        self.memory_value = self.create_card(
            card_container,
            "Memory Usage"
        )

        self.battery_value = self.create_card(
            card_container,
            "Battery"
        )

        self.disk_value = self.create_card(
            card_container,
            "Disk Usage"
        )

    def create_card(
        self,
        parent,
        title
    ):
        card = ctk.CTkFrame(
            parent,
            height=130
        )

        card.pack(
            side="left",
            padx=(0, 15),
            expand=True,
            fill="x"
        )

        card.pack_propagate(False)

        label = ctk.CTkLabel(
            card,
            text=title,
            text_color="gray",
            font=ctk.CTkFont(
                size=14
            )
        )

        label.pack(
            pady=(25, 5)
        )

        value = ctk.CTkLabel(
            card,
            text="--",
            font=ctk.CTkFont(
                size=25,
                weight="bold"
            )
        )

        value.pack()

        return value

    def update_system_stats(self):

        cpu = get_cpu_usage()

        memory = get_memory_usage()

        battery = get_battery_info()

        disk = get_disk_usage()

        self.cpu_value.configure(
            text=f"{cpu}%"
        )

        self.memory_value.configure(
            text=f"{memory['percent']}%"
        )

        if battery["available"]:

            battery_text = f"{battery['percent']}%"

            if battery["charging"]:
                battery_text += " ⚡"

        else:
            battery_text = "N/A"

        self.battery_value.configure(
            text=battery_text
        )

        self.disk_value.configure(
            text=f"{disk['percent']}%"
        )

        self.after(
            1000,
            self.update_system_stats
        )


if __name__ == "__main__":
    app = AlgoBenchApp()
    app.mainloop()