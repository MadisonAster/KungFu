import unittest
from datetime import datetime

class ParkingStructure():
    def __init__(self):
        self.signal = 0
        self.parked_cars = []
        self.space_count = 100
    
    def open_gate(self):
        self.signal = True
        #self.Gate.emit(1)
    
    def close_gate(self):
        self.signal = False
        #self.Gate.emit(0)
        #time.sleep(self.min_gate_time)

    def add_car(self, PlateNumber):
        #if len(self.parked_cars) >= self.space_count:
        #    raise Exception('Lot Full!')
        self.parked_cars.append(PlateNumber)

class test_ParkingStructure(unittest.TestCase):
    def setUp(self):
        self.I = ParkingStructure()
        self.start_time = datetime.now()

    def tearDown(self):
        del self.I
        t = datetime.now()-self.start_time
        print(t, self.id())

    def test_init(self):
        print(self.I.parked_cars)

    def test_open_gate(self):
        self.I.open_gate()
        self.assertEqual(self.I.signal, True)
    
    def test_close_gate(self):
        self.I.open_gate()
        self.I.close_gate()
        self.assertEqual(self.I.signal, False)

    def test_add_car(self):
        self.I.add_car('ABCDEFG')
        self.I.add_car('1Il1l1l')
        self.assertEqual(len(self.I.parked_cars), 2)
        self.assertLessEqual(len(self.I.parked_cars), self.I.space_count)

    def test_too_many(self):
        for i in range(0, self.I.space_count):
            self.I.add_car(str(i).zfill(7))
        with self.assertRaises(Exception):
            self.I.add_car('1TOOMANY')
        self.assertEqual(len(self.I.parked_cars), self.I.space_count)
    


if __name__ == '__main__':
    unittest.main()