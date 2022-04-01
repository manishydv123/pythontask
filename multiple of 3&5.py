def function(limit):

    x = [i for i in range(0,limit + 1) if i % 3 == 0 or i % 5 == 0]
    return x

print(function(20))