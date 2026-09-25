import customtkinter as ctk

from ui.sidebar import Sidebar
from ui.dashboard import DashboardPage
from ui.system_overview import SystemOverviewPage
from ui.cpu_test import CPUTestPage
from ui.memory_test import MemoryTestPage
from ui.performance_test import PerformanceTestPage
from ui.stress_test import StressTestPage
from ui.all_in_one import AllInOnePage
from ui.history import HistoryPage
from ui.settings import SettingsPage


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

        # Sidebar
        self.sidebar = Sidebar(
            self,
            self.show_page
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        # Main content area
        self.content = ctk.CTkFrame(
            self,
            corner_radius=0
        )

        self.content.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.content.grid_rowconfigure(0, weight=1)
        self.content.grid_columnconfigure(0, weight=1)

        self.pages = {}

        self.create_pages()

        self.show_page("Dashboard")

    def create_pages(self):

        self.pages["Dashboard"] = DashboardPage(
            self.content
        )

        self.pages["System Overview"] = SystemOverviewPage(
            self.content
        )

        self.pages["CPU Test"] = CPUTestPage(
            self.content
        )

        self.pages["Memory Test"] = MemoryTestPage(
            self.content
        )

        self.pages["Performance Test"] = PerformanceTestPage(
            self.content
        )

        self.pages["Stress Test"] = StressTestPage(
            self.content
        )

        self.pages["All-in-One Test"] = AllInOnePage(
            self.content
        )

        self.pages["History"] = HistoryPage(
            self.content
        )

        self.pages["Settings"] = SettingsPage(
            self.content
        )

        for page in self.pages.values():

            page.grid(
                row=0,
                column=0,
                sticky="nsew"
            )

    def show_page(self, page_name):

        page = self.pages.get(page_name)

        if page:
            page.tkraise()


if __name__ == "__main__":

    app = AlgoBenchApp()
    app.mainloop()