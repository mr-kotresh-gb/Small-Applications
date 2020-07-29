from tkinter import *
import time
import datetime
from tkinter import ttk


msg1 = "Hello! Welcome to our hotel..."

text1 = ""
n = 0

# ===========================Calculator Functions=============================
def btn(numbers):
    global operator
    operator = operator + str(numbers)
    txt_input.set(operator)


def clear():
    global operator
    operator = ''
    txt_input.set('')
    Display.insert(0, 'Start calculating...')


def equal():
    global operator
    sum_up = float(eval(operator))
    txt_input.set(sum_up)
    operator = ''

# ================================Total Function==============================
def total_result():
    verme1 = Meal_dicator.get()
    verme2 = Meal1.get()
    if verme1 == 'Fried Rice':
        verme3 = (verme2*30)
        Cost.set(verme3)
    elif verme1 == 'Idli Sambar':
        verme3 = (verme2*30)
        Cost.set(verme3)
    elif verme1 == 'Paneer Masala':
        verme3 = (verme2 * 150)
        Cost.set(verme3)
    elif verme1 == 'Paneer Kabab':
        verme3 = (verme2 * 150)
        Cost.set(verme3)
    elif verme1 == 'Matar Thali':
        verme3 = (verme2 * 100)
        Cost.set(verme3)
    elif verme1 == 'Dosa (Butter)':
        verme3 = (verme2 * 50)
        Cost.set(verme3)
    elif verme1 == 'Shahi Paneer':
        verme3 = (verme2 * 200)
        Cost.set(verme3)
    elif verme1 == 'Malai Kofta':
        verme3 = (verme2 * 50)
        Cost.set(verme3)
    elif verme1 == 'Tandoori Roti':
        verme3 = (verme2 * 15)
        Cost.set(verme3)
    elif verme1 == 'Roomali Roti':
        verme3 = (verme2 * 20)
        Cost.set(verme3)
    elif verme1 == 'Butter Roti':
        verme3 = (verme2 * 15)
        Cost.set(verme3)
    elif verme1 == 'Soya Dum Biryani':
        verme3 = (verme2 * 80)
        Cost.set(verme3)
    elif verme1 == 'Manchurian Gravy':
        verme3 = (verme2 * 70)
        Cost.set(verme3)
    else:
        verme3 = (verme2 * 0.0)
        Cost.set(verme3)

    verdi1 = Drink_dicator.get()
    verdi2 = Drink1.get()
    if verdi1 == 'Coca cola':
        verdi3 = (verdi2 * 30)
        Drinks.set(verdi3)
    elif verdi1 == 'Thumbs up':
        verdi3 = (verdi2 * 30)
        Drinks.set(verdi3)
    elif verdi1 == 'Pepsi':
        verdi3 = (verdi2 * 20)
        Drinks.set(verdi3)
    elif verdi1 == 'Orange':
        verdi3 = (verdi2 * 25)
        Drinks.set(verdi3)
    else:
        verdi3 = (verdi2 * 0.0)
        Drinks.set(verdi3)

    # =============Delivery cost============
    num1 = float(Cost.get())
    num2 = float(Drinks.get())
    delivery = (num1 + num2) * 0.2

    # =============Cost of room============
    room = v.get()
    null = 0.0

    rvip = 1800.0  # Cost of A/C room
    rvip1 = delivery/(1800*0.5)  # A/C room delivery cost

    rnormal = 1000.0  # Cost of non A/C room
    rnormal1 = delivery/(1000*2.5)  # Non A/C room delivery cost

    if room == 1:
        if chkb1.get() == 1:
            ServiceCharge.set(rvip1)
            RoomCost.set(1800.0)
            DevCost.set(delivery)
        else:
            ServiceCharge.set(null)
            DevCost.set(null)
            RoomCost.set(1800.0)

    elif room == 2:
        if chkb1.get() == 1:
            ServiceCharge.set(rnormal1)
            RoomCost.set(1000.0)
            DevCost.set(delivery)
        else:
            ServiceCharge.set(null)
            DevCost.set(null)
            RoomCost.set(1000.0)

    elif room == 3:
        if chkb1.get() == 1:
            ServiceCharge.set(null)
            RoomCost.set(null)
            DevCost.set(null)
        else:
            ServiceCharge.set(null)
            DevCost.set(null)
            RoomCost.set(null)

    # ===================Total Result=====================
    num3 = float(DevCost.get())
    num4 = float(RoomCost.get())
    num5 = float(ServiceCharge.get())

    my_total = num1 + num2 + num3 + num4 + num5
    Total.set(my_total)
    final_total = "Rs", my_total

    num6 = Total.get()
    Display.delete(0, END)
    Display.insert(0, final_total)

    if num6 == '0.0':
        Display.delete(0, END)
        Display.insert(0, 'Please make an order...')


