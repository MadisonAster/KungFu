import unittest

class ParkingStructure():
    def __init__(self):
        self.parked_cars = []
        self.space_count = 100
        self.register_balance = 0
        self.day_price = 5
        self.cust_count = 0
    
    def open_gate(self):
        self.signal = True

    def close_gate(self):
        self.signal = False

    def add_car(self, PlateNumber):
        if len(self.parked_cars) >= self.space_count:
            raise Exception('Lot Full!')
        self.parked_cars.append(PlateNumber)

    def checkout_car(self, PlateNumber):
        self.parked_cars.remove(PlateNumber)
        self.register_balance += self.day_price
        self.cust_count += 1

class test_ParkingStructure(unittest.TestCase):
    def setUp(self):
        self.I = ParkingStructure()
    def tearDown(self):
        del self.I

    def test_init(self):
        print(self.I)
    
    def test_open_gate(self):
        self.I.open_gate()
        self.assertEqual(self.I.signal, True)
        self.I.close_gate()

    def test_close_gate(self):
        self.I.open_gate()
        self.I.close_gate()
        self.assertEqual(self.I.signal, False)

    def test_add_car(self):
        self.I.add_car('ABCDEFG')
        self.I.add_car('1lI1lI1')
        self.assertEqual(len(self.I.parked_cars), 2)
        self.assertEqual(len(self.I.parked_cars)<=self.I.space_count, True)

    def test_too_many(self):
        for i in range(0,self.I.space_count):
            self.I.add_car(str(i).zfill(7))
        with self.assertRaises(Exception):
            self.I.add_car('1TOOMNY')
        print(self.I.parked_cars)
        self.assertEqual(len(self.I.parked_cars), self.I.space_count)

    def test_checkout_car(self):
        for i in range(0,self.I.space_count):
            self.I.add_car(str(i).zfill(7))
        for i in range(0,self.I.space_count):
            self.I.checkout_car(str(i).zfill(7))
        print(self.I.parked_cars)
        self.assertEqual(self.I.cust_count, self.I.space_count)
        self.assertEqual(self.I.register_balance, self.I.cust_count*self.I.day_price)
        self.assertEqual(len(self.I.parked_cars), 0)

if __name__ == '__main__':
    unittest.main()