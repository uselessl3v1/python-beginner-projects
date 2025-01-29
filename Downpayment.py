good_credit = False
house = 1000000
if good_credit:
    print(f"You will need to put down {house / 10 * 1} dollar")
elif not good_credit:
    print(f"You will need to put down {house / 10 * 2} dollar")
