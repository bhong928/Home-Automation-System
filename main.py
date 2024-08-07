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
        


    

    