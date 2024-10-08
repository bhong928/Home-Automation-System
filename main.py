from abc import ABC, abstractmethod
import time

#Device Interface
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass
    
    @abstractmethod
    def get_status(self):
        pass
    
    @abstractmethod
    def get_name(self):
        pass
    
# Lighting Controls
class Light(Device):
    # initialize a new instance of Light with default settings
    def __init__(self):
        self.is_on = False # keeps track of the lights on/off status
        self.brightness = 100 # sets the initial brightness of the light to 100%
        self.color = "white" # sets the color of the light to white
        
    # activate the light
    def turn_on(self):
        self.is_on = True
        print("Light is turned on")
    
    # deactivate the light 
    def turn_off(self):
        self.is_on = False
        print("Light turned off.")
    
    # Adjust the brightness of the light
    def set_brightness(self, level):
        if not 0 <= level <= 100:
            print("Brightness level must be between 0 and 100.")
            return
        self.brightness = level
        print(f"Light brightness set to {self.brightness}%.")

    # change the lights color
    def set_color(self, color):
        self.color = color
        print(f"Light color set to {self.color}.")
        
    # current operational status of the light
    def get_status(self):
        return "Light is on" if self.is_on else "Light is off"

    # provide the name of the device
    def get_name(self):
        return "Light"
    
# Climate Control
class ClimateControl(Device):
    # Initialize a new instance of climate control with default settings
    def __init__(self):
        self.is_on = False
        self.temperature = 22
        self.humidity = 50
        self.fan_speed = 0
        self.mode = "Cooling"

    # Activate climate control system
    def turn_on(self):
        self.is_on = True
        print("Climate control turned on.")

    # Deactivate climate control system
    def turn_off(self):
        self.is_on = False
        print("Climate control turned off.")

    # Adjust room temperature
    def set_temperature(self, temp):
        if not 10 <= temp <= 30:
            print("Temperature must be between 10 and 30°C.")
            return
        self.temperature = temp
        print(f"Temperature set to {self.temperature}°C.")

    # Adjust humidity level
    def set_humidity(self, hum):
        if not 0 <= hum <= 100:
            print("Humidity level must be between 0 and 100%.")
            return
        self.humidity = hum
        print(f"Humidity set to {self.humidity}%.")

    # Adjust fan speed
    def set_fan_speed(self, speed):
        if not 0 <= speed <= 3:
            print("Fan speed must be between 0 (Off) and 3 (High).")
            return
        self.fan_speed = speed
        fan_speed_names = ["Off", "Low", "Medium", "High"]
        print(f"Fan speed set to {fan_speed_names[self.fan_speed]}.")

    # Changing the operating mode of the climate control
    def set_mode(self, mode):
        if mode not in ["Cooling", "Heating"]:
            print("Mode must be either 'Cooling' or 'Heating'.")
            return
        self.mode = mode
        print(f"Mode set to {self.mode}.")

    # Provide detailed status of the climate control system
    def get_status(self):
        if not self.is_on:
            return "Climate control is off"
        return f"Climate control is on, Temperature: {self.temperature}°C, Humidity: {self.humidity}%, Fan Speed: {['Off', 'Low', 'Medium', 'High'][self.fan_speed]}, Mode: {self.mode}"

    # Indentify the device type
    def get_name(self):
        return "Climate Control"
        

# Security System
class SecuritySystem(Device):
    def __init__(self):
        self.is_armed = False
        self.alarm_on = False
        self.motion_detected = False
        self.camera_active = False
        self.motion_sensitivity = 5
        self.logs = []

    def turn_on(self):
        self.is_armed = True
        self.camera_active = True
        self.add_log("Security system armed and cameras activated.")
        print("Security system armed and cameras activated.")

    def turn_off(self):
        self.is_armed = False
        self.alarm_on = False
        self.camera_active = False
        self.add_log("Security system disarmed and cameras deactivated.")
        print("Security system disarmed and cameras deactivated.")

    def trigger_alarm(self):
        if self.is_armed:
            self.alarm_on = True
            self.add_log("Alarm triggered!")
            print("Alarm triggered!")

    def detect_motion(self):
        if self.is_armed:
            self.motion_detected = True
            self.trigger_alarm()
            self.add_log("Motion detected!")
            print("Motion detected!")

    def reset_alarm(self):
        self.alarm_on = False
        self.motion_detected = False
        self.add_log("Alarm reset.")
        print("Alarm reset.")

    def start_camera_recording(self):
        if self.camera_active:
            self.add_log("Camera recording started.")
            print("Camera recording started.")

    def stop_camera_recording(self):
        if self.camera_active:
            self.add_log("Camera recording stopped.")
            print("Camera recording stopped.")

    def set_motion_sensitivity(self, level):
        if not 1 <= level <= 10:
            print("Motion sensitivity must be between 1 and 10.")
            return
        self.motion_sensitivity = level
        self.add_log(f"Motion sensitivity set to {level}")
        print(f"Motion sensitivity set to {level}")

    def show_logs(self):
        print("Security System Logs:")
        for log in self.logs:
            print(log)

    def get_status(self):
        if self.is_armed:
            if self.alarm_on:
                return "Security system is armed, alarm is triggered!"
            if self.motion_detected:
                return "Security system is armed, motion detected!"
            return "Security system is armed, all is secure."
        return "Security system is disarmed"

    def get_name(self):
        return "Security System"

    def add_log(self, event):
        dt = time.ctime()
        self.logs.append(f"{dt}: {event}")

