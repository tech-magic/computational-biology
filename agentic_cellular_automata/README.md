# 🔥 Simulating Fire Evacuation with Multi-Agent Systems (MAS)

**A Multi-agent based Approach to simulate Uncertainty of a Crowd in Panic with Sharable Ontologies** at the
**Proceedings of the 9th Annual Sessions, Sri Lanka Association for Artificial Intelligence - 2012**
(see https://slaai.lk/proc/2012/s1203.pdf & https://slaai.lk/p2012/)

## 🧠 What Is This?

The above publication describes about an attempt to simulate **how people evacuate a building during a fire**, using a concept called **emergence** from **multi-agent systems** (MAS).  
We treat **each person** and even the **fire itself** as **independent "agents"** — like tiny, smart decision-makers that act on their own, but also influence each other.

Think of it like this:
- 🧍 Each person in the building is an agent.
- 🔥 The fire is also an agent.
- 🌐 There is a "global brain" (global ontology) that knows general facts.
- 🧠 Each agent has its own "local brain" (local ontology), which updates based on what it learns from:
  - The environment (like smoke or crowding)
  - Nearby agents (like others running)
  - The global brain (basic knowledge, like “fire is dangerous”)

As all these agents act and react, **complex and realistic evacuation behavior “emerges”** — without any one agent being “in charge.”

---

## 👩‍🔬 Why This Matters

- Simulating this helps us **understand how people behave in emergencies**.
- It allows building designers, firefighters, and safety engineers to **predict bottlenecks**, **plan better exits**, and **improve safety protocols**.
- Instead of guessing how crowds will behave, we can **watch it unfold dynamically in the simulation**.

---

## 🛠️ How It Works (In Simple Terms)

1. **The Building Is Set Up**  
   We create a digital version of a building: rooms, doors, exits.

2. **Agents Are Placed Inside**  
   - 🧍 People agents are placed randomly inside the building.  
   - 🔥 Fire agents are placed at specific ignition points.

3. **Ontologies: Agent Knowledge**  
   - **Global Ontology** contains general knowledge (e.g., “smoke reduces visibility”).
   - **Local Ontology** for each agent contains what it currently *knows or believes*.  
     For example, a person might know:  
     - Nearest visible exit  
     - Where the fire seems to be  
     - Where other people are going

4. **Simulation Begins**  
   - 🔥 The fire spreads.  
   - 🧍 People perceive their surroundings (smoke, heat, exits, crowding).  
   - They update their local knowledge and **decide where to go**.  
   - Some may help others, follow the crowd, or get confused.

5. **Emergence Happens**  
   Even though each agent acts independently, we observe group behavior:  
   - Crowds forming at exits  
   - Blockages in hallways  
   - Panic spreading in waves  
   - Some people finding smarter paths

---

# 🧬 Cross-Application of Multi-Agent Systems and Emergence in Cellular Automata

## 🧠 What Is This?

The concept of **emergence** from **multi-agent systems (MAS)** can be used alongside **cellular automata (CA)** to simulate **cell bhaviour** by modelling cells as intelligent agents.

We blend two powerful models:
- 🧠 **Multi-Agent Systems** — Each part of the cell (e.g., nucleus, membrane, organelles) acts as an intelligent agent.
- 🧮 **Cellular Automata** — A grid-based environment where each square (cell) updates based on local rules.

Together, they simulate how **complex biological behaviors** that can **emerge** from many simple, local interactions.

---

## 🧩 Why Combine MAS with Cellular Automata?

- **Cellular Automata (CA)** are great at modeling spatial processes using simple rules.
- **Multi-Agent Systems (MAS)** bring in adaptability, memory, and reasoning.
- Combining them helps us simulate **more realistic and intelligent cell behavior**, especially in complex, dynamic events like mitosis.

---

## TO BE CONTINUED