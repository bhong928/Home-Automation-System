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

def print_seperator():
    print("-" * 50)
    
# Display Menu
def display_menu():
    print_seperator()
    print("Smart Home Automation System Menu:")
    print("1. Turn on all devices")
    print("2. Turn off all devices")
    print("3. Show status of all devices")
    print("4. Interact with a specific device")
    print("5. Exit")
    print_seperator()

#Light interaction Menu
def light_interaction_menu(light):
    while True:
        print_seperator()
        print("Options for Light:")
        print("1. Turn on")
        print("2. Turn off")
        print("3. Set Brightness")
        print("4. Set Color")
        print("5. Return to Main Menu")
        light_choice = input("Choose an option: ")
        print_seperator()
        if light_choice == '1':
            light.turn_on()
            print("Light turned on.")
        elif light_choice == '2':
            light.turn_off()
            print("Light turned off.")
        elif light_choice == '3':
            try:
                brightness_level = int(input("Enter brightness level (0-100): "))
                print_seperator()
                light.set_brightness(brightness_level)
            except ValueError:
                print("Please enter a valid integer for brightness.")
        elif light_choice == '4':
            light_color = input("Enter color of light: ")
            print_seperator()
            light.set_color(light_color)
        elif light_choice == '5':
            break
        else:
            print("Invalid option.")
        print_seperator()
        print("Current Status of Light:")
        print(light.get_status())

    
# Main function
def main():
    hub = CentralHub()

    # Creating devices
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
        print_seperator()
        if choice == '5':
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
                device_name = input("Enter the device name (Light, Climate Control, Security System): ")
                device = hub.interact_with_device(device_name)
                if device:
                    # Light Options
                    if isinstance(device, Light):
                        light_interaction_menu(device)
                    else:
                        print(f"{device.get_name()} does not support these options.")
                    hub.show_status()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid choice. Please enter a number.")

if __name__ == "__main__":
    main()
