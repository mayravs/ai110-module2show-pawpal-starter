from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Pet:
    name: str
    breed: str
    age: int
    medications: list[str] = field(default_factory=list)

    def add_pet(self):
        pass

    def remove_pet(self):
        pass

    def update_pet_info(self):
        pass


@dataclass
class Task:
    type: str
    name: str
    priority: str
    time: str

    def create_task(self):
        pass

    def update_task(self):
        pass


class Schedule:
    def __init__(self):
        self.tasks: list[Task] = []
        self._tracked_pets: list[Pet] = []

    def add_task(self, task: Task):
        pass


class Owner:
    def __init__(self, name: str, address: str, phone: str):
        self.name = name
        self.address = address
        self.phone = phone
        self.pets: list[Pet] = []
        self.schedule: Schedule = Schedule()
