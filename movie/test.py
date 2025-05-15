import customtkinter as ct

ct.set_appearance_mode("System")
ct.set_default_color_theme("blue")

class App(ct.CTk):
        def __init__(self):
            super().__init__()
            #Windows
            self.title("Connor's cinema")
            self.geometry(f"{800}x{600}")
            self.after(0, lambda:self.state('zoomed'))

            #Search
            self.grid_columnconfigure(0, weight=10)
            self.Search = ct.CTkFrame(self, height=60, width=180)
            self.Search.grid(padx=30, pady=30, column=0, row=0, sticky="nsew")

            #Login/ signu
            self.grid_columnconfigure(1, weight=1)
            self.Login = ct.CTkFrame(self, height=60, width=180)
            self.Login.grid(padx=30, pady=30, column=1, row=0, sticky="nsew")
            self.grid_columnconfigure(2, weight=1)
            self.SignUp = ct.CTkFrame(self, height=60, width=180)
            self.SignUp.grid(padx=30, pady=30, column=2, row=0, sticky="nsew")





app = App()
app.mainloop()