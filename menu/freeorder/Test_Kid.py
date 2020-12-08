import unittest
from menu.freeorder.kidsmeal import kidsmeal

class test_kids(unittest.TestCase):  
    @classmethod
    def setUpClass(cls):
        print('Set Up Test for module: kidsmeal')
        
    def setUp(self): 
        self.k1 = kidsmeal()
        self.k1.burger(22)
        self.k1.setGift("Toy")
        self.k1.setGift("Book")
        self.k1.review_order()
        self.k2 = kidsmeal()
        self.k2.burger(25)
        self.k2.review_order()
        self.k3 = kidsmeal()
        self.k3.burger(24)
        self.k3.beverage(27)
        self.k3.beverage(29)
        self.k3.snack(30)
        self.k3.snack(33)
        self.k3.setGift("Toy")
        self.k3.review_order()
        self.k4 = kidsmeal()
        self.k4.review_order()
        print('Set Up Each Test')
        
    def test_gift(self):          
        self.assertEqual(self.k1.gift, 'Book')
        self.assertEqual(self.k2.gift, 'Book')
        self.assertEqual(self.k3.gift, 'None')        
        self.assertEqual(self.k4.gift, 'None')
        
    def test_menu(self):     
        self.assertIsNotNone(self.k1.menu())
        self.assertIsNotNone(self.k2.menu())
        self.assertIsNotNone(self.k3.menu())
        self.assertIsNotNone(self.k4.menu())

    def test_review(self):
        self.assertIsNotNone(self.k1.review_order())
        self.assertIsNotNone(self.k2.review_order())
        self.assertEqual(self.k3.review_order(),"Please review your order and make sure no more than 4 items selected for this kids meal, thank you!")
        self.assertEqual(self.k4.review_order(),"Please choose [Book] or [Toy] for this kids meal and no more than 4 items for the order!")

    def tearDown(self):                                       
        print('Tear Down Each Test')

    @classmethod
    def tearDownClass(cls):
        print('Tear Down Test for module: kidsmeal')
        
#unittest.main(argv=[''], verbosity=2, exit=False) 



