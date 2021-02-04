import pygame
from pygame.locals import *
import os


class Card():

    def __init__(self, rank, suit, point_value):
        self.rank = rank
        self.suit = suit
        self.point_value = point_value
        self.up = True
        self.back = pygame.image.load(os.path.join('Images', 'card_back.jpg'))
        if suit == "SPADES":
            if rank == "ACE":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Ace_Spades.jpg'))
            elif rank == "TWO":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Two_Spades.jpg'))
            elif rank == "THREE":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Three_Spades.jpg'))
            elif rank == "FOUR":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Four_Spades.jpg'))
            elif rank == "FIVE":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Five_Spades.jpg'))
            elif rank == "SIX":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Six_Spades.jpg'))
            elif rank == "SEVEN":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Seven_Spades.jpg'))
            elif rank == "EIGHT":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Eight_Spades.jpg'))
            elif rank == "NINE":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Nine_Spades.jpg'))
            elif rank == "TEN":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Ten_Spades.jpg'))
            elif rank == "JACK":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Jack_Spades.jpg'))
            elif rank == "QUEEN":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Queen_Spades.jpg'))
            elif rank == "KING":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'King_Spades.jpg'))
        elif suit == "CLUBS":
            if rank == "ACE":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Ace_Clubs.jpg'))
            elif rank == "TWO":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Two_Clubs.jpg'))
            elif rank == "THREE":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Three_Clubs.jpg'))
            elif rank == "FOUR":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Four_Clubs.jpg'))
            elif rank == "FIVE":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Five_Clubs.jpg'))
            elif rank == "SIX":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Six_Spades.jpg'))
            elif rank == "SEVEN":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Seven_Clubs.jpg'))
            elif rank == "EIGHT":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Eight_Clubs.jpg'))
            elif rank == "NINE":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Nine_Clubs.jpg'))
            elif rank == "TEN":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Ten_Spades.jpg'))
            elif rank == "JACK":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Jack_Clubs.jpg'))
            elif rank == "QUEEN":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Queen_Clubs.jpg'))
            elif rank == "KING":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'King_Clubs.jpg'))
        elif suit == "HEARTS":
            if rank == "ACE":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Ace_Hearts.jpg'))
            elif rank == "TWO":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Two_Hearts.jpg'))
            elif rank == "THREE":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Three_Hearts.jpg'))
            elif rank == "FOUR":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Four_Hearts.jpg'))
            elif rank == "FIVE":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Five_Hearts.jpg'))
            elif rank == "SIX":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Six_Hearts.jpg'))
            elif rank == "SEVEN":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Seven_Hearts.jpg'))
            elif rank == "EIGHT":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Eight_Hearts.jpg'))
            elif rank == "NINE":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Nine_Hearts.jpg'))
            elif rank == "TEN":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Ten_Hearts.jpg'))
            elif rank == "JACK":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Jack_Hearts.jpg'))
            elif rank == "QUEEN":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Queen_Hearts.jpg'))
            elif rank == "KING":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'King_Hearts.jpg'))
        elif suit == "DIAMONDS":
            if rank == "ACE":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Ace_Diamonds.jpg'))
            elif rank == "TWO":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Two_Diamonds.jpg'))
            elif rank == "THREE":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Three_Diamonds.jpg'))
            elif rank == "FOUR":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Four_Diamonds.jpg'))
            elif rank == "FIVE":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Five_Diamonds.jpg'))
            elif rank == "SIX":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Six_Diamonds.jpg'))
            elif rank == "SEVEN":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Seven_Diamonds.jpg'))
            elif rank == "EIGHT":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Eight_Diamonds.jpg'))
            elif rank == "NINE":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Nine_Diamonds.jpg'))
            elif rank == "TEN":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Ten_Diamonds.jpg'))
            elif rank == "JACK":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Jack_Diamonds.jpg'))
            elif rank == "QUEEN":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'Queen_Diamonds.jpg'))
            elif rank == "KING":
               self.front_image = pygame.image.load(os.path.join(
                   'Images', 'King_Diamonds.jpg'))
       
    
    def __str__(self):
        return '{} of {} (Value = {})'.format(
            self.rank,self.suit,self.point_value)

    def draw(self,win,x,y):
        if self.up:
            win.blit(self.front_image,(x,y))
        else:
            win.blit(self.back,(x,y))

    def flip(self):
        if self.up:
            self.up = False
        else:
            self.up = True
