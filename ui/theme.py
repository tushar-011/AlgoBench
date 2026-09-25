import customtkinter as ctk


COLORS = {
    "app_bg": (
        "#F4F7FB",
        "#111827"
    ),

    "sidebar": (
        "#FFFFFF",
        "#0F172A"
    ),

    "surface": (
        "#FFFFFF",
        "#182235"
    ),

    "surface_hover": (
        "#EEF2F7",
        "#202C41"
    ),

    "surface_light": (
        "#F1F5F9",
        "#243047"
    ),

    "border": (
        "#DCE3EC",
        "#293548"
    ),

    "accent": (
        "#2563EB",
        "#3B82F6"
    ),

    "accent_hover": (
        "#1D4ED8",
        "#2563EB"
    ),

    "accent_soft": (
        "#DBEAFE",
        "#172E55"
    ),

    "text": (
        "#0F172A",
        "#F8FAFC"
    ),

    "text_secondary": (
        "#475569",
        "#94A3B8"
    ),

    "text_muted": (
        "#64748B",
        "#64748B"
    ),

    "success": (
        "#16A34A",
        "#22C55E"
    ),

    "warning": (
        "#D97706",
        "#F59E0B"
    ),

    "danger": (
        "#DC2626",
        "#EF4444"
    )
}


FONTS = {
    "page_title": (
        "Segoe UI",
        30,
        "bold"
    ),

    "page_subtitle": (
        "Segoe UI",
        13
    ),

    "section": (
        "Segoe UI",
        19,
        "bold"
    ),

    "card_title": (
        "Segoe UI",
        13
    ),

    "metric": (
        "Segoe UI",
        28,
        "bold"
    ),

    "metric_large": (
        "Segoe UI",
        42,
        "bold"
    ),

    "body": (
        "Segoe UI",
        13
    ),

    "body_bold": (
        "Segoe UI",
        13,
        "bold"
    ),

    "small": (
        "Segoe UI",
        11
    ),

    "sidebar_logo": (
        "Segoe UI",
        25,
        "bold"
    ),

    "sidebar": (
        "Segoe UI",
        13
    )
}


SPACING = {
    "page_x": 28,
    "page_top": 25,
    "card": 18,
    "section_gap": 16,
    "radius": 14
}


def get_color(name):

    color = COLORS[name]

    if not isinstance(
        color,
        tuple
    ):
        return color

    appearance = (
        ctk.get_appearance_mode()
    )

    if appearance == "Light":
        return color[0]

    return color[1]