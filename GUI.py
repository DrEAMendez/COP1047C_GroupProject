from tkinter import *
from PIL import ImageTk, Image




# Main Instance
pizza = Tk()
pizza.geometry('600x700')
pizza.title("Salcedo's Pizza Shop")

'''
        0           1           2           3
0   
1
2   Name:          Entry
3   Phone:         Entry
4   
5                                          Logo
6   Toppings:      List                    Chef
7   Select Drink   (One size)                        
8                  
9   Add Drink:     Add Pizza               Checkout
10  dkOrder        pzOrder         


'''
#Initialize variables
subTotal= 0
pzOrder = []
dkOrder = []
toppingLst = []
toppingCt = 0
totalPz = 0
dkTotal = 0

#Button Functionality

#running order
def showOrder():
    order_lbl = Label(pizza, text="========\nYour Order:\n========")
    order_lbl.grid(row=9, column=0)

    dkOrder_lbl = Label(pizza, text= dkOrder)
    dkOrder_lbl.grid(row=9, column=1)


# def add_pizza():
#     result= ""
#     toppingCt = 0
#     for topping in pizza_toppings.curselection():
#         
#         result = result + str(pizza_toppings.get(topping)) + "\n"

#         add_lbl.config(text="Your Topping Selection: " + "\n" + result)

def add_pizza():
    global totalPz
    global toppingLst

    for topping in pizza_toppings.curselection():
        toppingLst.append(topping)
    totalPz += 1

    return show_pzOrder(pzOrder)

def show_pzOrder(order):
    toppingCt = 0
    #topping count
    for toppings in toppingLst:
        toppingCt +=1

    #string construction
    pzOutput = f'\nPizza(s): {totalPz}\n========\nExtra Topping(s): {toppingCt}'

    #output
    # print(dkOutput)
    pz_lbl = Label(pizza, text=str(pzOutput))
    pz_lbl.grid(row=10, column=1)


def add_drink():
    global dkOrder
    dkSelection = drinks.get()
    dkOrder.append(dkSelection)
    return show_dkOrder(dkOrder)

def show_dkOrder(order):
    #initialize variables
    ColaCt = 0
    KolaCt = 0
    BeerCt = 0
    PiscoCt = 0
    ChicaCt = 0
    
    #loop through order
    for obj in order:
      if obj =="Coca-Cola":
        ColaCt += 1
      elif obj == "Inca Kola":
        KolaCt += 1
      elif obj =="Beer":
        BeerCt += 1
      elif obj == "Pisco":
        PiscoCt += 1
      elif obj == "Chica":
        ChicaCt += 1
      dkTotal = ColaCt + KolaCt + BeerCt + PiscoCt + ChicaCt

    #string construction
    dkOutput = f'\nTotal Drinks: {dkTotal}\n==========\n{ColaCt} Coca-Cola(s)\n{KolaCt} Inca Kola(s)\n{BeerCt} Beer(s)\n{PiscoCt} Pisco(s)\n{ChicaCt} Chica(s)'

    #output
    # print(dkOutput)
    dk_lbl = Label(pizza, text=str(dkOutput))
    dk_lbl.grid(row=10, column=0)

def checkout():
    fName = fname_entry.get() 
    lName = lname_entry.get()
    discountRate = 0
    if lName =="Salcedo":
        if fName == "Eduardo":
            discountRate = 1
        else:
            discountRate = 0.10
    else:
        discountRate = 0

    preDiscountSubtotal = (dkTotal*2.5) + (totalPz * 12.99) + (toppingCt)
    discount = preDiscountSubtotal * discountRate
    subtotal = preDiscountSubtotal - discount
    taxrate = .07
    tax = subtotal * .07
    total = subtotal * (1+ tax) 

    # custName = name_entry.get()
    # new_lbl = Label(pizza, text= "Name: " + text1)
    # new_lbl.grid(row=8, column=3)

    # text2 = phone_entry.get()
    # new_lbl2 = Label(pizza, text = text2)
    # new_lbl2.grid(row=9, column=3)

    totals = f"Subtotal: ${preDiscountSubtotal:.2f}\nDiscount ({discountRate*100:.0f}%): (${discount:.2f})\nTax ({taxrate*100:.0f}%): ${tax:.2f}\n\nTOTAL: ${total:.2f}"
    new_lbl2 = Label(pizza, text = totals)
    new_lbl2.grid(row=10, column=3)

# def clearOrder ():
#     pizza_toppings.delete(0, 5)


# name Entry
name_label = Label(pizza, text ="First Name: ")
name_label.grid(row=2, column=0)

fname_entry = Entry(pizza, width = 30)
fname_entry.grid(row=2, column= 1)

# phone Entry
lname_label = Label(pizza, text ="Last Name: ")
lname_label.grid(row=3, column=0)

lname_entry = Entry(pizza, width = 30)
lname_entry.grid(row=3, column= 1)

# Toppings Title 
toppings_text = Label(pizza, text= "Extra Toppings: \n        $0.99/ea")
toppings_text.grid(row = 6, column=0)

# Pizza toppings
my_pizza_toppings = ["Corn", "Shrimp", "Olives", "Broccoli", "Pineaple", "Sausage", "Pico de Gallo", "Lomo Saltado"]

pizza_toppings = Listbox(pizza, selectmode= MULTIPLE, bg="gray", fg="white")
pizza_toppings.grid(row=6, column=1)

for topping in my_pizza_toppings:
    pizza_toppings.insert(0, topping)

add_lbl = Label(pizza, text="")
add_lbl.grid(row=7, column=1)

# remove_button = Button(pizza, text="Clear Order", command = clearOrder)
# remove_button.grid(row=8,column=3)

#size dropdown
# pizzaSizes = StringVar()

# pizzaSize = OptionMenu(pizza, pizzaSizes, "Small ($8.99)", "Medium ($10.99)", "Large ($13.99)", "X-Large ($15.99)")
# pizzaSizes.set("Choose a size")
# pizzaSize.grid(row=7, column=1)

#drinks drop-down
drinks = StringVar()

drink = OptionMenu(pizza, drinks, "Coca-Cola", "Inca Kola", "Beer",  "Pisco", "Chica")
drinks.set("Select Drinks")
drink.grid(row=7, column=0)
dkSelection = drinks.get()

#order buttons
clr_toppings = Button(pizza, text="Clear Toppings", command= lambda: pizza_toppings.selection_clear(0, 'end'))
clr_toppings.grid(row=7, column=1)

addPz_button = Button(pizza, text="Add Pizza\n($12.99)", command= add_pizza)
addPz_button.grid(row=9, column=1)

addDk_button = Button(pizza, text="Add Drink\n($2.50)", command= add_drink)
addDk_button.grid(row=9, column=0)

checkout_button = Button(pizza, text="Checkout", command= checkout)
checkout_button.grid(row=7, column=3)


#Chef Picture
# chef_path = "C:\Users\emendez\Documents\Coding\MDC"
chef_pic = ImageTk.PhotoImage(Image.open("chef_smallest.png"))
pic_lbl = Label(pizza, image=chef_pic)
pic_lbl.grid(row=6, column=3)

#logo
logo_pic = ImageTk.PhotoImage(Image.open("logo.png"))
pic_lbl2 = Label(pizza, image=logo_pic)
pic_lbl2.grid(row=5, column=3)

#Main
pizza.mainloop()
