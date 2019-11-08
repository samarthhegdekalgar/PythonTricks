def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price'], 'Invalid input discount'
    return price


shoe = {'name': 'Fancy Shoes', 'price': 14900}
print(apply_discount(shoe, 0.25))  # valid Input/Output

print(apply_discount(shoe, 2.0))  # Invalid Input and Assertion Error

# Assertion syntax => assert_stmt ::= "assert' expression1 ["," expression2]
# Assertion must not be used for authentication and validation of data
# Assertion statements can be disabled by python debugger which leads security issue
# Assertion statement always be true if you pass a tuple, for example assert (1 == 2 'It should fail')
