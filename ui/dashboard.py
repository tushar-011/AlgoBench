from collections import deque

import customtkinter as ctk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from database.db import get_setting

from system.monitor import (
    get_cpu_usage,
    get_memory_usage,
    get_battery_info,
    get_disk_usage
)

from ui.theme import (
    COLORS,
    FONTS,
    SPACING,
    get_color
)

from ui.components import (
    PageHeader,
    Card,
    MetricCard,
    StatusBadge
)


class DashboardPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color=COLORS["app_bg"]
        )

        self.grid_columnconfigure(
            (0, 1, 2, 3),
            weight=1,
            uniform="dashboard_cards"
        )

        self.grid_rowconfigure(
            3,
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
        self.create_metric_cards()
        self.create_monitoring_area()

        self.update_system_stats()

    def create_header(self):

        header = PageHeader(
            self,
            title="Dashboard",
            subtitle=(
                "Real-time overview of your "
                "system performance and health."
            )
        )

        header.grid(
            row=0,
            column=0,
            columnspan=4,
            sticky="ew",
            padx=SPACING["page_x"],
            pady=(
                SPACING["page_top"],
                22
            )
        )

    def create_metric_cards(self):

        self.cpu_card = MetricCard(
            self,
            title="CPU Usage",
            value="--",
            subtitle="Processor activity"
        )

        self.cpu_card.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=(
                SPACING["page_x"],
                7
            ),
            pady=(0, 10)
        )

        self.memory_card = MetricCard(
            self,
            title="Memory Usage",
            value="--",
            subtitle="System memory"
        )

        self.memory_card.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=7,
            pady=(0, 10)
        )

        self.battery_card = MetricCard(
            self,
            title="Battery",
            value="--",
            subtitle="Power status"
        )

        self.battery_card.grid(
            row=1,
            column=2,
            sticky="nsew",
            padx=7,
            pady=(0, 10)
        )

        self.disk_card = MetricCard(
            self,
            title="Storage",
            value="--",
            subtitle="Disk usage"
        )

        self.disk_card.grid(
            row=1,
            column=3,
            sticky="nsew",
            padx=(
                7,
                SPACING["page_x"]
            ),
            pady=(0, 10)
        )

    def create_monitoring_area(self):

        self.create_graph_panel()
        self.create_status_panel()

    def create_graph_panel(self):

        graph_panel = Card(
            self
        )

        graph_panel.grid(
            row=2,
            column=0,
            columnspan=3,
            rowspan=2,
            sticky="nsew",
            padx=(
                SPACING["page_x"],
                8
            ),
            pady=(
                8,
                SPACING["page_x"]
            )
        )

        graph_panel.grid_rowconfigure(
            2,
            weight=1
        )

        graph_panel.grid_columnconfigure(
            0,
            weight=1
        )

        title_frame = ctk.CTkFrame(
            graph_panel,
            fg_color="transparent"
        )

        title_frame.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=22,
            pady=(20, 0)
        )

        graph_title = ctk.CTkLabel(
            title_frame,
            text="Performance Activity",
            font=FONTS["section"],
            text_color=COLORS["text"]
        )

        graph_title.pack(
            side="left"
        )

        live_badge = StatusBadge(
            title_frame,
            text="LIVE",
            status="success"
        )

        live_badge.pack(
            side="right"
        )

        graph_subtitle = ctk.CTkLabel(
            graph_panel,
            text=(
                "CPU and memory activity "
                "during the last 30 updates."
            ),
            font=FONTS["small"],
            text_color=COLORS["text_secondary"]
        )

        graph_subtitle.grid(
            row=1,
            column=0,
            sticky="w",
            padx=22,
            pady=(5, 4)
        )

        self.figure = Figure(
            figsize=(7, 3.5),
            dpi=100
        )

        self.axis = self.figure.add_subplot(
            111
        )

        self.apply_graph_theme()

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

        self.axis.set_xlabel(
            "Recent activity"
        )

        self.axis.grid(
            True,
            alpha=0.12
        )

        self.cpu_line, = self.axis.plot(
            list(self.cpu_history),
            label="CPU",
            linewidth=2
        )

        self.memory_line, = self.axis.plot(
            list(self.memory_history),
            label="Memory",
            linewidth=2
        )

        self.legend = self.axis.legend(
            loc="upper left",
            frameon=True
        )

        self.figure.tight_layout(
            pad=1.8
        )

        self.canvas_frame = ctk.CTkFrame(
            graph_panel,
            fg_color="transparent"
        )

        self.canvas_frame.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=12,
            pady=(4, 12)
        )

        self.canvas = FigureCanvasTkAgg(
            self.figure,
            master=self.canvas_frame
        )

        self.canvas.draw()

        self.canvas_widget = (
            self.canvas.get_tk_widget()
        )

        self.canvas_widget.configure(
            bg=get_color("surface"),
            highlightthickness=0
        )

        self.canvas_widget.pack(
            fill="both",
            expand=True
        )

        self.apply_graph_theme()

    def apply_graph_theme(self):

        surface = get_color(
            "surface"
        )

        surface_light = get_color(
            "surface_light"
        )

        border = get_color(
            "border"
        )

        text = get_color(
            "text"
        )

        text_secondary = get_color(
            "text_secondary"
        )

        text_muted = get_color(
            "text_muted"
        )

        self.figure.patch.set_facecolor(
            surface
        )

        self.axis.set_facecolor(
            surface
        )

        self.axis.tick_params(
            colors=text_muted,
            labelsize=8
        )

        self.axis.xaxis.label.set_color(
            text_muted
        )

        self.axis.yaxis.label.set_color(
            text_secondary
        )

        for spine in (
            self.axis.spines.values()
        ):

            spine.set_color(
                border
            )

        if hasattr(
            self,
            "legend"
        ):

            self.legend.get_frame().set_facecolor(
                surface_light
            )

            self.legend.get_frame().set_edgecolor(
                border
            )

            for legend_text in (
                self.legend.get_texts()
            ):

                legend_text.set_color(
                    text
                )

        if hasattr(
            self,
            "canvas_widget"
        ):

            self.canvas_widget.configure(
                bg=surface
            )

        if hasattr(
            self,
            "canvas"
        ):

            self.canvas.draw_idle()

    def create_status_panel(self):

        status_panel = Card(
            self
        )

        status_panel.grid(
            row=2,
            column=3,
            rowspan=2,
            sticky="nsew",
            padx=(
                8,
                SPACING["page_x"]
            ),
            pady=(
                8,
                SPACING["page_x"]
            )
        )

        heading_frame = ctk.CTkFrame(
            status_panel,
            fg_color="transparent"
        )

        heading_frame.pack(
            fill="x",
            padx=22,
            pady=(20, 0)
        )

        heading = ctk.CTkLabel(
            heading_frame,
            text="System Health",
            font=FONTS["section"],
            text_color=COLORS["text"]
        )

        heading.pack(
            side="left"
        )

        self.status_badge = StatusBadge(
            heading_frame,
            text="CHECKING",
            status="normal"
        )

        self.status_badge.pack(
            side="right"
        )

        separator = ctk.CTkFrame(
            status_panel,
            height=1,
            fg_color=COLORS["border"]
        )

        separator.pack(
            fill="x",
            padx=22,
            pady=(18, 18)
        )

        self.status_value = ctk.CTkLabel(
            status_panel,
            text="Checking...",
            font=("Segoe UI", 27, "bold"),
            text_color=COLORS["text"]
        )

        self.status_value.pack(
            pady=(10, 6)
        )

        self.status_info = ctk.CTkLabel(
            status_panel,
            text="Monitoring system resources",
            font=FONTS["small"],
            text_color=COLORS["text_secondary"],
            wraplength=230,
            justify="center"
        )

        self.status_info.pack(
            padx=22,
            pady=(0, 24)
        )

        resources = ctk.CTkFrame(
            status_panel,
            fg_color=COLORS["surface_light"],
            corner_radius=10
        )

        resources.pack(
            fill="x",
            padx=20,
            pady=(0, 18)
        )

        self.live_cpu_label = (
            self.create_status_row(
                resources,
                "CPU",
                "--"
            )
        )

        self.live_memory_label = (
            self.create_status_row(
                resources,
                "Memory",
                "--"
            )
        )

        self.live_battery_label = (
            self.create_status_row(
                resources,
                "Battery",
                "--"
            )
        )

        self.live_disk_label = (
            self.create_status_row(
                resources,
                "Storage",
                "--"
            )
        )

        footer = ctk.CTkLabel(
            status_panel,
            text="Monitoring automatically",
            font=FONTS["small"],
            text_color=COLORS["text_muted"]
        )

        footer.pack(
            side="bottom",
            pady=18
        )

    def create_status_row(
        self,
        parent,
        title,
        value
    ):

        row = ctk.CTkFrame(
            parent,
            fg_color="transparent"
        )

        row.pack(
            fill="x",
            padx=14,
            pady=9
        )

        title_label = ctk.CTkLabel(
            row,
            text=title,
            font=FONTS["body"],
            text_color=COLORS["text_secondary"]
        )

        title_label.pack(
            side="left"
        )

        value_label = ctk.CTkLabel(
            row,
            text=value,
            font=FONTS["body_bold"],
            text_color=COLORS["text"]
        )

        value_label.pack(
            side="right"
        )

        return value_label

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
                "System resources are operating comfortably.",
                "NORMAL",
                "success"
            )

        if highest_usage < 75:

            return (
                "Active",
                "System is handling a moderate workload.",
                "ACTIVE",
                "normal"
            )

        if highest_usage < 90:

            return (
                "High Load",
                "System resources are currently heavily used.",
                "HIGH",
                "warning"
            )

        return (
            "Very High Load",
            "System resources are close to maximum usage.",
            "VERY HIGH",
            "danger"
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

    def refresh_theme(self):

        self.apply_graph_theme()

    def update_system_stats(self):

        try:

            cpu = get_cpu_usage()

            memory = get_memory_usage()

            battery = get_battery_info()

            disk = get_disk_usage()

            memory_percent = (
                memory["percent"]
            )

            disk_percent = (
                disk["percent"]
            )

            self.cpu_card.set_value(
                f"{cpu:.0f}%"
            )

            self.memory_card.set_value(
                f"{memory_percent:.0f}%"
            )

            self.disk_card.set_value(
                f"{disk_percent:.0f}%"
            )

            if battery["available"]:

                battery_percent = (
                    battery["percent"]
                )

                battery_text = (
                    f"{battery_percent:.0f}%"
                )

                if battery["charging"]:

                    battery_subtitle = (
                        "Charging"
                    )

                else:

                    battery_subtitle = (
                        "On battery"
                    )

            else:

                battery_percent = None

                battery_text = "N/A"

                battery_subtitle = (
                    "Battery unavailable"
                )

            self.battery_card.set_value(
                battery_text
            )

            if (
                self.battery_card.subtitle_label
                is not None
            ):

                self.battery_card.subtitle_label.configure(
                    text=battery_subtitle
                )

            (
                status,
                message,
                badge_text,
                badge_type
            ) = self.get_status(
                cpu,
                memory_percent
            )

            self.status_value.configure(
                text=status
            )

            self.status_info.configure(
                text=message
            )

            self.status_badge.set_status(
                badge_text,
                badge_type
            )

            self.live_cpu_label.configure(
                text=f"{cpu:.0f}%"
            )

            self.live_memory_label.configure(
                text=(
                    f"{memory_percent:.0f}%"
                )
            )

            if battery_percent is not None:

                self.live_battery_label.configure(
                    text=(
                        f"{battery_percent:.0f}%"
                    )
                )

            else:

                self.live_battery_label.configure(
                    text="N/A"
                )

            self.live_disk_label.configure(
                text=(
                    f"{disk_percent:.0f}%"
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

        try:

            refresh_rate = int(
                get_setting(
                    "refresh_rate",
                    "1"
                )
            )

        except (
            TypeError,
            ValueError
        ):

            refresh_rate = 1

        self.after(
            refresh_rate * 1000,
            self.update_system_stats
        )