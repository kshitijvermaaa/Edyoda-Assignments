#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random
import datetime as dt
import time


# In[6]:


cust_history = []
admin_dict = {'admin':'admin', 'kshitij':'12345'}
users_dict = {'cust':'cust'}
users_detail_dict = {}
newdict = {}
food_items = {6183: ['FOOD NAME: Burger', 'FOOD QUANTITY: 120gm', 'PRICE: 120', 'DISCOUNTED PRICE: 100', 'FOOD ID: 6183', 10],6672: ['FOOD NAME: Chicken Chilly', 'FOOD QUANTITY: 12 Pieces', 'PRICE: 120', 'DISCOUNTED PRICE: 100', 'FOOD ID: 6672', 10]}


# In[7]:


class Foodfactory:
    def __init__(self):
        print("*******************************************")
        print('\n'"Welcome to the FoodFactory App.")
        print('\n'"*******************************************")
        time.sleep(1)
        self.login_menu()
        
    def login_menu(self):
        reg_inp = int(input(" 1. Login as an Admin\n 2. Already a user?? Log in here!!\n 3. Dont have an account?? Make a new one here! \n4. Exit"))
        login = False
        if reg_inp == 1:
            self.email = input("Enter your Email Admin: ")
            self.password = input("Enter your Password Admin: ")
            for values in admin_dict:
                if self.email == values and self.password == admin_dict[values]:
                    print("Scrolling our Database")
                    time.sleep(1)
                    print("============================>")
                    time.sleep(1)
                    print("Login Successfull")
                    login = True
                    Admin()

            else:
                if login is False:
                    print("We cant find your credentials, Please check again")
                    time.sleep(2)
                    self.login_menu()
                    
                    
        
        
        if reg_inp == 2:
            self.email = input("Enter your Email: ")
            self.password = input("Enter your Password: ")
            for values in users_dict:
                if self.email == values and self.password == users_dict[values]:
                    print("Scrolling our Database")
                    time.sleep(2)
                    print("Login Successfull")
                    login = True
                    customers()
            else:
                if login is False:
                    print("We cant find your credentials, Please check again")
                    time.sleep(2)
                    self.login_menu()           
                    
        
        
        if reg_inp == 3:
            self.name = input("Enter your full name: ")
            self.phonum = input("Enter your Mobile Number: ")
            self.address = input("Enter your Address: ")
            self.email = input("Enter your Email: ")
            self.password = input("Enter your Password: ")
            self.customerID = random.randint(10000,99999)
            temp_cust_list = [self.name,self.phonum,self.address,self.email,self.password]
            users_detail_dict[self.customerID] = temp_cust_list
            users_dict[self.email] = self.password
            time.sleep(1)
            print("Successfully Created the account, Thank You")
            time.sleep(2)
            self.login_menu()
        if reg_inp == 4:
            exit()
