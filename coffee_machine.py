
class CoffeeMachine:
    def ui_input(self):
        a = input()
        self.make(a)

    def __init__(self):
        self.water, self.milk, self.beans, self.cups, self.money = 400, 540, 120, 9, 550
        self.state = 'action'
        self.ui_input()

    def buy(self, x):
        if x == 'back':
            self.state == 'action'
            print('Write action (buy, fill, take, remaining, exit):')
            return self.ui_input()
        elif int(x) == 1:
            w, b, c = self.water // 250, self.beans // 16, self.cups
            if min(w, b, c) > 0:
                print('I have enough resources, making you a coffee!')
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4
            else:
                print('Sorry, not enough', 'water!' if w == 0 else 'coffee beans!' if b == 0 else 'cups!')
        elif int(x) == 2:
            w, m, b, c = self.water // 350, self.milk // 75, self.beans // 20, self.cups
            if min(w, m, b, c) > 0:
                print('I have enough resources, making you a coffee!')
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7
            else:
                print('Sorry, not enough', 'water!' if w == 0 else 'milk!' if m == 0 else 'coffee beans!' if b == 0 else 'cups!')
        elif int(x) == 3:
            w, m, b, c = self.water // 200, self.milk // 100, self.beans // 12, self.cups
            if min(w, m, b, c) > 0:
                print('I have enough resources, making you a coffee!')
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6
            else:
                print('Sorry, not enough', 'water!' if w == 0 else 'milk!' if m == 0 else 'coffee beans!' if b == 0 else 'cups!')
        print('Write action (buy, fill, take, remaining, exit):')
        self.ui_input()

    def take(self):
        print('I gave you $', self.money)
        self.money = 0
        print('Write action (buy, fill, take, remaining, exit):')
        return self.ui_input()

    def remaining(self):
        print('The coffee machine has:')
        print(self.water, 'of water')
        print(self.milk, 'of milk')
        print(self.beans, 'of coffee beans')
        print(self.cups, 'of disposable cups')
        print(self.money, 'of money')
        print('Write action (buy, fill, take, remaining, exit):')
        return self.ui_input()

    def make(self, xxx):
        if self.state == 'action':
            if xxx == 'buy':
                print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
                self.state = 'buy'
                return self.ui_input()
            elif xxx == 'fill':
                print('Write how many ml of water do you want to add:')
                self.state = 'fill water'
                return self.ui_input()
            elif xxx == 'take':
                return self.take()
            elif xxx == 'remaining':
                return self.remaining()
            elif xxx == 'exit':
                self.state = None
                return None
        elif self.state == 'buy':
            self.state = 'action'
            return self.buy(xxx)
        elif self.state == 'fill water':
            self.water += int(xxx)
            print('Write how many ml of milk do you want to add:')
            self.state = 'fill milk'
            return self.ui_input()
        elif self.state == 'fill milk':
            self.milk += int(xxx)
            print('Write how many grams of coffee beans do you want to add:')
            self.state = 'fill beans'
            return self.ui_input()
        elif self.state == 'fill beans':
            self.beans += int(xxx)
            print('Write how many disposable cups of coffee do you want to add:')
            self.state = 'fill cups'
            return self.ui_input()
        elif self.state == 'fill cups':
            self.cups += int(xxx)
            print('Write action (buy, fill, take, remaining, exit):')
            self.state = 'action'
            return self.ui_input()


print('Write action (buy, fill, take, remaining, exit):')
auto1 = CoffeeMachine()
# auto1.make(input())


# def fill():
#     global water, milk, beans, cups
#     print('Write how many ml of water do you want to add:')
#     water = water + int(input())
#     print('Write how many ml of milk do you want to add:')
#     milk = milk + int(input())
#     print('Write how many grams of coffee beans do you want to add:')
#     beans = beans + int(input())
#     print('Write how many disposable cups of coffee do you want to add:')
#     cups = cups + int(input())
# actions = {
#     'buy': buy,
#     'fill': fill,
#     'take': take,
#     'remaining': remaining
# }
