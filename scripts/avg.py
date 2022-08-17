import os

FILES = 250
s = 0
minimum = [0, 1e100]
maximum = [0, 0]

for i in range(1, FILES + 1):
    if os.path.exists(".{}tools{}res{}{}.txt".format(os.sep, os.sep, os.sep, i)):
        with open(".{}tools{}res{}{}.txt".format(os.sep, os.sep, os.sep, i)) as f:
            lines = f.readlines()
            for line in lines:
                if(line.count("Score =")):
                    t = int(line.split(" = ")[1])
                    if(t):
                        s += t
                        if(t < minimum[1]):
                            minimum = [i, t]
                        if(t > maximum[1]):
                            maximum = [i, t]
                    else:
                        print("Error on {}".format(i))
    else:
        print("File {} not found".format(i))


print("Average score: {}".format(s/FILES))
print("Minimum score: {} on {}".format(minimum[1], minimum[0]))
print("Maximum score: {} on {}".format(maximum[1], maximum[0]))
