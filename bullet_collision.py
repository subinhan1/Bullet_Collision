#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 22:16:26 2023

@author: SubinHan
"""

import pymunk, pygame, sys

pygame.init()
screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 0)
bullet_m = 1
bullet_size = 10
box_l = 40
box_m = 5
box_pos = (900, 400)

def create_bullet(space):
    bullet = pymunk.Body(bullet_m, 50, body_type=pymunk.Body.DYNAMIC)
    bullet.position = (400, 400)
    shape = pymunk.Circle(bullet, bullet_size)
    space.add(bullet, shape)
    return shape

def draw_bullets(bullets):
    for b in bullets:
        pos_x = int(b.body.position.x)
        pos_y = int(b.body.position.y)
        pygame.draw.circle(screen, (0,0,0), (pos_x, pos_y), bullet_size)
        
      
        
      
def create_box(space):
    box = pymunk.Body(box_m, 100, body_type=pymunk.Body.DYNAMIC)
    box.position = box_pos
    shape = pymunk.Poly.create_box(box, (box_l, box_l))
    space.add(box, shape)
    return shape

def draw_boxes(boxes):
    for b in boxes:
        rect = pygame.Rect(box_pos, (box_l, box_l))
        pygame.draw.rect(screen, (0,0,255), rect)



bullets = []
bullets.append(create_bullet(space))
boxes = []
boxes.append(create_box(space))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill((217, 217, 217))
    draw_bullets(bullets)
    draw_boxes(boxes)
    space.step(0.02)
    pygame.display.update()
    clock.tick(60)
            
            
            

