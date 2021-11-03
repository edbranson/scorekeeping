from django.test import TestCase
from django.test import SimpleTestCase

from django.urls import reverse, reverse_lazy


from player.models import Player



class PlayerCreateTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.player_test = Player.objects.create(name='Hearts')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/player/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('player-create'))
        self.assertEqual(response.status_code, 200)    

    def test_uses_correct_template(self):
        response = self.client.get(reverse('player-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'player/player_list.html')
        response = self.client.post(reverse('player-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'player/player_form.html')


class PlayerUpdateTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.player_test = Player.objects.create(name='Hearts')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/player/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('player-detail', kwargs={'pk': self.player_test.pk}))
        self.assertEqual(response.status_code, 200)    

    def test_uses_correct_template(self):
        response = self.client.get(reverse('player-detail', kwargs={'pk': self.player_test.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'player/player_detail.html')
        response = self.client.post(reverse('player-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'player/player_form.html')

class PlayerListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        Player.objects.create(name='Hearts')

        # test_user = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        # test_user.save()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/player/')
        self.assertEqual(response.status_code, 200)  

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('player-list'))
        self.assertEqual(response.status_code, 200)          

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('player-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'player/player_list.html')   

class PlayerDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.player_test = Player.objects.create(name='Hearts') 
        
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/player/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('player-detail', kwargs={'pk': self.player_test.pk}))
        self.assertEqual(response.status_code, 200)                

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('player-detail', kwargs={'pk': self.player_test.pk}))
        # response = self.client.get(reverse('author-detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'player/player_detail.html')   

class PlayerDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.player_test = Player.objects.create(name='Hearts') 

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/player/1')
        self.assertEqual(response.status_code, 200)             

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('player-detail', kwargs={'pk': self.player_test.pk}))
        self.assertEqual(response.status_code, 200)    

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('player-detail', kwargs={'pk': self.player_test.pk}))
        # response = self.client.get(reverse('author-detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'player/player_detail.html')                      

    def test_view_success_url_exists_at_desired_location(self):
        response = self.client.get(reverse_lazy('player-list'))
        self.assertEqual(response.status_code, 200)             
