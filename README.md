
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Project Title >>
## CS110 Final Project  << Semester, Year >>

## Team Members

Tristan

***

## Project Description

This will be a simple game of Blackjack against a CPU. The player and CPU will be dealt with 2 cards, both of your cards being shown and only one of the CPU's cards being shown. You can choose to either stand or hit. If you hit and go over you will be presented with a gameover screen. If you hit and don't go over and the CPU goes over then you will be met with a winning screen. You will also be automatically met with a winning screen if both you and the CPU stand and you have a higher value of cards or if you hit 21.
***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design


![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. start menu
2. hit button
3. deal button
4. stand button
5. lose screen
6. win screen

### Classes

Deal: A class that lets the player deal their beginning cards
Hit: A class that lets the player take a hit with a goal of winning the game.
Stand: A class that lets the player stand with their cards and not take a hit.
Deck: A class that makes a deck of cards and shuffles them.
Hand: A class that determines the total value of cards that the player is currently holding and 

## ATP

| Step                 |Procedure                                        |Expected Results                                                        |
|----------------------|:-----------------------------------------------:|-----------------------------------------------------------------------:|
|  1                   | Type template_final-project master/src          | Black Jack game appears                                                |
|  2                   | Click deal button                               | Players and CPU are dealt 2 cards                                      |
|  3                   | Click hit button                                | Player is hit with a card and loses if user goes over but stays if not.|
|  4                   | Click stand button                              | Player does not draw and wins/loses depending on CPU                   |
|  5                   | Check that card values are being added properly | Proper winner will receieve a win at the end of a match                |
|  6                   | Start game and play until either lose/win.      | Lose/win screen pops up after losing/winning.                          |

