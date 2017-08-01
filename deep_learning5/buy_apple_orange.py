from add_layer import *
from mul_layer import *

apple = 100
apple_num = 2
orange = 150
orange_num = 3
tax = 1.1

mul_apple_layer = MulLayer()
mul_orange_layer = MulLayer()
add_apple_orange_layer = AddLayer()
mul_tax_layer = MulLayer()

apple_price = mul_apple_layer.forward(apple, apple_num)
orange_price = mul_orange_layer.forward(orange, orange_num)
all_price = add_apple_orange_layer.forward(apple_price, orange_price)
price = mul_tax_layer.forward(all_price, tax)
print("price: {0}", price)

dprice = 1
dall_price, dtax = mul_tax_layer.backword(dprice)
dapple_price, dorange_price = add_apple_orange_layer.backword(dall_price)
dapple, dapple_num = mul_apple_layer.backword(dapple_price)
dorange, dorange_num = mul_orange_layer.backword(dorange_price)

print("dapple: {0}", dapple)
print("dapple_num: {0}", dapple_num)
print("dorange: {0}", dorange)
print("dorange_num: {0}", dorange_num)
print("dtax: {0}", dtax)
