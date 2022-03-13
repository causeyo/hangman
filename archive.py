def redraw_window(window, buttons, font, password, guessed_letters):
    global GUESSED
    global HANGMAN_PICS
    global LIMBS
    window.fill(GREEN)
    for i in range(len(buttons)):
        if buttons[i][4]:
            pygame.draw.circle(window, BLACK, (buttons[i][1], buttons[i][2]), buttons[i][3])
            pygame.draw.circle(window, buttons[i][0], (buttons[i][1], buttons[i][2]), buttons[i][3] - 2)
            label = font.render(chr(buttons[i][5]), 1, BLACK)
            window.blit(label, (buttons[i][1] - (label.get_width() / 2), buttons[i][2] - (label.get_height() / 2)))
    password = hide_password(password, guessed_letters)
    password_label = font.render(password, 1, BLACK)
    frame = password_label.get_rect()
    frame_length = frame[2]
    window.blit(password_label, (WIN_WIDTH/2 - frame_length/2, 400))
    pygame.display.update()
    input("dajesz mordo: ")
    return window