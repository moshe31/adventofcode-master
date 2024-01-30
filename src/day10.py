# day 10 advent of code
import math

inputData = open("./inputs/input-10.txt").read()


def mapCoordinates(data):
    asteroids = []
    _inputData = data.split("\n")[:]

    for topPosition, line in enumerate(_inputData):
        for elementPos, ele in enumerate(list(line)):
            if ele == "#":
                asteroids.append({'x': elementPos, 'y': topPosition})
    return asteroids


def getDistance(a, b):
    return math.hypot(a['x'] - b['x'], a['y'] - b['y'])


def getAngle(y, x):
    return ((math.atan2(x, y) * 180) / math.pi) * 2

# gretest common divisor will help us with line of sight
# recursive gcd pluked from stack


def gcd(a, b):
    a = abs(a)
    b = abs(b)

    if not b:
        return a

    return gcd(b, a % b)


def findOptimalLocations(currentAsteriod, asteriodMap):
    visibilityMap = []
    for i, asteriod in enumerate(asteriodMap):
        if not (currentAsteriod['x'] == asteriod['x'] and currentAsteriod['y'] == asteriod['y']):
            [x, y] = currentAsteriod['x'], currentAsteriod['y']
            deltaX = x - asteriod['x']
            deltaY = y - asteriod['y']

            ratio = gcd(deltaX, deltaY)

            posDiff = str(deltaX / ratio) + ', '+str(deltaY / ratio)
            distance = getDistance(currentAsteriod, asteriod)
            angle = getAngle(deltaY, deltaX)

            index = -1

            for j, a in enumerate(visibilityMap):
                if a['posDiff'] == posDiff:
                    index = j
                    break
                else:
                    index = -1

            asteriodObj = {
                **asteriod,
                'posDiff': posDiff,
                'distance': distance,
                'angle': angle
            }

            if index > -1:
                try:
                    visibilityMap[index]

                    if visibilityMap[index]['distance'] > asteriodObj['distance']:
                        visibilityMap[index] = asteriodObj

                except IndexError:
                    visibilityMap.append(asteriodObj)
            else:
                visibilityMap.append(asteriodObj)

    [x, y] = currentAsteriod['x'], currentAsteriod['y']

    return sorted(visibilityMap, key=lambda asteroid: getAngle(asteroid['y'] - y, asteroid['x'] - x), reverse=True)


def part_1(asteriodMap):
    optimalLocation = []
    for i in range(len(asteriodMap)):
        optimalLocation.append(
            {**asteriodMap[i], 'lineOfSight': len(findOptimalLocations(asteriodMap[i], asteriodMap))})

    # optimalLocation.sort(key=lambda x: x['lineOfSight'], reverse=True)
    return sorted(optimalLocation, key=lambda x: x['lineOfSight'], reverse=True)[0]


def vapourizeAsteriods(monitoringStation, _map, nthAsteroid):
    asteriodsMap = _map[:]
    vapourizedAsteriods = []

    while len(asteriodsMap) - 1:
        markedAsteriods = findOptimalLocations(monitoringStation, asteriodsMap)

        for i, markedAsteriod in enumerate(markedAsteriods):
            for j, asteriod in enumerate(asteriodsMap):
                if markedAsteriod['x'] == asteriod['x'] and markedAsteriod['y'] == asteriod['y']:
                    vapourizedAsteriods.append(asteriod)
                    del asteriodsMap[j]

    if vapourizedAsteriods[nthAsteroid - 1]:
        [x, y] = vapourizedAsteriods[nthAsteroid -
                                     1]['x'], vapourizedAsteriods[nthAsteroid - 1]['y']
        return x * 100 + y
    else:
        return vapourizedAsteriods[len(vapourizedAsteriods) - 1]


asteriodMap = mapCoordinates(inputData)

# part 1
print(part_1(asteriodMap))
# part 2
print(vapourizeAsteriods(part_1(asteriodMap), asteriodMap, 200))
