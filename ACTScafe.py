menu={
    'hot coffee':60,
    'cold coffee':70,
    'lemonade':90,
    'french fries':120,
    'pizza':300,
    'burger':150,
    'chocolate brownie':200,
    'pull up cake':400,
}
print("Welcome To ACTS Cafe")
print("\n hot coffee: Rs60 \n cold coffee:Rs70 \n lemonade:90 \n french fries:120 \n pizza:300 \n burger:150 \n chocolate brownie:200 \n pull up cake:400")

ordertotal=0

first_item= input("enter the first item you want to order=")
if first_item in menu:
    ordertotal= ordertotal+ menu[first_item]
    print("your choice", first_item , "has been added to the list")
else:
    print("oops! currently unavailable. please order something else")
i=1
while(i>0):
    anotherorder= input("do you want to continue ordering? (y/n):")
    if anotherorder=="y":
     second_order=input("enter the second item you want=")
     if second_order in menu:
        ordertotal= ordertotal+ menu[second_order]
     else:
        print("oops! currently anavailable. please order something else")
    elif anotherorder=="n":
        break
print("the total amount is to be paid=",ordertotal)

        

