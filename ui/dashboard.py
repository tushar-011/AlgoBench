from collections import deque

import customtkinter as ctk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from system.monitor import (
    get_cpu_usage,
    get_memory_usage,
    get_battery_info,
    get_disk_usage
)


class DashboardPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(
            (0, 1, 2, 3),
            weight=1
        )

        self.grid_rowconfigure(
            4,
            weight=1
        )

        self.cpu_history = deque(
            [0] * 30,
            maxlen=30
        )

        self.memory_history = deque(
            [0] * 30,
            maxlen=30
        )

        self.create_header()
        self.create_system_cards()
        self.create_graph_area()

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
            text=(
                "Monitor your system performance "
                "in real time."
            ),
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

    def create_card(
        self,
        column,
        title
    ):

        card = ctk.CTkFrame(
            self,
            corner_radius=12,
            height=135
        )

        card.grid(
            row=2,
            column=column,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        card.grid_propagate(
            False
        )

        title_label = ctk.CTkLabel(
            card,
            text=title,
            text_color="gray",
            font=ctk.CTkFont(
                size=14
            )
        )

        title_label.pack(
            pady=(22, 5)
        )

        value_label = ctk.CTkLabel(
            card,
            text="--",
            font=ctk.CTkFont(
                size=28,
                weight="bold"
            )
        )

        value_label.pack()

        return value_label

    def create_graph_area(self):

        graph_panel = ctk.CTkFrame(
            self,
            corner_radius=12
        )

        graph_panel.grid(
            row=3,
            column=0,
            columnspan=3,
            sticky="nsew",
            padx=(10, 5),
            pady=(15, 25)
        )

        graph_title = ctk.CTkLabel(
            graph_panel,
            text="Live Performance",
            font=ctk.CTkFont(
                size=20,
                weight="bold"
            )
        )

        graph_title.pack(
            anchor="w",
            padx=20,
            pady=(18, 5)
        )

        graph_subtitle = ctk.CTkLabel(
            graph_panel,
            text="Last 30 seconds",
            text_color="gray"
        )

        graph_subtitle.pack(
            anchor="w",
            padx=20,
            pady=(0, 5)
        )

        self.figure = Figure(
            figsize=(7, 3.5),
            dpi=100
        )

        self.figure.patch.set_facecolor(
            "#2b2b2b"
        )

        self.axis = (
            self.figure.add_subplot(
                111
            )
        )

        self.axis.set_facecolor(
            "#2b2b2b"
        )

        self.axis.set_ylim(
            0,
            100
        )

        self.axis.set_xlim(
            0,
            29
        )

        self.axis.set_ylabel(
            "Usage %"
        )

        self.axis.tick_params(
            colors="gray"
        )

        self.axis.xaxis.label.set_color(
            "gray"
        )

        self.axis.yaxis.label.set_color(
            "gray"
        )

        for spine in (
            self.axis.spines.values()
        ):
            spine.set_color(
                "#555555"
            )

        self.cpu_line, = (
            self.axis.plot(
                list(self.cpu_history),
                label="CPU"
            )
        )

        self.memory_line, = (
            self.axis.plot(
                list(self.memory_history),
                label="Memory"
            )
        )

        legend = self.axis.legend(
            loc="upper left"
        )

        legend.get_frame().set_facecolor(
            "#2b2b2b"
        )

        for text in (
            legend.get_texts()
        ):
            text.set_color(
                "white"
            )

        self.figure.tight_layout()

        self.canvas = (
            FigureCanvasTkAgg(
                self.figure,
                master=graph_panel
            )
        )

        self.canvas.draw()

        self.canvas.get_tk_widget().pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 10)
        )

        self.create_status_panel()

    def create_status_panel(self):

        status_panel = ctk.CTkFrame(
            self,
            corner_radius=12
        )

        status_panel.grid(
            row=3,
            column=3,
            sticky="nsew",
            padx=(5, 10),
            pady=(15, 25)
        )

        heading = ctk.CTkLabel(
            status_panel,
            text="System Status",
            font=ctk.CTkFont(
                size=20,
                weight="bold"
            )
        )

        heading.pack(
            anchor="w",
            padx=20,
            pady=(20, 20)
        )

        self.status_value = (
            ctk.CTkLabel(
                status_panel,
                text="Checking...",
                font=ctk.CTkFont(
                    size=22,
                    weight="bold"
                )
            )
        )

        self.status_value.pack(
            pady=(15, 8)
        )

        self.status_info = (
            ctk.CTkLabel(
                status_panel,
                text="Monitoring system",
                text_color="gray",
                justify="center"
            )
        )

        self.status_info.pack(
            padx=15,
            pady=5
        )

        self.live_cpu_label = (
            ctk.CTkLabel(
                status_panel,
                text="CPU: --"
            )
        )

        self.live_cpu_label.pack(
            pady=(25, 5)
        )

        self.live_memory_label = (
            ctk.CTkLabel(
                status_panel,
                text="Memory: --"
            )
        )

        self.live_memory_label.pack(
            pady=5
        )

    def get_status(
        self,
        cpu,
        memory
    ):

        highest_usage = max(
            cpu,
            memory
        )

        if highest_usage < 50:

            return (
                "Normal",
                "System is running comfortably."
            )

        if highest_usage < 75:

            return (
                "Active",
                "System is handling moderate load."
            )

        if highest_usage < 90:

            return (
                "High Load",
                "System resources are heavily used."
            )

        return (
            "Very High Load",
            "System is close to maximum usage."
        )

    def update_graph(
        self,
        cpu,
        memory
    ):

        self.cpu_history.append(
            cpu
        )

        self.memory_history.append(
            memory
        )

        x_values = list(
            range(
                len(
                    self.cpu_history
                )
            )
        )

        self.cpu_line.set_data(
            x_values,
            list(
                self.cpu_history
            )
        )

        self.memory_line.set_data(
            x_values,
            list(
                self.memory_history
            )
        )

        self.canvas.draw_idle()

    def update_system_stats(self):

        try:

            cpu = get_cpu_usage()

            memory = (
                get_memory_usage()
            )

            battery = (
                get_battery_info()
            )

            disk = (
                get_disk_usage()
            )

            memory_percent = (
                memory["percent"]
            )

            self.cpu_value.configure(
                text=f"{cpu:.0f}%"
            )

            self.memory_value.configure(
                text=(
                    f"{memory_percent:.0f}%"
                )
            )

            if battery["available"]:

                battery_text = (
                    f"{battery['percent']:.0f}%"
                )

                if battery["charging"]:

                    battery_text += " ⚡"

            else:

                battery_text = "N/A"

            self.battery_value.configure(
                text=battery_text
            )

            self.disk_value.configure(
                text=(
                    f"{disk['percent']:.0f}%"
                )
            )

            status, message = (
                self.get_status(
                    cpu,
                    memory_percent
                )
            )

            self.status_value.configure(
                text=status
            )

            self.status_info.configure(
                text=message
            )

            self.live_cpu_label.configure(
                text=(
                    f"CPU: {cpu:.0f}%"
                )
            )

            self.live_memory_label.configure(
                text=(
                    "Memory: "
                    f"{memory_percent:.0f}%"
                )
            )

            self.update_graph(
                cpu,
                memory_percent
            )

        except Exception as error:

            print(
                "Dashboard monitoring "
                f"error: {error}"
            )

        self.after(
            1000,
            self.update_system_stats
        )