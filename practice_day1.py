def add_numbers(a,b):
    result= a+b
    return result
print(add_numbers(4,5))    



def is_adult(age):
    if(age >= 18):
        return True
    else:
        return False
print(is_adult(9))    



def calculate_discount(price, discount_percent):
    return price - (price * discount_percent / 100)


applications_ids=[101,102,103,104,105,106]
def count_even_ids(applications_ids):
    count =0
    for app_id in applications_ids:
        if(app_id%2==0):
            count = count +1
    return count   