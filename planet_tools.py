# python module

# Transfer bring get_planet_mass_from_dictionary
''' this is a docstring'''
import numpy as np

def get_planet_mass_from_dictionary(planet, dictionary_of_radii, average_planet_density) :
  ''' Here is the docstring for this function that describes what it does.
  This uses a dictionary of radii whose keys are planet names to calculate a mass estimate of a planet.  
  '''
  radius_of_planet = dictionary_of_radii[planet]
  mass = 4./3 *np.pi*radius_of_planet**3 * average_planet_density 
  return mass

planet_radii_km = {'mercury':2439, 'earth':6387, 'jupiter':71492} # km
average_density = 5.52e12 # kg/km^3 

#planet=input("Enter planet name: ")
print(get_planet_mass_from_dictionary(planet,planet_radii_km,average_density))
