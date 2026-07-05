import streamlit as st
from pawpal_system import Pet, Task, Owner

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
owner_address = st.text_input("Owner address", value="123 Main St")
owner_phone = st.text_input("Owner phone", value="555-1234")

# Initialize owner once; shared across all reruns
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name=owner_name, address=owner_address, phone=owner_phone)

owner: Owner = st.session_state.owner
# Keep owner name in sync with the text input
owner.name = owner_name

st.divider()

st.subheader("Your Pets")

if owner.pets:
    st.write("Current pets:")
    st.table([{"name": p.name, "species": p.species, "age": p.age} for p in owner.pets])
else:
    st.info("No pets yet. Add one below.")

with st.form("add_pet_form"):
    st.markdown("**Add a pet**")
    col1, col2 = st.columns(2)
    with col1:
        new_pet_name = st.text_input("Pet name", value="Mochi")
        new_age = st.number_input("Age", min_value=0, max_value=30, value=5)
    with col2:
        new_species = st.selectbox("Species", ["dog", "cat", "other"])
        new_medications = st.text_input("Medications (comma-separated)", value="")
    if st.form_submit_button("Add pet"):
        new_pet = Pet(
            name=new_pet_name,
            species=new_species,
            age=int(new_age),
            medications=[m.strip() for m in new_medications.split(",") if m.strip()],
        )
        st.session_state.owner.add_pet(new_pet)
        st.rerun()

# Use the first pet for task assignment if any exist
pet = owner.pets[0] if owner.pets else None

st.divider()

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if pet is None:
    st.warning("Add a pet above before adding tasks.")
    st.stop()

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
    task_time = st.text_input("Time (HH:MM)", value="08:00")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    frequency = st.selectbox("Frequency", ["daily", "weekly", "once"])
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)
    description = st.text_input("Description", value="")

if st.button("Add task"):
    task = Task.create_task(
        task_type=task_title,
        duration=int(duration),
        priority=priority,
        description=description,
        time=task_time,
        frequency=frequency,
        pet=pet,
    )
    owner.schedule.add_task(pet, task)
    st.rerun()

tasks = owner.schedule.get_tasks_for_pet(pet)
if tasks:
    st.write("Current tasks:")
    st.table([
        {"type": t.task_type, "time": t.time, "duration (min)": t.duration,
         "priority": t.priority, "frequency": t.frequency, "done": t.is_complete}
        for t in tasks
    ])
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    sorted_tasks = owner.schedule.get_tasks_sorted_by_time()
    pending = owner.schedule.get_all_pending_tasks()

    if sorted_tasks:
        st.markdown("**Full schedule (chronological):**")
        st.table([
            {"type": t.task_type, "time": t.time, "duration (min)": t.duration,
             "priority": t.priority, "done": t.is_complete}
            for t in sorted_tasks
        ])
        st.markdown(f"**Pending tasks:** {len(pending)} of {len(sorted_tasks)} remaining")
    else:
        st.info("No tasks scheduled yet. Add tasks above, then generate the schedule.")