from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Pet:
    name: str
    breed: str
    age: int
    medications: list[str] = field(default_factory=list)
    tasks: list["Task"] = field(default_factory=list)

    def update_pet_info(self, name: str = None, breed: str = None, age: int = None):
        """Update one or more pet fields; omitted fields are left unchanged."""
        if name is not None:
            self.name = name
        if breed is not None:
            self.breed = breed
        if age is not None:
            self.age = age

    def add_task(self, task: "Task"):
        """Append a task to this pet's task list."""
        self.tasks.append(task)

    def remove_task(self, task: "Task"):
        """Remove a task from this pet's task list."""
        self.tasks.remove(task)

    def get_pending_tasks(self) -> list["Task"]:
        """Return all tasks that have not yet been marked complete."""
        return [t for t in self.tasks if not t.is_complete]


@dataclass
class Task:
    task_type: str
    description: str
    time: str
    frequency: str          # e.g. "daily", "weekly", "once"
    is_complete: bool = False
    pet: Optional["Pet"] = None

    @classmethod
    def create_task(cls, task_type: str, description: str, time: str, frequency: str, pet: Optional["Pet"] = None) -> "Task":
        """Named constructor that builds a Task with an optional pet association."""
        return cls(task_type=task_type, description=description, time=time, frequency=frequency, pet=pet)

    def update_task(self, description: str = None, time: str = None, frequency: str = None):
        """Update one or more task fields; omitted fields are left unchanged."""
        if description is not None:
            self.description = description
        if time is not None:
            self.time = time
        if frequency is not None:
            self.frequency = frequency

    def mark_complete(self):
        """Mark this task as done."""
        self.is_complete = True


class Schedule:
    def __init__(self, pets: list[Pet] = None):
        self.pets: list[Pet] = pets if pets is not None else []

    def add_task(self, pet: Pet, task: Task):
        """Assign a task to a specific pet."""
        pet.add_task(task)

    def remove_task(self, pet: Pet, task: Task):
        """Remove a task from a specific pet."""
        pet.remove_task(task)

    def get_tasks_for_pet(self, pet: Pet) -> list[Task]:
        """Return all tasks belonging to a specific pet."""
        return pet.tasks

    def get_all_pending_tasks(self) -> list[Task]:
        """Return all incomplete tasks across every pet."""
        return [task for pet in self.pets for task in pet.get_pending_tasks()]

    def get_tasks_by_time(self, time: str) -> list[Task]:
        """Return all tasks scheduled at a given time across every pet."""
        return [task for pet in self.pets for task in pet.tasks if task.time == time]

    def get_tasks_by_type(self, task_type: str) -> list[Task]:
        """Return all tasks of a given type across every pet."""
        return [task for pet in self.pets for task in pet.tasks if task.task_type == task_type]

    def get_tasks_sorted_by_time(self) -> list[Task]:
        """Return all tasks across every pet sorted chronologically."""
        all_tasks = [task for pet in self.pets for task in pet.tasks]
        return sorted(all_tasks, key=lambda t: t.time)


class Owner:
    def __init__(self, name: str, address: str, phone: str):
        self.name = name
        self.address = address
        self.phone = phone
        self.pets: list[Pet] = []
        self.schedule: Schedule = Schedule(pets=self.pets)

    def add_pet(self, pet: Pet):
        """Add a pet to this owner's roster."""
        self.pets.append(pet)

    def remove_pet(self, pet: Pet):
        """Remove a pet from this owner's roster."""
        self.pets.remove(pet)

    def find_pet(self, name: str) -> Optional[Pet]:
        """Return the first pet matching the given name, or None if not found."""
        return next((p for p in self.pets if p.name == name), None)

    def get_all_tasks(self) -> list[Task]:
        """Return every task across all of this owner's pets."""
        return [task for pet in self.pets for task in pet.tasks]

    def get_all_pending_tasks(self) -> list[Task]:
        """Return all incomplete tasks across all of this owner's pets."""
        return [task for pet in self.pets for task in pet.get_pending_tasks()]