#!/usr/bin/python3

from models.base_model import BaseModel


class Place(BaseModel):
    """this class manages place objects"""

    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_of_rooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []