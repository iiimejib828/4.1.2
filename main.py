# Класс Store для работы с магазинами
class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    # добавить товар
    def add_item(self, item_name, price):
        self.items[item_name] = price

    #удалить товар
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    # получить цену товара
    def get_price(self, item_name):
        return self.items.get(item_name, None)

    # изменить цену товара
    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

    # получить полную информацию о товаре
    def __repr__(self):
        return f"Store('{self.name}', Address: {self.address}, Items: {self.items})"


# Тестирование класса Store
store1 = Store("Продуктовый Магазин", "ул. Ленина, 5")
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

store2 = Store("ТехноМаркет", "ул. Гагарина, 10")
store2.add_item("phone", 300)
store2.add_item("laptop", 1500)

store3 = Store("Одежда и Обувь", "ул. Мира, 25")
store3.add_item("t-shirt", 20)
store3.add_item("jeans", 50)

# Вывод списка созданных магазинов
print("\n".join(["Список магазинов:", str(store1), str(store2), str(store3)]))

# Тестирование методов магазина
print("\nМагазин 1:", store1)
store1.add_item("oranges", 1.2)
print("\nПосле добавления товара:")
print(store1)

store1.update_price("apples", 0.6)
print("\nПосле обновления цены на яблоки:")
print(store1)

store1.remove_item("bananas")
print("\nПосле удаления бананов:")
print(store1)

price_of_oranges = store1.get_price("oranges")
print(f"\nЦена апельсинов: {price_of_oranges}")
