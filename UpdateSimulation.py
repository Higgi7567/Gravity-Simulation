### This function reads in data from temporary database and updates it to next time-step

# imports
import myMath

testData = {0 : {"mass" : "10",
          "velocity" : ["5","2","-6"],
          "position" : ["-20","5","14"],
          "radius" : "2"},
          1 : {"mass" : "10",
          "velocity" : ["2","-3","4"],
          "position" : ["10","0","13"],
          "radius" : "2"},}

def update(data, timeStep):

    gConstant = 6.67430 * (10 ** (-11))

    for objMain in range(len(data)):

        posXmain, posYmain, posZmain = data[objMain]['position']
        velXmain, velYmain, velZmain = data[objMain]['velocity']

        posXmain = float(posXmain)
        posYmain = float(posYmain)
        posZmain = float(posZmain)

        velXmain = float(velXmain)
        velYmain = float(velYmain)
        velZmain = float(velZmain)
        
        netAcceleration = [0,0,0]

        for objSub in range(len(data)):

            if objMain != objSub:

                massSub = data[objSub]['mass']
                posXsub, posYsub, posZsub = data[objSub]["position"]

                posXsub = float(posXsub)
                posYsub = float(posYsub)
                posZsub = float(posZsub)

                # calculate distance between objMain and objSub

                xDistance = posXsub - posXmain
                yDistance = posYsub - posYmain
                zDistance = posZsub - posZmain

                distMagnitude = (xDistance ** 2 + yDistance ** 2 + zDistance ** 2) ** 0.5

                # calculate acceleration magnitude

                accelMagnitude = (gConstant * float(massSub)) / (distMagnitude ** 2)

                # calculate unit vectors and magnify for acceleration

                accelX = (xDistance / distMagnitude) * accelMagnitude
                accelY = (yDistance / distMagnitude) * accelMagnitude
                accelZ = (zDistance / distMagnitude) * accelMagnitude

                # add acceleration vector to netAcceleration

                netAcceleration[0] += accelX
                netAcceleration[1] += accelY
                netAcceleration[2] += accelZ

        # calculate new positions and velocities and formats them to database structure
            
        posXnew = '{:.6f}'.format((posXmain + (velXmain * timeStep) + (0.5 * netAcceleration[0] * (timeStep ** 2))))
        posYnew = '{:.6f}'.format((posYmain + (velYmain * timeStep) + (0.5 * netAcceleration[1] * (timeStep ** 2))))
        posZnew = '{:.6f}'.format((posZmain + (velZmain * timeStep) + (0.5 * netAcceleration[2] * (timeStep ** 2))))

        newPosition = [posXnew, posYnew, posZnew]
                
        velXnew = '{:.6f}'.format(velXmain + (netAcceleration[0] * timeStep))
        velYnew = '{:.6f}'.format(velYmain + (netAcceleration[1] * timeStep))
        velZnew = '{:.6f}'.format(velZmain + (netAcceleration[2] * timeStep))

        newVelocity = [velXnew, velYnew, velZnew]

        data[objMain]["position"] = newPosition
        data[objMain]["velocity"] = newVelocity

    return data



        

