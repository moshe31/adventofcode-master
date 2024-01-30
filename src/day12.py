import math

# Advent of code: day 12-12-2019
steps = 0
totalEnergy = 0

# first example

# puzzleSteps = 10
# moons = [
#     [-1, 0, 2],
#     [2, -10, -7],
#     [4, -8, 8],
#     [3, 5, -1]
# ]

# # second example
# puzzleSteps = 3000
# moons = [
#     [-8, -10, 0],
#     [5, 5, 10],
#     [2, -7, 3],
#     [9, -8, -3]
# ]

# puzzle input
puzzleSteps = 1000
moons = [
    [17, 5, 1],
    [-2, -8, 8],
    [7, -6, 14],
    [1, -10, 4]
]


def simulator(positions, velocities, steps=math.inf):
    original_positions, original_velocities = positions[:], velocities[:]

    step_number = 0

    while step_number < steps and (not step_number or positions != original_positions or velocities != original_velocities):
        for i in range(len(positions)):
            velocities[i] += sum(1 if positions[i] < position else - 1 for position in positions if position != positions[i])

        for i in range(len(positions)):
            positions[i] += velocities[i]

        step_number += 1
        
    return step_number


def getTotalEnergy(moons, steps):
    simulationData = {
        'x': getPositionsByDimension("x", moons),
        'y': getPositionsByDimension("y", moons),
        'z': getPositionsByDimension("z", moons)
    }

    for dimension in simulationData:
        positions, velocities = (
            simulationData[dimension]['positions'], simulationData[dimension]['velocities'])
        # simulate and mutates original data
        simulator(positions, velocities, steps)

    # once the simulator is done with each dimension separatly now we need to sum the data,
    # by dimentions in following order eg. x, y, z
    totalEnergy = 0
    x, y, z = (simulationData['x'], simulationData['y'], simulationData['z'])

    for i in range(0, 4):
        kinaticEnergy = 0
        potentialEnergy = 0

        potentialEnergy += abs(x['positions'][i]) + \
            abs(y['positions'][i]) + abs(z['positions'][i])

        kinaticEnergy += abs(x['velocities'][i]) + \
            abs(y['velocities'][i]) + abs(z['velocities'][i])

        totalEnergy += potentialEnergy * kinaticEnergy

    return totalEnergy


def getRepeatingState(moons):
    simulationData = {
        'x': getPositionsByDimension("x", moons),
        'y': getPositionsByDimension("y", moons),
        'z': getPositionsByDimension("z", moons)
    }

    for dimension in simulationData:
        positions, velocities = (
            simulationData[dimension]['positions'], simulationData[dimension]['velocities'])
        # simulate and mutates original data
        simulationData[dimension]['steps'] = simulator(positions, velocities)

    # lcm
    x, y, z = (simulationData['x'], simulationData['y'], simulationData['z'])
    xyLcm = math.floor((x['steps'] * y['steps']) / gcd(x['steps'], y['steps']))
    zLCM = math.floor((xyLcm * z['steps']) / gcd(xyLcm, z['steps']))

    return zLCM

# gretest common divisor
# pluked from stack


def gcd(a, b):
    if not b:
        return a

    return gcd(b, a % b)


def getPositionsByDimension(dimension, moons):
    positions = []

    # separating dimensions from all the moons
    # x from io, europa, gaynemede, calisto, y from io ... etc
    for moon in moons:
        [px, py, pz] = moon

        if dimension == "x":
            positions = [*positions, px]

        if dimension == "y":
            positions = [*positions, py]

        if dimension == "z":
            positions = [*positions, pz]
    # we also init velocities based on retured positions by dimension
    velocities = [0] * len(positions)

    return {
        'positions': positions,
        'velocities': velocities,
        'steps': 0
    }


print(getTotalEnergy(moons, puzzleSteps))  # 9876
print(getRepeatingState(moons)) # 307043147758488
