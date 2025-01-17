# -*- coding: utf-8 -*-
def decimal_to_dms(decimal_input, is_lat=True):
    degrees =  int(decimal_input)
    minutes = int((decimal_input - degrees) * 60)
    seconds = ((decimal_input - degrees) * 60 - minutes) * 60
    seconds = round(seconds, 1)
    if is_lat:
        direction = "N" if decimal_input >= 0 else "S"
    else:
        direction = "E" if decimal_input >= 0 else "W"
    return degrees, minutes, seconds, direction
    
decimal_input = 52.2928
degrees, minutes, seconds, direction = decimal_to_dms(52.2928)

print(f"{decimal_input}° = {degrees}°{minutes}′{seconds}″ {direction}")
