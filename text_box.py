import pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Text Box Demo")

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the text box rect and font
textbox_rect = pygame.Rect(50, 50, 300, 30)
textbox_font = pygame.font.Font(None, 24)

# Initialize the input string
input_string = ""

# Set up the main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Check if a letter key was pressed
            if event.unicode.isalpha():
                input_string += event.unicode
            # Check if the backspace key was pressed
            elif event.key == pygame.K_BACKSPACE:
                input_string = input_string[:-1]

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the text box
    pygame.draw.rect(screen, BLACK, textbox_rect, 2)

    # Render the input string and blit it to the screen
    input_text = textbox_font.render(input_string, True, BLACK)
    screen.blit(input_text, (textbox_rect.x+5, textbox_rect.y+5))

    # Update the screen
    pygame.display.flip()

# Clean up
pygame.quit()
