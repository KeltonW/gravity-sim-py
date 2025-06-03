from typing import Tuple
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import imageio

class Object:
    def __init__(self, mass: float, position: Tuple[float, float], velocity: Tuple[float, float]):
        self.mass = mass
        self.position = list(position)
        self.velocity = list(velocity)  # Use a list for mutability

class Step:
    def __init__(self, time: float, stepId: int, objects: list[Object]):
        self.time = time
        self.stepId = stepId
        self.objects = objects

constSteps = 1000000
timeStep = 20
gravitationConstant = 6.67430e-11  # m^3 kg^-1 s^-2

fps = 120
animationLength = 60

def main():
    firstObject = Object(1.0, (0.3089693008, 0.4236727692), (0.0, 0.0))
    secondObject = Object(10.0, (-0.5, 0.0), (0.0, 0.0))
    thirdObject = Object(1.0, (0.5, 0.0), (0.0, 0.0))

    steps = []

    for stepId in range(constSteps):
        newStep = Step(float(stepId) * timeStep, stepId, [firstObject, secondObject, thirdObject])

        for i in range(len(newStep.objects)):
            for j in range(len(newStep.objects)):
                if i != j:
                    dx = newStep.objects[j].position[0] - newStep.objects[i].position[0]
                    dy = newStep.objects[j].position[1] - newStep.objects[i].position[1]

                    r = (dx**2 + dy**2)**0.5
                    force = gravitationConstant * (newStep.objects[i].mass * newStep.objects[j].mass) / (r**2)
                    angle = math.atan2(dy, dx)
                    fx = force * math.cos(angle)
                    fy = force * math.sin(angle)
                    newStep.objects[i].velocity[0] += fx / newStep.objects[i].mass * timeStep
                    newStep.objects[i].velocity[1] += fy / newStep.objects[i].mass * timeStep

        for object in newStep.objects:
            object.position[0] += object.velocity[0] * timeStep
            object.position[1] += object.velocity[1] * timeStep
        
        firstObject = newStep.objects[0]
        secondObject = newStep.objects[1]
        thirdObject = newStep.objects[2]

        steps.append(newStep)

        if stepId % 1000 == 0:
            print(firstObject.position)


main()
                    