objectTree = {}
orbitsInfo = {}
orbitCount = 0


def orbitFinder(_object={}, count=0, relation=""):
    if not 'parents' in _object:
        return {'count': count, 'relation': relation} if count else {count: 0, relation: ""}
    else:
        foundobject = ""

        for n in _object['parents']:
            if n in _object['parents']:
                foundobject = n

        relation = _object['name'] + " > " + \
            relation if relation else _object['name']

        return orbitFinder(objectTree[foundobject], count + 1, relation) if foundobject else {'count': count, 'relation': relation}


def findJumps(setA, setB):
    setA.remove("YOU")
    setB.remove("SAN")
    jumps = setA
    for elem in setB:
        if elem in jumps:
            jumps.remove(elem)
        else:
            jumps.append(elem)

    return jumps


# Puzzle input
_file = open("./inputs/input-6.txt").read().split('\n')

for line in _file:

    [a, b] = line.split(")")

    a = a.strip()
    b = b.strip()

    # parent
    if not a in objectTree:
        objectTree[a] = {'name': a, 'childs': {}}

    if 'childs' in objectTree[a]:
        objectTree[a]['childs'] = {
            **objectTree[a]['childs'],
            b: True
        }
    else:
        objectTree[a]['childs'] = {b: True}

    # child
    if not b in objectTree:
        objectTree[b] = {'name': b, 'parents': {}}

    if 'parents' in objectTree[b]:
        objectTree[b]['parents'] = {
            **objectTree[b]['parents'],
            a: True
        }
    else:
        objectTree[b]['parents'] = {a: True}

for _object in objectTree:
    orbitsInfo[_object] = orbitFinder(objectTree[_object])
    orbitCount += orbitsInfo[_object]['count'] if 'count' in orbitsInfo[_object] else 0

you = orbitsInfo["YOU"]['relation'].split(" > ")
san = orbitsInfo["SAN"]['relation'].split(" > ")

totalJumps = findJumps(you, san)

# part 1
print(orbitCount)
# part 2
print(len(totalJumps))
