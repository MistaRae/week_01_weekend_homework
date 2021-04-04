# WRITE YOUR FUNCTIONS HERE
# import pdb

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

# def get_stock_count(cc_pet_shop, )