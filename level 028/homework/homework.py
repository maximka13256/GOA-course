positive_numbers = 0
negative_numbers = 0
for i in range(5):
    num = int(input("please enter a number"))

    if num > 0:
        positive_numbers = positive_numbers + 1
    elif num < 0:
        negative_numbers = negative_numbers + 1

        print("positive numbers count: " + str(positive_numbers))
        print("negative numbers count: " + str(negative_numbers))
        
        #1
        can = int(input("enter year: "))

        if can >= 18:
            print("no discount")
        else:
            if can >= 13:
                print("discount 20 %")
            else:
                print("discount 10 %")

                #2 
                count = 1

                while count <= 10:
                    print(count)