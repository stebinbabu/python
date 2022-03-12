list1 = ["red", "blue", "yellow","black","brown","green"]
list2 = ["green", "pink", "red"]
for element in list1:
    if element not in list2:
        print(element)