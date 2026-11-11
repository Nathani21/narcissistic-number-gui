import os
import sys

import customtkinter as ctk

from narcissistic_number import (
    digit_power_breakdown,
    find_narcissistic_numbers,
    is_narcissistic,
    parse_number,
)


def resource_path(relative_path):
    """Find a bundled file, both when run from source and inside the PyInstaller exe."""
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative_path)


class NarcissisticApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Narcissistic Number Checker v1.1")
        self.geometry("460x500")
        self.minsize(400, 460)
        self.after(250, self._set_icon)  # CustomTkinter sets its own icon just after opening

        self._build_widgets()

    def _set_icon(self):
        try:
            self.iconbitmap(resource_path(os.path.join("assets", "icon.ico")))
        except Exception:
            pass

    def _build_widgets(self):
        ctk.CTkLabel(
            self,
            text="Narcissistic Number Checker",
            font=ctk.CTkFont(size=22, weight="bold"),
        ).pack(pady=(24, 4))
        ctk.CTkLabel(self, text="Enter a whole number to check it.").pack(pady=(0, 16))

        self.entry = ctk.CTkEntry(
            self, width=240, placeholder_text="e.g. 153", justify="center"
        )
        self.entry.pack(pady=(0, 12))
        self.entry.bind("<Return>", lambda event: self.action_check())

        ctk.CTkButton(self, text="Check", command=self.action_check).pack(pady=(0, 16))

        self.result_label = ctk.CTkLabel(
            self, text="", wraplength=380, font=ctk.CTkFont(size=16)
        )
        self.result_label.pack(pady=(0, 4))

        self.breakdown_label = ctk.CTkLabel(self, text="", wraplength=380)
        self.breakdown_label.pack(pady=(0, 12))

        ctk.CTkLabel(self, text="Find all narcissistic numbers up to:").pack(pady=(12, 4))

        self.range_entry = ctk.CTkEntry(
            self, width=240, placeholder_text="e.g. 10000", justify="center"
        )
        self.range_entry.pack(pady=(0, 12))
        self.range_entry.bind("<Return>", lambda event: self.action_find())

        ctk.CTkButton(self, text="Find", command=self.action_find).pack(pady=(0, 12))

        self.range_label = ctk.CTkLabel(self, text="", wraplength=380)
        self.range_label.pack(pady=(0, 16))

    def action_check(self):
        try:
            num = parse_number(self.entry.get())
        except ValueError as error:
            self.result_label.configure(text=str(error), text_color="#d9534f")
            self.breakdown_label.configure(text="")
            return

        self.breakdown_label.configure(text=digit_power_breakdown(num))

        if is_narcissistic(num):
            self.result_label.configure(
                text=f"{num} is a narcissistic number", text_color="#2e9e5b"
            )
        else:
            self.result_label.configure(
                text=f"{num} is not a narcissistic number",
                text_color=("gray10", "gray90"),
            )

    def action_find(self):
        try:
            limit = parse_number(self.range_entry.get())
            found = find_narcissistic_numbers(limit)
        except ValueError as error:
            self.range_label.configure(text=str(error), text_color="#d9534f")
            return

        numbers = ", ".join(str(n) for n in found)
        self.range_label.configure(
            text=f"{len(found)} found up to {limit:,}:\n{numbers}",
            text_color=("gray10", "gray90"),
        )


def main():
    app = NarcissisticApp()
    app.mainloop()


if __name__ == "__main__":
    main()