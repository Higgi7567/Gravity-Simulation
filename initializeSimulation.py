### This function will read in all user data and initialize objects.
### It should return a dictionary object.

# imports
import random
import myMath

# test_user inputs
test_population = 10     # number of object to spawn 
test_massMu = 10      # mean mass in unit(kg)
test_massSigma = 3      # standard deviation of mass in unt(kg)
test_velocityMu = 10       # mean velocity in unit(m/s)
test_velocitySigma = 1      # standard deviation of velocity in unit(m/s)
test_simSize = 1000     # length of x, y, z axis of simulation in unit(m)


def initSim(population, massMu, massSigma, velocityMu, velocitySigma, simSize):

    initData = {}
    pi = 3.1415
    density = 2  # 2 kg/m^2

    for obj in range(population):

        mass = random.normalvariate(massMu, massSigma)

        velocityX = '{:.6f}'.format(random.normalvariate(velocityMu, velocitySigma))
        velocityY = '{:.6f}'.format(random.normalvariate(velocityMu, velocitySigma))
        velocityZ = '{:.6f}'.format(random.normalvariate(velocityMu, velocitySigma))

        velocity = [velocityX, velocityY, velocityZ]

        positionX = random.randint(-0.5 * simSize, 0.5 * simSize)
        positionY = random.randint(-0.5 * simSize, 0.5 * simSize)
        positionZ = random.randint(-0.5 * simSize, 0.5 * simSize)

        position = [positionX, positionY, positionZ]

        radius = str(myMath.round((0.75 * mass * density / pi) ** (1/3)))

        object = {"mass" : str(mass),
                  "velocity" : velocity,
                  "position" : position,
                  "radius" : radius}
        
        initData[obj] = object

    return initData

myTest = initSim(test_population, test_massMu, test_massSigma, test_velocityMu, test_velocitySigma, test_simSize)
print(myTest)