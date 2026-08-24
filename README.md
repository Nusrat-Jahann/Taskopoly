# Taskopoly 🎮🌱

> **A gamified task management system powered by Python and Data Structures & Algorithms.**

Taskopoly is a gamified task management system designed to make everyday task management more engaging. Instead of treating tasks as a simple to-do list, Taskopoly turns them into challenges where users can earn XP, level up, and grow a virtual tree.

The project demonstrates the practical use of **Data Structures & Algorithms** through task management, searching, sorting, queues, stacks, and an XP-based progression system.

## ✨ Features

### 📝 Task Management

* Add new tasks
* View all tasks
* Edit existing tasks
* Delete tasks
* Mark tasks as completed
* Store tasks using a linked list

### 🏷️ Automatic Category & XP

Taskopoly automatically detects the category of a task based on keywords.

* Study
* Health
* Chores
* Creative
* Self-care
* General

Each category has a predefined XP reward, making task completion more engaging.

### 🔍 Search & Sorting

* Search tasks by name
* Sort tasks alphabetically
* Sort tasks by XP
* Sort tasks from low to high or high to low

### 📦 Completed Task Queue

Completed tasks are stored using a **Queue** data structure.

* Enqueue completed tasks
* Dequeue tasks
* View the front task
* Display the completed task queue

### XP & Virtual Tree

Users earn XP by completing tasks and progress through different levels.

* Level 1 — Seed 🌱
* Level 2 — Sprout 🌿
* Level 3 — Young Tree 🌳
* XP progress tracking
* Virtual tree growth based on user progress

### ↩️ Undo System

Taskopoly includes an **Undo Stack** based on the **LIFO (Last In, First Out)** principle.

* Records recent actions
* Reverses the most recent action
* Restores previous task states

## 🧠 Data Structures & Algorithms

Taskopoly demonstrates several fundamental DSA concepts:

* **Linked List** — Task storage and management
* **Queue** — Completed task management
* **Stack** — Undo functionality
* **Bubble Sort** — Task sorting
* **Linear Search** — Task searching
* **Keyword Matching** — Automatic category and XP detection

## 🛠️ Tech Stack

* **Python**
* **Data Structures & Algorithms**
* **Linked List**
* **Queue**
* **Stack**
* **Bubble Sort**
* **Linear Search**

## 📂 Project Structure

```text
Taskopoly/
│
├── main.py
├── quest.py
├── keywords.py
├── search_sort.py
├── queue.py
├── xp_tree.py
├── undo.py
├── README.md
└── .gitignore
```

### `main.py`

The main program that connects all Taskopoly features and provides the interactive menu.

### `quest.py`

Contains the linked-list implementation used to store and manage tasks.

### `keywords.py`

Handles automatic task category detection and XP assignment.

### `search_sort.py`

Contains searching and sorting functions for tasks.

### `queue.py`

Implements the queue used for completed tasks.

### `xp_tree.py`

Manages XP, levels, progress, and virtual tree growth.

### `undo.py`

Implements the stack used for the Undo feature.

## 🚀 Run Locally

### Prerequisites

* Python 3.x
* Git

### Clone the Repository

```bash
git clone https://github.com/Nusrat-Jahann/Taskopoly.git
```

### Navigate to the Project

```bash
cd Taskopoly
```

### Run Taskopoly

```bash
python main.py
```

## How It Works

1. The user creates a task.
2. Taskopoly automatically detects its category and XP.
3. The task is stored in the linked list.
4. When the task is completed, the user earns XP.
5. Completed tasks are added to the queue.
6. XP contributes to the user's level and virtual tree growth.
7. Users can search and sort their tasks.
8. The Undo feature allows users to reverse their most recent action.

## 🎓 Project

Taskopoly was created as a **team project for a Data Structures & Algorithms course**, focusing on applying fundamental DSA concepts to a practical and engaging task management system.

The project demonstrates how traditional data structures can be combined with gamification to create a more interactive user experience.
