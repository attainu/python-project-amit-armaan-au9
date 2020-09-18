
class Restaurant:
    restuarent_code = "0"
    menuCodeAndName = {}
    def __init__(self):
        self.res_list = ['RASOI DHABA', 'CURRY LEAVES', 'KADAK MASALA', 'SOUTH TADKA', 'FOOD PLAZA', 'KHANA KHAZANA']
        self.hotelCode = ["1", "2", "3", "4", "5", "6"]
        self.menuCode = {}
        self.user_selection_option = 0
        self.previos_user_selection_option = 0
        self.menu_list = {
            "1": {"PAV BHAJI": 35, "BREAD": 9, "ROAST CHICKEN": 85,
                  "MASALA DOSA": 85, "LAMPRAISE": 85},
            "2": {"CHICKEN SANDWICH": 50, "PANEER TIKKA": 370, "ROAST CHICKEN": 450,
                  "GRILLED PANEER": 190, "BUTTER CHICKEN": 150},
            "3": {"SOUPS": 695, "BURGER": 650, "BREAD": 11, "MAKI ROLLS": 109,
                  "CHICKEN SANDWICH": 50},
            "4": {"VEG BRIYANI": 115, "ROAST CHICKEN": 260, "PANEER TIKKA": 350, "SOYA CHAAP    ": 50,
                  "CHICKEN LOLLIPOP": 350},
            "5": {"PURI ": 50, "CHANNA ": 55},
            "6": {"DHOKHLA": 120, "FAFRA": 200, "PURI": 50}
        }

        self.menuItemForOrder = {}  # to store selected restaurent's menu items:
        self.orderedList = {}
        self.userClickCount=0

    def showRestaurants(self):
        print("CURRENTLY AVAILABLE RESTAURANTS : ","\n"*3)
        print("-" * 90)
        print(" "*10, "CODE", " " * 8," " * 30, "RESTAURANT NAME"," " * 16,sep="")#code=12,restuarent name=30
        print("-" * 90)

        for i in range(0, len(self.res_list)):
            code=i+1
            codeLen=2-len(str(code))

            resName=self.res_list[i]
            resNameLen=30-len(resName)

            print(" "*10, "( Code: ", code," "*codeLen, " )", " "*30, resName," "*resNameLen, sep="")#( code: 99 )

        print("-" * 90,"\n"*2)

        print("=========> To View Menu Item     ==========>Enter ( Code Number )")
        print("=========> Go Home/Login Page    ==========>Enter ( H )")

        print("")
        self.user_selection_option = input(">>> ").upper()
        self.checkUserInputUser()

    def checkUserInputUser(self):
        if self.user_selection_option in self.hotelCode:
            if self.user_selection_option != self.previos_user_selection_option:
                self.previos_user_selection_option = self.user_selection_option
                self.orderedList.clear()
            print()
            self.showMenuItems()
        elif self.user_selection_option == "H":
            print("\n"*20)
            self.displayHomeContent()

        else:
            self.user_selection_option = input(">>> SELECT VALID CHOICES : ").upper()
            self.checkUserInputUser()

    def showMenuItems(self):
        print("\n" * 10)
        print(">" * 30, "MENU OF", self.res_list[int(self.user_selection_option) - 1], "<" * 30)
        print("\n" * 2)
        if self.user_selection_option in self.menu_list:
            print("-" * 100)
            print(" "*5, "    CODE    ", " " * 25, "ITEMS :        ", " " * 28, "    PRICE: ",sep="")
            print("-" * 100)

            i = 0  # code id for menu items:
            #menuItemForOrder is a sub dict of menu list wch will contain menu of respective resturant
            self.menuItemsForOrder = self.menu_list[self.user_selection_option]
            for key, value in self.menuItemsForOrder.items():
                i += 1
                itemName=key
                itemNameLen=20-len(key)
                itemPrice=value
                itemPriceLen=4-len(str(itemPrice))
                self.menuCode[str(i)] = key
                print(" "*5, "( CODE: ", i, " )", " " * 25, itemName," "*itemNameLen, " " * 30, itemPrice," "*itemPriceLen, sep="")

            print("-" * 100, "\n" * 2)
            print("=========> To Select Menu Item     ==========>Enter ( Code Number )")
            print("=========> Go Home Page            ==========>Enter ( H )")

            selected_dish_code = input(">>> ").upper()
            self.checkItemCodeForOrder(selected_dish_code)

    def checkItemCodeForOrder(self, selected_dish_code):
        if selected_dish_code in self.menuCode:#placing the user seleted item to cart
            self.userClickCount+=1
            temp_dic = {}#sub dict for cart:
            name = self.menuCode[selected_dish_code]
            temp_dic["itemName"] = name

            temp_dic["price"] = self.menuItemsForOrder[name]#
            temp_dic["quantity"] = 1
            orderId = len(self.orderedList) + 1

            if len(self.orderedList) == 0:
                    self.orderedList[selected_dish_code] = temp_dic#orderList={1,{itemname:sambar,price:100,qnty:1}}
                    self.placeOrder()

            else:
                for key, value in self.orderedList.items():
                    if name in value["itemName"]:
                        qnty = value["quantity"]
                        if qnty == 3:
                            self.showRestuarentAvailability()
                        else:
                            if self.userClickCount>3:
                                self.showRestuarentAvailability()
                            else:
                                qnty += 1
                                value["quantity"] = qnty
                                self.orderedList[key] = value
                                self.placeOrder()

                if orderId > 3:
                   self.showRestuarentAvailability()
                else:
                    if(self.userClickCount<=3):
                        self.orderedList[selected_dish_code] = temp_dic
                        self.placeOrder()
                    else:
                        self.showRestuarentAvailability()
        elif selected_dish_code == "H":
            print("\n" * 20)
            self.displayHomeContent()




        else:
            self.selected_dish_code = input(">>> PLEASE SELECT VALID CHOICES : ").upper()
            self.checkItemCodeForOrder(self.selected_dish_code)

    def showRestuarentAvailability(self):
        print("\n" * 23, "*" * 16, "Restuarent Busy Now!!! Order Later or Try Other Restuarent", "*" * 16,
              "\n" * 2)
        print("YOUR CART: ","\n"*3)
        self.showcartTable()
        print("\n"*2)
        print("=========> To Place Order        ==========>Enter ( P )")
        print("=========> Go Home Page          ==========>Enter ( H )")

        userInput = input(">>> ").upper()
        self.checkPlaceOrder(userInput)
    def showcartTable(self):
        totalPrice = 0
        for key, value in self.orderedList.items():  # ordered list is the nested dict, wch contain temp_dict
            itemName = value["itemName"]
            itemNameLen = 20 - len(itemName)
            price = value["price"]
            PriceLen = 17 - len(str(price))

            quantity = value["quantity"]
            productTotalPrice = quantity * price
            totalPrice += productTotalPrice
            print(" " * 8, key, " " * 20, itemName, " " * itemNameLen, " " * 20, quantity, " " * 17, price,
                  " " * PriceLen, productTotalPrice, sep="")

        print("-" * 120)
        print("\t" * 20, "TOTAL PRICE : ", " " * 8, totalPrice)
        print("-" * 120, "\n" * 2)


    def placeOrder(self):#displaying our cart and let user to place items in his cart:
        print("\n" * 23, ">" * 30, "ITEMS IN YOUR CART", "<" * 30, "\n")
        print("-" * 120)
        print(" "*5, "ITEM_CODE", " " * 20, "ITEM"," "*16, " " * 12, "QUANTITY", " " * 12, "PRICE"," " *12,"AMOUNT",sep="")
        print("-" * 120)

        self.showcartTable()

        print("=========> To Place Order        ==========>Enter ( P )")
        print("=========> For More Order        ==========>Enter ( M )")
        print("=========> Go Home Page          ==========>Enter ( H )")

        selected_dish_code = input(">>> ").upper()
        while True:
            if selected_dish_code == "M":
                self.showMenuItems()
                break
            elif selected_dish_code =="P" or selected_dish_code =="H":
                self.checkPlaceOrder(selected_dish_code)
                break
            else:
                selected_dish_code = input(">>> PLEASE SELECT VALID OPTION: ").upper()

    def showInvoice(self):
        print("\n"*2,"Your Invoice Is :",)
        print("-" * 120)
        print(" " * 5, "ITEM_CODE", " " * 20, "ITEM", " " * 16, " " * 12, "QUANTITY", " " * 12, "PRICE", " " * 12,
              "AMOUNT", sep="")
        print("-" * 120)

        self.showcartTable()

    def checkPlaceOrder(self, userInput):

        if userInput == "P":
            print("\n"*20)
            print("*" * 30, "ORDER PLACED SUCCESSFULLY!!!!!!", "*" * 30)
            self.showInvoice()
            print("*" * 30, "****THANK YOU FOR PURCHASE****", "*" * 30)
            print("*" * 30, "****VISIT AGAIN!!!****", "*" * 30)

            print("\n"*2)

            print("=========> Show More Restuarent  ==========>Enter ( M )")
            print("=========> Go Home Page          ==========>Enter ( H )")
            userInput=input(">>> ").upper()
            self.orderedList.clear()

            while True:
                if userInput =="M":
                    print("\n"*15)
                    self.showRestaurants()
                    break
                elif userInput == "H":
                    print("\n" * 15)
                    self.displayHomeContent()
                    break
                else:
                    userInput=input("enter valid code >>> ")
        elif userInput == "H":
            print("\n"*10)
            self.displayHomeContent()

        else:
            self.userInput = input(">>> PLEASE SELECT VALID OPTION: ").upper()
            self.checkPlaceOrder(self.userInput)






