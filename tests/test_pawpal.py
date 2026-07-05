from pawpal_system import Pet, Task


def test_add_task_increases_pet_task_count():
    pet = Pet(name="Luna", species="dog", age=3)
    task = Task.create_task(
        task_type="exercise",
        description="30-minute walk",
        duration=30,
        priority="high",
        time="09:00",
        frequency="daily",
        pet=pet
    )

    assert len(pet.tasks) == 0

    pet.add_task(task)

    assert len(pet.tasks) == 1


def test_mark_complete_changes_status():
    task = Task.create_task(
        task_type="feeding",
        duration=10,
        priority="medium",
        description="Morning kibble",
        time="07:00",
        frequency="daily"
    )

    assert task.is_complete is False

    task.mark_complete()

    assert task.is_complete is True