# PawPal+ Project Reflection

## 1. System Design

- Core actions:
1. User should be able to add a pet
2. Create a schedule to keep track of tasks
3. Add/remove tasks

**a. Initial design**

- Briefly describe your initial UML design.

A schedule object contains many task objects and can track many pet objects. An owner can have zero or many pets. 

- What classes did you include, and what responsibilities did you assign to each?

Pet:
Attributes:
- name: String
- breed: String
- age: Int
- medications: list<String>
Methods:
- addPet()
- removePet()
- updatePetInfo()

Schedule:
Attributes:
- tasks: list<Task>
Methods:
- addTask(Task)

Task:
Attributes:
- type: String
- name: String
- priority: Int/String depending on project needs
- time: String
Methods:
- createTask()
- updateTask()

Owner:
Attributes:
- name: String
- address: String
- phone: String

**b. Design changes**

- Did your design change during implementation?

Yes, some classes had the wrong responsibilities. 

- If yes, describe at least one change and why you made it.

My Pet class had add/remove pet, but as AI pointed out, those responsibilities should lie with the Owner class. Which makes sense, a Pet should not be able to add or remove itself, that should be up to the Owner. 

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?

Time is the primary ordering constraint. get_tasks_sorted_by_time uses it as the first sort key so the day is always presented chronologically.

Duration is used in conflict detection. Without it, two tasks at 09:00 and 09:15 would look safe; with it, the scheduler knows a 30-minute task at 09:00 actually runs until 09:30.

Priority is a tiebreaker constraint. When two tasks share the same start time, high surfaces before medium before low.

- How did you decide which constraints mattered most?

Time and duration came first because a schedule without them isn't a schedule it's just a list. Conflict detection is meaningless if you only check start times and ignore how long each task runs.

Priority was added as secondary because pet care has real urgency differences: a medication dose is non-negotiable, grooming is flexible.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.

Schedule doesn't own tasks, Pet does. Every query method (get_all_pending_tasks, get_tasks_by_time, etc.) iterates self.pets and reaches into pet.tasks. Schedule is a facade, not a data owner. You can't query the schedule without going through the pet layer, and there's no way to have a task that isn't attached to a specific pet.

- Why is that tradeoff reasonable for this scenario?

Tasks naturally belong to their pet.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?

I used AI to help find the missing gaps in my inital system design. I also used it to generate tests for possible edge cases for the most important scheduling logic. 

- What kinds of prompts or questions were most helpful?

Asking AI if it notices any missing relationships or potential logic bottlenecks in my UML design.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.

When I asked it to add to the smart scheduler table in my README and it didn't follow the table structure and added additional information. I had to ask it to only follow the table structure requirements. 

- How did you evaluate or verify what the AI suggested?

I made sure to review the changes it wanted to make prior to accepting them. After accepting, if there was code that seemed to pythonic, I asked it to explain and possibly refactor for readability purposes. 
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?

I tested several including sorting, filtering, scheduling conflicts and reoccruing events. 

- Why were these tests important?

These tests check the core scheduling logic. Testing happy paths and edge cases ensure that we're making an accurate schedule for the user.

**b. Confidence**

- How confident are you that your scheduler works correctly?

I'm about 4/5 stars confident

- What edge cases would you test next if you had more time?

I would test displaying correct tasks depending on the pet. 
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I was the most satisfied with the sorting algorithm and using the priority of a task as a tie-breaker.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

I would work on the UI a bit more and add filtering by pet as a feature.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

I learned that taking the time to design systems helps the implementation part of a project run smoother. There may be tradeoffs along the way and several changes. Your original plan may not be an accurate reflection of your final version, but it's a really good starting point that AI can help craft. 
