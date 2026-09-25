import customtkinter as ctk


class AllInOnePage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text="All-in-One Page",
            font=ctk.CTkFont(size=30, weight="bold")
        )

        title.pack(
            anchor="w",
            padx=30,
            pady=30
        )