def convert():
    var2 = indicator.get()
    var3 = var1.get()
    if var2 == 'Australia':
        Display.delete(0, END)
        var4 = ('AUS_dollar', (var3 / 53.09))
        Display.insert(0, var4)
    elif var2 == 'France':
        Display.delete(0, END)
        var4 = ('Euro', (var3 / 87.93))
        Display.insert(0, var4)
    elif var2 == 'Mexico':
        Display.delete(0, END)
        var4 = ('Mexican_peso', (var3 / 3.41))
        Display.insert(0, var4)
    elif var2 == 'USA':
        Display.delete(0, END)
        var4 = ('US_Dollar', (var3 / 74.8))
        Display.insert(0, var4)
    elif var2 == 'India':
        Display.delete(0, END)
        var4 = ('Rupee', (var3 * 1.0))
        Display.insert(0, var4)
    else:
        Display.delete(0, END)
        Display.insert(0, 'Error: Select a country!')

# ===================Reset Button========================================
def hotel():
    Display.delete(0, END)
    Display.insert(0, 'Hotel management sys.')


def powered():
    Display.delete(0, END)
    Display.insert(0, 'Powered by Mr.KGB')


def reset():
    Display.delete(0, END)
    Display.insert(0, 'System resetting...')
    Display.after(2000, hotel)
    Display.after(4000, powered)
    Display.after(6000, rest)


def rest():
    clear()
    Display.delete(0, END)
    Display.insert(0, 'Hello! Welcome')
    Meal_dicator.set(value='Delicious Meal')
    Drink_dicator.set(value='Fresh Drink')
    indicator.set(value='Choose a country')
    txtQtyofmeal.delete(0, END)
    txtQtyofmeal.insert(0, 0)
    txtQtyofDrink.delete(0, END)
    txtQtyofDrink.insert(0, 0)
    txtAmount.delete(0, END)
    txtAmount.insert(0, 0)
    RoomCost.set(0.0)
    Total.set(0.0)
    ServiceCharge.set(0.0)
    Drinks.set(0.0)
    Cost.set(0.0)
    chkb1.set(0.0)
    v.set(3)
    DevCost.set(0.0)

# ======================Clear button==========================
def clear_screen():
    Display.delete(0, END)
    RoomCost.set('')
    Total.set('')
    ServiceCharge.set('')
    Drinks.set('')
    Cost.set('')
    DevCost.set('')

# =======================Exit=================================
def stop():
    root.destroy()


def Exit():
    Display.delete(0, END)
    Display.insert(0, 'Thanks for patronage...')
    Display.after(3000, stop)


def tick():
    d = datetime.datetime.now()
    today = '{:%B %d, %Y}'.format(d)

    my_time = time.strftime('%I:%M:%S%p')
    lblInfo.config(text=(my_time+' '+today))
    lblInfo.after(200, tick)

# ========================scroll function============================
def display():
    global text1, n, msg1
    for t in range(len(msg1)):
        # j = t
        for k in range(len(msg1) - t):
            text1 += ' '
        for g in range(t+1):
            text1 += msg1[g]
            # j = j+1
        text1 = text1.strip()
        f2.update()
        f2.after(100)
        # text1 = text1.strip()
        scroll_text.set('')
        scroll_text.set(text1)
        text1 = ''
    scroll_text.set('')
    txtscroll.after(200, display)


root = Tk()
root.geometry('1600x800+0+0')
root.title("Hotel Management System")

