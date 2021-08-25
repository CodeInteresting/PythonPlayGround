# Demo program for Coffee Shop
from datetime import datetime
from datetime import date
import os


def clear():
    os.system('cls')


class Coffee:
    def __init__(
            self, name, place_of_origin, acidity, degree_of_roasting,
            sweetness, price):
        self.name = name
        self.place_of_origin = place_of_origin
        self.acidity = acidity
        self.degree_of_roasting = degree_of_roasting
        self.sweetness = sweetness
        self.price = price

    def __repr__(self) -> str:
        return f"名称：{self.name} | 产地：{self.place_of_origin} \
| 酸度：{self.acidity} | 烘培度：{self.degree_of_roasting} \
| 甜度：{self.sweetness} | 价格: {self.price}"


price_rules = {}


def prepare_price_rules():
    price_rules[5] = discount_on_wed


def discount_on_wed(original_price):
    reason = "周三特惠8折"
    new_price = original_price
    today = date.today()
    if today.weekday() == 2:  # if wednesday
        new_price = original_price * 0.8  # 20% off
    return (new_price, reason)


def loadCoffee():
    dict_of_Coffee = {}
    dict_of_Coffee[1] = Coffee("Espresso", "Italy", 2, 2, 1, 20.0)
    dict_of_Coffee[2] = Coffee("Espresso Macchiato", "Italy", 2, 2, 1, 23.0)
    dict_of_Coffee[3] = Coffee("Americano", "USA", 2, 2, 1, 21.0)
    dict_of_Coffee[4] = Coffee("Flat White", "Malaysia", 2, 2, 1, 25.0)
    dict_of_Coffee[5] = Coffee("Latte", "USA", 2, 2, 1, 29.0)
    dict_of_Coffee[6] = Coffee("Mocha", "USA", 2, 2, 1, 26.0)
    dict_of_Coffee[7] = Coffee("Viennese Coffee", "Austria", 2, 2, 1, 20.0)
    dict_of_Coffee[8] = Coffee("Over the Rainbow", "Hawaii", 2, 2, 1, 34.0)
    return dict_of_Coffee


def print_menu():
    print("===菜单Menu===")
    for id, coffee in loadCoffee().items():
        print(f"{id} - {coffee}")
    print("===End of Menu===")


def print_bill(orders):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    total_price = 0
    print("---账单 Billing note:---")
    print(f"    时间 Time --{dt_string}--")
    for coffee_id, num in orders:
        coffee = coffee_menu[coffee_id]
        if coffee_id in price_rules:   # There is discount
            old_price = coffee.price * num
            current_price, discount_reason = price_rules[coffee_id](old_price)
            print(f"     项目Item：{coffee.name} x {num} 杯cup(s) \
- 原价 RMB {old_price} 折后价 RMB {current_price:.2f} - {discount_reason}")
        else:
            current_price = coffee.price * num
            print(f"     项目Item：{coffee.name} x {num} 杯cup(s) \
- RMB {current_price}")

        total_price += current_price

    print(f"---总计total：RMB {total_price:.2f}")


# init
coffee_menu = loadCoffee()
prepare_price_rules()

# Main Entry
while True:
    clear()
    print_menu()
    orders = []
    while True:
        while True:
            coffee_id = int(
                input(
                    "亲想喝什么咖啡？\
Which Coffee do you want? (Input the id of Coffee): "))

            print()  # blank line
            if coffee_id == 0:
                print_menu()
            else:
                break

        numOfCups = int(
            input("多少杯？ How many cups do you want? (杯数Input number): "))

        print()  # blank line
        orders.append((coffee_id, numOfCups))

        print(f"你点了you ordered: \
{coffee_menu[coffee_id].name} x {numOfCups} 杯cups")
        print()  # blank line

        check = input("结账？Check? y or n: ")
        print()  # blank line
        if check.lower() == "y" or check.lower() == "yes":
            print_bill(orders)
            print()  # blank line
            input("按任意键继续点单 Press Any Key to contine...")
            break
