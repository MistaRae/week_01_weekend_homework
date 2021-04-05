# WRITE YOUR FUNCTIONS HERE
import pdb

def get_pet_shop_name(cc_pet_shop):
    return cc_pet_shop["name"]

def get_total_cash(cc_pet_shop):
    return cc_pet_shop["admin"]["total_cash"]

def add_or_remove_cash(cc_pet_shop, income_or_expenditure):
    #update the total cash value using a new argument
    cc_pet_shop["admin"]["total_cash"] += income_or_expenditure
    
def get_pets_sold(cc_pet_shop):
    return cc_pet_shop["admin"]["pets_sold"]

def increase_pets_sold(cc_pet_shop, no_of_pets_change):
    #update the pets sold value in admin dictionary using a new argument
    cc_pet_shop["admin"]["pets_sold"] += no_of_pets_change

def get_stock_count(cc_pet_shop):
    #set new pets in stock variable to zero and update it with the number of pets currently in the pet shop
    #check if there is a pet present - true/false
    #if true +1 to current pets total 

    #pets is a list, so just counting the number of entries in the list should suffice. 
    # current_pet_stock = 0
    return len(cc_pet_shop["pets"])

def get_pets_by_breed(cc_pet_shop, breed_searched_for):
    #for each pet, check its breed matches breed_searched_for
    #if breed matches add to list and count that list.
    # pdb.set_trace()
    pets_found = []
    for pet in cc_pet_shop["pets"]:
        if pet["breed"] == breed_searched_for:
            pets_found.append(pet)

    return pets_found

def find_pet_by_name(cc_pet_shop, name_of_pet):
    for pet in cc_pet_shop["pets"]:
        if pet["name"] == name_of_pet:
            return pet

def remove_pet_by_name(cc_pet_shop, name_of_pet):
    for pet in cc_pet_shop["pets"]:
        if pet["name"] == name_of_pet:
            cc_pet_shop["pets"].remove(pet)

def add_pet_to_stock(cc_pet_shop, new_pet):
    cc_pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash_to_be_removed):
    customer["cash"] -= cash_to_be_removed

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
        customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    return False

def sell_pet_to_customer(shop, new_pet, customer):
        #can customer afford the pet
        #remove pet from shop
        #increase pets sold
        #add pet to customer
        #remove cost of pet from customer 
        #add cost of pet to shop balance
    if new_pet:
        if customer_can_afford_pet(customer, new_pet):
            cash_to_be_removed = new_pet["price"]
            remove_customer_cash(customer, cash_to_be_removed)
            increase_pets_sold(shop, 1)
            add_pet_to_customer(customer, new_pet)
            add_or_remove_cash(shop, cash_to_be_removed)
    


