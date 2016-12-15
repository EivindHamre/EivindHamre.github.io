def fakultet(n) :
    if n > 10 :
        #print ("kan ikke gjøre dette.")
        return -1
    else :
        fakultet = 1
        for x in range(1, n+1):
            fakultet = fakultet * x
        return fakultet