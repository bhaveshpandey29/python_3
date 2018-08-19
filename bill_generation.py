while True:
    count_per = int(input("Please enter the number of persons : "))
    total_val = []
    for i in range(1,count_per +1):
        print("\nEnter the details of the person",i,"below:")
        person_starter = int(input("\nPlease enter the value of breakfast : "))
        person_meal = int(input("Please enter the value of meal : "))
        person_desert = int(input("Please enter the value for desert : "))
        value = (person_desert+person_meal+person_starter)
        total_val.insert(i,value)
        print("\nBill for person",i,"is:",value)

    coupon = str(input("\nGot any coupon?"))
    total = sum(total_val)
    if("FIFTY" in coupon):
        print("Congratulations for 50% OFF!!!\nNow your total Bill is = ",total-(total*.50))
    elif("FOURTY" in coupon):
        print("Congratulations for 40% OFF!!!\nNow your total Bill is = ",total-(total*.40))
    else:    
        print("\n\nTotal Bill is = ",total)