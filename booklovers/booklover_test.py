import unittest
import pandas as pd
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
        def setUp(self):
        #beginning bookLover object with test data
            self.book_lover = BookLover(name='Tim Sharpe', email='tjs@aol.net', fav_genre='War/History', book_list = pd.DataFrame({'book_name': ['Saving Private Ryan', 'War'], 'book_rating': [4, 5]}))
    
        def test_1_add_book(self): 
        # add a book and test if it is in `book_list`
            self.book_lover.add_book("Of Mice and Men", 2)
        
            self.assertIn('Of Mice and Men', self.book_lover.book_list['book_name'].values)

        def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
            self.book_lover.add_book("Unbroken", 4)
            self.book_lover.add_book("Unbroken", 4)
        
            self.assertEqual(len(self.book_lover.book_list[self.book_lover.book_list['book_name'] == 'Unbroken']), 1)
                
        def test_3_has_read(self): 
    # pass a book in the list and test if the answer is `True`.
            Sav_Priv_Ryan = self.book_lover.has_read("Saving Private Ryan")
        
            self.assertTrue(Sav_Priv_Ryan)
        
        def test_4_has_read(self): 
    # pass a book NOT in the list and use `assert False` to test the answer is `True`
            U_Boat = self.book_lover.has_read("U-boat")
        
            self.assertFalse(U_Boat)
        
        def test_5_num_books_read(self): 
    # add some books to the list, and test num_books matches expected.
            self.book_lover.add_book("Jane Eyre", 4)
            self.book_lover.add_book("Fight Club", 3)
            self.book_lover.add_book("The Divine Comedy", 5)
            self.book_lover.add_book("The Popol Vuh", 5)
        
            exp_result = 6 #2 initial + 4 added.
            self.assertEqual(self.book_lover.num_books_read(), exp_result)

        def test_6_fav_books(self):
    # add some books with ratings to the list, making sure some of them have rating > 3. 
    # Your test should check that the returned books have rating  > 3
            self.book_lover.add_book("Book 1", 2)
            self.book_lover.add_book("Book 2", 3)
            self.book_lover.add_book("Book 3", 5)
            self.book_lover.add_book("Book 4", 1)
            self.book_lover.add_book("Book 5", 4)
        
            fav_books = self.book_lover.fav_books()
            self.assertTrue(all(fav_books['book_rating'] > 3))
                
if __name__ == '__main__':
    
        unittest.main(verbosity=3)