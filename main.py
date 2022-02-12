def buy(high,low,risk,BEper,bt1,bt2,bt3):
    diff=high-low
    quantity=risk/diff
    my_BE=high+(high*(BEper/100))
    Target1=high+(diff*bt1)
    Target2=high+(diff*bt2)
    Target3=high+(diff*bt3)
    SL=low
    print(f"high = {high}")
    print(f"low = {low}")
    print(f"Quantity = {quantity}")
    print(f"Difference = {diff}")
    print(f"B/E = {my_BE}")
    print(f"Target1 = {Target1}")
    print(f"Target2 = {Target2}")
    print(f"Target3 = {Target3}")
    print(f"stoploss = {SL}")
    
    
def sell(high,low,risk,BEper,bt1,bt2,bt3):
    diff=high-low
    quantity=risk/diff
    my_BE=high-(high*(BEper/100))
    Target1=low-(diff*bt1)
    Target2=low-(diff*bt2)
    Target3=low-(diff*bt3)
    SL=high
    print(f"high = {high}")
    print(f"low = {low}")
    print(f"Quantity = {quantity}")
    print(f"Difference = {diff}")
    print(f"B/E = {my_BE}")
    print(f"Target1 = {Target1}")
    print(f"Target2 = {Target2}")
    print(f"Target3 = {Target3}")
    print(f"stoploss = {SL}")
    
    
high=float(input("enter high "))
low=float(input("enter low "))
risk=int(input("enter risk "))
BEper=float(input("enter BEper "))
bt1=float(input("enter bt1 "))
bt2=float(input("enter bt2 "))
bt3=float(input("enter bt3 "))
buy(high,low,risk,BEper,bt1,bt2,bt3)
sell(high,low,risk,BEper,bt1,bt2,bt3)