# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import restaurent
def print_welcome_notes(name):
    # Use a breakpoint in the code line below to debug your script.
    print("\n"*2,f'Hi Buddy...Welcome To  {name}',"\n"*2)
    #print(">"*31,'THESE ALL ARE OUR RESTUARANTS',"<"*31,"\n"*2)

    # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_welcome_notes('Swiggy')

    r1=restaurent.Restaurant()#creating instance
    r1.displayHomeContent()
    #r1.showRestaurants()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/