# ======================Window's Partition======================
Tops = Frame(root, width=1600, height=100, bg='black', relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=300, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

f3 = Frame(root, width=35, height=700, relief=SUNKEN)
f3.pack(side=LEFT)

f4 = Frame(root, width=100, height=700, relief=SUNKEN)
f4.pack(side=LEFT)

# ====================================Main Screen=======================================
txt_input = StringVar(value='Hello!..')
Display = Entry(Tops, font=('arial', 97, 'bold'), fg='chartreuse2', bd=50, bg='black',
                justify='right', textvariable=txt_input)
Display.grid(columnspan=4)

# =====================================Date and Time====================================
lblInfo = Label(f2, font=('arial', 13, 'bold'),  fg='dark blue', bd=3, anchor=W)
lblInfo.grid(row=1, column=0, columnspan=4)
tick()

# ======================================Row 1============================================
operator = ''
btn7 = Button(f2, padx=13, pady=4, bd=8, font=('arial', 30, 'bold'), text='7',
              command=lambda: btn(7)).grid(row=2, column=0)
btn8 = Button(f2, padx=13, pady=4, bd=8, font=('arial', 30, 'bold'), text='8',
              command=lambda: btn(8)).grid(row=2, column=1)
btn9 = Button(f2, padx=13, pady=4, bd=8, font=('arial', 30, 'bold'), text='9',
              command=lambda: btn(9)).grid(row=2, column=2)
btnC = Button(f2, padx=13, pady=4, bd=8, font=('arial', 30, 'bold'), text='C', bg='red2',
              command=clear).grid(row=2, column=3)

# ======================================Row 2============================================
btn4 = Button(f2, padx=13, pady=4, bd=8, font=('arial', 30, 'bold'), text='4',
              command=lambda: btn(4)).grid(row=3, column=0)
btn5 = Button(f2, padx=13, pady=4, bd=8, font=('arial', 30, 'bold'), text='5',
              command=lambda: btn(5)).grid(row=3, column=1)
btn6 = Button(f2, padx=13, pady=4, bd=8, font=('arial', 30, 'bold'), text='6',
              command=lambda: btn(6)).grid(row=3, column=2)
btn_plus = Button(f2, padx=18, pady=4, bd=8, font=('arial', 30, 'bold'), text='+', bg='blue2',
                  command=lambda: btn('+')).grid(row=3, column=3)

# ======================================Row 3============================================
btn1 = Button(f2, padx=13, pady=4, bd=8, font=('arial', 30, 'bold'), text='1',
              command=lambda: btn(1)).grid(row=4, column=0)
btn2 = Button(f2, padx=13, pady=4, bd=8, font=('arial', 30, 'bold'), text='2',
              command=lambda: btn(2)).grid(row=4, column=1)
btn3 = Button(f2, padx=13, pady=4, bd=8, font=('arial', 30, 'bold'), text='3',
              command=lambda: btn(3)).grid(row=4, column=2)
btn_minus = Button(f2, padx=23, pady=5, bd=8, font=('arial', 30, 'bold'), text='-', bg='blue2',
                   command=lambda: btn('-')).grid(row=4, column=3)

# ======================================Row 4============================================
btn0 = Button(f2, padx=13, pady=4, bd=8, font=('arial', 30, 'bold'), text='0',
              command=lambda: btn(0)).grid(row=5, column=0)
btn_dot = Button(f2, padx=21, pady=5, bd=8, font=('arial', 30, 'bold'), text='.', bg='blue2',
                 command=lambda: btn('.')).grid(row=5, column=1)
btn_division = Button(f2, padx=20, pady=5, bd=8, font=('arial', 30, 'bold'), text='/', bg='blue2',
                      command=lambda: btn('/')).grid(row=5, column=2)
btn_multiply = Button(f2, padx=19, pady=5, bd=8, font=('arial', 30, 'bold'), text='x', bg='blue2',
                      command=lambda: btn('*')).grid(row=5, column=3)

# ======================================Row 5============================================
btn_equals = Button(f2, padx=64, pady=2, bd=8, font=('arial', 30, 'bold'),
                    text='=', bg='green', command=equal).grid(row=6, column=0, columnspan=2)
btn_open_bracket = Button(f2, padx=19, pady=2, bd=8, font=('arial', 30, 'bold'),
                          text='(', bg='blue2', command=lambda: btn('(')).grid(row=6, column=2)
btn_close_bracket = Button(f2, padx=23, pady=2, bd=8, font=('arial', 30, 'bold'),
                           text=')', bg='blue2', command=lambda: btn(')')).grid(row=6, column=3)

# =====================================choose meal========================================
Meal1 = IntVar()
Meal_dicator = StringVar(value='Delicious Meals')

lbl_Meal = Label(f1, font=('arial', 16, 'bold'), text='Choose Meal', bd=10, anchor=W)
lbl_Meal.grid(row=0, column=0)
txt_meal = ttk.Combobox(f1, font=('arial', 16, 'bold'), textvariable=Meal_dicator)
txt_meal['values'] = ('Fried Rice', 'Idli Sambar', 'Paneer Masala', 'Paneer Kabab', 'Matar Thali', 'French Fries',
                      'Dosa (Butter)', 'Shahi Paneer', 'Malai Kofta', 'Tandoori Roti', 'Roomali Roti', 'Butter Roti',
                      'Manchurian Gravy', 'Soya Dum Biryani')
txt_meal.grid(row=0, column=1)

lbl_Q_meal = Label(f1, font=('arial', 16, 'bold'), text='Qty. of Meal', bd=10, anchor=W)
lbl_Q_meal.grid(row=1, column=0)
txtQtyofmeal = Entry(f1, font=('arial', 16, 'bold'), textvariable=Meal1, bd=10, insertwidth=4, bg='white', justify='right')
txtQtyofmeal.grid(row=1, column=1)

# ======================================Choose drinks=======================================
Drink1 = IntVar()
Drink_dicator = StringVar(value='Fresh Drinks')

lbl_Drink = Label(f1, font=('arial', 16, 'bold'), text='Choose Drink', bd=10, anchor=W)
lbl_Drink.grid(row=2, column=0)
txt_Drink = ttk.Combobox(f1, font=('arial', 16, 'bold'), textvariable=Drink_dicator)
txt_Drink['values'] = ('Coca cola', 'Thumbs up', 'Pepsi', 'Orange')
txt_Drink.grid(row=2, column=1)

lbl_Q_Drink = Label(f1, font=('arial', 16, 'bold'), text='Qty. of Drink', bd=10, anchor=W)
lbl_Q_Drink.grid(row=3, column=0)
txtQtyofDrink = Entry(f1, font=('arial', 16, 'bold'), textvariable=Drink1, bd=10, insertwidth=4, bg='white', justify='right')
txtQtyofDrink.grid(row=3, column=1)

# =====================================Order Delivery====================================
chkb1 = IntVar()
lblHomeDev = Label(f1, font=('arial', 16, 'bold'), text='Order Delivery', bd=10, anchor=W)
lblHomeDev.grid(row=4, column=0)
check1 = Checkbutton(f1, text='yes', variable=chkb1, font=('arial', 16, 'bold'))
check1.grid(row=4, column=1)

# ====================================Book a Room=======================================
v = IntVar()
v.set(3)
lblRoom = Label(f1, font=('arial', 16, 'bold'), text='Book a Room', bd=10, anchor=W)
lblRoom.grid(row=5, column=0)
MyRadios = Radiobutton(f1, text='A/C', font=('arial', 16, 'bold'), variable=v, value=1)
MyRadios.grid(row=5, column=1, sticky=W)
MyRadios = Radiobutton(f1, text='Non A/C', font=('arial', 16, 'bold'), variable=v, value=2)
MyRadios.grid(row=5, column=1)
MyRadios = Radiobutton(f1, text='No', font=('arial', 16, 'bold'), variable=v, value=3)
MyRadios.grid(row=5, column=1, sticky=E)

# ====================================Cost Display Screens====================================
Cost = StringVar()
lblMeal1 = Label(f1, font=('arial', 16, 'bold'), text='Cost of Meal(Rs)', bd=16, anchor=W)
lblMeal1.grid(row=0, column=2)
txtMeal1 = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cost, fg='white', bd=10, insertwidth=4,
                 bg='black', justify='right')
