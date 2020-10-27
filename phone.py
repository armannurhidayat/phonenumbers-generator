# -*- coding: utf-8 -*-
"""
Author @Syntaxdev
Copyright (C) 2020 - TODAY
"""

import datetime
import random
# import phonenumbers
# from phonenumbers import geocoder

date = datetime.datetime.now().strftime('%d-%m-%Y')
flag = """
______ _                                            _                     _____                           _             
| ___ \ |                                          | |                   |  __ \                         | |            
| |_/ / |__   ___  _ __   ___ _ __  _   _ _ __ ___ | |__   ___ _ __ ___  | |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
|  __/| '_ \ / _ \| '_ \ / _ \ '_ \| | | | '_ ` _ \| '_ \ / _ \ '__/ __| | | __ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |   | | | | (_) | | | |  __/ | | | |_| | | | | | | |_) |  __/ |  \__ \ | |_\ \  __/ | | |  __/ | | (_| | || (_) | |   
\_|   |_| |_|\___/|_| |_|\___|_| |_|\__,_|_| |_| |_|_.__/ \___|_|  |___/  \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                                           @Syntaxdev
"""
print(flag)

prefix  = input("Prefix : ")
dari    = input("Dari   : ")
sampai  = input("Sampai : ")
suffix  = input("Suffix : ")
acak    = input("Using random Y/N? ").upper()

x = "x" * ( len(dari) )
print( f"\nRandom Phonenumbers [ {prefix}{x}{suffix} ] \n" )

with open(f'Phonenumbers-{date}.txt', 'w') as data:
    for i in range(int(dari), int(sampai)+1):
        if acak == 'Y':
            length = random.randint(int(dari), int(sampai))
        else:
            length = "0" * ( len(dari) - len(str(i)) )

        phone   = f"{str(prefix)}{length}{i}{suffix if suffix else ''}"
        data.write(phone + '\n')
        print(phone)

print("Finally finished! :)")
