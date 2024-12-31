"""
main.py

This file serves as the main entry point for running the Snake Game.
"""

from snake_game.game import SnakeGame

if __name__ == "__main__":
    # Instantiate the game
    game = SnakeGame()
    
    # Run the main game loop
    game.run()