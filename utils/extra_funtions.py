import pygame

def message_display(text, size, posx, posy, window):
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (posx, posy)
    window.blit(TextSurf, TextRect)

def text_objects(text, font):
    textSurface = font.render(text, True, (0, 255, 0))
    return textSurface, textSurface.get_rect()