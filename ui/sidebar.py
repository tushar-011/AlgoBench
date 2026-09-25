import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent, navigation_callback):
        super().__init__(
            parent,
            width=220,
            corner_radius=0
        )

        self.navigation_callback = navigation_callback

        self.grid_propagate(False)

        logo = ctk.CTkLabel(
            self,
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

        for page_name in buttons:

            button = ctk.CTkButton(
                self,
                text=page_name,
                height=40,
                anchor="w",
                command=lambda name=page_name:
                    self.navigation_callback(name)
            )

            button.pack(
                fill="x",
                padx=20,
                pady=5
            )