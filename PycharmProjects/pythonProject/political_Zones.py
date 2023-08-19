from enum import Enum
import re


class Zones():
        NORTH_CENTRAL = "Benue", "Kogi", "Kwara", "Nasarawa", "Niger", "Plateau", "Abuja"
        NORTH_EAST = "Adamawa", "Bauch", "Bornu", "Gombe", "Taraba", "Yobe"
        NORTH_WEST = "Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi", "Sokoto", "Zamfara"
        SOUTH_EAST = "Abia", "Anambra", "Ebonyi", "Enugu", "Imo",
        SOUTH_SOUTH = "Akwa Ibom", "Bayelsa", "Cross River", "Delta", "Edo", "Rivers"
        SOUTH_WEST = "Ekiti", "Lagos", "Ogun", "Ondo", "Osun", "Oyo"


def geo_zone():
    while True:
        try:
            zone = input("Enter state: ")
            if not re.match(r"^(?!$)\D+$", zone):
                print("Not a state. Please enter again.")
                geo_zone()

            if zone.capitalize() in Zones.NORTH_CENTRAL:
                print("The state belongs to NORTH CENTRAL geopolitical zone")
            if zone.capitalize() in Zones.NORTH_WEST:
                print("The state belongs to NORTH WEST geopolitical zone" )

            if zone.capitalize() in Zones.NORTH_EAST:
                print("The state belongs to NORTH EAST geopolitical zone")

            if zone.capitalize() in Zones.SOUTH_EAST:
                print("The state belongs to SOUTH EAST geopolitical zone")

            if zone.capitalize() in Zones.SOUTH_WEST:
                print("The state belongs to SOUTH WEST geopolitical zone")

            if zone.capitalize() in Zones.SOUTH_SOUTH:
                print("The state belongs to SOUTH SOUTH geopolitical zone")

        except(SyntaxError, KeyboardInterrupt):
            print("Please enter correct input")
        break


Zones()


geo_zone()