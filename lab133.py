class NUMBERS:
    def __init__(self, oddnums=None, evennums=None, currentind=None):
        self.oddnums = oddnums or []
        self.evennums = evennums or []
        self.currentind = currentind or []

    def add_num(self, num):
        if isinstance(num, (int, float)):
            if num % 2 == 0:
                self.evennums.append(num)
            else:
                self.oddnums.append(num)
            self.currentind.append(num)

    def del_num(self, num):
        if num in self.evennums:
            self.evennums.remove(num)
        elif num in self.oddnums:
            self.oddnums.remove(num)
        self.currentind.remove(num)

    def alter_num(self, oldnum, newnum):
        if oldnum in self.evennums:
            self.evennums.remove(oldnum)
            self.add_num(newnum)
        elif oldnum in self.oddnums:
            self.oddnums.remove(oldnum)
            self.add_num(newnum)
        index = self.currentind.index(oldnum)
        self.currentind[index] = newnum

    def search_num(self, num):
        return num in self.currentind

    def print_nums(self):
        output = []
        for i in range(min(len(self.oddnums), len(self.evennums))):
            output.append(self.oddnums[i])
            output.append(self.evennums[i])

        if len(self.oddnums) > len(self.evennums):
            output.extend(self.oddnums[len(self.evennums):])
        elif len(self.evennums) > len(self.oddnums):
            output.extend(self.evennums[len(self.oddnums):])

        print(output)

    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        if self.a < len(self.currentind):
            result = self.currentind[self.a]
            self.a += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.currentind[index]

    def __setitem__(self, index, value):
        self.currentind[index] = value


def main():
    n = NUMBERS()
    n.add_num(2)
    n.add_num(51)
    n.add_num(6)
    n.add_num(5.4)
    n.add_num(5.9)
    n.add_num(92)
    n.add_num(11)
    n.add_num(0)
    n.print_nums()
    print()
    c = n[1]
    print(c)
    print()
    n[1] = 400
    it = iter(n)
    print(next(it))
    print(next(it))
    n.del_num(11)
    n.alter_num(92, 13)
    n.search_num(5.9)
    n.print_nums()


main()
