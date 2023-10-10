def convert(num):
    print(f"Your input {num} rods.")
    print("Conversions")
    my_meter=5.0292*num
    print(f"Meters:{my_meter}")
    my_feet=my_meter/0.3048
    print(f"Feet:{my_feet}")
    my_miles=my_meter/1609.34
    print(f"Miles:{my_miles}")
    my_furlong=num/40
    print(f"Furlongs:{my_furlong}")
    avg=(60*my_miles)/3.1
    print(f"Minutes to walk {num} rods:{avg}")
convert(num=float(input("Input rods:")))






