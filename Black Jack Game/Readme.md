# Blackjack Game in Python

This is a simple console-based Blackjack game implemented in Python. The game allows players to play against a dealer with the goal of getting a hand value closer to 21 without exceeding it.

## Features:

- Multiple players can participate in the game.
- The game includes standard card ranks and suits: Ace, 2-10, Jack, Queen, King.
- The dealer follows standard Blackjack rules (dealer must hit until they reach 17).
- A player can choose to "hit" (draw a card) or "stand" (keep their current hand).
- The game automatically handles busting (going over 21) and determines the winner after all players have played.

## How to Play:

1. The game will prompt you to enter player names separated by commas (e.g., `Alice, Bob`).
2. After inputting names, the game will deal two cards to each player and the dealer.
3. Each player will then have the option to "hit" or "stand".
4. The dealer will automatically play after all players have finished their turns (dealer will continue drawing cards until their hand is at least 17).
5. The game will then announce the outcome of each player's hand: win, lose, or tie.
