import BonusBase


class MouthStinkPotion(BonusBase):
    def __init__(self):
        super(MouthStinkPotion, self).__init__(
            'Зелье ротовой вони',
            'Играй в любой бой. Сразу убьёт Блуждающий нос или даст +2 любой стороне. Разовая шмотка.',
            100
        )

    def use_bonus(self, req, hero):  # используем бонус, улучшаем героя
        pass
    