class Admin:
    def __init__(self):
        print("Welcome Admin")
        print("1.Add A Food Item. \n2.Edit Food Item Using FOOD ID. \n3.View The List Of Food Available. \n4.Edit the Food Stock or Remove it from the Food List \n5.Sign-Out")
        print("Select appropriate option")
        foodinp = int(input())
        if foodinp == 1:
            self.addfood()
        elif foodinp == 2:
            self.editfooditem()
        elif foodinp == 3:
            self.viewfooditems()
        elif foodinp == 4:
            self.removeoraddstock()
        elif foodinp == 5:
            self.signout_admin()
        
        else:
            print("Not A Valid Choice!")
    
    def addfood(self):
        self.foodname = input("Enter The Name Of The Food You Want To Add: ")
        self.foodID = random.randint(1000,9999)
        time.sleep(1)
        print("Enter The Quantity Of {} To Be Added: ".format(self.foodname))
        self.quantity = input()
        print("Enter The Price Of {} ".format(self.foodname))
        self.price = input()
        print("Enter The Discounted Price of {} ".format(self.foodname))
        self.discount = input()
        print("Enter The Stock Quantity of {} ".format(self.foodname))
        self.stock = int(input())
        add_foodlist = ["FOOD NAME: "+str(self.foodname),"FOOD QUANTITY: "+str(self.quantity), "PRICE: "+str(self.price),"DISCOUNTED PRICE: "+str(self.discount),self.foodID, self.stock ]
        food_items[self.foodID] = add_foodlist
        time.sleep(1)
        print("{} Added Successfully".format(self.foodname))
        time.sleep(1)
        self.__init__()
        
    def editfooditem(self):
        print("Getting Food List")
        time.sleep(2)
        if food_items:
            print(food_items)
            self.changefoodid = int(input("Give the Food ID for the food you want to change: "))
            for values in food_items:
                if self.changefoodid == values:
                    self.changefoodname = input("Give the New Food Name for the food you want to change: ")
                    self.changequantity = input("Give the new quantity for the food you want to change: ")
                    self.changeprice= int(input("Give the new price for the food you want to change: "))
                    self.discountprice= int(input("Give the new discount price for the food you want to change: "))
                    self.changestock = int(input("Give the new stock amount for the food you want to change: "))
                    self.changedfoodlist = ["FOOD NAME: "+str(self.changefoodname),"FOOD QUANTITY: "+str(self.changequantity), "PRICE: "+str(self.changeprice),"DISCOUNTED PRICE: "+str(self.discountprice),self.changefoodid, self.changestock ]
                    food_items.pop(self.changefoodid)
                    food_items[self.changefoodid] = self.changedfoodlist
                    time.sleep(1)
                    print("{0} with food id {1} changed successfully".format(self.changefoodname,self.changefoodid))
                    print(food_items)
                    time.sleep(2)
                    self.__init__()
                else:
                    print("No such food item found")
                    self.__init__()
        
        else:
            print("Food List Empty, Add some food please")
            time.sleep(2)
            self.__init__()
        
        
    def viewfooditems(self):
        if food_items:
            print("Details of the Food is given below:- ")
            time.sleep(1)
            print(food_items)
            time.sleep(2)
            self.__init__()
        else:
            print("NO FOOD ITEM IS CURRENTLY LOGGED")
            time.sleep(2)
            self.__init__()
        
    def removeoraddstock(self):
        if food_items:
            print(food_items)
            time.sleep(2)
            print("1.Decrease or Increase the amount of stock of the food item.\n2.Remove the item fully")
            remove = int(input())
            if remove == 1:
                decfoodid = int(input("Enter the FoodID of the food: "))
                newstock = int(input("Enter the new stock amount: "))
                food_items[decfoodid][5] = newstock
                print("Successfully changed the Amount of stock of {}".format(food_items[decfoodid][0]))
                time.sleep(1)
                self.__init__()
            elif remove == 2:
                decfoodid = int(input("Enter the FoodID of the food: "))
                food_items.pop(decfoodid)
                print("Successfully removed the Food from the list")
                time.sleep(2)
                self.__init__()
            else:
                print("INVALID CHOICE")
                
        else:
            print("NO FOOD ITEM IS CURRENTLY LOGGED")
            self.__init__()

    def signout_admin(self):
        Foodfactory.login_menu(self)


class customers:
    def __init__(self):
        print("__________________________****__________________________")
        print("\n\t\tWelcome to Food Factory!!")
        print("\n__________________________****__________________________")
        custinp = int(input("1.Place new Order. \n2.View order history. \n3.Update your profile."))
        if custinp == 1:
            self.placeorder()
        elif custinp == 2:
            self.vieworders()
        elif custinp == 3:
            pass
        
        # else: 
        #     print("Invalid Option")
            
    def placeorder(self):
        
        if food_items:
            print("We have these food items: ")
            n = 1
            while n<len(food_items):
                for values in food_items:
                    newdict[n] = food_items[values][0]
                    n +=1
                print(newdict)
                time.sleep(1)
        
        for items in newdict:
            food_inn = int(input("Enter your choice: "))
            if food_inn in newdict:
                if food_inn == 1:
                    temp1 = 6183
                    food_items[temp1][5] -=1
                    print("{} Ordered Successfully".format(food_items[temp1][0]))
                    cust_history.append(food_items[temp1][0])
                elif food_inn == 2:
                    temp2 = 6672
                    food_items[temp2][5] -=1
                    cust_history.append(food_items[temp2][0])
                    print("{} Ordered Successfully".format(food_items[temp2][0]))
                elif food_inn == 3:
                    temp3 = 3
                    food_items[temp3][5] -=1
                    print("{} Ordered Successfully".format(food_items[temp][0]))
                self.__init__()
    def vieworders(self):
        print(cust_history)
            
 
            
    
        


# In[8]:


a = Foodfactory()


# In[ ]:




