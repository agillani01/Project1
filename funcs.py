from math import *

def poundsToKG(pounds):
   pass
   float(pounds)
   kilos = pounds*0.453592
   return kilos

# letter will be a one character string, for example: 't'
def getMassObject(letter):
   pass
   if (letter=='t'):
      return 0.1
   elif (letter=='p'):
      return 1.0
   elif (letter=='r'):
      return 3.0
   elif (letter=='g'):
      return 5.3
   elif (letter=='l'):
      return 9.07
   return 0.0

def getVelocityObject(distance):
   pass
   velocityObject = sqrt((9.8*distance)/2)
   return velocityObject

def getVelocitySkater(massSkater, massObject, velObject):
   pass
   velocitySkater = (massObject*velObject)/massSkater
   return velocitySkater