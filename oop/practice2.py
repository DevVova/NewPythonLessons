# Пример реального расчёта лота позиции для входа в сделку,
# где percentage_of_risk риск в %, а price_step стоимость 1 пункта.
# input_point - точка входа, точка выхода - output_point,
# ну а buy и sell это направления сделки, то есть покупка
# или продажа. size_of_the_deposit - это размер депозита.
def determine_the_lot_from_the_risk(size_of_the_deposit_input, percentage_of_risk, price_step):
    # Размер максимально возможного убытка в пунктах, исходя из стоимости цены.
    max_los_in_points = ((size_of_the_deposit_input / 100) * percentage_of_risk) / price_step

    def transaction_parameters(input_point, output_point, buy, sell):
        size_of_lot = 0
        if buy:
            size_of_lot = max_los_in_points // ((input_point - output_point) * price_step)
        if sell:
            size_of_lot = max_los_in_points // ((output_point - input_point) * price_step)
        return size_of_lot

    return transaction_parameters

size_of_the_deposit = 5000
min_warranty_provision = 2900
# Сначала проверяем достаточно ли средств для торговли.
if min_warranty_provision < size_of_the_deposit:
    gzz5_transaction = determine_the_lot_from_the_risk(size_of_the_deposit, 1, 1)
    lot_for_gzz5_transaction = gzz5_transaction(12000, 11980, True, False)
    print(f"Лот для входа в позицию равен - {lot_for_gzz5_transaction}")
else:
    print("Недостаточно средств.")

#_____________________________________________________________________________

class Car:
    model = "BMW"
    def __init__(self, color, price):
        self.color = color
        self.price = price
        print("Created a new car.")

    def __del__(self):
        print("The car deleted!")

    @classmethod
    def info_car_of_class(cls):
        print(f"The model of car is {cls.model}.")

    @staticmethod
    def wash_car():
        print("I wash a car.")

    def info(self):
        print(f"It's color is {self.color}. And price - {self.price}.")


print("_______________________\n")
toyota = Car("White", 33000)
print(toyota.model)
toyota.model = "Toyota"
print(toyota.model)
toyota.info_car_of_class()
toyota.info()
Car.wash_car()
toyota.wash_car()