txtMeal1.grid(row=0, column=3)

Drinks = StringVar()
lblDrink1 = Label(f1, font=('arial', 16, 'bold'), text='Cost of Drink(Rs)', bd=16, anchor=W)
lblDrink1.grid(row=1, column=2)
txtDrink1 = Entry(f1, font=('arial', 16, 'bold'), textvariable=Drinks, fg='white', bd=10, insertwidth=4,
                  bg='black', justify='right')
txtDrink1.grid(row=1, column=3)

DevCost = StringVar()
lblDev = Label(f1, font=('arial', 16, 'bold'), text='Delivery Cost(Rs)', bd=16, anchor=W)
lblDev.grid(row=2, column=2)
txtDev = Entry(f1, font=('arial', 16, 'bold'), textvariable=DevCost, fg='white', bd=10, insertwidth=4,
               bg='black', justify='right')
txtDev.grid(row=2, column=3)

RoomCost = StringVar()
lblRoom = Label(f1, font=('arial', 16, 'bold'), text='Cost of Room(Rs)', bd=16, anchor=W)
lblRoom.grid(row=3, column=2)
txtRoom = Entry(f1, font=('arial', 16, 'bold'), textvariable=RoomCost, fg='white', bd=10, insertwidth=4,
                bg='black', justify='right')
