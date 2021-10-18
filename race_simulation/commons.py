
import random
from config import Config

class vehicle:
    def __init__(self, odo_miles, avg_speed, max_speed):
        """
        Initialize each vehicle with common attributes - odo_miles, avg_speed, max_speed
        """
        self.odo_miles = odo_miles
        self.avg_speed = avg_speed
        self.max_speed = max_speed

    def reset(self):
        """
        Reset odometer to 0 after each simulation
        """
        self.odo_miles = 0

    def setOdometer(self):
        """
        Add average speed to odo_miles. 
        If a vehicle reaches the end of the race return true, 
        else get a random speed between avg_speed and max_speed and return False.
        """
        self.odo_miles += self.avg_speed            
        if self.odo_miles >= Config.RACE_LENGTH:   # Default value 1500 in config file
            return True
        self.avg_speed = random.randrange(self.avg_speed, self.max_speed)
        return False

class car(vehicle):
    """
    In adition to base qualities, add battery_type and tire_traction for car
    """
    def __init__(self, battery_type, tire_traction, odo_miles, avg_speed, max_speed):
        self.battery_type=battery_type
        self.tire_traction=tire_traction
        super().__init__(odo_miles, avg_speed, max_speed)

class motorcycle(vehicle):
    """
    In adition to base qualities, add max_rpm and curb_weight for motorcycle
    """
    def __init__(self, max_rpm, curb_weight, odo_miles, avg_speed, max_speed):
        self.max_rpm=max_rpm
        self.curb_weight=curb_weight
        super().__init__(odo_miles, avg_speed, max_speed)

class truck(vehicle):
    """
    In adition to base qualities, add engine_capacity and auto_transmission for truck
    """
    def __init__(self, engine_capacity, auto_transmission, odo_miles, avg_speed, max_speed):
        self.engine_capacity=engine_capacity
        self.auto_transmission=auto_transmission
        super().__init__(odo_miles, avg_speed, max_speed)