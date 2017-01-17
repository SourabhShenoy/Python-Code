def semverSort(item):
    versions = item.split('.')
    worth = int(versions[0])*10000

    if (len(versions) >= 2):
        if (len(versions) >= 3):
            worth += int(versions[2]) + 1
        worth += (int(versions[1]) + 1)*100

    return worth

def answer(l):
    l.sort(key=semverSort)
    return l

print answer(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])