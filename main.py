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
        
    

    