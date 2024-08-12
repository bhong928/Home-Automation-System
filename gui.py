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
        self.pack(expand=True, fill='both')  # Expand the frame to fill the root window
        self.create_widgets()

    def create_widgets(self):
        # Frame to hold the buttons centrally
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(expand=True)  # Center the frame within the Application frame
        
        # Light controls
        self.light_btn = tk.Button(self.button_frame, text="Toggle Light", command=self.toggle_light_on)
        self.light_btn.pack(side="top", expand=True, fill='both')  # Center button in button_frame

        # Climate controls
        self.climate_btn = tk.Button(self.button_frame, text="Toggle Climate Control", command=self.toggle_climate)
        self.climate_btn.pack(side="top", expand=True, fill='both')

        # Security controls
        self.security_btn = tk.Button(self.button_frame, text="Toggle Security System", command=self.toggle_security)
        self.security_btn.pack(side="top", expand=True, fill='both')

        # Exit button
        self.quit = tk.Button(self.button_frame, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom", expand=True, fill='both')

    def toggle_light_on(self):
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
root.geometry("500x500")
app = Application(master=root)
app.master.title("Home Automation System")
app.mainloop()
