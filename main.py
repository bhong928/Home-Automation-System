from abc import ABC, abstractmethod
import time

# Device Interface: This is an abstract base class (ABC) defining the blueprint for all devices.
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

# Lighting Control: A concrete implementation of the Device interface to control lights.
class Light(Device):
    def __init__(self):
        self.is_on = False
        self.brightness = 100  # Default brightness level
        self.color = "white"  # Default color

    def turn_on(self):
        self.is_on = True
        print("Light turned on.")

    def turn_off(self):
        self.is_on = False
        print("Light turned off.")

    def set_brightness(self, level):
        # Ensures brightness is within a valid range
        if not 0 <= level <= 100:
            print("Brightness level must be between 0 and 100.")
            return
        self.brightness = level
        print(f"Light brightness set to {self.brightness}%.")

    def set_color(self, color):
        self.color = color
        print(f"Light color set to {self.color}.")

    def get_status(self):
        return "Light is on" if self.is_on else "Light is off"

    def get_name(self):
        return "Light"

# Climate Control: Controls the temperature, humidity, and fan speed in a room.
class ClimateControl(Device):
    def __init__(self):
        self.is_on = False
        self.temperature = 22  # Default temperature in °C
        self.humidity = 50  # Default humidity percentage
        self.fan_speed = 0  # Default fan speed (0 = Off)
        self.mode = "Cooling"  # Default mode

    def turn_on(self):
        self.is_on = True
        print("Climate control turned on.")

    def turn_off(self):
        self.is_on = False
        print("Climate control turned off.")

    def set_temperature(self, temp):
        # Ensures temperature is within a valid range
        if not 10 <= temp <= 30:
            print("Temperature must be between 10 and 30°C.")
            return
        self.temperature = temp
        print(f"Temperature set to {self.temperature}°C.")

    def set_humidity(self, hum):
        # Ensures humidity is within a valid range
        if not 0 <= hum <= 100:
            print("Humidity level must be between 0 and 100%.")
            return
        self.humidity = hum
        print(f"Humidity set to {self.humidity}%.")

    def set_fan_speed(self, speed):
        # Ensures fan speed is within a valid range
        if not 0 <= speed <= 3:
            print("Fan speed must be between 0 (Off) and 3 (High).")
            return
        self.fan_speed = speed
        fan_speed_names = ["Off", "Low", "Medium", "High"]
        print(f"Fan speed set to {fan_speed_names[self.fan_speed]}.")

    def set_mode(self, mode):
        # Ensures mode is either 'Cooling' or 'Heating'
        if mode not in ["Cooling", "Heating"]:
            print("Mode must be either 'Cooling' or 'Heating'.")
            return
        self.mode = mode
        print(f"Mode set to {self.mode}.")

    def get_status(self):
        # Provides a detailed status of the climate control system
        if not self.is_on:
            return "Climate control is off"
        return f"Climate control is on, Temperature: {self.temperature}°C, Humidity: {self.humidity}%, Fan Speed: {['Off', 'Low', 'Medium', 'High'][self.fan_speed]}, Mode: {self.mode}"

    def get_name(self):
        return "Climate Control"

# Security System: Manages the security aspects of the home including alarms and motion detection.
class SecuritySystem(Device):
    def __init__(self):
        self.is_armed = False  # Whether the system is armed
        self.alarm_on = False  # Whether the alarm is currently triggered
        self.motion_detected = False  # Whether motion is detected
        self.camera_active = False  # Whether the cameras are active
        self.motion_sensitivity = 5  # Default motion sensitivity level
        self.logs = []  # Log of security events

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
        # Ensures motion sensitivity is within a valid range
        if not 1 <= level <= 10:
            print("Motion sensitivity must be between 1 and 10.")
            return
        self.motion_sensitivity = level
        self.add_log(f"Motion sensitivity set to {level}")
        print(f"Motion sensitivity set to {level}")

    def show_logs(self):
        # Displays the security logs
        print("Security System Logs:")
        for log in self.logs:
            print(log)

    def get_status(self):
        # Provides a status summary of the security system
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
        # Adds a log entry with a timestamp
        dt = time.ctime()
        self.logs.append(f"{dt}: {event}")

# Central Hub: Manages all devices and coordinates their operations.
class CentralHub:
    def __init__(self):
        self.devices = []  # List to store all connected devices

    def add_device(self, device):
        # Adds a device to the hub
        self.devices.append(device)

    def turn_on_all_devices(self):
        # Turns on all connected devices
        for device in self.devices:
            device.turn_on()

    def turn_off_all_devices(self):
        # Turns off all connected devices
        for device in self.devices:
            device.turn_off()

    def show_status(self):
        # Displays the status of all connected devices
        for device in self.devices:
            print(f"{device.get_name()}: {device.get_status()}")

    def interact_with_device(self, device_name):
        # Allows interaction with a specific device by name
        for device in self.devices:
            if device.get_name() == device_name:
                print(f"Interacting with {device_name}.")
                return device
        print("Device not found.")
        return None

# Display Menu: Provides a text-based menu for user interaction.
def display_menu():
    print("Smart Home Automation System Menu:")
    print("1. Turn on all devices")
    print("2. Turn off all devices")
    print("3. Show status of all devices")
    print("4. Interact with a specific device")
    print("5. Exit")

# Main function: Entry point of the program, manages user interactions.
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
        display_menu()  # Display the main menu
        choice = input("Enter your choice: ")
        if choice == '5':
            print("Exiting the system.")
            break
        try:
            choice = int(choice)
            if choice == 1:
                hub.turn_on_all_devices()  # Turn on all devices
            elif choice == 2:
                hub.turn_off_all_devices()  # Turn off all devices
            elif choice == 3:
                hub.show_status()  # Show status of all devices
            elif choice == 4:
                device_name = input("Enter the device name (Light, Climate Control, Security System): ")
                device = hub.interact_with_device(device_name)  # Interact with a specific device
                if device:
                    # Additional interaction based on device type could be implemented here
                    pass
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid choice. Please enter a number.")

if __name__ == "__main__":
    main()