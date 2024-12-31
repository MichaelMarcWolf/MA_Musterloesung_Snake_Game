<!-- README.md -->

# Python Snake Game

A simple, **modular** Snake game in Python using **Pygame**.

## Features
- **Modular Structure:** `snake_game/` holds core logic and utilities.
- **Customizable:** Screen size, cell size, and speed are easily adjustable.
- **Extendable:** Utility functions in `utils.py`; `main.py` as the game entry point.

## Installation
1. **Clone** this repo or download the source.
2. **Create** & **Activate** a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
3. **Install dependencies:
   ```bash
   pip install -r requirements.txt    

## Run
python main.py
Use arrow keys to move the snake, avoid collisions, and eat food.

## Project Structure
.
├── README.md
├── LICENSE
├── requirements.txt
├── main.py
└── snake_game/
    ├── utils.py
    └── snake_game.py