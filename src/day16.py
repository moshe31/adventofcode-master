from functools import reduce
# day 16 advent of code
# part 1


def fft(phases, outputDigits, basePattren, inputSignal):
    transformedSignal = inputSignal[:]
    initialPattren = []

    for index, ele in enumerate(transformedSignal):
        initialPattren.append(int(basePattren[index % len(basePattren)]))

    for i in range(0, phases):
        elements = []
        generatedPattren = initialPattren[:]

        for j in range(0, len(transformedSignal)):
            lineElements = []

            if j:
                newPattren = []
                for p in range(0, len(transformedSignal)):
                    if len(newPattren) <= len(transformedSignal):
                        newPattren = newPattren + [initialPattren[p]] * (j + 1)

                generatedPattren = newPattren

            generatedPattren = generatedPattren[1:] + generatedPattren[0: 1]

            for k in range(0, len(transformedSignal)):
                element = int(transformedSignal[k]) * int(generatedPattren[k])
                lineElements.append(element)

            lineElementsSum = reduce(
                (lambda x, y: int(x) + int(y)), lineElements)

            if not (lineElementsSum < 0 and lineElementsSum > 10):
                numStr = str(lineElementsSum)
                lineElementsSum = int(numStr[len(numStr) - 1])

            elements.append(abs(lineElementsSum))

        transformedSignal = elements

    return "".join(map(str, transformedSignal[0: outputDigits]))


def signalRepeater(times, signal):
    repeatedSignal = []
    offset = 0

    for i in range(0, times):
        repeatedSignal = repeatedSignal + signal

    # ignore half of the inputSignal
    offset = int("".join(map(str, repeatedSignal[0:7])))
    # return the rest
    return repeatedSignal[offset:]

# part 2


def getEmbeddedMsg(phases, outputDigits, inputSignal):
    # Patterns can skiped for this, because for the given offset all the pattern values will be 1s.
    transformedSignal = list(map(int, inputSignal[:]))

    for phase in range(0, phases):
        for i, e in reversed(list(enumerate(transformedSignal))):
            try:
                transformedSignal[i] = abs(
                    (transformedSignal[i + 1] + transformedSignal[i]) % 10)
            except IndexError:
                transformedSignal[i] = abs(transformedSignal[i] % 10)

    return "".join(map(str, transformedSignal[0: outputDigits]))


inputSignal = list(open("./inputs/input-16.txt").read())

# part 1 answer
print(fft(100, 8, [0, 1, 0, -1], inputSignal))

# part 2 answer
print(getEmbeddedMsg(100, 8, signalRepeater(10000, inputSignal)))
