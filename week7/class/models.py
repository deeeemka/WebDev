class SmartDevice:
    """Base Class for all smart electronics."""
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  
        self.is_on = False

    def toggle_power(self):
        self.is_on = not self.is_on
        status = "ON" if self.is_on else "OFF"
        return f"{self.brand} {self.model} is now {status}."

    def get_specs(self):
        return f"Brand: {self.brand}, Model: {self.model}, Battery: {self.battery_life}h"

    def __str__(self):
        return f"{self.brand} {self.model} (Smart Device)"


class Smartphone(SmartDevice):
    """Child Class representing a smartphone."""
    def __init__(self, brand, model, battery_life, screen_size):
        super().__init__(brand, model, battery_life)
        self.screen_size = screen_size  

    def send_text(self, contact, message):
        return f"[{self.model}] Sending to {contact}: {message}"

    def get_specs(self):
        return f"Smartphone -> {self.brand} {self.model} with a {self.screen_size}\" screen."


class SmartWatch(SmartDevice):
    """Child Class representing a wearable device."""
    def __init__(self, brand, model, battery_life, has_heart_rate_sensor=True):
        super().__init__(brand, model, battery_life)
        self.has_heart_rate_sensor = has_heart_rate_sensor 

    def track_steps(self, steps):
        return f"The {self.model} recorded {steps} steps today."

    def get_specs(self):
        sensor_status = "Sensor included" if self.has_heart_rate_sensor else "No sensor"
        return f"SmartWatch -> {self.brand} {self.model} ({sensor_status})."