# Central Hub
class CentralHub:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def turn_on_all_devices(self):
        for device in self.devices:
            device.turn_on()

    def turn_off_all_devices(self):
        for device in self.devices:
            device.turn_off()

    def show_status(self):
        for device in self.devices:
            print(f"{device.get_name()}: {device.get_status()}")

    def interact_with_device(self, device_name):
        for device in self.devices:
            if device.get_name() == device_name:
                print(f"Interacting with {device_name}.")
                if isinstance(device, Light):
                    return device
        print("Device not found.")
        return None

# Separator to Clean up Terminal
def print_separator():
    print("-" * 50)
    
# Light interaction
def handle_light_interaction(light):
    print("Options for Light:")
    print("1. Turn on")
    print("2. Turn off")
    print("3. Set Brightness")
    print("4. Set Color")
    print("5. Return to Main Menu")
    option = input("Choose an option: ")
    print_separator()
    
    if option == '1':
        light.turn_on()
    elif option == '2':
        light.turn_off()
    elif option == '3':
        try:
            brightness = int(input("Enter brightness (0-100): "))
            print_separator()
            light.set_brightness(brightness)
        except ValueError:
            print("Please enter a valid integer for brightness.")
            print_separator()
    elif option == '4':
        color = input("Enter color name: ")
        print_separator()
        light.set_color(color)
    elif option == '5':
        return
    else:
        print("Invalid option.")
    
    print("Current Status of Light:")
    print(light.get_status())
    print_separator()

# Climate interaction
def handle_climate_interaction(climate):
    print("Options for Climate Control:")
    print("1. Turn on")
    print("2. Turn off")
    print("3. Set Temperature")
    print("4. Set Humidity")
    print("5. Set Fan Speed")
    print("6. Set Mode")
    print("7. Return to Main Menu")
    option = input("Choose an option: ")

    if option == '1':
        climate.turn_on()
    elif option == '2':
        climate.turn_off()
    elif option == '3':
        try:
            temperature = int(input("Enter temperature (10-30°C): "))
            print_separator()
            climate.set_temperature(temperature)
        except ValueError:
            print("Please enter a valid integer for temperature.")
            print_separator()
    elif option == '4':
        try:
            humidity = int(input("Enter humidity (0-100%): "))
            print_separator()
            climate.set_humidity(humidity)
        except ValueError:
            print("Please enter a valid integer for humidity.")
            print_separator()
    elif option == '5':
        try:
            speed = int(input("Enter fan speed (0-3): "))
            print_separator()
            climate.set_fan_speed(speed)
        except ValueError:
            print("Please enter a valid integer for fan speed.")
            print_separator()
    elif option == '6':
        mode = input("Enter mode (Cooling or Heating): ")
        print_separator()
        climate.set_mode(mode)
    elif option == '7':
        return
    else:
        print("Invalid option.")

    print("Current Status of Climate Control:")
    print(climate.get_status())
    print_separator()

# Security interaction 
def handle_security_interaction(security):
    print("Options for Security System:")
    print("1. Arm System")
    print("2. Disarm System")
    print("3. Trigger Alarm")
    print("4. Detect Motion")
    print("5. Set Motion Sensitivity")
    print("6. Show Logs")
    print("7. Return to Main Menu")
    option = input("Choose an option: ")
    print_separator()

    if option == '1':
        security.turn_on()
    elif option == '2':
        security.turn_off()
    elif option == '3':
        security.trigger_alarm()
    elif option == '4':
        security.detect_motion()
    elif option == '5':
        try:
            sensitivity = int(input("Enter motion sensitivity (1-10): "))
            print_separator()
            security.set_motion_sensitivity(sensitivity)
        except ValueError:
            print("Please enter a valid integer for sensitivity.")
            print_separator()
    elif option == '6':
        security.show_logs()
    elif option == '7':
        return
    else:
        print("Invalid option.")

    print("Current Status of Security System:")
    print(security.get_status())
    print_separator()

# Display Menu
def display_menu():
    print_separator()
    print("Smart Home Automation System Menu:")
    print("1. Turn on all devices")
    print("2. Turn off all devices")
    print("3. Show status of all devices")
    print("4. Interact with Light")
    print("5. Interact with Climate Control")
    print("6. Interact with Security System")
    print("7. Exit")
    print_separator()

# Main function
def main():
    hub = CentralHub()
    light = Light()
    climate = ClimateControl()
    security = SecuritySystem()

    # Adding devices to the hub
    hub.add_device(light)
    hub.add_device(climate)
    hub.add_device(security)

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        print_separator()
        if choice == '7':
            print("Exiting the system.")
            break
        try:
            choice = int(choice)
            if choice == 1:
                hub.turn_on_all_devices()
            elif choice == 2:
                hub.turn_off_all_devices()
            elif choice == 3:
                hub.show_status()
            elif choice == 4:
                handle_light_interaction(light)
            elif choice == 5:
                handle_climate_interaction(climate)
            elif choice == 6:
                handle_security_interaction(security)
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid choice. Please enter a number.")

if __name__ == "__main__":
    main()