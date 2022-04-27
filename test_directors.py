import unittest
import directors
import models

class TestDirectors(unittest.TestCase):
    def setUp(self):
        """
        Inisialisasi
        """
        self.app = models.Directors

    def test_director_read_one(self):
        """
        Testing ambil 1 director apakah id dan namanya sesuai
        """
        director_check = directors.read_one(4762)
        self.assertEqual(director_check['name'], 'James Cameron')
    
    def test_update_director(self):
        """
        Testing update apakah status codenya ketika berhasil akan 200
        """
        updated_director = {
            'name': 'Test Edit Director',
            'gender': 0,
            'uid': 65454,
            'department': 'Directing'
        }

        self.assertEqual(directors.update(7111, updated_director)[1], 200)
        
if __name__ == '__main__':
    unittest.main()