# Two-Dice Pig Game

## Table of Contents
1. [Project Overview](#project-overview)
2. [Rules of Two-Dice Pig](#rules-of-two-dice-pig)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Running the Game](#running-the-game)
6. [Running Tests](#running-tests)
7. [Generating Documentation](#generating-documentation)
8. [Generating UML Diagrams](#generating-uml-diagrams)
9. [Developer Guide](#developer-guide)


---

## Project Overview
The **Two-Dice Pig Game** is a turn-based dice game implemented in Python. Players take turns rolling two dice to accumulate points, but rolling a “1” has penalties. The first player to reach **100 points** wins.

This project includes:

- Persistent player statistics with serialization (`pickle`)
- AI opponents with different difficulty levels
- High-score tracking
- Unit tests for all main classes
- Sphinx documentation with API and usage guides
- UML diagrams generated with Pyreverse

---

## Rules of Two-Dice Pig
- On each turn, a player rolls **two dice**.
- **No 1s rolled** → sum is added to turn score.
- **One 1 rolled** → turn ends, turn score is lost.
- **Double 1s** → total score resets to 0.
- Player can **hold** to add turn score to total score.
- First to **100 points** wins.

---

## Project Structure
assignment_2/
│
├── dice/
│ ├── dice_class.py
│ ├── dice_hand.py
│ ├── game.py
│ ├── highScore.py
│ ├── histogram.py
│ ├── intelligence.py
│ ├── player.py
│ ├── main.py # Entry point for the game
│ ├── rules.txt
│ └── *.ser # Serialized statistics
│
├── test/
│ ├── test_diceclass.py
│ ├── test_dicehand.py
│ ├── test_game.py
│ ├── test_highscore.py
│ ├── test_histogram.py
│ ├── test_intelligence.py
│ ├── test_main.py
│ ├── test_player.py
│ └── init.py
│
├── docs/
│ ├── Makefile
│ ├── make.bat
│ └── source/
│ ├── index.rst
│ ├── api.rst
│ ├── usage.rst
│ └── conf.py
│
├── README.md
├── requirements.txt
├── Makefile
└── LICENSE.md


---

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd assignment_2

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3. Install dependencies:
pip install -r requirements.txt

---

## Running the game
From the project root:
python -m dice.main

---

## Running tests
Run all tests using:
python -m unittest discover -s test -v

Check test coverage:
python -m coverage run -m unittest discover -s test
python -m coverage report -m
python -m coverage html

---

## Generating documentation



# Generating uml diagrams
We used Pyreverse (from Pylint) to generate UML diagrams.
1. Ensure Pylint is installed:
pip install pylint

2. Generate class diagrams:
pyreverse -o png -p TwoDicePigGame dice/

---

## Developer guide
Developer Guide
*Game logic is in dice/

*Unit tests are in test/

*Sphinx docs are in docs/source/

*Serialized player stats: dice/history.ser and dice/user_id.ser

---


## Code quality
Run linting and static analysis:
pylint dice/ test/
flake8 .

---

