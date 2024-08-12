import tkinter as tk
from main import Light, ClimateControl, SecuritySystem, CentralHub

# Initialize the central hub and devices
hub = CentralHub()
light = Light()
climate = ClimateControl()
security = SecuritySystem()

hub.add_device(light)
hub.add_device(climate)
hub.add_device(security)

# GUI Application
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Light controls
        self.light_btn = tk.Button(self, text="Toggle Light", command=self.toggle_light)
        self.light_btn.pack(side="top")

        # Climate controls
        self.climate_btn = tk.Button(self, text="Toggle Climate Control", command=self.toggle_climate)
        self.climate_btn.pack(side="top")

        # Security controls
        self.security_btn = tk.Button(self, text="Toggle Security System", command=self.toggle_security)
        self.security_btn.pack(side="top")

        # Exit button
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def toggle_light(self):
        if light.is_on:
            light.turn_off()
        else:
            light.turn_on()
        print(light.get_status())

    def toggle_climate(self):
        if climate.is_on:
            climate.turn_off()
        else:
            climate.turn_on()
        print(climate.get_status())

    def toggle_security(self):
        if security.is_armed:
            security.turn_off()
        else:
            security.turn_on()
        print(security.get_status())

root = tk.Tk()
app = Application(master=root)
app.master.title("Home Automation System")
app.mainloop()
