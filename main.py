import pygame
import numpy as np


def calc_acceleration(m1, m2, p1, p2, p3):
    G = 1000
    return -G * m1 * (p1 - p2) / (np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**3) - \
        G * m2 * (p1 - p3)/(np.sqrt((p1[0] - p3[0])**2 + (p1[1] - p3[1])**2)**3)

def draw_text(bodies):
    b1_vel_surf = font.render("b1 vel: " + str(b1["vel"]), False, (255,255,255))
    screen.blit(b1_vel_surf, (10, 10))
    b1_pos_surf = font.render("b1 pos: " + str(b1["pos"]), False, (255,255,255))
    screen.blit(b1_pos_surf, (10, 25))

    b2_vel_surf = font.render("b2 vel: " + str(b2["vel"]), False, (255,255,255))
    screen.blit(b2_vel_surf, (10, 45))
    b2_pos_surf = font.render("b2 pos: " + str(b2["pos"]), False, (255,255,255))
    screen.blit(b2_pos_surf, (10, 60))

    b3_vel_surf = font.render("b3 vel: " + str(b3["vel"]), False, (255,255,255))
    screen.blit(b3_vel_surf, (10, 80))
    b3_pos_surf = font.render("b3 pos: " + str(b3["pos"]), False, (255,255,255))
    screen.blit(b3_pos_surf, (10, 95))

def draw_bodies():
    pygame.draw.circle(screen, b1["color"], pygame.Vector2(b1["pos"][0], b1["pos"][1]), 5)
    pygame.draw.circle(screen, b2["color"], pygame.Vector2(b2["pos"][0], b2["pos"][1]), 5)
    pygame.draw.circle(screen, b3["color"], pygame.Vector2(b3["pos"][0], b3["pos"][1]), 5)


pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 18)


b1 = {
    "color": (207, 195, 39),
    "mass": 600,
    "pos": np.array([int(screen.get_width() / 3), int(screen.get_height() / 3)]),
    "vel": np.array([-3, 3])
}

b2 = {
    "color": (61, 24, 168),
    "mass": 600,
    "pos": np.array([int(screen.get_width() / 3 * 2), int(screen.get_height() / 3)]),
    "vel": np.array([-3, -3])
}

b3 = {
    "color": (168, 67, 24),
    "mass": 600,
    "pos": np.array([int(screen.get_width() / 2), int(screen.get_height() / 3 * 2)]),
    "vel": np.array([3, -3])
}

clock = pygame.time.Clock()
running = True
delta_time = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    b1_acc = calc_acceleration(b2["mass"], b3["mass"], b1["pos"], b2["pos"], b3["pos"])
    b2_acc = calc_acceleration(b3["mass"], b1["mass"], b2["pos"], b3["pos"], b1["pos"])
    b3_acc = calc_acceleration(b1["mass"], b2["mass"], b3["pos"], b1["pos"], b2["pos"])

    b1["vel"] = b1["vel"] + delta_time * b1_acc
    b2["vel"] = b2["vel"] + delta_time * b2_acc
    b3["vel"] = b3["vel"] + delta_time * b3_acc

    b1["pos"] = b1["pos"] + delta_time * b1["vel"]
    b2["pos"] = b2["pos"] + delta_time * b2["vel"]
    b3["pos"] = b3["pos"] + delta_time * b3["vel"]

    screen.fill((20, 12, 43))

    draw_text([b1, b2, b3])
    draw_bodies()

    pygame.display.flip()
    delta_time = clock.tick(60) / 500

pygame.quit()

