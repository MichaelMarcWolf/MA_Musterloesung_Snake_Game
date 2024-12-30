import pygame    # type: ignore
import numpy as np    # type: ignore
import random  
from collections import deque  

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400  
GRID_SIZE = 20  
SNAKE_SPEED = 10  

# Define the main SnakeGame class
class SnakeGame:
    def __init__(self):
        # Initialize pygame and set up the game window
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create the game screen
        pygame.display.set_caption("Snake Game")  # Set the window title
        self.clock = pygame.time.Clock()  # Create a clock to control game speed
        # Initialize a grid to represent the game board
        self.grid = np.zeros((SCREEN_WIDTH // GRID_SIZE, SCREEN_HEIGHT // GRID_SIZE), dtype=int)
        
        # Initialize the snake
        self.snake = deque([(5, 5)])  # The snake starts as a single segment at position (5, 5)
        self.food = self.spawn_food()  # Place the first food randomly
        self.direction = (0, 1)  # The snake starts by moving to the right
        self.running = True  # A flag to indicate whether the game is running

    def spawn_food(self):
        """
        Randomly places the food on the grid at a position that is not occupied by the snake.
        """
        while True:
            x, y = random.randint(0, SCREEN_WIDTH // GRID_SIZE - 1), random.randint(0, SCREEN_HEIGHT // GRID_SIZE - 1)
            if (x, y) not in self.snake:  # Ensure the food doesn't spawn on the snake
                return x, y

    def render_grid(self):
        """
        Draws the game elements (snake and food) on the screen.
        """
        self.screen.fill((0, 0, 0))  # Clear the screen by filling it with black
        # Draw each segment of the snake as a green rectangle
        for x, y in self.snake:
            pygame.draw.rect(self.screen, (0, 255, 0), (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        # Draw the food as a red rectangle
        pygame.draw.rect(self.screen, (255, 0, 0), (self.food[0] * GRID_SIZE, self.food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        pygame.display.flip()  # Update the screen

    def move(self):
        """
        Moves the snake in the current direction and handles collisions (walls, self, and food).
        """
        head_x, head_y = self.snake[0]  # Get the current position of the snake's head
        new_head = (head_x + self.direction[0], head_y + self.direction[1])  # Calculate the new head position

        # Check if the snake collides with itself or the walls
        if (
            new_head in self.snake or  # Collision with the snake's own body
            new_head[0] < 0 or new_head[1] < 0 or  # Collision with the top/left wall
            new_head[0] >= SCREEN_WIDTH // GRID_SIZE or new_head[1] >= SCREEN_HEIGHT // GRID_SIZE  # Collision with the bottom/right wall
        ):
            self.running = False  # Stop the game
            return

        # Move the snake: Add the new head position to the front of the deque
        self.snake.appendleft(new_head)
        if new_head == self.food:  # Check if the snake eats the food
            self.food = self.spawn_food()  # Spawn new food
        else:
            self.snake.pop()  # Remove the last segment to maintain the snake's length

    def change_direction(self, new_dir):
        """
        Changes the snake's direction, preventing it from reversing into itself.
        """
        # Prevent the snake from reversing (e.g., going from left to right and vice versa)
        if (new_dir[0] * -1, new_dir[1] * -1) != self.direction:
            self.direction = new_dir

    def run(self):
        """
        Main game loop that keeps the game running until the user quits or loses.
        """
        while self.running:
            # Handle user input and events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Check if the user closes the window
                    self.running = False
                if event.type == pygame.KEYDOWN:  # Check if the user presses a key
                    # Update the snake's direction based on arrow keys
                    if event.key == pygame.K_UP:
                        self.change_direction((0, -1))
                    elif event.key == pygame.K_DOWN:
                        self.change_direction((0, 1))
                    elif event.key == pygame.K_LEFT:
                        self.change_direction((-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        self.change_direction((1, 0))

            # Update the game state
            self.move()  
            self.render_grid()  
            self.clock.tick(SNAKE_SPEED)  

        pygame.quit()  # Quit pygame when the game loop ends


# Entry point of the script
if __name__ == "__main__":
    game = SnakeGame()  
    game.run()  