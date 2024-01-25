class EasterGift:
    def __init__(self):
        self.list_gitfs = []

    def implement_easter_gift_task(self):
        self.list_gitfs = self._take_gifts()
        gitfs = []
        while True:
            command = self._take_input()
            if command == "No Money":
                break

            info = command.split(" ")
            if info[0] == "OutOfStock":
                current_gift = info[1]
                self.list_gitfs = self._out_of_stock(self.list_gitfs, current_gift)

            elif info[0] == "Required":
                req_gift, index_ = info[1], int(info[2])
                self.list_gitfs = self._required_gift(self.list_gitfs, req_gift, index_)

            elif info[0] == "JustInCase":
                just_in_case_gift = info[1]
                self.list_gitfs = self._just_in_case(self.list_gitfs, just_in_case_gift)

        return gitfs

    def print_gifts_collection(self):
        return print(*[g for g in self.list_gitfs if g != "None"])

    # Helper methods
    def _is_valid(self, lst, idx):
        return 0 <= idx < len(lst)

    def _take_gifts(self):
        return [x for x in input().split(" ")]

    def _take_input(self):
        return input()

    def _out_of_stock(self, lst, gift):
        lst = ["None" if g == gift else g for g in lst]

        # for i, g in enumerate(lst):
        #     if g == gift:
        #         lst[i] = "None"
        return lst

    def _required_gift(self, lst, gift, idx):
        if self._is_valid(lst, idx):
            lst = [gift if i == idx else g for i, g in enumerate(lst)]

            # for i, g in enumerate(lst):
            #     if i == idx:
            #         lst[i] = gift
        return lst

    def _just_in_case(self, lst, gift):
        lst[-1] = gift
        return lst


easter_gift = EasterGift()
easter_gift.implement_easter_gift_task()
easter_gift.print_gifts_collection()
