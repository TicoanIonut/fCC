import collections

def user_menu():
    return int(input("1) Add order to the queue\n"
                     "2) Delete the order from the queue\n"
                     "3) Count orders\n"
                     "4) Output on display\n"
                     "0) Exit the program\n"
                     "?\n"))


def add_order(queue_):
    order_data = dict()
    order_data["name"] = input("Enter the name: ")
    order_data["address"] = input("Enter the address: ")
    order_data["order"] = []
    total_amount = 0
    while True:
        pizza_data = dict()
        pizza_data['name'] = input("Enter the name of the pizza: ")
        pizza_data['cost'] = float(input("Enter the cost of the pizza: "))
        pizza_data['quantity'] = int(input("Enter the quantity: "))
        total_amount += pizza_data["cost"] * pizza_data["quantity"]
        order_data["order"].append(pizza_data)
        if not int(input("Finish order 0-yes 1-no\n")):
            break
    order_data["amount"] = total_amount
    print("Total amount ${}".format(total_amount))
    queue_.append(order_data)


def delete_order(queue_):
    order = queue_.popleft()
    with open('my_order.txt', 'a') as fh:
        fh.write('_'*80 + '\n')
        fh.write("Name {}| Address {}| Total amount {}\n".format(
            order["name"],
            order["address"],
            order["amount"],
        ))
        fh.write('_'*80 + '\n')


def count_orders(queue_):
    print("Number of clients {}".format(len(queue_)))

def output_on_display(queue_):
    temp_queue = queue_.copy()
    counter = 0
    print(len(temp_queue))
    while len(temp_queue):
        order = temp_queue.popleft()
        counter += 1
        print('-'*80)
        print("Order {}".format(counter))
        print("Name {}".format(order["name"]))
        print("Address {}".format(order["address"]))
        print("Total amount {}".format(order["amount"]))
        print('-'*80)
        
MENU_ITEMS = {
    1: add_order,
    2: delete_order,
    3: count_orders,
    4: output_on_display,
}
orders_queue = collections.deque()
while True:
    choice = user_menu()
    if not choice:
        break
    MENU_ITEMS[choice](orders_queue)
    