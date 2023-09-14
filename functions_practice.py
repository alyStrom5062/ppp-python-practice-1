def hello():
    print("Hello, user!")

def pack(one, two, three):
    my_list = (one, two, three)
    print(my_list)
    return my_list

list = ["soup", "salad", "chicken", "rice"]

def eat_lunch(lunch_list):
    if len(lunch_list) == 0:
        print("My lunchbox is empty!")
    else: 
        for food in lunch_list:
            if food == lunch_list[0]:
                print("First I eat " + food)
            else: 
                print("Next I eat " + food)

hello()
pack("purse", "lip gloss", "perfume")
eat_lunch(list)  