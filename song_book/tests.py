from django.test import TestCase
from users.tests import RegisterLoginTest as rl
from .models import Song
from users.models import MyUser

    
class SongBookTest(TestCase):   

    def test_song_book_template_used(self):
        rl.sign_up_and_login(self)
        response = self.client.get('/song_book/1/')
        self.assertTemplateUsed(response, 'song_book/base_songbook.html')

    def sign_in_song_post(self):
        rl.sign_up_and_login(self)
        self.client.post('/song_book/1/song_post/to_learn/', data={'to_learn_input' : 'Starman'})
    
    def test_song_input_saved(self):
        self.sign_in_song_post()
        new_item = Song.objects.first()
        self.assertEqual(new_item.text, 'Starman')
        self.assertEqual(new_item.status, 'to_learn')
    
    def test_song_delete(self):
        self.sign_in_song_post()
        the_user = MyUser.objects.get(pk=1)
        self.client.post('/song_book/1/song_post/rusty/', data={'rusty_input' : 'Under Pressure'})
        songs = Song.objects.filter(user=the_user)
        self.assertEqual(songs.count(), 2)
        self.client.post('/song_book/1/song_delete/2/')
        self.assertEqual(songs.count(), 1)
    
    def test_song_move(self):
        self.sign_in_song_post()
        self.client.post('/song_book/1/song_post/learning/', data={'learning_input' : 'Life On Mars'})
        self.client.post('/song_book/1/song_post/rusty/', data={'rusty_input' : 'Under Pressure'})
        
        self.client.post('/song_book/song_move/', data={'user_pk': 1, 'song_pk': 1,
                        'list_index': 0, 'status': 'rusty',})
        starman = Song.objects.get(pk = 1)
        self.assertEqual(starman.list_index, 0)
        self.assertEqual(starman.status, 'rusty')
    
    def test_song_note(self):
        self.sign_in_song_post()
        self.client.post('/song_book/song_note/', data={ 'user_pk': 1, 'song_pk': 1, 'note_input': 'Verse chords are D, Am, C and G'})
        starman = Song.objects.get(pk = 1)
        self.assertEqual(starman.note, 'Verse chords are D, Am, C and G')

    def test_song_video(self):
        self.sign_in_song_post()
        self.client.post('/song_book/1/song_video/1/', data={'link_input': 'https://www.youtube.com/watch?v=aWOppc3Udto&ab_channel=LeftHandedGuitarist'})
        starman = Song.objects.get(pk = 1)
        self.assertEqual(starman.video, 'https://www.youtube.com/embed/aWOppc3Udto')




