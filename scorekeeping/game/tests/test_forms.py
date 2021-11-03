# from django.test import TestCase  we don't need this because no test data is needed instead import SimpleTestCase
from django.test import SimpleTestCase

from game.forms import GameCreateForm

class GameCreateFormTest(SimpleTestCase):
    def test_game_description_field_label(self):
        form = GameCreateForm()
        self.assertTrue(form.fields['description'].label is None or form.fields['description'].label == 'description')
