import customtkinter as ctk

from system.monitor import (
    get_system_info,
    get_memory_usage,
    get_disk_usage,
    get_battery_info,
    get_cpu_usage,
    get_system_uptime
)

from ui.theme import (
    COLORS,
    FONTS,
    SPACING
)

from ui.components import (
    PageHeader,
    Card,
    MetricCard,
    StatusBadge
)


class SystemOverviewPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color=COLORS["app_bg"]
        )

        self.grid_columnconfigure(
            (0, 1),
            weight=1,
            uniform="overview_columns"
        )

        self.grid_rowconfigure(
            3,
            weight=1
        )

        self.create_header()
        self.create_device_section()
        self.create_resource_section()

        self.update_live_data()

    def create_header(self):

        header = PageHeader(
            self,
            title="System Overview",
            subtitle=(
                "View your device information "
                "and current system status."
            )
        )

        header.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=SPACING["page_x"],
            pady=(
                SPACING["page_top"],
                20
            )
        )

    def create_device_section(self):

        system_info = get_system_info()

        device_card = Card(
            self
        )

        device_card.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=(
                SPACING["page_x"],
                8
            ),
            pady=(0, 10)
        )

        processor_card = Card(
            self
        )

        processor_card.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=(
                8,
                SPACING["page_x"]
            ),
            pady=(0, 10)
        )

        self.create_section_heading(
            device_card,
            "Device Information"
        )

        device_name = system_info.get(
            "device_name",
            "Unknown"
        )

        os_name = system_info.get(
            "os",
            "Unknown"
        )

        architecture = system_info.get(
            "architecture",
            "Unknown"
        )

        self.create_info_row(
            device_card,
            "Device Name",
            device_name
        )

        self.create_info_row(
            device_card,
            "Operating System",
            os_name
        )

        self.create_info_row(
            device_card,
            "Architecture",
            architecture
        )

        self.create_section_heading(
            processor_card,
            "Processor"
        )

        processor = system_info.get(
            "processor",
            "Unknown"
        )

        cores = system_info.get(
            "physical_cores",
            "--"
        )

        threads = system_info.get(
            "threads",
            "--"
        )

        processor_name = ctk.CTkLabel(
            processor_card,
            text=processor,
            font=FONTS["body_bold"],
            text_color=COLORS["text"],
            wraplength=480,
            justify="left"
        )

        processor_name.pack(
            anchor="w",
            padx=22,
            pady=(4, 15)
        )

        specs_frame = ctk.CTkFrame(
            processor_card,
            fg_color="transparent"
        )

        specs_frame.pack(
            fill="x",
            padx=22,
            pady=(0, 20)
        )

        self.create_spec_chip(
            specs_frame,
            "Cores",
            str(cores)
        )

        self.create_spec_chip(
            specs_frame,
            "Threads",
            str(threads)
        )

    def create_resource_section(self):

        title = ctk.CTkLabel(
            self,
            text="Live Resources",
            font=FONTS["section"],
            text_color=COLORS["text"]
        )

        title.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="w",
            padx=SPACING["page_x"],
            pady=(10, 10)
        )

        resources = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        resources.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky="nsew",
            padx=SPACING["page_x"],
            pady=(0, SPACING["page_x"])
        )

        resources.grid_columnconfigure(
            (0, 1, 2, 3),
            weight=1,
            uniform="resource_cards"
        )

        self.memory_card = MetricCard(
            resources,
            title="Memory",
            value="--",
            subtitle="System memory"
        )

        self.memory_card.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 6),
            pady=(0, 10)
        )

        self.storage_card = MetricCard(
            resources,
            title="Storage",
            value="--",
            subtitle="Disk usage"
        )

        self.storage_card.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=6,
            pady=(0, 10)
        )

        self.battery_card = MetricCard(
            resources,
            title="Battery",
            value="--",
            subtitle="Power status"
        )

        self.battery_card.grid(
            row=0,
            column=2,
            sticky="nsew",
            padx=6,
            pady=(0, 10)
        )

        self.cpu_card = MetricCard(
            resources,
            title="CPU",
            value="--",
            subtitle="Current activity"
        )

        self.cpu_card.grid(
            row=0,
            column=3,
            sticky="nsew",
            padx=(6, 0),
            pady=(0, 10)
        )

        system_card = Card(
            resources
        )

        system_card.grid(
            row=1,
            column=0,
            columnspan=4,
            sticky="ew",
            pady=(6, 0)
        )

        header = ctk.CTkFrame(
            system_card,
            fg_color="transparent"
        )

        header.pack(
            fill="x",
            padx=22,
            pady=(18, 12)
        )

        ctk.CTkLabel(
            header,
            text="System Status",
            font=FONTS["section"],
            text_color=COLORS["text"]
        ).pack(
            side="left"
        )

        self.status_badge = StatusBadge(
            header,
            text="MONITORING",
            status="success"
        )

        self.status_badge.pack(
            side="right"
        )

        details = ctk.CTkFrame(
            system_card,
            fg_color=COLORS["surface_light"],
            corner_radius=10
        )

        details.pack(
            fill="x",
            padx=22,
            pady=(0, 18)
        )

        self.uptime_label = self.create_status_row(
            details,
            "System Uptime"
        )

        self.memory_detail_label = self.create_status_row(
            details,
            "Memory Used"
        )

        self.storage_detail_label = self.create_status_row(
            details,
            "Storage Free"
        )

        self.power_detail_label = self.create_status_row(
            details,
            "Power"
        )

    def create_section_heading(
        self,
        parent,
        text
    ):

        ctk.CTkLabel(
            parent,
            text=text,
            font=FONTS["section"],
            text_color=COLORS["text"]
        ).pack(
            anchor="w",
            padx=22,
            pady=(20, 12)
        )

    def create_info_row(
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
            padx=22,
            pady=7
        )

        ctk.CTkLabel(
            row,
            text=title,
            font=FONTS["body"],
            text_color=COLORS["text_secondary"]
        ).pack(
            side="left"
        )

        ctk.CTkLabel(
            row,
            text=str(value),
            font=FONTS["body_bold"],
            text_color=COLORS["text"]
        ).pack(
            side="right"
        )

    def create_spec_chip(
        self,
        parent,
        title,
        value
    ):

        chip = ctk.CTkFrame(
            parent,
            fg_color=COLORS["surface_light"],
            corner_radius=9
        )

        chip.pack(
            side="left",
            padx=(0, 10)
        )

        ctk.CTkLabel(
            chip,
            text=f"{title}: {value}",
            font=FONTS["small"],
            text_color=COLORS["text"]
        ).pack(
            padx=12,
            pady=7
        )

    def create_status_row(
        self,
        parent,
        title
    ):

        row = ctk.CTkFrame(
            parent,
            fg_color="transparent"
        )

        row.pack(
            fill="x",
            padx=14,
            pady=8
        )

        ctk.CTkLabel(
            row,
            text=title,
            font=FONTS["body"],
            text_color=COLORS["text_secondary"]
        ).pack(
            side="left"
        )

        value = ctk.CTkLabel(
            row,
            text="--",
            font=FONTS["body_bold"],
            text_color=COLORS["text"]
        )

        value.pack(
            side="right"
        )

        return value

    def update_live_data(self):

        try:

            memory = get_memory_usage()

            disk = get_disk_usage()

            battery = get_battery_info()

            cpu = get_cpu_usage()

            uptime = get_system_uptime()

            memory_percent = (
                memory["percent"]
            )

            self.memory_card.set_value(
                f"{memory_percent:.0f}%"
            )

            if (
                self.memory_card.subtitle_label
                is not None
            ):

                self.memory_card.subtitle_label.configure(
                    text=(
                        f"{memory['used_gb']:.1f} / "
                        f"{memory['total_gb']:.1f} GB"
                    )
                )

            self.storage_card.set_value(
                f"{disk['percent']:.0f}%"
            )

            if (
                self.storage_card.subtitle_label
                is not None
            ):

                self.storage_card.subtitle_label.configure(
                    text=(
                        f"{disk['used_gb']:.1f} / "
                        f"{disk['total_gb']:.1f} GB"
                    )
                )

            if battery["available"]:

                battery_text = (
                    f"{battery['percent']:.0f}%"
                )

                power_text = (
                    "Charging"
                    if battery["charging"]
                    else "On Battery"
                )

            else:

                battery_text = "N/A"
                power_text = "Unavailable"

            self.battery_card.set_value(
                battery_text
            )

            if (
                self.battery_card.subtitle_label
                is not None
            ):

                self.battery_card.subtitle_label.configure(
                    text=power_text
                )

            self.cpu_card.set_value(
                f"{cpu:.0f}%"
            )

            self.uptime_label.configure(
                text=uptime
            )

            self.memory_detail_label.configure(
                text=(
                    f"{memory['used_gb']:.1f} GB"
                )
            )

            self.storage_detail_label.configure(
                text=(
                    f"{disk['free_gb']:.1f} GB free"
                )
            )

            self.power_detail_label.configure(
                text=power_text
            )

        except Exception as error:

            print(
                "System overview error: "
                f"{error}"
            )

        self.after(
            2000,
            self.update_live_data
        )