#Admin


    def displayHomeContent(self):# displays home page
        print("HOME PAGE :","\n"*5)
        print(" "*15,"-"*30)
        print(" "*15,"| ","Click A to Login as ADMIN"," |")
        print(" "*15,"-"*30)

        print(" " * 15, "-" * 30)
        print(" " * 15, "| ", "Click U to Login as USER", " |")
        print(" " * 15, "-" * 30,"\n"*5)

        userInput=input(">>>").upper()#level 1 user Input
        self.checkUserInput(1,userInput)

    def checkUserInput(self,case,userInput):
        if case==1:#login page
            if userInput == "A":#admin
                print("\n"*15)
                self.showRestaurantsForAdmin()
            elif userInput=="U":#user
                print("\n"*15)
                self.showRestaurants()
            else:
                userInput=input("Enter Valid Data : >>>")
                self.checkUserInput(1,userInput) #self calling

        if case==2: #restuarent page of admi
            if userInput in self.hotelCode: #restaurent code
                self.showMenuItemsForAdmin(userInput)
            elif userInput=="A":
                self.addNewRestuarent()
            elif userInput == "H":  # direct to home page
                print("\n" * 15)
                self.displayHomeContent()
            else:
                userInput = input("Enter Valid Data : >>>")
                self.checkUserInput(2, userInput) #self calling
        if case==3: #menu page of restaurant of admin
            if userInput=="A": #add new menu
                self.addNewMenuItem()
            elif userInput in self.menuCodeAndName: # update menu item
                self.updateMenuItem(userInput)
            elif userInput=="H": # direct to home page
                print("\n"*15)
                self.displayHomeContent()
            elif userInput=="S": #display restuarent list
                print("\n"*15)
                self.showRestaurantsForAdmin()
            else:
                userInput = input("Enter Valid Data : >>>")
                self.checkUserInput(3, userInput) #self calling

    def showRestaurantsForAdmin(self):
        print("-" * 90)
        print(" "*10, "CODE", " " * 8," " * 30, "RESTAURANT NAME"," " * 16,sep="")#code=12,restuarent name=30
        print("-" * 90)

        for i in range(0, len(self.res_list)):#displayying restuarant code & name
            code=i+1
            codeLen=2-len(str(code))

            resName=self.res_list[i]
            resNameLen=30-len(resName)

            print("( Code: ", code," "*codeLen, " )", " "*30, resName," "*resNameLen, sep="")#( code: 99 )

        print("-" * 90,"\n"*3)

        print("=========> Alter Restuarent Menu ==========>Enter ( Code Number )")
        print("=========> Add New Restuarent    ==========>Enter ( A )")
        print("=========> Go Home Page          ==========>Enter ( H )")

        userInput=input(">>>").upper() #level 2
        self.checkUserInput(2,userInput)

    def showMenuItemsForAdmin(self,user_selection_option):
            self.restuarent_code=user_selection_option
            print("\n" * 10)
            print(">" * 30, "MENU OF", self.res_list[int(user_selection_option) - 1], "<" * 30)
            print("\n" * 2)
            if user_selection_option in self.menu_list:
                print("-" * 100)
                print(" " * 5, "    CODE    ", " " * 25, "ITEMS :        ", " " * 28, "    PRICE: ", sep="")
                print("-" * 100)

                i = 0  # code id for menu items:
                menuItemsForOrder = self.menu_list[user_selection_option]
                for key, value in menuItemsForOrder.items():
                    i += 1
                    itemName = key
                    itemNameLen = 20 - len(key)
                    itemPrice = value
                    itemPriceLen = 4 - len(str(itemPrice))
                    self.menuCodeAndName[str(i)] = key
                    print(" " * 5, "( CODE: ", i, " )", " " * 25, itemName, " " * itemNameLen, " " * 30, itemPrice,
                          " " * itemPriceLen, sep="")

                print("-" * 100, "\n" * 2)
                print("=========> Show Restuarent List ==========>Enter ( S )")
                print("=========> Go Home Page         ==========>Enter ( H )")
                print("=========> Add New Menu Item    ==========>Enter ( A )")
                print("=========> Alter Menu Item      ==========>Enter Code Number")

                userInput=input(">>>").upper() #level 3
                self.checkUserInput(3,userInput)

    def addNewMenuItem(self):
        print("Enter Name and Price [ ex: MenuName1 ,100 ]")
        name,price=input(">>>").split(",")
        self.menu_list[self.restuarent_code][name]=price
        self.showMenuItemsForAdmin(self.restuarent_code)

    def updateMenuItem(self,user_selected_code):
        name=self.menuCodeAndName[user_selected_code]
        price=self.menu_list[self.restuarent_code][name]
        print("Old Name is :",name,"Old Price is :",price)
        print("Enter New Name and Price [Example : New Name1 , New Price ]")
        newName,newPrice=input(">>>").split(",")
        del self.menu_list[self.restuarent_code][name]
        self.menu_list[self.restuarent_code][newName]=newPrice
        self.showMenuItemsForAdmin(self.restuarent_code)

    def addNewRestuarent(self):
        restuarentName=input("Enter New Restuarent Name >>> ")
        totalMenuItem = input("Enter Total Number of Menu Item >>> ")

        while True:
            try:
                if type(int(totalMenuItem)) == int:
                    break
            except ValueError:
                totalMenuItem=input("Enter a Valid Number >>> ")


        tempMenuList={}#creating sub dic for menu item
        for i in range(0,int(totalMenuItem)):
            print("Enter",i+1," Menu Name & Price [ EXAMPLE : Menu name 1 , price ]")

            while True:
                try:
                    menuName, price = input(">>> ").upper().split(",") #splitting user input by comma(,)
                    if type(int(price)) == int: #posibility to throw typeCast erro.So used exception Handling.
                        break
                except ValueError:
                    print("Not a valid data")
                    continue

            tempMenuList[menuName]=int(price)


        self.res_list.append(restuarentName)#adding new restaurant name into restaurantList
        restuarentCode= len(self.res_list)
        self.hotelCode.append(str(restuarentCode))#adding restaurant code
        self.menu_list[str(restuarentCode)]=tempMenuList
        print("\n"*20)
        self.showRestaurantsForAdmin()
