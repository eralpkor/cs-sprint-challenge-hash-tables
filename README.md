# Sprint Challenge: Hash Tables

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This challenge allows you to practice the concepts and techniques learned over the past sprint and apply them in a concrete project. This sprint explored hash tables. During this sprint, you studied hash functions, collision resolution, complexity analysis of hash tables, load factor, resizing, and various use cases for hash tables. In your challenge this week, you will demonstrate mastery of these skills by solving five problems related to hash tables.

The sprint challenge is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the sprint challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your TL if you need direction.

_You have **three hours** to complete this challenge. Plan your time accordingly._

## Introduction

This challenge requires you to solve algorithm problems that are amenable to being solved efficiently with a hash table.

### Commits

Commit your code regularly and meaningfully. This practice helps both you (in case you ever need to return to old code for any number of reasons) and your Team Lead as they evaluate your solution.

## Interview Questions

Be prepared to demonstrate your understanding of this week's concepts by answering questions on the following topics. You might prepare by writing down your answers beforehand.

-- A hash procedure must be deterministic—meaning that for a given input value it must always generate the same hash value. In other words, it must be a function of the data to be hashed, in the mathematical sense of the term.

1. Hashing functions
  - In simple terms, a hash function maps a big number or string to a small integer that can be used as the index in the hash table.

2. Collision resolution
  - Collision: A collision occurs when two keys are hashed to the same index in a hash table.

Open Addressing and Linear Probing:
   -  One method is to start at the collision location and move sequentially through the slots in the hash table until we find an empty slot. That empty slot is used instead of the original collision location. To cover the entire hash table, sometimes you even have to go back to the first slot (circularly). This type of collision resolution is called open addressing with linear probing.

Chaining
  - In the chaining approach, the hash table is an array of linked lists i.e., each index has its own linked list.

  All key-value pairs mapping to the same index will be stored in the linked list of that index.
The benefits of chaining
  - Through chaining, insertion in a hash table always occurs in `O(1)` since linked - lists allow insertion in constant time.
  - Theoretically, a chained hash table can grow infinitely as long as there is enough space.
A hash table which uses chaining will never need to be resized.

3. Performance of basic hash table operations
- Insert: `O(1)`, Deletion: `O(1)`, worst `O(n)`, Access: `O(1)`, worst `O(n)`

4. Load factor
You take the number of items stored in the hash table divided by the number of slots.

5. Automatic resizing
- The general rule of thumb is to resize your hash table when your load factor is greater than 0.7. Also, when you resize, it is common to double the size of the hash table. When you resize the array, you need to re-insert all of the items into this new hash table. You cannot simply copy the old items into the new hash table. Each item has to be rerun through the hashing function because the hashing function takes into account the size of the hash table when determining the index that it returns.

6. Various use cases for hash tables
- a digital phone book (maps a person’s name to their phone number).
  - DNS resolution (maps a web address to an IP address).
  - student records (a unique student id maps to student information).
  - library system (a book’s unique identifier maps to detailed book information).
  

We expect you to be able to answer questions in these areas. Your responses contribute to your Sprint Challenge grade.

## Instructions

### Task 1: Project Set-Up

- [ ] Create a forked copy of this project
- [ ] Add your team lead as a collaborator on Github
- [ ] Clone your OWN version of the repository (Not Lambda's by mistake!)
- [ ] Create a new branch: git checkout -b `<firstName-lastName>`.
- [ ] Implement the project on your newly created `<firstName-lastName>` branch, committing changes regularly
- [ ] Push commits: git push origin `<firstName-lastName>`

### Task 2: Project Requirements

Your finished project must include all of the following requirements:

- [ ] Solve any three of the five problems

For each problem that you choose to solve, complete the following:

- [ ] Navigate into each exercise's directory
- [ ] Read the instructions for the exercise in the README
- [ ] Implement your solution in the `.py` skeleton file
- [ ] Make sure your code passes the tests running the test script with make tests

*Note: For these exercises, we expect you to use Python's built-in `dict` as a hashtable. That said, if you wish, you can attempt to solve using your own hashtable implementation, as well. All solutions should utilize a `dict` or hashtable. You should not use Sets. (Though you can make a `dict` behave like a set if you wish.)*

### Task 3: Stretch Goals

After finishing your required elements, you can push your work further. These goals may or may not be things you have learned in this module, but they build on the material you just studied. Time allowing, stretch your limits, and see if you can deliver on the following optional goals:

- [ ] Solve any four of the five problems
- [ ] Solve all five problems

## Submission format

Follow these steps to complete your project.

- [ ] Submit a Pull-Request to merge <firstName-lastName> Branch into master (student's  Repo). **Please don't merge your own pull request**
- [ ] Add your team lead as a reviewer on the pull-request
- [ ] Your team lead will count the project as complete after receiving your pull-request

