# Unit Converter
# Python 3.9.1
# Created by deathlezz
# Date 06.03.2021


# Say Hi
print()
print('* Welcome to Unit Converter *')
print()


# Create infinite loop
while True:

    # Create menu
    print('Choose unit category:')
    print('[1] Length' + '         ' + '[4] Volume')
    print('[2] Temperature' + '    ' + '[5] Weight')
    print('[3] Area' + '           ' + '[6] Time')
    print()

    # Create user choice
    try:
        menuChoice = int(input('Enter your choice: '))
        print()
    except ValueError:
        print()
        print('# Enter value from 1 to 6 #')
        print()
        continue

    if menuChoice == 1:
        print('Choose unit type:')
        print('[1] Kilometer' + '      ' + '[5] Mile')
        print('[2] Meter' + '          ' + '[6] Yard')
        print('[3] Centimeter' + '     ' + '[7] Foot')
        print('[4] Millimeter' + '     ' + '[8] Inch')
        print()

        # Create user sub choice
        try:
            subMenuChoice = int(input('Enter your choice: '))
            print()
        except ValueError:
            print()
            print('# Enter value from 1 to 8 #')
            print()
            continue

        if subMenuChoice == 1:

            try:
                kilometers = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if kilometers > 0:

                # To avoid scientific notation use this: ("%.25f" % n).rstrip('0').rstrip('.')
                meters = ("%.25f" % (kilometers * 1000)).rstrip('0').rstrip('.')
                centimeters = ("%.25f" % (kilometers * 100000)).rstrip('0').rstrip('.')
                millimeters = ("%.25f" % (kilometers * 1000000)).rstrip('0').rstrip('.')
                miles = ("%.25f" % (kilometers * 0.621)).rstrip('0').rstrip('.')
                yards = ("%.25f" % (kilometers * 1093.613)).rstrip('0').rstrip('.')
                feet = ("%.25f" % (kilometers * 3280.84)).rstrip('0').rstrip('.')
                inches = ("%.25f" % (kilometers * 39370.0787)).rstrip('0').rstrip('.')

                print(f'{kilometers} km = {meters} m')
                print(f'{kilometers} km = {centimeters} cm')
                print(f'{kilometers} km = {millimeters} mm')
                print(f'{kilometers} km = {miles} mi')
                print(f'{kilometers} km = {yards} yd')
                print(f'{kilometers} km = {feet} ft')
                print(f'{kilometers} km = {inches} in')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 2:

            try:
                meters = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if meters > 0:

                kilometers = ("%.25f" % (meters * 0.001)).rstrip('0').rstrip('.')
                centimeters = ("%.25f" % (meters * 100)).rstrip('0').rstrip('.')
                millimeters = ("%.25f" % (meters * 1000)).rstrip('0').rstrip('.')
                miles = ("%.25f" % (meters * 0.000621)).rstrip('0').rstrip('.')
                yards = ("%.25f" % (meters * 1.0936)).rstrip('0').rstrip('.')
                feet = ("%.25f" % (meters * 3.281)).rstrip('0').rstrip('.')
                inches = ("%.25f" % (meters * 39.37)).rstrip('0').rstrip('.')

                print(f'{meters} m = {kilometers} km')
                print(f'{meters} m = {centimeters} cm')
                print(f'{meters} m = {millimeters} mm')
                print(f'{meters} m = {miles} mi')
                print(f'{meters} m = {yards} yd')
                print(f'{meters} m = {feet} ft')
                print(f'{meters} m = {inches} in')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 3:

            try:
                centimeters = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if centimeters > 0:

                kilometers = ("%.25f" % (centimeters * 0.00001)).rstrip('0').rstrip('.')
                meters = ("%.25f" % (centimeters * 0.01)).rstrip('0').rstrip('.')
                millimeters = ("%.25f" % (centimeters * 10)).rstrip('0').rstrip('.')
                miles = ("%.25f" % (centimeters * 0.00000621)).rstrip('0').rstrip('.')
                yards = ("%.25f" % (centimeters * 0.0109)).rstrip('0').rstrip('.')
                feet = ("%.25f" % (centimeters * 0.0328)).rstrip('0').rstrip('.')
                inches = ("%.25f" % (centimeters * 0.394)).rstrip('0').rstrip('.')

                print(f'{centimeters} cm = {kilometers} km')
                print(f'{centimeters} cm = {meters} m')
                print(f'{centimeters} cm = {millimeters} mm')
                print(f'{centimeters} cm = {miles} mi')
                print(f'{centimeters} cm = {yards} yd')
                print(f'{centimeters} cm = {feet} ft')
                print(f'{centimeters} cm = {inches} in')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 4:

            try:
                millimeters = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if millimeters > 0:

                kilometers = ("%.25f" % (millimeters * 0.000001)).rstrip('0').rstrip('.')
                meters = ("%.25f" % (millimeters * 0.001)).rstrip('0').rstrip('.')
                centimeters = ("%.25f" % (millimeters * 0.1)).rstrip('0').rstrip('.')
                miles = ("%.25f" % (millimeters * 0.000000621)).rstrip('0').rstrip('.')
                yards = ("%.25f" % (millimeters * 0.00109)).rstrip('0').rstrip('.')
                feet = ("%.25f" % (millimeters * 0.00328)).rstrip('0').rstrip('.')
                inches = ("%.25f" % (millimeters * 0.0394)).rstrip('0').rstrip('.')

                print(f'{millimeters} mm = {kilometers} km')
                print(f'{millimeters} mm = {meters} m')
                print(f'{millimeters} mm = {centimeters} cm')
                print(f'{millimeters} mm = {miles} mi')
                print(f'{millimeters} mm = {yards} yd')
                print(f'{millimeters} mm = {feet} ft')
                print(f'{millimeters} mm = {inches} in')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 5:

            try:
                miles = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if miles > 0:

                kilometers = ("%.25f" % (miles * 1.609)).rstrip('0').rstrip('.')
                meters = ("%.25f" % (miles * 1609.344)).rstrip('0').rstrip('.')
                centimeters = ("%.25f" % (miles * 160934.4)).rstrip('0').rstrip('.')
                millimeters = ("%.25f" % (miles * 1609344)).rstrip('0').rstrip('.')
                yards = ("%.25f" % (miles * 1760)).rstrip('0').rstrip('.')
                feet = ("%.25f" % (miles * 5280)).rstrip('0').rstrip('.')
                inches = ("%.25f" % (miles * 63360)).rstrip('0').rstrip('.')

                print(f'{miles} mi = {kilometers} km')
                print(f'{miles} mi = {meters} m')
                print(f'{miles} mi = {centimeters} cm')
                print(f'{miles} mi = {millimeters} mm')
                print(f'{miles} mi = {yards} yd')
                print(f'{miles} mi = {feet} ft')
                print(f'{miles} mi = {inches} in')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 6:

            try:
                yards = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if yards > 0:

                kilometers = ("%.25f" % (yards * 0.000914)).rstrip('0').rstrip('.')
                meters = ("%.25f" % (yards * 0.914)).rstrip('0').rstrip('.')
                centimeters = ("%.25f" % (yards * 91.44)).rstrip('0').rstrip('.')
                millimeters = ("%.25f" % (yards * 914.4)).rstrip('0').rstrip('.')
                miles = ("%.25f" % (yards * 0.000568)).rstrip('0').rstrip('.')
                feet = ("%.25f" % (yards * 3)).rstrip('0').rstrip('.')
                inches = ("%.25f" % (yards * 36)).rstrip('0').rstrip('.')

                print(f'{yards} yd = {kilometers} km')
                print(f'{yards} yd = {meters} m')
                print(f'{yards} yd = {centimeters} cm')
                print(f'{yards} yd = {millimeters} mm')
                print(f'{yards} yd = {miles} mi')
                print(f'{yards} yd = {feet} ft')
                print(f'{yards} yd = {inches} in')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 7:

            try:
                feet = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if feet > 0:

                kilometers = ("%.25f" % (feet * 0.0003048)).rstrip('0').rstrip('.')
                meters = ("%.25f" % (feet * 0.3048)).rstrip('0').rstrip('.')
                centimeters = ("%.25f" % (feet * 30.48)).rstrip('0').rstrip('.')
                millimeters = ("%.25f" % (feet * 304.8)).rstrip('0').rstrip('.')
                miles = ("%.25f" % (feet * 0.000189)).rstrip('0').rstrip('.')
                yards = ("%.25f" % (feet * 0.333)).rstrip('0').rstrip('.')
                inches = ("%.25f" % (feet * 12)).rstrip('0').rstrip('.')

                print(f'{feet} ft = {kilometers} km')
                print(f'{feet} ft = {meters} m')
                print(f'{feet} ft = {centimeters} cm')
                print(f'{feet} ft = {millimeters} mm')
                print(f'{feet} ft = {miles} mi')
                print(f'{feet} ft = {yards} yd')
                print(f'{feet} ft = {inches} in')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 8:

            try:
                inches = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if inches > 0:

                kilometers = ("%.25f" % (inches * 0.0000254)).rstrip('0').rstrip('.')
                meters = ("%.25f" % (inches * 0.0254)).rstrip('0').rstrip('.')
                centimeters = ("%.25f" % (inches * 2.54)).rstrip('0').rstrip('.')
                millimeters = ("%.25f" % (inches * 25.4)).rstrip('0').rstrip('.')
                miles = ("%.25f" % (inches * 0.0000158)).rstrip('0').rstrip('.')
                yards = ("%.25f" % (inches * 0.0278)).rstrip('0').rstrip('.')
                feet = ("%.25f" % (inches * 0.0833)).rstrip('0').rstrip('.')

                print(f'{inches} in = {kilometers} km')
                print(f'{inches} in = {meters} m')
                print(f'{inches} in = {centimeters} cm')
                print(f'{inches} in = {millimeters} mm')
                print(f'{inches} in = {miles} mi')
                print(f'{inches} in = {yards} yd')
                print(f'{inches} in = {feet} ft')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        else:
            print('# Enter value from 1 to 8 #')
            print()

    elif menuChoice == 2:
        print('Choose unit type:')
        print('[1] Celsius')
        print('[2] Kelvin')
        print('[3] Fahrenheit')
        print()

        try:
            subMenuChoice = int(input('Enter your choice: '))
            print()
        except ValueError:
            print()
            print('# Enter value from 1 to 3 #')
            print()
            continue

        if subMenuChoice == 1:

            try:
                celsius = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            kelvin = round((celsius + 273.15), 2)
            fahrenheit = round(((celsius * 1.8) + 32), 2)

            print(f'{celsius} ??C = {kelvin} K')
            print(f'{celsius} ??C = {fahrenheit} ??F')
            print()

        elif subMenuChoice == 2:

            try:
                kelvin = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            celsius = round((kelvin - 273.15), 2)
            fahrenheit = round(((kelvin * 1.8) - 459.67), 2)

            print(f'{kelvin} K = {celsius} ??C')
            print(f'{kelvin} K = {fahrenheit} ??F')
            print()

        elif subMenuChoice == 3:

            try:
                fahrenheit = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            celsius = round(((fahrenheit - 32) * 5 / 9), 2)
            kelvin = round(((fahrenheit + 459.67) / 1.8), 2)

            print(f'{fahrenheit} ??F = {celsius} ??C')
            print(f'{fahrenheit} ??F = {kelvin} K')
            print()

        else:
            print('# Enter value from 1 to 3 #')
            print()

    elif menuChoice == 3:
        print('Choose unit type:')
        print('[1] Square Kilometer' + '      ' + '[6] Square Mile')
        print('[2] Square Meter' + '          ' + '[7] Square Yard')
        print('[3] Square Centimeter' + '     ' + '[8] Square Foot')
        print('[4] Square Millimeter' + '     ' + '[9] Square Inch')
        print('[5] Hectare' + '               ' + '[10] Acre')
        print()

        try:
            subMenuChoice = int(input('Enter your choice: '))
            print()
        except ValueError:
            print()
            print('# Enter value from 1 to 10 #')
            print()
            continue

        if subMenuChoice == 1:

            try:
                squareKilometer = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if squareKilometer > 0:

                squareMeter = ("%.25f" % (squareKilometer * 1000000)).rstrip('0').rstrip('.')
                squareCentimeter = ("%.25f" % (squareKilometer * 10000000000)).rstrip('0').rstrip('.')
                squareMillimeter = ("%.25f" % (squareKilometer * 1000000000000)).rstrip('0').rstrip('.')
                hectare = ("%.25f" % (squareKilometer * 100)).rstrip('0').rstrip('.')
                squareMile = ("%.25f" % (squareKilometer * 0.386)).rstrip('0').rstrip('.')
                squareYard = ("%.25f" % (squareKilometer * 1195990.0463)).rstrip('0').rstrip('.')
                squareFoot = ("%.25f" % (squareKilometer * 10763910.417)).rstrip('0').rstrip('.')
                squareInch = ("%.25f" % (squareKilometer * 1550003100)).rstrip('0').rstrip('.')
                acre = ("%.25f" % (squareKilometer * 247.105)).rstrip('0').rstrip('.')

                print(f'{squareKilometer} km?? = {squareMeter} m??')
                print(f'{squareKilometer} km?? = {squareCentimeter} cm??')
                print(f'{squareKilometer} km?? = {squareMillimeter} mm??')
                print(f'{squareKilometer} km?? = {hectare} ha')
                print(f'{squareKilometer} km?? = {squareMile} mi??')
                print(f'{squareKilometer} km?? = {squareYard} yd??')
                print(f'{squareKilometer} km?? = {squareFoot} ft??')
                print(f'{squareKilometer} km?? = {squareInch} in??')
                print(f'{squareKilometer} km?? = {acre} ac')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 2:

            try:
                squareMeter = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if squareMeter > 0:

                squareKilometer = ("%.25f" % (squareMeter * 0.000001)).rstrip('0').rstrip('.')
                squareCentimeter = ("%.25f" % (squareMeter * 10000)).rstrip('0').rstrip('.')
                squareMillimeter = ("%.25f" % (squareMeter * 1000000)).rstrip('0').rstrip('.')
                hectare = ("%.25f" % (squareMeter * 0.0001)).rstrip('0').rstrip('.')
                squareMile = ("%.25f" % (squareMeter * 0.000000386)).rstrip('0').rstrip('.')
                squareYard = ("%.25f" % (squareMeter * 1.196)).rstrip('0').rstrip('.')
                squareFoot = ("%.25f" % (squareMeter * 10.764)).rstrip('0').rstrip('.')
                squareInch = ("%.25f" % (squareMeter * 1550.0031)).rstrip('0').rstrip('.')
                acre = ("%.25f" % (squareMeter * 0.000247)).rstrip('0').rstrip('.')

                print(f'{squareMeter} m?? = {squareKilometer} km??')
                print(f'{squareMeter} m?? = {squareCentimeter} cm??')
                print(f'{squareMeter} m?? = {squareMillimeter} mm??')
                print(f'{squareMeter} m?? = {hectare} ha')
                print(f'{squareMeter} m?? = {squareMile} mi??')
                print(f'{squareMeter} m?? = {squareYard} yd??')
                print(f'{squareMeter} m?? = {squareFoot} ft??')
                print(f'{squareMeter} m?? = {squareInch} in??')
                print(f'{squareMeter} m?? = {acre} ac')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 3:

            try:
                squareCentimeter = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if squareCentimeter > 0:

                squareKilometer = ("%.25f" % (squareCentimeter * 0.0000000001)).rstrip('0').rstrip('.')
                squareMeter = ("%.25f" % (squareCentimeter * 0.0001)).rstrip('0').rstrip('.')
                squareMillimeter = ("%.25f" % (squareCentimeter * 100)).rstrip('0').rstrip('.')
                hectare = ("%.25f" % (squareCentimeter * 0.00000001)).rstrip('0').rstrip('.')
                squareMile = ("%.25f" % (squareCentimeter * 0.0000000000386)).rstrip('0').rstrip('.')
                squareYard = ("%.25f" % (squareCentimeter * 0.00012)).rstrip('0').rstrip('.')
                squareFoot = ("%.25f" % (squareCentimeter * 0.00108)).rstrip('0').rstrip('.')
                squareInch = ("%.25f" % (squareCentimeter * 0.155)).rstrip('0').rstrip('.')
                acre = ("%.25f" % (squareCentimeter * 0.0000000247)).rstrip('0').rstrip('.')

                print(f'{squareCentimeter} cm?? = {squareKilometer} km??')
                print(f'{squareCentimeter} cm?? = {squareMeter} m??')
                print(f'{squareCentimeter} cm?? = {squareMillimeter} mm??')
                print(f'{squareCentimeter} cm?? = {hectare} ha')
                print(f'{squareCentimeter} cm?? = {squareMile} mi??')
                print(f'{squareCentimeter} cm?? = {squareYard} yd??')
                print(f'{squareCentimeter} cm?? = {squareFoot} ft??')
                print(f'{squareCentimeter} cm?? = {squareInch} in??')
                print(f'{squareCentimeter} cm?? = {acre} ac')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 4:

            try:
                squareMillimeter = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if squareMillimeter > 0:

                squareKilometer = ("%.25f" % (squareMillimeter * 0.000000000001)).rstrip('0').rstrip('.')
                squareMeter = ("%.25f" % (squareMillimeter * 0.000001)).rstrip('0').rstrip('.')
                squareCentimeter = ("%.25f" % (squareMillimeter * 0.01)).rstrip('0').rstrip('.')
                hectare = ("%.25f" % (squareMillimeter * 0.0000000001)).rstrip('0').rstrip('.')
                squareMile = ("%.25f" % (squareMillimeter * 0.000000000000386)).rstrip('0').rstrip('.')
                squareYard = ("%.25f" % (squareMillimeter * 0.0000012)).rstrip('0').rstrip('.')
                squareFoot = ("%.25f" % (squareMillimeter * 0.0000108)).rstrip('0').rstrip('.')
                squareInch = ("%.25f" % (squareMillimeter * 0.00155)).rstrip('0').rstrip('.')
                acre = ("%.25f" % (squareMillimeter * 0.000000000247)).rstrip('0').rstrip('.')

                print(f'{squareMillimeter} mm?? = {squareKilometer} km??')
                print(f'{squareMillimeter} mm?? = {squareMeter} m??')
                print(f'{squareMillimeter} mm?? = {squareCentimeter} cm??')
                print(f'{squareMillimeter} mm?? = {hectare} ha')
                print(f'{squareMillimeter} mm?? = {squareMile} mi??')
                print(f'{squareMillimeter} mm?? = {squareYard} yd??')
                print(f'{squareMillimeter} mm?? = {squareFoot} ft??')
                print(f'{squareMillimeter} mm?? = {squareInch} in??')
                print(f'{squareMillimeter} mm?? = {acre} ac')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 5:

            try:
                hectare = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if hectare > 0:

                squareKilometer = ("%.25f" % (hectare * 0.01)).rstrip('0').rstrip('.')
                squareMeter = ("%.25f" % (hectare * 10000)).rstrip('0').rstrip('.')
                squareCentimeter = ("%.25f" % (hectare * 100000000)).rstrip('0').rstrip('.')
                squareMillimeter = ("%.25f" % (hectare * 10000000000)).rstrip('0').rstrip('.')
                squareMile = ("%.25f" % (hectare * 0.00386)).rstrip('0').rstrip('.')
                squareYard = ("%.25f" % (hectare * 11959.9)).rstrip('0').rstrip('.')
                squareFoot = ("%.25f" % (hectare * 107639.104)).rstrip('0').rstrip('.')
                squareInch = ("%.25f" % (hectare * 15500031)).rstrip('0').rstrip('.')
                acre = ("%.25f" % (hectare * 2.471)).rstrip('0').rstrip('.')

                print(f'{hectare} ha = {squareKilometer} km??')
                print(f'{hectare} ha = {squareMeter} m??')
                print(f'{hectare} ha = {squareCentimeter} cm??')
                print(f'{hectare} ha = {squareMillimeter} mm??')
                print(f'{hectare} ha = {squareMile} mi??')
                print(f'{hectare} ha = {squareYard} yd??')
                print(f'{hectare} ha = {squareFoot} ft??')
                print(f'{hectare} ha = {squareInch} in??')
                print(f'{hectare} ha = {acre} ac')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 6:

            try:
                squareMile = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if squareMile > 0:

                squareKilometer = ("%.25f" % (squareMile * 2.59)).rstrip('0').rstrip('.')
                squareMeter = ("%.25f" % (squareMile * 2589990)).rstrip('0').rstrip('.')
                squareCentimeter = ("%.25f" % (squareMile * 25899900000)).rstrip('0').rstrip('.')
                squareMillimeter = ("%.25f" % (squareMile * 2589990000000)).rstrip('0').rstrip('.')
                hectare = ("%.25f" % (squareMile * 258.999)).rstrip('0').rstrip('.')
                squareYard = ("%.25f" % (squareMile * 3097602.26)).rstrip('0').rstrip('.')
                squareFoot = ("%.25f" % (squareMile * 27878420.34)).rstrip('0').rstrip('.')
                squareInch = ("%.25f" % (squareMile * 4014492529)).rstrip('0').rstrip('.')
                acre = ("%.25f" % (squareMile * 640.000467)).rstrip('0').rstrip('.')

                print(f'{squareMile} mi?? = {squareKilometer} km??')
                print(f'{squareMile} mi?? = {squareMeter} m??')
                print(f'{squareMile} mi?? = {squareCentimeter} cm??')
                print(f'{squareMile} mi?? = {squareMillimeter} mm??')
                print(f'{squareMile} mi?? = {hectare} ha')
                print(f'{squareMile} mi?? = {squareYard} yd??')
                print(f'{squareMile} mi?? = {squareFoot} ft??')
                print(f'{squareMile} mi?? = {squareInch} in??')
                print(f'{squareMile} mi?? = {acre} ac')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 7:

            try:
                squareYard = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if squareYard > 0:

                squareKilometer = ("%.25f" % (squareYard * 0.000000836)).rstrip('0').rstrip('.')
                squareMeter = ("%.25f" % (squareYard * 0.836)).rstrip('0').rstrip('.')
                squareCentimeter = ("%.25f" % (squareYard * 8361.274)).rstrip('0').rstrip('.')
                squareMillimeter = ("%.25f" % (squareYard * 836127.36)).rstrip('0').rstrip('.')
                hectare = ("%.25f" % (squareYard * 0.0000836)).rstrip('0').rstrip('.')
                squareMile = ("%.25f" % (squareYard * 0.000000323)).rstrip('0').rstrip('.')
                squareFoot = ("%.25f" % (squareYard * 9)).rstrip('0').rstrip('.')
                squareInch = ("%.25f" % (squareYard * 1296)).rstrip('0').rstrip('.')
                acre = ("%.25f" % (squareYard * 0.000207)).rstrip('0').rstrip('.')

                print(f'{squareYard} yd?? = {squareKilometer} km??')
                print(f'{squareYard} yd?? = {squareMeter} m??')
                print(f'{squareYard} yd?? = {squareCentimeter} cm??')
                print(f'{squareYard} yd?? = {squareMillimeter} mm??')
                print(f'{squareYard} yd?? = {hectare} ha')
                print(f'{squareYard} yd?? = {squareMile} mi??')
                print(f'{squareYard} yd?? = {squareFoot} ft??')
                print(f'{squareYard} yd?? = {squareInch} in??')
                print(f'{squareYard} yd?? = {acre} ac')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 8:

            try:
                squareFoot = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if squareFoot > 0:

                squareKilometer = ("%.25f" % (squareFoot * 0.0000000929)).rstrip('0').rstrip('.')
                squareMeter = ("%.25f" % (squareFoot * 0.0929)).rstrip('0').rstrip('.')
                squareCentimeter = ("%.25f" % (squareFoot * 929.0304)).rstrip('0').rstrip('.')
                squareMillimeter = ("%.25f" % (squareFoot * 92903.04)).rstrip('0').rstrip('.')
                hectare = ("%.25f" % (squareFoot * 0.00000929)).rstrip('0').rstrip('.')
                squareMile = ("%.25f" % (squareFoot * 0.0000000359)).rstrip('0').rstrip('.')
                squareYard = ("%.25f" % (squareFoot * 0.111)).rstrip('0').rstrip('.')
                squareInch = ("%.25f" % (squareFoot * 144)).rstrip('0').rstrip('.')
                acre = ("%.25f" % (squareFoot * 0.0000229)).rstrip('0').rstrip('.')

                print(f'{squareFoot} ft?? = {squareKilometer} km??')
                print(f'{squareFoot} ft?? = {squareMeter} m??')
                print(f'{squareFoot} ft?? = {squareCentimeter} cm??')
                print(f'{squareFoot} ft?? = {squareMillimeter} mm??')
                print(f'{squareFoot} ft?? = {hectare} ha')
                print(f'{squareFoot} ft?? = {squareMile} mi??')
                print(f'{squareFoot} ft?? = {squareYard} yd??')
                print(f'{squareFoot} ft?? = {squareInch} in??')
                print(f'{squareFoot} ft?? = {acre} ac')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 9:

            try:
                squareInch = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if squareInch > 0:

                squareKilometer = ("%.25f" % (squareInch * 0.000000000645)).rstrip('0').rstrip('.')
                squareMeter = ("%.25f" % (squareInch * 0.000645)).rstrip('0').rstrip('.')
                squareCentimeter = ("%.25f" % (squareInch * 6.452)).rstrip('0').rstrip('.')
                squareMillimeter = ("%.25f" % (squareInch * 645.16)).rstrip('0').rstrip('.')
                hectare = ("%.25f" % (squareInch * 0.0000000645)).rstrip('0').rstrip('.')
                squareMile = ("%.25f" % (squareInch * 0.000000000249)).rstrip('0').rstrip('.')
                squareYard = ("%.25f" % (squareInch * 0.000772)).rstrip('0').rstrip('.')
                squareFoot = ("%.25f" % (squareInch * 0.00694)).rstrip('0').rstrip('.')
                acre = ("%.25f" % (squareInch * 0.000000159)).rstrip('0').rstrip('.')

                print(f'{squareInch} in?? = {squareKilometer} km??')
                print(f'{squareInch} in?? = {squareMeter} m??')
                print(f'{squareInch} in?? = {squareCentimeter} cm??')
                print(f'{squareInch} in?? = {squareMillimeter} mm??')
                print(f'{squareInch} in?? = {hectare} ha')
                print(f'{squareInch} in?? = {squareMile} mi??')
                print(f'{squareInch} in?? = {squareYard} yd??')
                print(f'{squareInch} in?? = {squareFoot} ft??')
                print(f'{squareInch} in?? = {acre} ac')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 10:

            try:
                acre = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if acre > 0:

                squareKilometer = ("%.25f" % (acre * 0.00405)).rstrip('0').rstrip('.')
                squareMeter = ("%.25f" % (acre * 4046.856)).rstrip('0').rstrip('.')
                squareCentimeter = ("%.25f" % (acre * 40468564.224)).rstrip('0').rstrip('.')
                squareMillimeter = ("%.25f" % (acre * 4046856422.4)).rstrip('0').rstrip('.')
                hectare = ("%.25f" % (acre * 0.405)).rstrip('0').rstrip('.')
                squareMile = ("%.25f" % (acre * 0.00156)).rstrip('0').rstrip('.')
                squareYard = ("%.25f" % (acre * 4840)).rstrip('0').rstrip('.')
                squareFoot = ("%.25f" % (acre * 43560)).rstrip('0').rstrip('.')
                squareInch = ("%.25f" % (acre * 6272640)).rstrip('0').rstrip('.')

                print(f'{acre} ac = {squareKilometer} km??')
                print(f'{acre} ac = {squareMeter} m??')
                print(f'{acre} ac = {squareCentimeter} cm??')
                print(f'{acre} ac = {squareMillimeter} mm??')
                print(f'{acre} ac = {hectare} ha')
                print(f'{acre} ac = {squareMile} mi??')
                print(f'{acre} ac = {squareYard} yd??')
                print(f'{acre} ac = {squareFoot} ft??')
                print(f'{acre} ac = {squareInch} in??')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        else:
            print('# Enter value from 1 to 10 #')
            print()

    elif menuChoice == 4:
        print('Choose unit type:')
        print('[1] Cubic Kilometer' + '      ' + '[7] Cubic Mile' + '      ' + '[13] US Pint')
        print('[2] Cubic Meter' + '          ' + '[8] Cubic Yard' + '      ' + '[14] US Cup')
        print('[3] Cubic Centimeter' + '     ' + '[9] Cubic Foot' + '      ' + '[15] Imperial Gallon')
        print('[4] Cubic Millimeter' + '     ' + '[10] Cubic Inch' + '     ' + '[16] Imperial Quart')
        print('[5] Liter' + '                ' + '[11] US Gallon' + '      ' + '[17] Imperial Pint')
        print('[6] Milliliter' + '           ' + '[12] US Quart')
        print()

        try:
            subMenuChoice = int(input('Enter your choice: '))
            print()
        except ValueError:
            print()
            print('# Enter value from 1 to 17 #')
            print()
            continue

        if subMenuChoice == 1:

            try:
                cubicKilometer = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if cubicKilometer > 0:

                cubicMeter = ("%.25f" % (cubicKilometer * 1000000000)).rstrip('0').rstrip('.')
                cubicCentimeter = ("%.25f" % (cubicKilometer * 1000000000000000)).rstrip('0').rstrip('.')
                cubicMillimeter = ("%.25f" % (cubicKilometer * 1000000000000000000)).rstrip('0').rstrip('.')
                liter = ("%.25f" % (cubicKilometer * 1000000000000)).rstrip('0').rstrip('.')
                milliLiter = ("%.25f" % (cubicKilometer * 1000000000000000)).rstrip('0').rstrip('.')
                cubicMile = ("%.25f" % (cubicKilometer * 0.24)).rstrip('0').rstrip('.')
                cubicYard = ("%.25f" % (cubicKilometer * 1307950619.3)).rstrip('0').rstrip('.')
                cubicFoot = ("%.25f" % (cubicKilometer * 35314666721)).rstrip('0').rstrip('.')
                cubicInch = ("%.25f" % (cubicKilometer * 61023744094732)).rstrip('0').rstrip('.')
                usGallon = ("%.25f" % (cubicKilometer * 264172176858)).rstrip('0').rstrip('.')
                usQuart = ("%.25f" % (cubicKilometer * 1056688707432)).rstrip('0').rstrip('.')
                usPint = ("%.25f" % (cubicKilometer * 2113377414864)).rstrip('0').rstrip('.')
                usCup = ("%.25f" % (cubicKilometer * 4226754829728)).rstrip('0').rstrip('.')
                imperialGallon = ("%.25f" % (cubicKilometer * 219969248299)).rstrip('0').rstrip('.')
                imperialQuart = ("%.25f" % (cubicKilometer * 879876993196)).rstrip('0').rstrip('.')
                imperialPint = ("%.25f" % (cubicKilometer * 1759753986393)).rstrip('0').rstrip('.')

                print(f'{cubicKilometer} km?? = {cubicMeter} m??')
                print(f'{cubicKilometer} km?? = {cubicCentimeter} cm??')
                print(f'{cubicKilometer} km?? = {cubicMillimeter} mm??')
                print(f'{cubicKilometer} km?? = {liter} l')
                print(f'{cubicKilometer} km?? = {milliLiter} ml')
                print(f'{cubicKilometer} km?? = {cubicMile} mi??')
                print(f'{cubicKilometer} km?? = {cubicYard} yd??')
                print(f'{cubicKilometer} km?? = {cubicFoot} ft??')
                print(f'{cubicKilometer} km?? = {cubicInch} in??')
                print(f'{cubicKilometer} km?? = {usGallon} gal [US]')
                print(f'{cubicKilometer} km?? = {usQuart} qt [US]')
                print(f'{cubicKilometer} km?? = {usPint} pt [US]')
                print(f'{cubicKilometer} km?? = {usCup} cup [US]')
                print(f'{cubicKilometer} km?? = {imperialGallon} gal [imp]')
                print(f'{cubicKilometer} km?? = {imperialQuart} qt [imp]')
                print(f'{cubicKilometer} km?? = {imperialPint} pt [imp]')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 2:

            try:
                cubicMeter = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if cubicMeter > 0:

                cubicKilometer = ("%.25f" % (cubicMeter * 0.000000001)).rstrip('0').rstrip('.')
                cubicCentimeter = ("%.25f" % (cubicMeter * 1000000)).rstrip('0').rstrip('.')
                cubicMillimeter = ("%.25f" % (cubicMeter * 1000000000)).rstrip('0').rstrip('.')
                liter = ("%.25f" % (cubicMeter * 1000)).rstrip('0').rstrip('.')
                milliLiter = ("%.25f" % (cubicMeter * 1000000)).rstrip('0').rstrip('.')
                cubicMile = ("%.25f" % (cubicMeter * 0.00000000024)).rstrip('0').rstrip('.')
                cubicYard = ("%.25f" % (cubicMeter * 1.308)).rstrip('0').rstrip('.')
                cubicFoot = ("%.25f" % (cubicMeter * 35.315)).rstrip('0').rstrip('.')
                cubicInch = ("%.25f" % (cubicMeter * 61023.744)).rstrip('0').rstrip('.')
                usGallon = ("%.25f" % (cubicMeter * 264.172)).rstrip('0').rstrip('.')
                usQuart = ("%.25f" % (cubicMeter * 1056.689)).rstrip('0').rstrip('.')
                usPint = ("%.25f" % (cubicMeter * 2113.377)).rstrip('0').rstrip('.')
                usCup = ("%.25f" % (cubicMeter * 4226.755)).rstrip('0').rstrip('.')
                imperialGallon = ("%.25f" % (cubicMeter * 219.97)).rstrip('0').rstrip('.')
                imperialQuart = ("%.25f" % (cubicMeter * 879.877)).rstrip('0').rstrip('.')
                imperialPint = ("%.25f" % (cubicMeter * 1759.754)).rstrip('0').rstrip('.')

                print(f'{cubicMeter} m?? = {cubicKilometer} km??')
                print(f'{cubicMeter} m?? = {cubicCentimeter} cm??')
                print(f'{cubicMeter} m?? = {cubicMillimeter} mm??')
                print(f'{cubicMeter} m?? = {liter} l')
                print(f'{cubicMeter} m?? = {milliLiter} ml')
                print(f'{cubicMeter} m?? = {cubicMile} mi??')
                print(f'{cubicMeter} m?? = {cubicYard} yd??')
                print(f'{cubicMeter} m?? = {cubicFoot} ft??')
                print(f'{cubicMeter} m?? = {cubicInch} in??')
                print(f'{cubicMeter} m?? = {usGallon} gal [US]')
                print(f'{cubicMeter} m?? = {usQuart} qt [US]')
                print(f'{cubicMeter} m?? = {usPint} pt [US]')
                print(f'{cubicMeter} m?? = {usCup} cup [US]')
                print(f'{cubicMeter} m?? = {imperialGallon} gal [imp]')
                print(f'{cubicMeter} m?? = {imperialQuart} qt [imp]')
                print(f'{cubicMeter} m?? = {imperialPint} pt [imp]')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 3:

            try:
                cubicCentimeter = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if cubicCentimeter > 0:

                cubicKilometer = ("%.25f" % (cubicCentimeter * 1e-15)).rstrip('0').rstrip('.')
                cubicMeter = ("%.25f" % (cubicCentimeter * 0.000001)).rstrip('0').rstrip('.')
                cubicMillimeter = ("%.25f" % (cubicCentimeter * 1000)).rstrip('0').rstrip('.')
                liter = ("%.25f" % (cubicCentimeter * 0.001)).rstrip('0').rstrip('.')
                milliLiter = ("%.25f" % (cubicCentimeter * 1)).rstrip('0').rstrip('.')
                cubicMile = ("%.25f" % (cubicCentimeter * 2.399e-16)).rstrip('0').rstrip('.')
                cubicYard = ("%.25f" % (cubicCentimeter * 0.00000131)).rstrip('0').rstrip('.')
                cubicFoot = ("%.25f" % (cubicCentimeter * 0.0000353)).rstrip('0').rstrip('.')
                cubicInch = ("%.25f" % (cubicCentimeter * 0.061)).rstrip('0').rstrip('.')
                usGallon = ("%.25f" % (cubicCentimeter * 0.000264)).rstrip('0').rstrip('.')
                usQuart = ("%.25f" % (cubicCentimeter * 0.00106)).rstrip('0').rstrip('.')
                usPint = ("%.25f" % (cubicCentimeter * 0.00211)).rstrip('0').rstrip('.')
                usCup = ("%.25f" % (cubicCentimeter * 0.00423)).rstrip('0').rstrip('.')
                imperialGallon = ("%.25f" % (cubicCentimeter * 0.00022)).rstrip('0').rstrip('.')
                imperialQuart = ("%.25f" % (cubicCentimeter * 0.00088)).rstrip('0').rstrip('.')
                imperialPint = ("%.25f" % (cubicCentimeter * 0.00176)).rstrip('0').rstrip('.')

                print(f'{cubicCentimeter} cm?? = {cubicKilometer} km??')
                print(f'{cubicCentimeter} cm?? = {cubicMeter} m??')
                print(f'{cubicCentimeter} cm?? = {cubicMillimeter} mm??')
                print(f'{cubicCentimeter} cm?? = {liter} l')
                print(f'{cubicCentimeter} cm?? = {milliLiter} ml')
                print(f'{cubicCentimeter} cm?? = {cubicMile} mi??')
                print(f'{cubicCentimeter} cm?? = {cubicYard} yd??')
                print(f'{cubicCentimeter} cm?? = {cubicFoot} ft??')
                print(f'{cubicCentimeter} cm?? = {cubicInch} in??')
                print(f'{cubicCentimeter} cm?? = {usGallon} gal [US]')
                print(f'{cubicCentimeter} cm?? = {usQuart} qt [US]')
                print(f'{cubicCentimeter} cm?? = {usPint} pt [US]')
                print(f'{cubicCentimeter} cm?? = {usCup} cup [US]')
                print(f'{cubicCentimeter} cm?? = {imperialGallon} gal [imp]')
                print(f'{cubicCentimeter} cm?? = {imperialQuart} qt [imp]')
                print(f'{cubicCentimeter} cm?? = {imperialPint} pt [imp]')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 4:

            try:
                cubicMillimeter = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if cubicMillimeter > 0:

                cubicKilometer = ("%.25f" % (cubicMillimeter * 1e-18)).rstrip('0').rstrip('.')
                cubicMeter = ("%.25f" % (cubicMillimeter * 1e-9)).rstrip('0').rstrip('.')
                cubicCentimeter = ("%.25f" % (cubicMillimeter * 0.001)).rstrip('0').rstrip('.')
                liter = ("%.25f" % (cubicMillimeter * 0.000001)).rstrip('0').rstrip('.')
                milliLiter = ("%.25f" % (cubicMillimeter * 0.001)).rstrip('0').rstrip('.')
                cubicMile = ("%.25f" % (cubicMillimeter * 2.399e-19)).rstrip('0').rstrip('.')
                cubicYard = ("%.25f" % (cubicMillimeter * 1.308e-9)).rstrip('0').rstrip('.')
                cubicFoot = ("%.25f" % (cubicMillimeter * 3.531e-8)).rstrip('0').rstrip('.')
                cubicInch = ("%.25f" % (cubicMillimeter * 0.000061)).rstrip('0').rstrip('.')
                usGallon = ("%.25f" % (cubicMillimeter * 2.642e-7)).rstrip('0').rstrip('.')
                usQuart = ("%.25f" % (cubicMillimeter * 0.00000106)).rstrip('0').rstrip('.')
                usPint = ("%.25f" % (cubicMillimeter * 0.00000211)).rstrip('0').rstrip('.')
                usCup = ("%.25f" % (cubicMillimeter * 0.00000423)).rstrip('0').rstrip('.')
                imperialGallon = ("%.25f" % (cubicMillimeter * 2.2e-7)).rstrip('0').rstrip('.')
                imperialQuart = ("%.25f" % (cubicMillimeter * 8.799e-7)).rstrip('0').rstrip('.')
                imperialPint = ("%.25f" % (cubicMillimeter * 0.00000176)).rstrip('0').rstrip('.')

                print(f'{cubicMillimeter} mm?? = {cubicKilometer} km??')
                print(f'{cubicMillimeter} mm?? = {cubicMeter} m??')
                print(f'{cubicMillimeter} mm?? = {cubicCentimeter} cm??')
                print(f'{cubicMillimeter} mm?? = {liter} l')
                print(f'{cubicMillimeter} mm?? = {milliLiter} ml')
                print(f'{cubicMillimeter} mm?? = {cubicMile} mi??')
                print(f'{cubicMillimeter} mm?? = {cubicYard} yd??')
                print(f'{cubicMillimeter} mm?? = {cubicFoot} ft??')
                print(f'{cubicMillimeter} mm?? = {cubicInch} in??')
                print(f'{cubicMillimeter} mm?? = {usGallon} gal [US]')
                print(f'{cubicMillimeter} mm?? = {usQuart} qt [US]')
                print(f'{cubicMillimeter} mm?? = {usPint} pt [US]')
                print(f'{cubicMillimeter} mm?? = {usCup} cup [US]')
                print(f'{cubicMillimeter} mm?? = {imperialGallon} gal [imp]')
                print(f'{cubicMillimeter} mm?? = {imperialQuart} qt [imp]')
                print(f'{cubicMillimeter} mm?? = {imperialPint} pt [imp]')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 5:

            try:
                liter = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if liter > 0:

                cubicKilometer = ("%.25f" % (liter * 1e-12)).rstrip('0').rstrip('.')
                cubicMeter = ("%.25f" % (liter * 0.001)).rstrip('0').rstrip('.')
                cubicCentimeter = ("%.25f" % (liter * 1000)).rstrip('0').rstrip('.')
                cubicMillimeter = ("%.25f" % (liter * 1000000)).rstrip('0').rstrip('.')
                milliLiter = ("%.25f" % (liter * 1000)).rstrip('0').rstrip('.')
                cubicMile = ("%.25f" % (liter * 2.399e-13)).rstrip('0').rstrip('.')
                cubicYard = ("%.25f" % (liter * 0.00131)).rstrip('0').rstrip('.')
                cubicFoot = ("%.25f" % (liter * 0.0353)).rstrip('0').rstrip('.')
                cubicInch = ("%.25f" % (liter * 61.0237)).rstrip('0').rstrip('.')
                usGallon = ("%.25f" % (liter * 0.264)).rstrip('0').rstrip('.')
                usQuart = ("%.25f" % (liter * 1.0567)).rstrip('0').rstrip('.')
                usPint = ("%.25f" % (liter * 2.113)).rstrip('0').rstrip('.')
                usCup = ("%.25f" % (liter * 4.227)).rstrip('0').rstrip('.')
                imperialGallon = ("%.25f" % (liter * 0.22)).rstrip('0').rstrip('.')
                imperialQuart = ("%.25f" % (liter * 0.88)).rstrip('0').rstrip('.')
                imperialPint = ("%.25f" % (liter * 1.76)).rstrip('0').rstrip('.')

                print(f'{liter} l = {cubicKilometer} km??')
                print(f'{liter} l = {cubicMeter} m??')
                print(f'{liter} l = {cubicCentimeter} cm??')
                print(f'{liter} l = {cubicMillimeter} mm??')
                print(f'{liter} l = {milliLiter} ml')
                print(f'{liter} l = {cubicMile} mi??')
                print(f'{liter} l = {cubicYard} yd??')
                print(f'{liter} l = {cubicFoot} ft??')
                print(f'{liter} l = {cubicInch} in??')
                print(f'{liter} l = {usGallon} gal [US]')
                print(f'{liter} l = {usQuart} qt [US]')
                print(f'{liter} l = {usPint} pt [US]')
                print(f'{liter} l = {usCup} cup [US]')
                print(f'{liter} l = {imperialGallon} gal [imp]')
                print(f'{liter} l = {imperialQuart} qt [imp]')
                print(f'{liter} l = {imperialPint} pt [imp]')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 6:

            try:
                milliLiter = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if milliLiter > 0:

                cubicKilometer = ("%.25f" % (milliLiter * 1e-15)).rstrip('0').rstrip('.')
                cubicMeter = ("%.25f" % (milliLiter * 0.000001)).rstrip('0').rstrip('.')
                cubicCentimeter = ("%.25f" % (milliLiter * 1)).rstrip('0').rstrip('.')
                cubicMillimeter = ("%.25f" % (milliLiter * 1000)).rstrip('0').rstrip('.')
                liter = ("%.25f" % (milliLiter * 0.001)).rstrip('0').rstrip('.')
                cubicMile = ("%.25f" % (milliLiter * 2.399e-16)).rstrip('0').rstrip('.')
                cubicYard = ("%.25f" % (milliLiter * 0.00000131)).rstrip('0').rstrip('.')
                cubicFoot = ("%.25f" % (milliLiter * 0.0000353)).rstrip('0').rstrip('.')
                cubicInch = ("%.25f" % (milliLiter * 0.061)).rstrip('0').rstrip('.')
                usGallon = ("%.25f" % (milliLiter * 0.000264)).rstrip('0').rstrip('.')
                usQuart = ("%.25f" % (milliLiter * 0.00106)).rstrip('0').rstrip('.')
                usPint = ("%.25f" % (milliLiter * 0.00211)).rstrip('0').rstrip('.')
                usCup = ("%.25f" % (milliLiter * 0.00423)).rstrip('0').rstrip('.')
                imperialGallon = ("%.25f" % (milliLiter * 0.00022)).rstrip('0').rstrip('.')
                imperialQuart = ("%.25f" % (milliLiter * 0.00088)).rstrip('0').rstrip('.')
                imperialPint = ("%.25f" % (milliLiter * 0.00176)).rstrip('0').rstrip('.')

                print(f'{milliLiter} ml = {cubicKilometer} km??')
                print(f'{milliLiter} ml = {cubicMeter} m??')
                print(f'{milliLiter} ml = {cubicCentimeter} cm??')
                print(f'{milliLiter} ml = {cubicMillimeter} mm??')
                print(f'{milliLiter} ml = {liter} l')
                print(f'{milliLiter} ml = {cubicMile} mi??')
                print(f'{milliLiter} ml = {cubicYard} yd??')
                print(f'{milliLiter} ml = {cubicFoot} ft??')
                print(f'{milliLiter} ml = {cubicInch} in??')
                print(f'{milliLiter} ml = {usGallon} gal [US]')
                print(f'{milliLiter} ml = {usQuart} qt [US]')
                print(f'{milliLiter} ml = {usPint} pt [US]')
                print(f'{milliLiter} ml = {usCup} cup [US]')
                print(f'{milliLiter} ml = {imperialGallon} gal [imp]')
                print(f'{milliLiter} ml = {imperialQuart} qt [imp]')
                print(f'{milliLiter} ml = {imperialPint} pt [imp]')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 7:

            try:
                cubicMile = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if cubicMile > 0:

                cubicKilometer = ("%.25f" % (cubicMile * 4.168)).rstrip('0').rstrip('.')
                cubicMeter = ("%.25f" % (cubicMile * 4168181825.441)).rstrip('0').rstrip('.')
                cubicCentimeter = ("%.25f" % (cubicMile * 4.168e+15)).rstrip('0').rstrip('.')
                cubicMillimeter = ("%.25f" % (cubicMile * 4.168e+18)).rstrip('0').rstrip('.')
                liter = ("%.25f" % (cubicMile * 4168181825440.6)).rstrip('0').rstrip('.')
                milliLiter = ("%.25f" % (cubicMile * 4168181825440000)).rstrip('0').rstrip('.')
                cubicYard = ("%.25f" % (cubicMile * 5451773612.4)).rstrip('0').rstrip('.')
                cubicFoot = ("%.25f" % (cubicMile * 147197887535)).rstrip('0').rstrip('.')
                cubicInch = ("%.25f" % (cubicMile * 254357949660781)).rstrip('0').rstrip('.')
                usGallon = ("%.25f" % (cubicMile * 1101117184136)).rstrip('0').rstrip('.')
                usQuart = ("%.25f" % (cubicMile * 4404468736544)).rstrip('0').rstrip('.')
                usPint = ("%.25f" % (cubicMile * 8808937473087)).rstrip('0').rstrip('.')
                usCup = ("%.25f" % (cubicMile * 17617874946175)).rstrip('0').rstrip('.')
                imperialGallon = ("%.25f" % (cubicMile * 916871421375)).rstrip('0').rstrip('.')
                imperialQuart = ("%.25f" % (cubicMile * 3667485685501)).rstrip('0').rstrip('.')
                imperialPint = ("%.25f" % (cubicMile * 7334971371002)).rstrip('0').rstrip('.')

                print(f'{cubicMile} mi?? = {cubicKilometer} km??')
                print(f'{cubicMile} mi?? = {cubicMeter} m??')
                print(f'{cubicMile} mi?? = {cubicCentimeter} cm??')
                print(f'{cubicMile} mi?? = {cubicMillimeter} mm??')
                print(f'{cubicMile} mi?? = {liter} l')
                print(f'{cubicMile} mi?? = {milliLiter} ml')
                print(f'{cubicMile} mi?? = {cubicYard} yd??')
                print(f'{cubicMile} mi?? = {cubicFoot} ft??')
                print(f'{cubicMile} mi?? = {cubicInch} in??')
                print(f'{cubicMile} mi?? = {usGallon} gal [US]')
                print(f'{cubicMile} mi?? = {usQuart} qt [US]')
                print(f'{cubicMile} mi?? = {usPint} pt [US]')
                print(f'{cubicMile} mi?? = {usCup} cup [US]')
                print(f'{cubicMile} mi?? = {imperialGallon} gal [imp]')
                print(f'{cubicMile} mi?? = {imperialQuart} qt [imp]')
                print(f'{cubicMile} mi?? = {imperialPint} pt [imp]')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 8:

            try:
                cubicYard = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if cubicYard > 0:

                cubicKilometer = ("%.25f" % (cubicYard * 7.645e-10)).rstrip('0').rstrip('.')
                cubicMeter = ("%.25f" % (cubicYard * 0.764)).rstrip('0').rstrip('.')
                cubicCentimeter = ("%.25f" % (cubicYard * 764554.858)).rstrip('0').rstrip('.')
                cubicMillimeter = ("%.25f" % (cubicYard * 764554857.98)).rstrip('0').rstrip('.')
                liter = ("%.25f" % (cubicYard * 764.555)).rstrip('0').rstrip('.')
                milliLiter = ("%.25f" % (cubicYard * 764554.858)).rstrip('0').rstrip('.')
                cubicMile = ("%.25f" % (cubicYard * 1.834e-10)).rstrip('0').rstrip('.')
                cubicFoot = ("%.25f" % (cubicYard * 27)).rstrip('0').rstrip('.')
                cubicInch = ("%.25f" % (cubicYard * 46656)).rstrip('0').rstrip('.')
                usGallon = ("%.25f" % (cubicYard * 201.974)).rstrip('0').rstrip('.')
                usQuart = ("%.25f" % (cubicYard * 807.896)).rstrip('0').rstrip('.')
                usPint = ("%.25f" % (cubicYard * 1615.793)).rstrip('0').rstrip('.')
                usCup = ("%.25f" % (cubicYard * 3231.586)).rstrip('0').rstrip('.')
                imperialGallon = ("%.25f" % (cubicYard * 168.178)).rstrip('0').rstrip('.')
                imperialQuart = ("%.25f" % (cubicYard * 672.714)).rstrip('0').rstrip('.')
                imperialPint = ("%.25f" % (cubicYard * 1345.428)).rstrip('0').rstrip('.')

                print(f'{cubicYard} yd?? = {cubicKilometer} km??')
                print(f'{cubicYard} yd?? = {cubicMeter} m??')
                print(f'{cubicYard} yd?? = {cubicCentimeter} cm??')
                print(f'{cubicYard} yd?? = {cubicMillimeter} mm??')
                print(f'{cubicYard} yd?? = {liter} l')
                print(f'{cubicYard} yd?? = {milliLiter} ml')
                print(f'{cubicYard} yd?? = {cubicMile} mi??')
                print(f'{cubicYard} yd?? = {cubicFoot} ft??')
                print(f'{cubicYard} yd?? = {cubicInch} in??')
                print(f'{cubicYard} yd?? = {usGallon} gal [US]')
                print(f'{cubicYard} yd?? = {usQuart} qt [US]')
                print(f'{cubicYard} yd?? = {usPint} pt [US]')
                print(f'{cubicYard} yd?? = {usCup} cup [US]')
                print(f'{cubicMile} yd?? = {imperialGallon} gal [imp]')
                print(f'{cubicYard} yd?? = {imperialQuart} qt [imp]')
                print(f'{cubicYard} yd?? = {imperialPint} pt [imp]')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 9:

            try:
                cubicFoot = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if cubicFoot > 0:

                cubicKilometer = ("%.25f" % (cubicFoot * 2.832e-11)).rstrip('0').rstrip('.')
                cubicMeter = ("%.25f" % (cubicFoot * 0.0283)).rstrip('0').rstrip('.')
                cubicCentimeter = ("%.25f" % (cubicFoot * 28316.846)).rstrip('0').rstrip('.')
                cubicMillimeter = ("%.25f" % (cubicFoot * 28316846.592)).rstrip('0').rstrip('.')
                liter = ("%.25f" % (cubicFoot * 28.317)).rstrip('0').rstrip('.')
                milliLiter = ("%.25f" % (cubicFoot * 28316.846)).rstrip('0').rstrip('.')
                cubicMile = ("%.25f" % (cubicFoot * 6.793e-12)).rstrip('0').rstrip('.')
                cubicYard = ("%.25f" % (cubicFoot * 0.037)).rstrip('0').rstrip('.')
                cubicInch = ("%.25f" % (cubicFoot * 1728)).rstrip('0').rstrip('.')
                usGallon = ("%.25f" % (cubicFoot * 7.48)).rstrip('0').rstrip('.')
                usQuart = ("%.25f" % (cubicFoot * 29.922)).rstrip('0').rstrip('.')
                usPint = ("%.25f" % (cubicFoot * 59.844)).rstrip('0').rstrip('.')
                usCup = ("%.25f" % (cubicFoot * 119.688)).rstrip('0').rstrip('.')
                imperialGallon = ("%.25f" % (cubicFoot * 6.229)).rstrip('0').rstrip('.')
                imperialQuart = ("%.25f" % (cubicFoot * 24.915)).rstrip('0').rstrip('.')
                imperialPint = ("%.25f" % (cubicFoot * 49.831)).rstrip('0').rstrip('.')

                print(f'{cubicFoot} ft?? = {cubicKilometer} km??')
                print(f'{cubicFoot} ft?? = {cubicMeter} m??')
                print(f'{cubicFoot} ft?? = {cubicCentimeter} cm??')
                print(f'{cubicFoot} ft?? = {cubicMillimeter} mm??')
                print(f'{cubicFoot} ft?? = {liter} l')
                print(f'{cubicFoot} ft?? = {milliLiter} ml')
                print(f'{cubicFoot} ft?? = {cubicMile} mi??')
                print(f'{cubicFoot} ft?? = {cubicYard} yd??')
                print(f'{cubicFoot} ft?? = {cubicInch} in??')
                print(f'{cubicFoot} ft?? = {usGallon} gal [US]')
                print(f'{cubicFoot} ft?? = {usQuart} qt [US]')
                print(f'{cubicFoot} ft?? = {usPint} pt [US]')
                print(f'{cubicFoot} ft?? = {usCup} cup [US]')
                print(f'{cubicFoot} ft?? = {imperialGallon} gal [imp]')
                print(f'{cubicFoot} ft?? = {imperialQuart} qt [imp]')
                print(f'{cubicFoot} ft?? = {imperialPint} pt [imp]')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 10:

            try:
                cubicInch = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if cubicInch > 0:

                cubicKilometer = ("%.25f" % (cubicInch * 1.639e-14)).rstrip('0').rstrip('.')
                cubicMeter = ("%.25f" % (cubicInch * 0.0000164)).rstrip('0').rstrip('.')
                cubicCentimeter = ("%.25f" % (cubicInch * 16.387)).rstrip('0').rstrip('.')
                cubicMillimeter = ("%.25f" % (cubicInch * 16387.064)).rstrip('0').rstrip('.')
                liter = ("%.25f" % (cubicInch * 0.0164)).rstrip('0').rstrip('.')
                milliLiter = ("%.25f" % (cubicInch * 16.387)).rstrip('0').rstrip('.')
                cubicMile = ("%.25f" % (cubicInch * 3.931e-15)).rstrip('0').rstrip('.')
                cubicYard = ("%.25f" % (cubicInch * 0.0000214)).rstrip('0').rstrip('.')
                cubicFoot = ("%.25f" % (cubicInch * 0.000579)).rstrip('0').rstrip('.')
                usGallon = ("%.25f" % (cubicInch * 0.00433)).rstrip('0').rstrip('.')
                usQuart = ("%.25f" % (cubicInch * 0.0173)).rstrip('0').rstrip('.')
                usPint = ("%.25f" % (cubicInch * 0.0346)).rstrip('0').rstrip('.')
                usCup = ("%.25f" % (cubicInch * 0.0693)).rstrip('0').rstrip('.')
                imperialGallon = ("%.25f" % (cubicInch * 0.0036)).rstrip('0').rstrip('.')
                imperialQuart = ("%.25f" % (cubicInch * 0.0144)).rstrip('0').rstrip('.')
                imperialPint = ("%.25f" % (cubicInch * 0.0288)).rstrip('0').rstrip('.')

                print(f'{cubicInch} in?? = {cubicKilometer} km??')
                print(f'{cubicInch} in?? = {cubicMeter} m??')
                print(f'{cubicInch} in?? = {cubicCentimeter} cm??')
                print(f'{cubicInch} in?? = {cubicMillimeter} mm??')
                print(f'{cubicInch} in?? = {liter} l')
                print(f'{cubicInch} in?? = {milliLiter} ml')
                print(f'{cubicInch} in?? = {cubicMile} mi??')
                print(f'{cubicInch} in?? = {cubicYard} yd??')
                print(f'{cubicInch} in?? = {cubicFoot} ft??')
                print(f'{cubicInch} in?? = {usGallon} gal [US]')
                print(f'{cubicInch} in?? = {usQuart} qt [US]')
                print(f'{cubicInch} in?? = {usPint} pt [US]')
                print(f'{cubicInch} in?? = {usCup} cup [US]')
                print(f'{cubicInch} in?? = {imperialGallon} gal [imp]')
                print(f'{cubicInch} in?? = {imperialQuart} qt [imp]')
                print(f'{cubicInch} in?? = {imperialPint} pt [imp]')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 11:

            try:
                usGallon = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if usGallon > 0:

                cubicKilometer = ("%.25f" % (usGallon * 3.785e-12)).rstrip('0').rstrip('.')
                cubicMeter = ("%.25f" % (usGallon * 0.00378)).rstrip('0').rstrip('.')
                cubicCentimeter = ("%.25f" % (usGallon * 3785.41)).rstrip('0').rstrip('.')
                cubicMillimeter = ("%.25f" % (usGallon * 3785410)).rstrip('0').rstrip('.')
                liter = ("%.25f" % (usGallon * 3.785)).rstrip('0').rstrip('.')
                milliLiter = ("%.25f" % (usGallon * 3785.41)).rstrip('0').rstrip('.')
                cubicMile = ("%.25f" % (usGallon * 9.0817e-13)).rstrip('0').rstrip('.')
                cubicYard = ("%.25f" % (usGallon * 0.00495)).rstrip('0').rstrip('.')
                cubicFoot = ("%.25f" % (usGallon * 0.134)).rstrip('0').rstrip('.')
                cubicInch = ("%.25f" % (usGallon * 230.1)).rstrip('0').rstrip('.')
                usQuart = ("%.25f" % (usGallon * 4)).rstrip('0').rstrip('.')
                usPint = ("%.25f" % (usGallon * 8)).rstrip('0').rstrip('.')
                usCup = ("%.25f" % (usGallon * 16)).rstrip('0').rstrip('.')
                imperialGallon = ("%.25f" % (usGallon * 0.833)).rstrip('0').rstrip('.')
                imperialQuart = ("%.25f" % (usGallon * 3.331)).rstrip('0').rstrip('.')
                imperialPint = ("%.25f" % (usGallon * 6.661)).rstrip('0').rstrip('.')

                print(f'{usGallon} gal [US] = {cubicKilometer} km??')
                print(f'{usGallon} gal [US] = {cubicMeter} m??')
                print(f'{usGallon} gal [US] = {cubicCentimeter} cm??')
                print(f'{usGallon} gal [US] = {cubicMillimeter} mm??')
                print(f'{usGallon} gal [US] = {liter} l')
                print(f'{usGallon} gal [US] = {milliLiter} ml')
                print(f'{usGallon} gal [US] = {cubicMile} mi??')
                print(f'{usGallon} gal [US] = {cubicYard} yd??')
                print(f'{usGallon} gal [US] = {cubicFoot} ft??')
                print(f'{usGallon} gal [US] = {cubicInch} in??')
                print(f'{usGallon} gal [US] = {usQuart} qt [US]')
                print(f'{usGallon} gal [US] = {usPint} pt [US]')
                print(f'{usGallon} gal [US] = {usCup} cup [US]')
                print(f'{usGallon} gal [US] = {imperialGallon} gal [imp]')
                print(f'{usGallon} gal [US] = {imperialQuart} qt [imp]')
                print(f'{usGallon} gal [US] = {imperialPint} pt [imp]')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 12:

            try:
                usQuart = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if usQuart > 0:

                cubicKilometer = ("%.25f" % (usQuart * 9.463e-13)).rstrip('0').rstrip('.')
                cubicMeter = ("%.25f" % (usQuart * 0.000946)).rstrip('0').rstrip('.')
                cubicCentimeter = ("%.25f" % (usQuart * 946.353)).rstrip('0').rstrip('.')
                cubicMillimeter = ("%.25f" % (usQuart * 946352.5)).rstrip('0').rstrip('.')
                liter = ("%.25f" % (usQuart * 0.946)).rstrip('0').rstrip('.')
                milliLiter = ("%.25f" % (usQuart * 946.353)).rstrip('0').rstrip('.')
                cubicMile = ("%.25f" % (usQuart * 2.27e-13)).rstrip('0').rstrip('.')
                cubicYard = ("%.25f" % (usQuart * 0.00124)).rstrip('0').rstrip('.')
                cubicFoot = ("%.25f" % (usQuart * 0.0334)).rstrip('0').rstrip('.')
                cubicInch = ("%.25f" % (usQuart * 57.75)).rstrip('0').rstrip('.')
                usGallon = ("%.25f" % (usQuart * 0.25)).rstrip('0').rstrip('.')
                usPint = ("%.25f" % (usQuart * 2)).rstrip('0').rstrip('.')
                usCup = ("%.25f" % (usQuart * 4)).rstrip('0').rstrip('.')
                imperialGallon = ("%.25f" % (usQuart * 0.208)).rstrip('0').rstrip('.')
                imperialQuart = ("%.25f" % (usQuart * 0.833)).rstrip('0').rstrip('.')
                imperialPint = ("%.25f" % (usQuart * 1.665)).rstrip('0').rstrip('.')

                print(f'{usQuart} qt [US] = {cubicKilometer} km??')
                print(f'{usQuart} qt [US] = {cubicMeter} m??')
                print(f'{usQuart} qt [US] = {cubicCentimeter} cm??')
                print(f'{usQuart} qt [US] = {cubicMillimeter} mm??')
                print(f'{usQuart} qt [US] = {liter} l')
                print(f'{usQuart} qt [US] = {milliLiter} ml')
                print(f'{usQuart} qt [US] = {cubicMile} mi??')
                print(f'{usQuart} qt [US] = {cubicYard} yd??')
                print(f'{usQuart} qt [US] = {cubicFoot} ft??')
                print(f'{usQuart} qt [US] = {cubicInch} in??')
                print(f'{usQuart} qt [US] = {usGallon} gal [US]')
                print(f'{usQuart} qt [US] = {usPint} pt [US]')
                print(f'{usQuart} qt [US] = {usCup} cup [US]')
                print(f'{usQuart} qt [US] = {imperialGallon} gal [imp]')
                print(f'{usQuart} qt [US] = {imperialQuart} qt [imp]')
                print(f'{usQuart} qt [US] = {imperialPint} pt [imp]')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 13:

            try:
                usPint = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if usPint > 0:

                cubicKilometer = ("%.25f" % (usPint * 4.732e-13)).rstrip('0').rstrip('.')
                cubicMeter = ("%.25f" % (usPint * 0.000473)).rstrip('0').rstrip('.')
                cubicCentimeter = ("%.25f" % (usPint * 473.176)).rstrip('0').rstrip('.')
                cubicMillimeter = ("%.25f" % (usPint * 473176.25)).rstrip('0').rstrip('.')
                liter = ("%.25f" % (usPint * 0.473)).rstrip('0').rstrip('.')
                milliLiter = ("%.25f" % (usPint * 473.176)).rstrip('0').rstrip('.')
                cubicMile = ("%.25f" % (usPint * 1.135e-13)).rstrip('0').rstrip('.')
                cubicYard = ("%.25f" % (usPint * 0.000619)).rstrip('0').rstrip('.')
                cubicFoot = ("%.25f" % (usPint * 0.0167)).rstrip('0').rstrip('.')
                cubicInch = ("%.25f" % (usPint * 28.875)).rstrip('0').rstrip('.')
                usGallon = ("%.25f" % (usPint * 0.125)).rstrip('0').rstrip('.')
                usQuart = ("%.25f" % (usPint * 0.5)).rstrip('0').rstrip('.')
                usCup = ("%.25f" % (usPint * 2)).rstrip('0').rstrip('.')
                imperialGallon = ("%.25f" % (usPint * 0.104)).rstrip('0').rstrip('.')
                imperialQuart = ("%.25f" % (usPint * 0.416)).rstrip('0').rstrip('.')
                imperialPint = ("%.25f" % (usPint * 0.833)).rstrip('0').rstrip('.')

                print(f'{usPint} pt [US] = {cubicKilometer} km??')
                print(f'{usPint} pt [US] = {cubicMeter} m??')
                print(f'{usPint} pt [US] = {cubicCentimeter} cm??')
                print(f'{usPint} pt [US] = {cubicMillimeter} mm??')
                print(f'{usPint} pt [US] = {liter} l')
                print(f'{usPint} pt [US] = {milliLiter} ml')
                print(f'{usPint} pt [US] = {cubicMile} mi??')
                print(f'{usPint} pt [US] = {cubicYard} yd??')
                print(f'{usPint} pt [US] = {cubicFoot} ft??')
                print(f'{usPint} pt [US] = {cubicInch} in??')
                print(f'{usPint} pt [US] = {usGallon} gal [US]')
                print(f'{usPint} pt [US] = {usQuart} qt [US]')
                print(f'{usPint} pt [US] = {usCup} cup [US]')
                print(f'{usPint} pt [US] = {imperialGallon} gal [imp]')
                print(f'{usPint} pt [US] = {imperialQuart} qt [imp]')
                print(f'{usPint} pt [US] = {imperialPint} pt [imp]')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 14:

            try:
                usCup = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if usCup > 0:

                cubicKilometer = ("%.25f" % (usCup * 2.366e-13)).rstrip('0').rstrip('.')
                cubicMeter = ("%.25f" % (usCup * 0.000236)).rstrip('0').rstrip('.')
                cubicCentimeter = ("%.25f" % (usCup * 236.588)).rstrip('0').rstrip('.')
                cubicMillimeter = ("%.25f" % (usCup * 236588.125)).rstrip('0').rstrip('.')
                liter = ("%.25f" % (usCup * 0.236)).rstrip('0').rstrip('.')
                milliLiter = ("%.25f" % (usCup * 236.588)).rstrip('0').rstrip('.')
                cubicMile = ("%.25f" % (usCup * 5.676e-14)).rstrip('0').rstrip('.')
                cubicYard = ("%.25f" % (usCup * 0.000309)).rstrip('0').rstrip('.')
                cubicFoot = ("%.25f" % (usCup * 0.00835)).rstrip('0').rstrip('.')
                cubicInch = ("%.25f" % (usCup * 14.437)).rstrip('0').rstrip('.')
                usGallon = ("%.25f" % (usCup * 0.0625)).rstrip('0').rstrip('.')
                usQuart = ("%.25f" % (usCup * 0.25)).rstrip('0').rstrip('.')
                usPint = ("%.25f" % (usCup * 0.5)).rstrip('0').rstrip('.')
                imperialGallon = ("%.25f" % (usCup * 0.052)).rstrip('0').rstrip('.')
                imperialQuart = ("%.25f" % (usCup * 0.208)).rstrip('0').rstrip('.')
                imperialPint = ("%.25f" % (usCup * 0.416)).rstrip('0').rstrip('.')

                print(f'{usCup} cup [US] = {cubicKilometer} km??')
                print(f'{usCup} cup [US] = {cubicMeter} m??')
                print(f'{usCup} cup [US] = {cubicCentimeter} cm??')
                print(f'{usCup} cup [US] = {cubicMillimeter} mm??')
                print(f'{usCup} cup [US] = {liter} l')
                print(f'{usCup} cup [US] = {milliLiter} ml')
                print(f'{usCup} cup [US] = {cubicMile} mi??')
                print(f'{usCup} cup [US] = {cubicYard} yd??')
                print(f'{usCup} cup [US] = {cubicFoot} ft??')
                print(f'{usCup} cup [US] = {cubicInch} in??')
                print(f'{usCup} cup [US] = {usGallon} gal [US]')
                print(f'{usCup} cup [US] = {usQuart} qt [US]')
                print(f'{usCup} cup [US] = {usPint} pt [US]')
                print(f'{usCup} cup [US] = {imperialGallon} gal [imp]')
                print(f'{usCup} cup [US] = {imperialQuart} qt [imp]')
                print(f'{usCup} cup [US] = {imperialPint} pt [imp]')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 15:

            try:
                imperialGallon = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if imperialGallon > 0:

                cubicKilometer = ("%.25f" % (imperialGallon * 4.546e-12)).rstrip('0').rstrip('.')
                cubicMeter = ("%.25f" % (imperialGallon * 0.00455)).rstrip('0').rstrip('.')
                cubicCentimeter = ("%.25f" % (imperialGallon * 4546.09)).rstrip('0').rstrip('.')
                cubicMillimeter = ("%.25f" % (imperialGallon * 4546090)).rstrip('0').rstrip('.')
                liter = ("%.25f" % (imperialGallon * 4.546)).rstrip('0').rstrip('.')
                milliLiter = ("%.25f" % (imperialGallon * 4546.09)).rstrip('0').rstrip('.')
                cubicMile = ("%.25f" % (imperialGallon * 1.0907e-12)).rstrip('0').rstrip('.')
                cubicYard = ("%.25f" % (imperialGallon * 0.00595)).rstrip('0').rstrip('.')
                cubicFoot = ("%.25f" % (imperialGallon * 0.16)).rstrip('0').rstrip('.')
                cubicInch = ("%.25f" % (imperialGallon * 277.419)).rstrip('0').rstrip('.')
                usGallon = ("%.25f" % (imperialGallon * 1.201)).rstrip('0').rstrip('.')
                usQuart = ("%.25f" % (imperialGallon * 4.804)).rstrip('0').rstrip('.')
                usPint = ("%.25f" % (imperialGallon * 9.608)).rstrip('0').rstrip('.')
                usCup = ("%.25f" % (imperialGallon * 19.215)).rstrip('0').rstrip('.')
                imperialQuart = ("%.25f" % (imperialGallon * 4)).rstrip('0').rstrip('.')
                imperialPint = ("%.25f" % (imperialGallon * 8)).rstrip('0').rstrip('.')

                print(f'{imperialGallon} gal [imp] = {cubicKilometer} km??')
                print(f'{imperialGallon} gal [imp] = {cubicMeter} m??')
                print(f'{imperialGallon} gal [imp] = {cubicCentimeter} cm??')
                print(f'{imperialGallon} gal [imp] = {cubicMillimeter} mm??')
                print(f'{imperialGallon} gal [imp] = {liter} l')
                print(f'{imperialGallon} gal [imp] = {milliLiter} ml')
                print(f'{imperialGallon} gal [imp] = {cubicMile} mi??')
                print(f'{imperialGallon} gal [imp] = {cubicYard} yd??')
                print(f'{imperialGallon} gal [imp] = {cubicFoot} ft??')
                print(f'{imperialGallon} gal [imp] = {cubicInch} in??')
                print(f'{imperialGallon} gal [imp] = {usGallon} gal [US]')
                print(f'{imperialGallon} gal [imp] = {usQuart} qt [US]')
                print(f'{imperialGallon} gal [imp] = {usPint} pt [US]')
                print(f'{imperialGallon} gal [imp] = {usCup} cup [US]')
                print(f'{imperialGallon} gal [imp] = {imperialQuart} qt [imp]')
                print(f'{imperialGallon} gal [imp] = {imperialPint} pt [imp]')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 16:

            try:
                imperialQuart = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if imperialQuart > 0:

                cubicKilometer = ("%.25f" % (imperialQuart * 1.136e-12)).rstrip('0').rstrip('.')
                cubicMeter = ("%.25f" % (imperialQuart * 0.00114)).rstrip('0').rstrip('.')
                cubicCentimeter = ("%.25f" % (imperialQuart * 1136.522)).rstrip('0').rstrip('.')
                cubicMillimeter = ("%.25f" % (imperialQuart * 1136522.5)).rstrip('0').rstrip('.')
                liter = ("%.25f" % (imperialQuart * 1.136)).rstrip('0').rstrip('.')
                milliLiter = ("%.25f" % (imperialQuart * 1136.522)).rstrip('0').rstrip('.')
                cubicMile = ("%.25f" % (imperialQuart * 2.727e-13)).rstrip('0').rstrip('.')
                cubicYard = ("%.25f" % (imperialQuart * 0.00147)).rstrip('0').rstrip('.')
                cubicFoot = ("%.25f" % (imperialQuart * 0.0401)).rstrip('0').rstrip('.')
                cubicInch = ("%.25f" % (imperialQuart * 69.355)).rstrip('0').rstrip('.')
                usGallon = ("%.25f" % (imperialQuart * 0.3)).rstrip('0').rstrip('.')
                usQuart = ("%.25f" % (imperialQuart * 1.201)).rstrip('0').rstrip('.')
                usPint = ("%.25f" % (imperialQuart * 2.402)).rstrip('0').rstrip('.')
                usCup = ("%.25f" % (imperialQuart * 4.804)).rstrip('0').rstrip('.')
                imperialGallon = ("%.25f" % (imperialQuart * 0.25)).rstrip('0').rstrip('.')
                imperialPint = ("%.25f" % (imperialQuart * 2)).rstrip('0').rstrip('.')

                print(f'{imperialQuart} qt [imp] = {cubicKilometer} km??')
                print(f'{imperialQuart} qt [imp] = {cubicMeter} m??')
                print(f'{imperialQuart} qt [imp] = {cubicCentimeter} cm??')
                print(f'{imperialQuart} qt [imp] = {cubicMillimeter} mm??')
                print(f'{imperialQuart} qt [imp] = {liter} l')
                print(f'{imperialQuart} qt [imp] = {milliLiter} ml')
                print(f'{imperialQuart} qt [imp] = {cubicMile} mi??')
                print(f'{imperialQuart} qt [imp] = {cubicYard} yd??')
                print(f'{imperialQuart} qt [imp] = {cubicFoot} ft??')
                print(f'{imperialQuart} qt [imp] = {cubicInch} in??')
                print(f'{imperialQuart} qt [imp] = {usGallon} gal [US]')
                print(f'{imperialQuart} qt [imp] = {usQuart} qt [US]')
                print(f'{imperialQuart} qt [imp] = {usPint} pt [US]')
                print(f'{imperialQuart} qt [imp] = {usCup} cup [US]')
                print(f'{imperialQuart} qt [imp] = {imperialGallon} gal [imp]')
                print(f'{imperialQuart} qt [imp] = {imperialPint} pt [imp]')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 17:

            try:
                imperialPint = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if imperialPint > 0:

                cubicKilometer = ("%.25f" % (imperialPint * 5.683e-13)).rstrip('0').rstrip('.')
                cubicMeter = ("%.25f" % (imperialPint * 0.000568)).rstrip('0').rstrip('.')
                cubicCentimeter = ("%.25f" % (imperialPint * 568.261)).rstrip('0').rstrip('.')
                cubicMillimeter = ("%.25f" % (imperialPint * 568261.25)).rstrip('0').rstrip('.')
                liter = ("%.25f" % (imperialPint * 0.568)).rstrip('0').rstrip('.')
                milliLiter = ("%.25f" % (imperialPint * 568.261)).rstrip('0').rstrip('.')
                cubicMile = ("%.25f" % (imperialPint * 1.363e-13)).rstrip('0').rstrip('.')
                cubicYard = ("%.25f" % (imperialPint * 0.000743)).rstrip('0').rstrip('.')
                cubicFoot = ("%.25f" % (imperialPint * 0.0201)).rstrip('0').rstrip('.')
                cubicInch = ("%.25f" % (imperialPint * 34.677)).rstrip('0').rstrip('.')
                usGallon = ("%.25f" % (imperialPint * 0.15)).rstrip('0').rstrip('.')
                usQuart = ("%.25f" % (imperialPint * 0.6)).rstrip('0').rstrip('.')
                usPint = ("%.25f" % (imperialPint * 1.201)).rstrip('0').rstrip('.')
                usCup = ("%.25f" % (imperialPint * 2.402)).rstrip('0').rstrip('.')
                imperialGallon = ("%.25f" % (imperialPint * 0.125)).rstrip('0').rstrip('.')
                imperialQuart = ("%.25f" % (imperialPint * 0.5)).rstrip('0').rstrip('.')

                print(f'{imperialPint} pt [imp] = {cubicKilometer} km??')
                print(f'{imperialPint} pt [imp] = {cubicMeter} m??')
                print(f'{imperialPint} pt [imp] = {cubicCentimeter} cm??')
                print(f'{imperialPint} pt [imp] = {cubicMillimeter} mm??')
                print(f'{imperialPint} pt [imp] = {liter} l')
                print(f'{imperialPint} pt [imp] = {milliLiter} ml')
                print(f'{imperialPint} pt [imp] = {cubicMile} mi??')
                print(f'{imperialPint} pt [imp] = {cubicYard} yd??')
                print(f'{imperialPint} pt [imp] = {cubicFoot} ft??')
                print(f'{imperialPint} pt [imp] = {cubicInch} in??')
                print(f'{imperialPint} pt [imp] = {usGallon} gal [US]')
                print(f'{imperialPint} pt [imp] = {usQuart} qt [US]')
                print(f'{imperialPint} pt [imp] = {usPint} pt [US]')
                print(f'{imperialPint} pt [imp] = {usCup} cup [US]')
                print(f'{imperialPint} pt [imp] = {imperialGallon} gal [imp]')
                print(f'{imperialPint} pt [imp] = {imperialQuart} qt [imp]')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        else:
            print('# Enter value from 1 to 17 #')
            print()

    elif menuChoice == 5:
        print('Choose unit type:')
        print('[1] Kilogram' + '      ' + '[6] Short Ton')
        print('[2] Gram' + '          ' + '[7] Pound')
        print('[3] Milligram' + '     ' + '[8] Ounce')
        print('[4] Metric Ton' + '    ' + '[9] Carat')
        print('[5] Long Ton')
        print()

        try:
            subMenuChoice = int(input('Enter your choice: '))
            print()
        except ValueError:
            print()
            print('# Enter value from 1 to 10 #')
            print()
            continue

        if subMenuChoice == 1:

            try:
                kilogram = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if kilogram > 0:

                gram = ("%.25f" % (kilogram * 1000)).rstrip('0').rstrip('.')
                milligram = ("%.25f" % (kilogram * 1000000)).rstrip('0').rstrip('.')
                metricTon = ("%.25f" % (kilogram * 0.001)).rstrip('0').rstrip('.')
                longTon = ("%.25f" % (kilogram * 0.000984)).rstrip('0').rstrip('.')
                shortTon = ("%.25f" % (kilogram * 0.0011)).rstrip('0').rstrip('.')
                pound = ("%.25f" % (kilogram * 2.205)).rstrip('0').rstrip('.')
                ounce = ("%.25f" % (kilogram * 35.274)).rstrip('0').rstrip('.')
                carat = ("%.25f" % (kilogram * 5000)).rstrip('0').rstrip('.')

                print(f'{kilogram} kg = {gram} g')
                print(f'{kilogram} kg = {milligram} mg')
                print(f'{kilogram} kg = {metricTon} t')
                print(f'{kilogram} kg = {longTon} t [long]')
                print(f'{kilogram} kg = {shortTon} t [short]')
                print(f'{kilogram} kg = {pound} lb')
                print(f'{kilogram} kg = {ounce} oz')
                print(f'{kilogram} kg = {carat} ct')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 2:

            try:
                gram = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if gram > 0:

                kiloGram = ("%.25f" % (gram * 0.001)).rstrip('0').rstrip('.')
                milligram = ("%.25f" % (gram * 1000)).rstrip('0').rstrip('.')
                metricTon = ("%.25f" % (gram * 0.000001)).rstrip('0').rstrip('.')
                longTon = ("%.25f" % (gram * 9.842e-7)).rstrip('0').rstrip('.')
                shortTon = ("%.25f" % (gram * 0.0000011)).rstrip('0').rstrip('.')
                pound = ("%.25f" % (gram * 0.0022)).rstrip('0').rstrip('.')
                ounce = ("%.25f" % (gram * 0.0353)).rstrip('0').rstrip('.')
                carat = ("%.25f" % (gram * 5)).rstrip('0').rstrip('.')

                print(f'{gram} g = {kiloGram} kg')
                print(f'{gram} g = {milligram} mg')
                print(f'{gram} g = {metricTon} t')
                print(f'{gram} g = {longTon} t [long]')
                print(f'{gram} g = {shortTon} t [short]')
                print(f'{gram} g = {pound} lb')
                print(f'{gram} g = {ounce} oz')
                print(f'{gram} g = {carat} ct')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 3:

            try:
                milliGram = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if milliGram > 0:

                kiloGram = ("%.25f" % (milliGram * 0.000001)).rstrip('0').rstrip('.')
                gram = ("%.25f" % (milliGram * 0.001)).rstrip('0').rstrip('.')
                metricTon = ("%.25f" % (milliGram * 1e-9)).rstrip('0').rstrip('.')
                longTon = ("%.25f" % (milliGram * 9.842e-10)).rstrip('0').rstrip('.')
                shortTon = ("%.25f" % (milliGram * 1.102e-9)).rstrip('0').rstrip('.')
                pound = ("%.25f" % (milliGram * 0.0000022)).rstrip('0').rstrip('.')
                ounce = ("%.25f" % (milliGram * 0.0000353)).rstrip('0').rstrip('.')
                carat = ("%.25f" % (milliGram * 0.005)).rstrip('0').rstrip('.')

                print(f'{milliGram} mg = {kiloGram} kg')
                print(f'{milliGram} mg = {gram} g')
                print(f'{milliGram} mg = {metricTon} t')
                print(f'{milliGram} mg = {longTon} t [long]')
                print(f'{milliGram} mg = {shortTon} t [short]')
                print(f'{milliGram} mg = {pound} lb')
                print(f'{milliGram} mg = {ounce} oz')
                print(f'{milliGram} mg = {carat} ct')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 4:

            try:
                metricTon = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if metricTon > 0:

                kiloGram = ("%.25f" % (metricTon * 1000)).rstrip('0').rstrip('.')
                gram = ("%.25f" % (metricTon * 1000000)).rstrip('0').rstrip('.')
                milliGram = ("%.25f" % (metricTon * 1000000000)).rstrip('0').rstrip('.')
                longTon = ("%.25f" % (metricTon * 0.984)).rstrip('0').rstrip('.')
                shortTon = ("%.25f" % (metricTon * 1.102)).rstrip('0').rstrip('.')
                pound = ("%.25f" % (metricTon * 2204.624)).rstrip('0').rstrip('.')
                ounce = ("%.25f" % (metricTon * 35273.991)).rstrip('0').rstrip('.')
                carat = ("%.25f" % (metricTon * 5000000)).rstrip('0').rstrip('.')

                print(f'{metricTon} t = {kiloGram} kg')
                print(f'{metricTon} t = {gram} g')
                print(f'{metricTon} t = {milliGram} mg')
                print(f'{metricTon} t = {longTon} t [long]')
                print(f'{metricTon} t = {shortTon} t [short]')
                print(f'{metricTon} t = {pound} lb')
                print(f'{metricTon} t = {ounce} oz')
                print(f'{metricTon} t = {carat} ct')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 5:

            try:
                longTon = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if longTon > 0:

                kiloGram = ("%.25f" % (longTon * 1016.0461)).rstrip('0').rstrip('.')
                gram = ("%.25f" % (longTon * 1016046.08)).rstrip('0').rstrip('.')
                milliGram = ("%.25f" % (longTon * 1016046080)).rstrip('0').rstrip('.')
                metricTon = ("%.25f" % (longTon * 1.016)).rstrip('0').rstrip('.')
                shortTon = ("%.25f" % (longTon * 1.12)).rstrip('0').rstrip('.')
                pound = ("%.25f" % (longTon * 2240)).rstrip('0').rstrip('.')
                ounce = ("%.25f" % (longTon * 35840)).rstrip('0').rstrip('.')
                carat = ("%.25f" % (longTon * 5080230.4)).rstrip('0').rstrip('.')

                print(f'{longTon} t [long] = {kiloGram} kg')
                print(f'{longTon} t [long] = {gram} g')
                print(f'{longTon} t [long] = {milliGram} mg')
                print(f'{longTon} t [long] = {metricTon} t')
                print(f'{longTon} t [long] = {shortTon} t [short]')
                print(f'{longTon} t [long] = {pound} lb')
                print(f'{longTon} t [long] = {ounce} oz')
                print(f'{longTon} t [long] = {carat} ct')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 6:

            try:
                shortTon = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if shortTon > 0:

                kiloGram = ("%.25f" % (shortTon * 907.184)).rstrip('0').rstrip('.')
                gram = ("%.25f" % (shortTon * 907184)).rstrip('0').rstrip('.')
                milliGram = ("%.25f" % (shortTon * 907184000)).rstrip('0').rstrip('.')
                metricTon = ("%.25f" % (shortTon * 0.907)).rstrip('0').rstrip('.')
                longTon = ("%.25f" % (shortTon * 0.893)).rstrip('0').rstrip('.')
                pound = ("%.25f" % (shortTon * 2000)).rstrip('0').rstrip('.')
                ounce = ("%.25f" % (shortTon * 32000)).rstrip('0').rstrip('.')
                carat = ("%.25f" % (shortTon * 4535920)).rstrip('0').rstrip('.')

                print(f'{shortTon} t [short] = {kiloGram} kg')
                print(f'{shortTon} t [short] = {gram} g')
                print(f'{shortTon} t [short] = {milliGram} mg')
                print(f'{shortTon} t [short] = {metricTon} t')
                print(f'{shortTon} t [short] = {longTon} t [long]')
                print(f'{shortTon} t [short] = {pound} lb')
                print(f'{shortTon} t [short] = {ounce} oz')
                print(f'{shortTon} t [short] = {carat} ct')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 7:

            try:
                pound = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if pound > 0:

                kiloGram = ("%.25f" % (pound * 0.453)).rstrip('0').rstrip('.')
                gram = ("%.25f" % (pound * 453.592)).rstrip('0').rstrip('.')
                milliGram = ("%.25f" % (pound * 453592)).rstrip('0').rstrip('.')
                metricTon = ("%.25f" % (pound * 0.000453)).rstrip('0').rstrip('.')
                longTon = ("%.25f" % (pound * 0.000446)).rstrip('0').rstrip('.')
                shortTon = ("%.25f" % (pound * 0.0005)).rstrip('0').rstrip('.')
                ounce = ("%.25f" % (pound * 16)).rstrip('0').rstrip('.')
                carat = ("%.25f" % (pound * 2267.96)).rstrip('0').rstrip('.')

                print(f'{pound} lb = {kiloGram} kg')
                print(f'{pound} lb = {gram} g')
                print(f'{pound} lb = {milliGram} mg')
                print(f'{pound} lb = {metricTon} t')
                print(f'{pound} lb = {longTon} t [long]')
                print(f'{pound} lb = {shortTon} t [short]')
                print(f'{pound} lb = {ounce} oz')
                print(f'{pound} lb = {carat} ct')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 8:

            try:
                ounce = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if ounce > 0:

                kiloGram = ("%.25f" % (ounce * 0.0283)).rstrip('0').rstrip('.')
                gram = ("%.25f" % (ounce * 28.349)).rstrip('0').rstrip('.')
                milliGram = ("%.25f" % (ounce * 28349.5)).rstrip('0').rstrip('.')
                metricTon = ("%.25f" % (ounce * 0.0000283)).rstrip('0').rstrip('.')
                longTon = ("%.25f" % (ounce * 0.0000279)).rstrip('0').rstrip('.')
                shortTon = ("%.25f" % (ounce * 0.0000312)).rstrip('0').rstrip('.')
                pound = ("%.25f" % (ounce * 0.0625)).rstrip('0').rstrip('.')
                carat = ("%.25f" % (ounce * 141.747)).rstrip('0').rstrip('.')

                print(f'{ounce} oz = {kiloGram} kg')
                print(f'{ounce} oz = {gram} g')
                print(f'{ounce} oz = {milliGram} mg')
                print(f'{ounce} oz = {metricTon} t')
                print(f'{ounce} oz = {longTon} t [long]')
                print(f'{ounce} oz = {shortTon} t [short]')
                print(f'{ounce} oz = {pound} lb')
                print(f'{ounce} oz = {carat} ct')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 9:

            try:
                carat = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if carat > 0:

                kiloGram = ("%.25f" % (carat * 0.0002)).rstrip('0').rstrip('.')
                gram = ("%.25f" % (carat * 0.2)).rstrip('0').rstrip('.')
                milliGram = ("%.25f" % (carat * 200)).rstrip('0').rstrip('.')
                metricTon = ("%.25f" % (carat * 2e-7)).rstrip('0').rstrip('.')
                longTon = ("%.25f" % (carat * 1.968e-7)).rstrip('0').rstrip('.')
                shortTon = ("%.25f" % (carat * 2.205e-7)).rstrip('0').rstrip('.')
                pound = ("%.25f" % (carat * 0.000441)).rstrip('0').rstrip('.')
                ounce = ("%.25f" % (carat * 0.00705)).rstrip('0').rstrip('.')

                print(f'{carat} ct = {kiloGram} kg')
                print(f'{carat} ct = {gram} g')
                print(f'{carat} ct = {milliGram} mg')
                print(f'{carat} ct = {metricTon} t')
                print(f'{carat} ct = {longTon} t [long]')
                print(f'{carat} ct = {shortTon} t [short]')
                print(f'{carat} ct = {pound} lb')
                print(f'{carat} ct = {ounce} oz')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        else:
            print('# Enter value from 1 to 9 #')
            print()

    elif menuChoice == 6:
        print('Choose unit type:')
        print('[1] Year' + '        ' + '[5] Hour')
        print('[2] Month' + '       ' + '[6] Minute')
        print('[3] Week' + '        ' + '[7] Second')
        print('[4] Day' + '         ' + '[8] Millisecond')
        print()

        try:
            subMenuChoice = int(input('Enter your choice: '))
            print()
        except ValueError:
            print()
            print('# Enter value from 1 to 8 #')
            print()
            continue

        if subMenuChoice == 1:

            try:
                year = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if year > 0:

                month = ("%.25f" % (year * 12)).rstrip('0').rstrip('.')
                week = ("%.25f" % (year * 52.177)).rstrip('0').rstrip('.')
                day = ("%.25f" % (year * 365.242)).rstrip('0').rstrip('.')
                hour = ("%.25f" % (year * 8765.813)).rstrip('0').rstrip('.')
                minute = ("%.25f" % (year * 525948.767)).rstrip('0').rstrip('.')
                second = ("%.25f" % (year * 31556926)).rstrip('0').rstrip('.')
                millisecond = ("%.25f" % (year * 31556926000)).rstrip('0').rstrip('.')

                print(f'{year} year(s) = {month} month(s)')
                print(f'{year} year(s) = {week} week(s)')
                print(f'{year} year(s) = {day} day(s)')
                print(f'{year} year(s) = {hour} hour(s)')
                print(f'{year} year(s) = {minute} minute(s)')
                print(f'{year} year(s) = {second} second(s)')
                print(f'{year} year(s) = {millisecond} millisecond(s)')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 2:

            try:
                month = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if month > 0:

                year = ("%.25f" % (month * 0.0833)).rstrip('0').rstrip('.')
                week = ("%.25f" % (month * 4.348)).rstrip('0').rstrip('.')
                day = ("%.25f" % (month * 30.437)).rstrip('0').rstrip('.')
                hour = ("%.25f" % (month * 730.484)).rstrip('0').rstrip('.')
                minute = ("%.25f" % (month * 43829.0639)).rstrip('0').rstrip('.')
                second = ("%.25f" % (month * 2629743.833)).rstrip('0').rstrip('.')
                millisecond = ("%.25f" % (month * 2629743833.333)).rstrip('0').rstrip('.')

                print(f'{month} month(s) = {year} year(s)')
                print(f'{month} month(s) = {week} week(s)')
                print(f'{month} month(s) = {day} day(s)')
                print(f'{month} month(s) = {hour} hour(s)')
                print(f'{month} month(s) = {minute} minute(s)')
                print(f'{month} month(s) = {second} second(s)')
                print(f'{month} month(s) = {millisecond} millisecond(s)')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 3:

            try:
                week = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if week > 0:

                year = ("%.25f" % (week * 0.0192)).rstrip('0').rstrip('.')
                month = ("%.25f" % (week * 0.23)).rstrip('0').rstrip('.')
                day = ("%.25f" % (week * 7)).rstrip('0').rstrip('.')
                hour = ("%.25f" % (week * 168)).rstrip('0').rstrip('.')
                minute = ("%.25f" % (week * 10080)).rstrip('0').rstrip('.')
                second = ("%.25f" % (week * 604800)).rstrip('0').rstrip('.')
                millisecond = ("%.25f" % (week * 604800000)).rstrip('0').rstrip('.')

                print(f'{week} week(s) = {year} year(s)')
                print(f'{week} week(s) = {month} month(s)')
                print(f'{week} week(s) = {day} day(s)')
                print(f'{week} week(s) = {hour} hour(s)')
                print(f'{week} week(s) = {minute} minute(s)')
                print(f'{week} week(s) = {second} second(s)')
                print(f'{week} week(s) = {millisecond} millisecond(s)')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 4:

            try:
                day = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if day > 0:

                year = ("%.25f" % (day * 0.00274)).rstrip('0').rstrip('.')
                month = ("%.25f" % (day * 0.0328)).rstrip('0').rstrip('.')
                week = ("%.25f" % (day * 0.143)).rstrip('0').rstrip('.')
                hour = ("%.25f" % (day * 24)).rstrip('0').rstrip('.')
                minute = ("%.25f" % (day * 1440)).rstrip('0').rstrip('.')
                second = ("%.25f" % (day * 86400)).rstrip('0').rstrip('.')
                millisecond = ("%.25f" % (day * 86400000)).rstrip('0').rstrip('.')

                print(f'{day} day(s) = {year} year(s)')
                print(f'{day} day(s) = {month} month(s)')
                print(f'{day} day(s) = {week} week(s)')
                print(f'{day} day(s) = {hour} hour(s)')
                print(f'{day} day(s) = {minute} minute(s)')
                print(f'{day} day(s) = {second} second(s)')
                print(f'{day} day(s) = {millisecond} millisecond(s)')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 5:

            try:
                hour = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if hour > 0:

                year = ("%.25f" % (hour * 0.000114)).rstrip('0').rstrip('.')
                month = ("%.25f" % (hour * 0.00137)).rstrip('0').rstrip('.')
                week = ("%.25f" % (hour * 0.00595)).rstrip('0').rstrip('.')
                day = ("%.25f" % (hour * 0.0417)).rstrip('0').rstrip('.')
                minute = ("%.25f" % (hour * 60)).rstrip('0').rstrip('.')
                second = ("%.25f" % (hour * 3600)).rstrip('0').rstrip('.')
                millisecond = ("%.25f" % (hour * 3600000)).rstrip('0').rstrip('.')

                print(f'{hour} hour(s) = {year} year(s)')
                print(f'{hour} hour(s) = {month} month(s)')
                print(f'{hour} hour(s) = {week} week(s)')
                print(f'{hour} hour(s) = {day} day(s)')
                print(f'{hour} hour(s) = {minute} minute(s)')
                print(f'{hour} hour(s) = {second} second(s)')
                print(f'{hour} hour(s) = {millisecond} millisecond(s)')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 6:

            try:
                minute = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if minute > 0:

                year = ("%.25f" % (minute * 1.901e-6)).rstrip('0').rstrip('.')
                month = ("%.25f" % (minute * 2.281e-5)).rstrip('0').rstrip('.')
                week = ("%.25f" % (minute * 9.921e-5)).rstrip('0').rstrip('.')
                day = ("%.25f" % (minute * 0.000694)).rstrip('0').rstrip('.')
                hour = ("%.25f" % (minute * 0.0167)).rstrip('0').rstrip('.')
                second = ("%.25f" % (minute * 60)).rstrip('0').rstrip('.')
                millisecond = ("%.25f" % (minute * 60000)).rstrip('0').rstrip('.')

                print(f'{minute} minute(s) = {year} year(s)')
                print(f'{minute} minute(s) = {month} month(s)')
                print(f'{minute} minute(s) = {week} week(s)')
                print(f'{minute} minute(s) = {day} day(s)')
                print(f'{minute} minute(s) = {hour} hour(s)')
                print(f'{minute} minute(s) = {second} second(s)')
                print(f'{minute} minute(s) = {millisecond} millisecond(s)')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 7:

            try:
                second = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if second > 0:

                year = ("%.25f" % (second * 3.169e-8)).rstrip('0').rstrip('.')
                month = ("%.25f" % (second * 3.803e-7)).rstrip('0').rstrip('.')
                week = ("%.25f" % (second * 1.653e-6)).rstrip('0').rstrip('.')
                day = ("%.25f" % (second * 1.157e-5)).rstrip('0').rstrip('.')
                hour = ("%.25f" % (second * 0.000278)).rstrip('0').rstrip('.')
                minute = ("%.25f" % (second * 0.0167)).rstrip('0').rstrip('.')
                millisecond = ("%.25f" % (second * 1000)).rstrip('0').rstrip('.')

                print(f'{second} second(s) = {year} year(s)')
                print(f'{second} second(s) = {month} month(s)')
                print(f'{second} second(s) = {week} week(s)')
                print(f'{second} second(s) = {day} day(s)')
                print(f'{second} second(s) = {hour} hour(s)')
                print(f'{second} second(s) = {minute} minute(s)')
                print(f'{second} second(s) = {millisecond} millisecond(s)')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        elif subMenuChoice == 8:

            try:
                milliSecond = float(input('Enter value to convert: '))
                print()
            except ValueError:
                print()
                print('# Enter numbers only #')
                print()
                continue

            if milliSecond > 0:

                year = ("%.25f" % (milliSecond * 3.169e-11)).rstrip('0').rstrip('.')
                month = ("%.25f" % (milliSecond * 3.803e-10)).rstrip('0').rstrip('.')
                week = ("%.25f" % (milliSecond * 1.653e-9)).rstrip('0').rstrip('.')
                day = ("%.25f" % (milliSecond * 1.157e-8)).rstrip('0').rstrip('.')
                hour = ("%.25f" % (milliSecond * 2.778e-7)).rstrip('0').rstrip('.')
                minute = ("%.25f" % (milliSecond * 1.667e-5)).rstrip('0').rstrip('.')
                second = ("%.25f" % (milliSecond * 0.001)).rstrip('0').rstrip('.')

                print(f'{milliSecond} millisecond(s) = {year} year(s)')
                print(f'{milliSecond} millisecond(s) = {month} month(s)')
                print(f'{milliSecond} millisecond(s) = {week} week(s)')
                print(f'{milliSecond} millisecond(s) = {day} day(s)')
                print(f'{milliSecond} millisecond(s) = {hour} hour(s)')
                print(f'{milliSecond} millisecond(s) = {minute} minute(s)')
                print(f'{milliSecond} millisecond(s) = {second} second(s)')
                print()

            else:
                print('# Enter value bigger than 0 #')
                print()

        else:
            print('# Enter value from 1 to 8 #')
            print()

    else:
        print('# Enter value from 1 to 6 #')
        print()