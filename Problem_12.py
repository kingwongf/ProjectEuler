import numpy as np

ans = 1
common_factors = 0
count = 1
while common_factors < 500:
    count +=1
    ans += count
    print(ans)
    d =1
    common_factors = 0
    while d <= ans**0.5:
        if ans%d == 0:
            common_factors += 1
        d+=1
    common_factors *= 2

print(ans)