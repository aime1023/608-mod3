import random
import statistics

numrand = []
for i in range(0,100):
    num = random.randint(1,1000)
    numrand.append(num)

statistics.variance(numrand)
statistics.pstdev(numrand)
