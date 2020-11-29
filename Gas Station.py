def complete_gas(gas, cost):
    if sum(gas)<sum(cost):
        return -1
    start = 0
    remain = 0
    for i in range(len(gas)):
        if gas[i] + remain< cost[i]:
            start = i+1
            remain = 0
        else:
            remain = gas[i] - cost[i] + remain
    return start
A = [1,2,3,4,5]
B = [3,4,5,1,2]
print(complete_gas(A, B))

