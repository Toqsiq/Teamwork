class Product:
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price          # цена в рублях
        self.quantity = quantity    # сколько штук осталось

    def __str__(self):
        return f"{self.name:20} | {self.price:4} ₽ | осталось: {self.quantity}"


class VendingMachine:
    def __init__(self):
        self.products = {
            "1": Product("Вода 0.5л", 50, 10),
            "2": Product("Кола 0.5л", 80, 8),
            "3": Product("Сникерс", 70, 15),
            "4": Product("Чипсы", 90, 6),
            "5": Product("Батончик", 60, 12),
        }
        self.balance = 0  # сколько денег сейчас внесено

    def show_menu(self):
        print("\n" + "=" * 45)
        print("           ВЕНДИНГОВЫЙ АППАРАТ")
        print("=" * 45)
        for code, product in self.products.items():
            print(f"  [{code}]  {product}")
        print("=" * 45)
        print(f"Внесено: {self.balance} ₽")
        print("-" * 45)

    def insert_money(self, amount: int):
        if amount <= 0:
            print("Нельзя внести отрицательную или нулевую сумму!")
            return
        self.balance += amount
        print(f"Внесено {amount} ₽. Текущий баланс: {self.balance} ₽")

    def buy(self, code: str):
        product = self.products.get(code)
        
        if not product:
            print("Такого товара нет!")
            return

        if product.quantity <= 0:
            print(f"Товар «{product.name}» закончился!")
            return

        if self.balance < product.price:
            print(f"Недостаточно средств! Нужно ещё {product.price - self.balance} ₽")
            return

        # Выдаём товар
        product.quantity -= 1
        self.balance -= product.price
        print(f"\n>>> Выдан товар: {product.name}")
        print(f">>> Списано: {product.price} ₽")
        
        if self.balance > 0:
            print(f">>> Ваша сдача: {self.balance} ₽")
            self.balance = 0
        else:
            print(">>> Сдачи нет")

    def return_money(self):
        if self.balance > 0:
            print(f"Возвращено: {self.balance} ₽")
            self.balance = 0
        else:
            print("Нечего возвращать")


# ==================== РАБОТА АППАРАТА ====================

machine = VendingMachine()

while True:
    machine.show_menu()
    print("Команды:")
    print("  деньги <сумма>  — внести деньги (например: деньги 100)")
    print("  купить <код>    — купить товар (например: купить 1)")
    print("  сдача           — вернуть деньги")
    print("  выход           — выключить аппарат")
    print()

    command = input("Введите команду: ").strip().lower()

    if command == "выход":
        machine.return_money()
        print("Аппарат выключен. До свидания!")
        break

    elif command == "сдача":
        machine.return_money()

    elif command.startswith("деньги "):
        try:
            amount = int(command.split()[1])
            machine.insert_money(amount)
        except (IndexError, ValueError):
            print("Ошибка! Пример: деньги 100")

    elif command.startswith("купить "):
        try:
            code = command.split()[1]
            machine.buy(code)
        except IndexError:
            print("Ошибка! Пример: купить 2")

    else:
        print("Неизвестная команда!")
