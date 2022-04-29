import MonsterBase


class Burp(MonsterBase):
    def __init__(self):
        super(Burp, self).__init__(6, 'Рыгачу', 'Рвота, в атаку! Придётся сбросить всю руку.', 2, 1)

    def fight_or_not(self, req, hero):  # убежать или драться? Сравнение силы
        pass

    def fight(self, req, hero):  # после использования бонусов, мы сражаемся и смотрим кто победил
        pass

    def do_bad_things(self, req, hero):  # он не убежал
        pass
