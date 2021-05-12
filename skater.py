from math import *
import funcs
# Project 1
#
# Name: Al Gillani
# Instructor: Workman
# Section: 03
#

def main():
   pass

   weight = float(input("How much do you weigh (pounds)? "))
   skaterMass = funcs.poundsToKG(weight)
   profDistance = int(input("How far away is your professor (meters)? "))
   objectThrown = input("Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? ")
   objectMass = funcs.getMassObject(objectThrown)
   objectVelocity = funcs.getVelocityObject(profDistance)
   skaterVelocity = round(funcs.getVelocitySkater(skaterMass, objectMass, objectVelocity), 3)
   
   if (objectMass<=0.1):
      print("\nNice throw! You're going to get an F!")
   elif (objectMass>0.1 and objectMass<=1.0):
      print("\nNice throw! Make sure your professor is OK.")
   else: 
      if (profDistance<20):
         print("\nNice throw! How far away is the hospital?")
      else:
         print("\nNice throw! RIP professor.")
   if (skaterVelocity==0):
      print ("Velocity of skater: 0.000 m/s")
   else:
      print("Velocity of skater: " + str(skaterVelocity) + " m/s")
   if (skaterVelocity<0.2):
      print("My grandmother skates faster than you!")
   elif (skaterVelocity>=1.0):
      print("Look out for that railing!!!")


if __name__ == '__main__':
   main()