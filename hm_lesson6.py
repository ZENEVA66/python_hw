product=100
while True:
    demand= int(input("How much you want?:"))
    if product >= demand:
        print("wait a second i will give you the product")
        product=product-demand
    else:
        print("i can't give you what you want")
        break