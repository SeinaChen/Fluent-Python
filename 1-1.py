import collections

#シーケンスとしてのトランプ組
Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in(2,11)]+list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                                      for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card('7','diamonds')
print(beer_card)

deck = FrenchDeck()
print(len(deck))

#ランダムにカードを選ぶ
from random import choice
print(choice(deck))

#トランプ組中のカード確認
for card in deck:
    print(card)

#カード順を逆
for card in reversed(deck):
    print(card)

#カードの有無判断
print(Card('Q', 'hearts') in deck)

#ルールの強さ
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)
