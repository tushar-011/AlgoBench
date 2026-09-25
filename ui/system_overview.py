import customtkinter as ctk

from system.monitor import (
    get_system_info,
    get_memory_usage,
    get_disk_usage,
    get_battery_info,
    get_cpu_usage,
    get_system_uptime
)


class SystemOverviewPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure((0, 1), weight=1)

        self.create_header()
        self.create_information_cards()

        self.update_live_information()

    def create_header(self):

        title = ctk.CTkLabel(
            self,
            text="System Overview",
            font=ctk.CTkFont(
                size=30,
                weight="bold"
            )
        )

        title.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="w",
            padx=30,
            pady=(30, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="View your device information and current system status.",
            text_color="gray"
        )

        subtitle.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="w",
            padx=30,
            pady=(0, 25)
        )

    def create_information_cards(self):

        system_info = get_system_info()

        self.device_card = self.create_card(
            row=2,
            column=0,
            title="Device",
            lines=[
                f"Name: {system_info['device_name']}",
                f"Operating System: {system_info['os']}",
                f"Architecture: {system_info['architecture']}"
            ]
        )

        self.processor_card = self.create_card(
            row=2,
            column=1,
            title="Processor",
            lines=[
                system_info["processor"],
                f"CPU Cores: {system_info['physical_cores']}",
                f"Threads: {system_info['threads']}"
            ]
        )

        self.memory_value = self.create_dynamic_card(
            row=3,
            column=0,
            title="Memory"
        )

        self.storage_value = self.create_dynamic_card(
            row=3,
            column=1,
            title="Storage"
        )

        self.battery_value = self.create_dynamic_card(
            row=4,
            column=0,
            title="Battery & Power"
        )

        self.status_value = self.create_dynamic_card(
            row=4,
            column=1,
            title="System Status"
        )

    def create_card(self, row, column, title, lines):

        card = ctk.CTkFrame(
            self,
            corner_radius=12
        )

        card.grid(
            row=row,
            column=column,
            sticky="nsew",
            padx=15,
            pady=10
        )

        title_label = ctk.CTkLabel(
            card,
            text=title,
            font=ctk.CTkFont(
                size=18,
                weight="bold"
            )
        )

        title_label.pack(
            anchor="w",
            padx=20,
            pady=(18, 10)
        )

        for line in lines:

            label = ctk.CTkLabel(
                card,
                text=line,
                text_color="gray",
                anchor="w"
            )

            label.pack(
                anchor="w",
                padx=20,
                pady=3
            )

        return card

    def create_dynamic_card(self, row, column, title):

        card = ctk.CTkFrame(
            self,
            corner_radius=12,
            height=130
        )

        card.grid(
            row=row,
            column=column,
            sticky="nsew",
            padx=15,
            pady=10
        )

        card.grid_propagate(False)

        title_label = ctk.CTkLabel(
            card,
            text=title,
            font=ctk.CTkFont(
                size=18,
                weight="bold"
            )
        )

        title_label.pack(
            anchor="w",
            padx=20,
            pady=(18, 8)
        )

        value_label = ctk.CTkLabel(
            card,
            text="Loading...",
            text_color="gray",
            justify="left",
            anchor="w"
        )

        value_label.pack(
            anchor="w",
            padx=20
        )

        return value_label

    def update_live_information(self):

        try:

            memory = get_memory_usage()
            disk = get_disk_usage()
            battery = get_battery_info()
            cpu = get_cpu_usage()
            uptime = get_system_uptime()

            self.memory_value.configure(
                text=(
                    f"Used: {memory['used_gb']} GB / "
                    f"{memory['total_gb']} GB\n"
                    f"Usage: {memory['percent']:.0f}%"
                )
            )

            self.storage_value.configure(
                text=(
                    f"Used: {disk['used_gb']} GB / "
                    f"{disk['total_gb']} GB\n"
                    f"Free: {disk['free_gb']} GB"
                )
            )

            if battery["available"]:

                battery_status = (
                    "Charging"
                    if battery["charging"]
                    else "On Battery"
                )

                battery_text = (
                    f"Battery: {battery['percent']:.0f}%\n"
                    f"Power: {battery_status}"
                )

            else:
                battery_text = "Battery information unavailable"

            self.battery_value.configure(
                text=battery_text
            )

            self.status_value.configure(
                text=(
                    f"CPU Usage: {cpu:.0f}%\n"
                    f"System Uptime: {uptime}"
                )
            )

        except Exception as error:
            print(
                f"System overview error: {error}"
            )

        self.after(
            2000,
            self.update_live_information
        )