

def are_reverses(s1, s2):
    countit = 0
    if len(s1) == len(s2):
        for f in range(len(s1)):
            x = len(s2) - f-1
            if s1[f] == s2[x]:
                countit += 1
                print("Count", countit)
                if countit == len(s1):
                    return "It equals"
                else:
                    pass
            else:
                return "It doesnt equal"
    else:
        return "It doesnt equal"




print(are_reverses(s1='roo1', s2='12or'))