def towerOfHanoi(no,source,destination,helper):
    if no==0:
        return
    towerOfHanoi(no-1,source,helper,destination)
    print(f"{no} --> {source} to {destination}")
    towerOfHanoi(no-1,helper,destination,source)

towerOfHanoi(3,'A','B','C')
