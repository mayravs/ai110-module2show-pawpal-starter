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
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
