from django.test import TestCase

from game.models import Game

class TestModelGame(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Game.objects.create(description='Hearts')
        Game.objects.create(description='Spades')
        pass

    def setUp(self):
        # setUp: Run once for every test method to setup clean data.
        pass

    def test_name_label(self):
        game = Game.objects.get(id=1)
        field_label = game._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')
        pass

    def test_get_absolute_url(self):
        game = Game.objects.get(id=1)
        self.assertEqual(game.get_absolute_url(), '/game/1')
        pass