txtRoom.grid(row=3, column=3)

ServiceCharge = StringVar()
lblFees = Label(f1, font=('arial', 16, 'bold'), text='Service Fee(Rs)', bd=16, anchor=W)
lblFees.grid(row=4, column=2)
txtFees = Entry(f1, font=('arial', 16, 'bold'), textvariable=ServiceCharge, fg='white', bd=10, insertwidth=4,
                bg='black', justify='right')
txtFees.grid(row=4, column=3)

Total = StringVar()
lblTotal = Label(f1, font=('arial', 16, 'bold'), text='Total Cost(Rs)', bd=16, anchor=W)
lblTotal.grid(row=5, column=2)
txtTotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=Total, fg='white', bd=10, insertwidth=4,
                 bg='black', justify='right')
txtTotal.grid(row=5, column=3)

# ========================================Currency Converter====================================================
var1 = IntVar()
indicator = StringVar(value='Choose a Country')
lblCurCun = Label(f1, font=('arial', 16, 'bold italic'),
                  text='------------------------------------ Currency Converter --------------------------------------',
                  bd=20, anchor=W)
lblCurCun.grid(row=6, column=0, columnspan=4)

lblCountry = Label(f1, font=('arial', 16, 'bold'), text='Nationality', bd=20, anchor=W)
lblCountry.grid(row=7, column=0)
txtCountry = ttk.Combobox(f1, font=('arial', 16, 'bold'), textvariable=indicator)
txtCountry['values'] = ('India', 'Australia', 'France', 'Mexico', 'USA')
txtCountry.grid(row=7, column=1)

lblAmount = Label(f1, font=('arial', 16, 'bold'), text='Amount(Rs)', bd=20, anchor=W)
lblAmount.grid(row=7, column=2)
txtAmount = Entry(f1, font=('arial', 16, 'bold'), textvariable=var1, bd=10, insertwidth=4, bg='white', justify='right')
txtAmount.grid(row=7, column=3)

# ===========================================Control buttons==========================================
btnConvert = Button(f1, padx=10, pady=4, bd=16, fg='white', font=('arial', 16, 'bold'), width=10, text='Convert',
                    bg='orange', command=convert)
btnConvert.grid(row=8, column=2)

btnTotal = Button(f4, padx=10, pady=8, bd=16, fg='white', font=('arial', 16, 'bold'), width=10, text='Total',
                  bg='orange', command=total_result)
btnTotal.grid(row=0, column=0)

btnScreen = Button(f4, padx=10, pady=8, bd=16, fg='white', font=('arial', 16, 'bold'), width=10, text='Clear',
                   bg='blue', command=clear_screen)
btnScreen.grid(row=1, column=0)

btnReset = Button(f4, padx=10, pady=8, bd=16, fg='white', font=('arial', 16, 'bold'), width=10, text='Reset',
                  bg='green', command=reset)
btnReset.grid(row=2, column=0)

btnExit = Button(f4, padx=10, pady=8, bd=16, fg='white', font=('arial', 16, 'bold'), width=10, text='Exit',
                 bg='red', command=Exit)
btnExit.grid(row=3, column=0)

# ==========================================Logo===========================================
photo = PhotoImage(file='logo.png')
myphoto = Label(f1, image=photo)
myphoto.grid(row=8, column=0)

# ========================================Movable Text===================================
scroll_text = StringVar()
txtscroll = Entry(f2, textvariable=scroll_text, font=('arial', 14, 'bold'), fg='white', bd=10, bg='black', width=32)
txtscroll.grid(row=0, column=0, columnspan=4)
display()



root.mainloop()
