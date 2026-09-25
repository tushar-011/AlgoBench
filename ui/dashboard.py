import customtkinter as ctk

from system.monitor import (
    get_cpu_usage,
    get_memory_usage,
    get_battery_info,
    get_disk_usage
)


class DashboardPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self.create_header()
        self.create_system_cards()

        self.update_system_stats()

    def create_header(self):

        title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=ctk.CTkFont(
                size=30,
                weight="bold"
            )
        )

        title.grid(
            row=0,
            column=0,
            columnspan=4,
            sticky="w",
            padx=30,
            pady=(30, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Monitor your system performance in real time.",
            text_color="gray"
        )

        subtitle.grid(
            row=1,
            column=0,
            columnspan=4,
            sticky="w",
            padx=30,
            pady=(0, 25)
        )

    def create_system_cards(self):

        self.cpu_value = self.create_card(
            column=0,
            title="CPU Usage"
        )

        self.memory_value = self.create_card(
            column=1,
            title="Memory Usage"
        )

        self.battery_value = self.create_card(
            column=2,
            title="Battery"
        )

        self.disk_value = self.create_card(
            column=3,
            title="Disk Usage"
        )

    def create_card(self, column, title):

        card = ctk.CTkFrame(
            self,
            corner_radius=12,
            height=140
        )

        card.grid(
            row=2,
            column=column,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        card.grid_propagate(False)

        card_title = ctk.CTkLabel(
            card,
            text=title,
            text_color="gray",
            font=ctk.CTkFont(
                size=14
            )
        )

        card_title.pack(
            pady=(25, 8)
        )

        value = ctk.CTkLabel(
            card,
            text="--",
            font=ctk.CTkFont(
                size=28,
                weight="bold"
            )
        )

        value.pack()

        return value

    def update_system_stats(self):

        try:

            cpu = get_cpu_usage()
            memory = get_memory_usage()
            battery = get_battery_info()
            disk = get_disk_usage()

            self.cpu_value.configure(
                text=f"{cpu:.0f}%"
            )

            self.memory_value.configure(
                text=f"{memory['percent']:.0f}%"
            )

            if battery["available"]:

                battery_text = f"{battery['percent']:.0f}%"

                if battery["charging"]:
                    battery_text += " ⚡"

            else:
                battery_text = "N/A"

            self.battery_value.configure(
                text=battery_text
            )

            self.disk_value.configure(
                text=f"{disk['percent']:.0f}%"
            )

        except Exception as error:
            print(
                f"Dashboard monitoring error: {error}"
            )

        self.after(
            1000,
            self.update_system_stats
        )