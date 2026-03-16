from models import Smartphone, SmartWatch

def main():
    my_phone = Smartphone("Apple", "iPhone 15", 20, 6.1)
    my_watch = SmartWatch("Garmin", "Fenix 7", 336, True)

    device_inventory = [my_phone, my_watch]

    print("--- Inventory Report ---")
    
    for device in device_inventory:
        print(f"Checking: {device}")
        
        print(f"Details: {device.get_specs()}")
        
        print(device.toggle_power())

        if isinstance(device, Smartphone):
            print(device.send_text("Dev Team", "The OOP project is ready!"))
        elif isinstance(device, SmartWatch):
            print(device.track_steps(12500))
            
        print("-" * 30)

if __name__ == "__main__":
    main()