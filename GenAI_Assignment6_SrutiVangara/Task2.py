prices = [120,350,'abc',500,-200,800]
total = 0
for item in prices:
    try:
        if not isinstance(item, (int,float)):
            raise TypeError()
        if item < 0:
            raise ValueError()
        total += item
        print(f"Added:{item}. Running total:{total}")
    except TypeError as e :
        print("Type error:" ,e)
    except ValueError as e:
        print("Value Error:",e)
print("Final total:",total)