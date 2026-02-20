class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        s = ""
        for _ in range(self.size):
            s += "🍪"
        return s

    def deposit(self, n):
        if n < 0:
            raise ValueError
        self.size = self.size + n

    def withdraw(self, n):
        if n < 0:
            raise ValueError
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, n):
        if int(n) < 0:
            raise ValueError
        self._capacity = n

    @size.setter
    def size(self, n):
        if int(n) < 0 or int(n) > self.capacity:
            raise ValueError
        self._size = n


def main():
    jar = Jar(10)
    print(jar)

    jar.deposit(5)
    print(jar)

    jar.withdraw(3)
    print(jar)

    try:
        jar.withdraw(3) # trigger exception
    except ValueError:
        print("Couldn't withdraw 3 cookies.")

    try:
        jar.deposit(15) # trigger exception
    except ValueError:
        print("Couldn't deposit 15 cookies.")


if __name__ == "__main__":
    main()
