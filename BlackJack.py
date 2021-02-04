import pygame, sys
from pygame.locals import *
from Card import *
from BlackJackDeck import *
import random as rand
import os

#pygame constructor call and screen creation
pygame.init()
screen = pygame.display.set_mode((800,600))

#Creation of text size and font
helvetica_40 = pygame.font.Font(os.path.join("Fonts", "Helvetica.ttf"), 40)
chaucer_50 = pygame.font.Font(os.path.join("Fonts", "chaucerregular.ttf"), 50)
chaucer_30 = pygame.font.Font(os.path.join("Fonts", "chaucerregular.ttf"), 30)
helvetica_70 = pygame.font.Font(os.path.join("Fonts", "Helvetica.ttf"), 70)
helvetica_20 = pygame.font.Font(os.path.join("Fonts", "Helvetica.ttf"), 20)

deck = BlackJackDeck()
hand = []
player_hand = []
dealer_hand = []
play = True


#initializes variables for rendering font
font_1 = helvetica_40
text_1 = "Do you want to play a game?"
x_1 = 150
y_1 = 300

font_2 = helvetica_20
text_2 = "Press[ENTER] to start game or press [BACKSPACE] to quit"
x_2 = 135
y_2 = 350

rend_font = [font_1, text_1, x_1, y_1, font_2, text_2, x_2, y_2]

#Adds 2 cards to player and dealer hands (first card in dealer hand is face down)
for z in range(2):
    player_hand.append(deck.draw())
    dealer_hand.append(deck.draw())
dealer_hand[0].flip()


def game_text(f, t, x, y):
    if f != "none" and t != "none":
        print_text = f.render(t, 1, (0, 0, 0))
        screen.blit(print_text, (x, y))

#code to display main screen
def main_screen():
    display_text = game_text(rend_font[0], rend_font[1], rend_font[2], rend_font[3])
    display_text = game_text(rend_font[4], rend_font[5], rend_font[6], rend_font[7])
    

#code to play a game
def new_game(p):
    #Resets screen and displays "Black Jack", "Player Hand", "Dealer Hand", 
    #and instructions
    font_1 = "none"
    text_1 = "none"
    x_1 = 0
    y_1 = 0
    rend_font = [font_1, text_1, x_1, y_1]
    screen.fill((0, 180, 30))
    display_text = game_text(rend_font[0], rend_font[1], rend_font[2], rend_font[3])
    black_jack = chaucer_50.render("Black Jack", 1, (0, 0, 0))
    screen.blit(black_jack, (300, 5))
    player_prompts = helvetica_20.render("Press [SPACEBAR] to draw a new card or [SHIFT] to stand", 1, (0, 0, 0))
    screen.blit(player_prompts, (150, 570))
    player_text = chaucer_30.render("Player Hand", 1, (225, 0, 0))
    screen.blit(player_text, (10, 400))
    dealer_text = chaucer_30.render("Dealer Hand", 1, (225, 0, 0))
    screen.blit(dealer_text, (10, 120))
    
    #Print of Player and Dealer Hands
    player_x = 210
    dealer_x = 210
    player_value = 0
    dealer_value = 0
    for c in player_hand:
        c.draw(screen, player_x, 350)
        player_x += 30
        player_value += c.point_value
    for card in dealer_hand:
        card.draw(screen, dealer_x, 70)
        dealer_x += 30
        dealer_value += card.point_value
    #Game function
    if p == False:
        while dealer_value < 15:
            dealer_hand.append(deck.draw())
        if dealer_value >= 15 and dealer_value < 21:
            r = rand.randint(1, 10)
            if r % 3 == 0:
                dealer_hand.append(deck.draw())
        if dealer_value > 21:
            d_count = 0
            for d_c in dealer_hand:
                if d_c.rank == "ACE":
                    d_c.point_value = 1
            for c in dealer_hand:
                d_count += c.point_value
            if d_count > 21:
                player_win = helvetica_70.render("Player Wins!", 1, (0, 0, 0))
                screen.blit(player_win, (210, 275))
        elif dealer_value == 21:
            dealer_win = helvetica_70.render("Dealer Wins!", 1, (0, 0, 0))
            screen.blit(dealer_win, (210, 275))
        elif dealer_value == player_value:
            draw_win = helvetica_70.render("It's a push!", 1, (0, 0, 0))
            screen.blit(draw_win, (210, 275))
        elif dealer_value > player_value:
            dealer_win = helvetica_70.render("Dealer Wins!", 1, (0, 0, 0))
            screen.blit(dealer_win, (210, 275))
        elif player_value > dealer_value:
            player_win = helvetica_70.render("Player Wins!", 1, (0, 0, 0))
            screen.blit(player_win, (210, 275))
        elif player_value > 21:
            p_count = 0
            for p_c in player_hand:
                if p_c.rank == "ACE":
                    p_c.point_value = 1
            for card in player_hand:
                p_count += card.point_value
            if p_count > 21:
                dealer_win = helvetica_70.render("Dealer Wins!", 1, (0, 0, 0))
                screen.blit(dealer_win, (210, 275))
        elif player_value == 21:
            player_win = helvetica_70.render("Player Wins!", 1, (0, 0, 0))
            screen.blit(player_win, (210, 275))
    if player_value > 21:
        p_count = 0
        for p_c in player_hand:
            if p_c.rank == "ACE":
                p_c.point_value = 1
        for card in player_hand:
            p_count += card.point_value
        if p_count > 21:
            dealer_win = helvetica_70.render("Dealer Wins!", 1, (0, 0, 0))
            screen.blit(dealer_win, (210, 275))
    elif player_value == 21:
        player_win = helvetica_70.render("Player Wins!", 1, (0, 0, 0))
        screen.blit(player_win, (210, 275))
    print(p)
    pygame.display.update()

#code used at the end of a game to display the "Bye!" screen and quit program
def game_end():
    if event.key == K_BACKSPACE:
        screen.fill((0, 180, 30))
        end_game = helvetica_70.render("Bye!", 1, (0, 0, 0))
        screen.blit(end_game, (300, 275))
        pygame.display.update()
        pygame.quit()

keypress = False    
end = True
while end:
    screen.fill((0,180,30))
    black_jack = chaucer_50.render("Black Jack", 1, (0, 0, 0))
    screen.blit(black_jack, (300, 5))

    if keypress == False:
        main_screen()
    else:
        new_game(play)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type==KEYDOWN and event.key==K_ESCAPE):
            end = False
            pygame.quit()
        elif event.type == KEYDOWN:
            #starts a new game when player hits enter
            if event.key == K_RETURN:
                keypress = True
                new_game(play)
            #allows player to stand by pressing shift
            elif event.key == K_RSHIFT or event.key == K_LSHIFT:
                play = False
            #allows player to draw new card by hitting the spacebar
            elif event.key == pygame.K_SPACE:
                if play == True:
                    player_hand.append(deck.draw())
            else:
                game_end()
                
                
    pygame.display.update()

                
