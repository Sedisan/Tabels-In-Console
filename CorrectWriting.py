class ConstantValues:
    # from ProvideLengthOfTable import ProvideLength
    from shutil import get_terminal_size

    @staticmethod
    def separating():
        # separating = ConstantValues.ProvideLength().get_length_of_x() - 8
        separating = ConstantValues.get_terminal_size()[1] - 20
        if separating > 30:
            separating = 10
        return separating


class ConvertType:
    def change_dict_to_list(self, d):
        result = list(self.__change_dict_to_list(d, 0))
        keys = [x for x in result if x in d.keys()]
        values = list(filter(lambda x: x not in d.keys(), result))
        return list((keys, values))

    def __change_dict_to_list(self, d, flage=1):
        if flage:
            raise Exception("Using dunder not allowed")
        for value in d.items():
            yield from value

    def change_l_to_dict(self, l):
        return dict(zip(l[0], l[1]))


class Separate:
    def sep_by_number(self, what, number=ConstantValues.separating()):
        result = []
        for i in range(0, len(what), number):
            temp = what[i:i + number].strip()
            #        if temp.startswith(' '):
            #            temp = what[i+1:i+number]
            #        if temp.endswith(' '):
            #            temp = what[i:i+number-1]
            result.append(temp)
        return result

    def connect_all_days(self, *all_days):
        result = list(zip(*all_days[0]))
        return result


class Fill:
    def fill_elements(self, what, sep=ConstantValues.separating()):
        maximum = max([len(x) for x in what])
        for i in what:
            for j in range(0, maximum):
                if len(i) < maximum:
                    for n in range(len(i), maximum):
                        i.append(' ' * sep)
                if len(i[j]) < sep:
                    calculated_length = sep - len(i[j])
                    copied = i[j]
                    i.pop(j)
                    after = str(copied) + ' ' * calculated_length
                    i.insert(j, after)

    @staticmethod
    def fill_default(one_day_separate=ConstantValues.separating()):
        names = "Monday Tuesday Wednesday Thursday Friday Saturday Sunday"
        names = names.split()
        default_list = dict(zip([x for x in names], [' ' * one_day_separate] * 7))
        return default_list


class Printing:
    def print_separator(self, sep=ConstantValues.separating()):
        seven_days = sep * 7
        separator_counter = 7 + 1
        print('-' * (seven_days + separator_counter))

    def print_separator_for_days(self, sep=ConstantValues.separating()):
        seven_days = sep * 7
        separator_counter = 6
        print('|', end='')
        print('-' * (seven_days + separator_counter), end='')
        print('|', end='')
        print()

    def print_correct(self, what):
        for i in what:
            for j in i:
                print('|' + j, end='')
            print('|')
        self.print_separator_for_days()

    def print_correct_for_days(self, what, sep=ConstantValues.separating()):
        for i in what:
            for j in i:
                print('|' + str(j).center(sep), end='')
            print('|')
        self.print_separator_for_days()


class SpinAll:
    counter = 0

    def __init__(self):
        self.convert = ConvertType()
        self.printing = Printing()
        self.separate = Separate()
        self.fill = Fill()
        self.all_days = self.fill.fill_default()

    def set_choose_day(self, day, what):
        self.all_days[day] = what

    def spin_text(self):
        l_days = self.convert.change_dict_to_list(self.all_days)
        new_table_with_data = []
        for i in l_days[1]:
            new_table_with_data.append(self.separate.sep_by_number(i))
        self.fill.fill_elements(new_table_with_data)
        res = list(self.separate.connect_all_days(new_table_with_data))
        res = [list(x) for x in res]
        self.printing.print_correct(res)

    def spin_days(self):
        if SpinAll.counter == 0:
            new_table_with_keys = self.all_days.keys()
            new_table_with_keys = [self.separate.sep_by_number(x) for x in new_table_with_keys]
            new_table_with_keys = self.separate.connect_all_days(new_table_with_keys)
            self.printing.print_correct_for_days(new_table_with_keys)
            setattr(SpinAll, 'counter', 1)

    @staticmethod
    def call_all(days, what_fill):  # assumed the fill separated by \n and day by space/s
        if isinstance(type(days), type(str)):
            days = days.split()
        spin = SpinAll()
        what_fill = what_fill.split('\n')  # if you want separated what_fill not by '\n', but other, change this one
        for what, day in enumerate(days):
            try:
                spin.all_days[day] = what_fill[what]
            except IndexError:
                pass
        spin.spin_days()
        spin.spin_text()

    def clear(self):
        self.all_days = self.fill.fill_default()
        setattr(SpinAll, 'counter', 0)
        # print('\n' * ConstantValues.ProvideLength().get_length_of_y())  # preferred for console using
        print('\n' * 100)

# Example data
SpinAll.call_all("Monday Tuesday", "Eating hot-dogs\nEating a lot of chocolate")
SpinAll.call_all("Wednesday", "Eating day. I eat whatever I want to")
SpinAll.call_all("Friday", "Let's drink some beer")
SpinAll.call_all("Saturday", "Umm")
from time import sleep
sleep(3)