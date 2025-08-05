# The "Rock - Paper - Scissors" Game
This is a console based game I made using SoftUni's ideas and guidences.
## Game Rules:
This is a console based implementation of the well-known **Rock** - **Paper** - **Scissors** game

<img width="400" height="400" alt="rock-paper-scissors-game-rules" src="https://github.com/user-attachments/assets/62fbc5d4-823f-4f1b-a837-549a0eed695a" />

As the image shows the rules are simple:
The game is played by two players. Each player chooses '**Rock**', '**Paper**', or '**Scissors**' simultaneously. Rock beats scissors, scissors beats paper and paper beats rock. The **winner** is the player whose choice beats the choise of it's opponent.

In this console based implementation the user plays versus the computer. The user can choose '**Rock**', '**Paper**', or '**Scissors**' by typing '**r**', '**p**' or '**s**' respectively when prompted. Then the computer chooses **randomly** then reveals the **winner**.

### All posible situations:
<img width="215" height="204" alt="image" src="https://github.com/user-attachments/assets/7e6468a1-c8f1-4b03-b35c-30d6370cf11d" />

### Solution:
I used **While Loop** in order the game to be replayable. Then I used **conditional statements** for the logic of the game. I also imported the **random** module and used the **randint()** method for the random choice of the computer. I noticed that the outcome of the game was too fast and imported the **time** module and used the **time.sleep()** function in order the user to better grasp what had happened. I added **score counters** and **ANSI** color codes in the output text for a more pleasant user experience.

### Source code link: [Source Code](rock_paper_scissors.py)

### Screenshot from the game:
<img width="501" height="250" alt="rock_paper_scissors" src="https://github.com/user-attachments/assets/b29b4501-d730-4dc2-b595-32a3f6f00b84" />

### Live Demo:
You can play the game directly on your web brouser:
 [![Run on Replit](https://replit.com/badge/github/vakeca/RockPaperScissorsByIvan)](https://replit.com/new/github/vakeca/RockPaperScissorsByIvan)
