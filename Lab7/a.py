import pygame
import time

#1

# pygame.init()

# WINDOW_SIZE = (500, 500)


# clock_face = pygame.image.load("Lab7/images/mickeyclock.jpeg")
# hand_image = pygame.image.load("Lab7/images/Vlevo.png")
# hand_image = pygame.transform.rotate(hand_image, 180)


# clock_face = pygame.transform.scale(clock_face, WINDOW_SIZE)
# hand_image = pygame.transform.scale(hand_image, (250, 250))  #

# clock_width, clock_height = WINDOW_SIZE
# clock_center = (clock_width // 2, clock_height // 2)


# screen = pygame.display.set_mode(WINDOW_SIZE)
# pygame.display.set_caption("Mickey Mouse Clock")


# def draw_hand(image, angle, scale=1.0):

#     size = (int(image.get_width() * scale), int(image.get_height() * scale))
#     hand_resized = pygame.transform.scale(image, size)

#     rotated = pygame.transform.rotate(hand_resized, -angle)


#     rect = rotated.get_rect(center=clock_center)

#     screen.blit(rotated, rect)

# running = True
# while running:
#     screen.fill((255, 255, 255))
#     screen.blit(clock_face, (0, 0))  

#     t = time.localtime()
#     minutes = t.tm_min
#     seconds = t.tm_sec

    
#     min_angle = (minutes % 60) * 6 - 90
#     sec_angle = (seconds % 60) * 6 - 90


#     draw_hand(hand_image, min_angle, scale=0.9)   
#     draw_hand(hand_image, sec_angle, scale=1)   

 
#     pygame.display.flip()

  
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     time.sleep(1)

# pygame.quit()

#2

# import os

# pygame.init()

# WIDTH, HEIGHT = 400, 300
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Music Player")


# MUSIC_FOLDER = "Lab7/music"
# playlist = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith((".mp3", ".wav"))]
# current_track = 0  


# def play_music(track_index):
#     if 0 <= track_index < len(playlist):
#         pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, playlist[track_index]))
#         pygame.mixer.music.play()
#         print(f"Now Playing: {playlist[track_index]}")


# if playlist:
#     play_music(current_track)


# running = True
# paused = False

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE: 
#                 if pygame.mixer.music.get_busy():
#                     pygame.mixer.music.pause()
#                     paused = True
#                     print("Paused")
#                 else:
#                     pygame.mixer.music.unpause()
#                     paused = False
#                     print("Resumed")

#             elif event.key == pygame.K_n: 
#                 current_track = (current_track + 1) % len(playlist)
#                 play_music(current_track)

#             elif event.key == pygame.K_p: 
#                 current_track = (current_track - 1) % len(playlist)
#                 play_music(current_track)

# pygame.quit()

#3

# pygame.init()

# WIDTH, HEIGHT = 500, 400
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Moving Ball")

# RADIUS = 25
# ball_x, ball_y = WIDTH // 2, HEIGHT // 2
# BALL_SPEED = 20

# WHITE = (255, 255, 255)
# RED = (255, 0, 0)

# running = True
# while running:
#     screen.fill(WHITE)
#     pygame.draw.circle(screen, RED, (ball_x, ball_y), RADIUS)
#     pygame.display.flip()

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT and ball_x - RADIUS - BALL_SPEED >= 0:
#                 ball_x -= BALL_SPEED
#             elif event.key == pygame.K_RIGHT and ball_x + RADIUS + BALL_SPEED <= WIDTH:
#                 ball_x += BALL_SPEED
#             elif event.key == pygame.K_UP and ball_y - RADIUS - BALL_SPEED >= 0:
#                 ball_y -= BALL_SPEED
#             elif event.key == pygame.K_DOWN and ball_y + RADIUS + BALL_SPEED <= HEIGHT:
#                 ball_y += BALL_SPEED

# pygame.quit()


