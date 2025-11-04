import pytest
from app import app
from models import rooms, user_sessions
from rooms import create_room

def test_create_room():
    room_id = create_room("Test", "1234", "text")
    assert len(room_id) == 8
    room = rooms.find_one({"id": room_id})
    assert room["name"] == "Test"

def test_verify_pin():
    room_id = create_room("Test2", "5678", "multimedia")
    assert rooms.verify_pin(room_id, "5678") == True
    assert rooms.verify_pin(room_id, "0000") == False