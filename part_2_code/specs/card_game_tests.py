import unittest
from unittest import result
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.cardgame = CardGame()
        self.card_1 = Card("spades", 2)
        self.card_2 = Card("hearts", 1)
        self.card_3 = Card("diamonds", 4)
        self.total_cards = [self.card_1, self.card_2, self.card_3]
       

    def test_check_for_ace(self):
        result = self.cardgame.check_for_ace(self.card_2)
        self.assertTrue(result)

    def test_highest_card(self):
        result = self.cardgame.highest_card(self.card_1, self.card_2)
        self.assertEqual(self.card_1, result)

    def test_cards_total(self):
        total = self.cardgame.cards_total(self.total_cards)
        self.assertEqual("You have a total of" + str(7), total)