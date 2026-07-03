from pawpal_system import Owner, Pet, Task


def print_schedule(owner: Owner):
    print(f"\n{'='*40}")
    print(f"  Today's Schedule for {owner.name}'s Pets")
    print(f"{'='*40}")

    tasks = owner.schedule.get_tasks_sorted_by_time()

    if not tasks:
        print("  No tasks scheduled for today.")
    else:
        for task in tasks:
            status = "✓" if task.is_complete else "○"
            pet_name = task.pet.name if task.pet else "Unknown"
            print(f"  [{status}] {task.time} | {pet_name} | {task.task_type} — {task.description} ({task.frequency})")

    print(f"{'='*40}\n")


if __name__ == "__main__":
    owner = Owner("Alex", "123 Main St", "555-1234")

    luna = Pet(name="Luna", breed="Husky", age=3)
    mochi = Pet(name="Mochi", breed="Shiba Inu", age=5, medications=["Apoquel"])

    owner.add_pet(luna)
    owner.add_pet(mochi)

    owner.schedule.add_task(luna, Task.create_task(
        task_type="feeding",
        description="Morning kibble",
        time="07:00",
        frequency="daily",
        pet=luna
    ))

    owner.schedule.add_task(mochi, Task.create_task(
        task_type="medication",
        description="Give Apoquel with food",
        time="08:00",
        frequency="daily",
        pet=mochi
    ))

    owner.schedule.add_task(luna, Task.create_task(
        task_type="exercise",
        description="30-minute walk",
        time="09:00",
        frequency="daily",
        pet=luna
    ))

    owner.schedule.add_task(mochi, Task.create_task(
        task_type="grooming",
        description="Brush coat",
        time="17:00",
        frequency="weekly",
        pet=mochi
    ))

    print_schedule(owner)
