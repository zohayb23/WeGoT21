from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv, dotenv_values
import os
import requests

load_dotenv()

Base = declarative_base()

class Delivery(Base):
    __tablename__ = 'delivery'

    id = Column(Integer, primary_key=True, autoincrement=True)
    vehicle_id = Column(Integer)
    order_id = Column(Integer)
    update_id = Column(Integer)
    target_destination_lat = Column(Float)
    target_destination_long = Column(Float)

    def __init__(self, vehicle_id, order_id, update_id, target_destination_lat, target_destination_long):
        # Gets the DB logins
        env_vars = dotenv_values(".env")
        self._username = env_vars.get("USERNAME")
        self._pwd = env_vars.get("PWD")
        exists = True

        self.vehicle_id = vehicle_id
        self.order_id = order_id
        self.update_id = update_id
        self.target_destination_lat = target_destination_lat
        self.target_destination_long = target_destination_long

    @staticmethod
    def connect_to_db(db_url):
        engine = create_engine(db_url)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        return Session()

    # getters
    def get_vehicle_id(self):
        return self.vehicle_id

    def get_order_id(self):
        return self.order_id

    def get_update_id(self):
        return self.update_id

    def get_target_destination_lat(self):
        return self.target_destination_lat

    def get_target_destination_long(self):
        return self.target_destination_long

    # setters
    def set_vehicle_id(self, vehicle_id):
        self.vehicle_id = vehicle_id

    def set_order_id(self, order_id):
        self.order_id = order_id

    def set_update_id(self, update_id):
        self.update_id = update_id

    def set_target_destination_lat(self, target_destination_lat):
        self.target_destination_lat = target_destination_lat

    def set_target_destination_long(self, target_destination_long):
        self.target_destination_long = target_destination_long

    def assign_vehicle_to_order(self): # Function needs more discussion - unsure of purpose
        # Make a request to the vehicle request API to get a vehicle for this order
        url = 'https://myvehicleapi.com/requests'
        payload = {
            'order_id': self.order_id,
            'destination_lat': self.target_destination_lat,
            'destination_long': self.target_destination_long
        }
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            # If the request was successful, update the vehicle ID for this delivery
            vehicle_id = response.json().get('vehicle_id')
            self.set_vehicle_id(vehicle_id)
        else:
            # If the request was not successful, raise an exception
            raise Exception('Error assigning vehicle to order')
