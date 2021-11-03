from django.test import TestCase

from player.models import Player

class TestModelPlayer(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Player.objects.create(name='Jon', team='True')
        Player.objects.create(name='Ed')
      
        pass

    def setUp(self):
        # setUp: Run once for every test method to setup clean data.
        pass

    def test_name_label(self):
        player = Player.objects.get(id=1)
        field_label = Player._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
        pass

    def test_get_absolute_url(self):
        player = Player.objects.get(id=1)
        self.assertEqual(player.get_absolute_url(), '/player/1')
        pass
