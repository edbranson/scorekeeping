from django.test import TestCase
from django.test import SimpleTestCase

from django.urls import reverse, reverse_lazy


from game.models import Game

class GameIndex(SimpleTestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)          


class GameCreateTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.game_test = Game.objects.create(description='Hearts')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/game/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('game-create'))
        self.assertEqual(response.status_code, 200)    

    def test_uses_correct_template(self):
        response = self.client.get(reverse('game-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game/game_list.html')
        response = self.client.post(reverse('game-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game_form.html')


class GameUpdateTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.game_test = Game.objects.create(description='Hearts')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/game/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('game-detail', kwargs={'pk': self.game_test.pk}))
        self.assertEqual(response.status_code, 200)    

    def test_uses_correct_template(self):
        response = self.client.get(reverse('game-detail', kwargs={'pk': self.game_test.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game/game_detail.html')
        response = self.client.post(reverse('game-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game_form.html')

class GameListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        Game.objects.create(description='Hearts')

        # test_user = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        # test_user.save()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/game/')
        self.assertEqual(response.status_code, 200)  

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('game-list'))
        self.assertEqual(response.status_code, 200)          

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('game-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game/game_list.html')   

class GameDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.game_test = Game.objects.create(description='Hearts') 
        
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/game/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('game-detail', kwargs={'pk': self.game_test.pk}))
        self.assertEqual(response.status_code, 200)                

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('game-detail', kwargs={'pk': self.game_test.pk}))
        # response = self.client.get(reverse('author-detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game/game_detail.html')   

class GameDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.game_test = Game.objects.create(description='Hearts') 

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/game/1')
        self.assertEqual(response.status_code, 200)             

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('game-detail', kwargs={'pk': self.game_test.pk}))
        self.assertEqual(response.status_code, 200)    

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('game-detail', kwargs={'pk': self.game_test.pk}))
        # response = self.client.get(reverse('author-detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game/game_detail.html')                      

    def test_view_success_url_exists_at_desired_location(self):
        response = self.client.get(reverse_lazy('game-list'))
        self.assertEqual(response.status_code, 200)             
