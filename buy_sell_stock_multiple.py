def buy_and_sell_stock_multiple(nums):
    #  greedy
    max_profit = 0
    for i in range(1, len(nums)):
        if nums[i]-nums[i-1]>0:
            max_profit += nums[i]-nums[i-1]
    return max_profit
