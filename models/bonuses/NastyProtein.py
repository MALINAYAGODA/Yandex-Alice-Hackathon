import BonusBase


class NastyProtein(BonusBase):
    def __init__(self):
        super(NastyProtein, self).__init__(
            'Противный Протеин',
            'Играй в любой бой. +2 любой стороне. Разовая шмотка.',
            200
        )

    def use_bonus(self, req, hero):  # используем бонус, улучшаем героя
        pass
    