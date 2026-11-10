import customtkinter as ctk

from narcissistic_number import is_narcissistic, parse_number


class NarcissisticApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Narcissistic Number Checker")
        self.geometry("460x300")
        self.minsize(400, 260)

        self._build_widgets()

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
        self.result_label.pack(pady=(0, 12))

    def action_check(self):
        try:
            num = parse_number(self.entry.get())
        except ValueError as error:
            self.result_label.configure(text=str(error), text_color="#d9534f")
            return

        if is_narcissistic(num):
            self.result_label.configure(
                text=f"{num} is a narcissistic number", text_color="#2e9e5b"
            )
        else:
            self.result_label.configure(
                text=f"{num} is not a narcissistic number",
                text_color=("gray10", "gray90"),
            )


def main():
    app = NarcissisticApp()
    app.mainloop()


if __name__ == "__main__":
    main()