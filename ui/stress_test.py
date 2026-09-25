import customtkinter as ctk


class StressTestPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text="Stress Test",
            font=ctk.CTkFont(size=30, weight="bold")
        )

        title.pack(
            anchor="w",
            padx=30,
            pady=30
        )