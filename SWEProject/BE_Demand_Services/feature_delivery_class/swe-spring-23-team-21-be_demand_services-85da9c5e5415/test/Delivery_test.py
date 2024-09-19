import unittest
from unittest.mock import MagicMock, patch
from Delivery import Delivery

class DeliveryTests(unittest.TestCase):

    def test_get():
        delivery = Delivery(vehicle_id=1, order_id=2, update_id=3, target_destination_lat=40.7128, target_destination_long=-74.0060)
        assert delivery.get_vehicle_id() == 1
        assert delivery.get_order_id() == 2
        assert delivery.get_update_id() == 3
        assert delivery.get_target_destination_lat() == 40.7128
        assert delivery.get_target_destination_long() == -74.0060

    def test_set_vehicle_id():
        delivery = Delivery(vehicle_id=1, order_id=2, update_id=3, target_destination_lat=40.7128, target_destination_long=-74.0060)
        delivery.set_vehicle_id(2)
        assert delivery.get_vehicle_id() == 2

    def test_set_order_id():
        delivery = Delivery(vehicle_id=1, order_id=2, update_id=3, target_destination_lat=40.7128, target_destination_long=-74.0060)
        delivery.set_order_id(4)
        assert delivery.get_order_id() == 4
        
    def test_set_update_id():
        delivery = Delivery(vehicle_id=1, order_id=2, update_id=3, target_destination_lat=40.7128, target_destination_long=-74.0060)
        delivery.set_update_id(5)
        assert delivery.get_update_id() == 5

    
    def test_set_destination():
        delivery = Delivery(vehicle_id=1, order_id=2, update_id=3, target_destination_lat=40.7128, target_destination_long=-74.0060)
        delivery.set_target_destination_lat(41.8781)
        delivery.set_target_destination_long(-87.6298)
        assert delivery.get_target_destination_lat() == 41.8781
        assert delivery.get_target_destination_long() == -87.6298

    def test_incorrect_id():
        try:
            delivery = Delivery(vehicle_id="not an integer", order_id=2, update_id=3, target_destination_lat=40.7128, target_destination_long=-74.0060)
            assert False
        except:
            assert True

    def test_missing_id():
        # for example, missing vehicle_id
        try:
            delivery = Delivery(order_id=2, update_id=3, target_destination_lat=40.7128, target_destination_long=-74.0060)
            assert False
        except:
            assert True


    
