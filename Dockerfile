# Use a slim Python image to keep container size down
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the project files
# This includes main.py, utils.py, game.py (in subfolder), README.md, etc.
COPY . .

# Set the default command to run your main script
CMD ["python", "main.py"]