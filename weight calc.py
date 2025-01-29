weight = input("Weight: ")
kilo_ibs_input = input("(K)kg or (L)bs: ")
kilo_ibs = str(kilo_ibs_input.upper())
if kilo_ibs == "K":
    ibs_weight = int(weight) * 2.2
    print("Weight in Ibs: " + str(ibs_weight))
elif kilo_ibs == "L":
    ibs_weight = int(weight) // 2.2
    print("Weight in Kg: " + str(ibs_weight))
else: print("Please try again and enter with 'k' or 'l'")