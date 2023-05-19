import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        player_walk1 = pygame.image.load('runner assets/player run/player_walk1.png').convert_alpha()
        player_walk2 = pygame.image.load('runner assets/player run/player_walk2.png').convert_alpha()
        player_walk3 = pygame.image.load('runner assets/player run/player_walk3.png').convert_alpha()
        player_walk4 = pygame.image.load('runner assets/player run/player_walk4.png').convert_alpha()
        player_walk5 = pygame.image.load('runner assets/player run/player_walk5.png').convert_alpha()
        player_walk6 = pygame.image.load('runner assets/player run/player_walk6.png').convert_alpha()
        player_walk1 = pygame.transform.scale(player_walk1, (72, 72))
        player_walk2 = pygame.transform.scale(player_walk2, (72, 72))
        player_walk3 = pygame.transform.scale(player_walk3, (72, 72))
        player_walk4 = pygame.transform.scale(player_walk4, (72, 72))
        player_walk5 = pygame.transform.scale(player_walk5, (72, 72))
        player_walk6 = pygame.transform.scale(player_walk6, (72, 72))
        self.player_walk = [player_walk1, player_walk2, player_walk3, player_walk4, player_walk5, player_walk6]
        self.player_walk_index = 0

        # JUMP ANIMATION
        player_jump1 = pygame.image.load('runner assets/player jump up/player jump1.png').convert_alpha()
        player_jump2 = pygame.image.load('runner assets/player jump up/player jump2.png').convert_alpha()
        player_jump3 = pygame.image.load('runner assets/player jump up/player jump3.png').convert_alpha()
        player_jump1 = pygame.transform.scale(player_jump1, (72, 72))
        player_jump2 = pygame.transform.scale(player_jump2, (72, 72))
        player_jump3 = pygame.transform.scale(player_jump3, (72, 72))
        self.player_jump = [player_jump1, player_jump2, player_jump3]
        self.player_jump_index = 0
        self.image = self.player_walk[self.player_jump_index]


        self.rect = self.image.get_rect(midbottom=(100, 640))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('runner assets/audio/jump.mp3')
        self.jump_sound.set_volume(0.7)
        self.landing_sound = pygame.mixer.Sound('runner assets/audio/landing.mp3')


    def player_input(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.rect.bottom >= 640:
            self.gravity = -24
            self.jump_sound.play()


    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 640:
            self.rect.bottom = 640


    def animation_frame(self):
        if self.rect.bottom < 640:
            self.player_jump_index += 0.3
            if self.player_jump_index >= len(self.player_jump):
                self.player_jump_index = 0
            self.player_surface = self.player_jump[int(self.player_jump_index)]

        else:
            self.player_walk_index += 0.3
            if self.player_walk_index >= len(self.player_walk):
                self.player_walk_index = 0
            self.image = self.player_walk[int(self.player_walk_index)]


    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_frame()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            fly_fly1 = pygame.image.load('runner assets/fly fly/fly_fly1.png').convert()
            fly_fly2 = pygame.image.load('runner assets/fly fly/fly_fly2.png').convert()
            fly_fly3 = pygame.image.load('runner assets/fly fly/fly_fly3.png').convert()
            fly_fly1 = pygame.transform.scale(fly_fly1, (36, 36))
            fly_fly2 = pygame.transform.scale(fly_fly2, (36, 36))
            fly_fly3 = pygame.transform.scale(fly_fly3, (36, 36))
            self.frames = [fly_fly1, fly_fly2, fly_fly3]
            y_pos = 440

            self.speed = 10

        else:
            mush_walk1 = pygame.image.load('runner assets/mushroom walk/mushroom_walk1.png').convert()
            mush_walk2 = pygame.image.load('runner assets/mushroom walk/mushroom_walk2.png').convert()
            mush_walk3 = pygame.image.load('runner assets/mushroom walk/mushroom_walk3.png').convert()
            mush_walk4 = pygame.image.load('runner assets/mushroom walk/mushroom_walk4.png').convert()
            mush_walk5 = pygame.image.load('runner assets/mushroom walk/mushroom_walk5.png').convert()
            mush_walk6 = pygame.image.load('runner assets/mushroom walk/mushroom_walk6.png').convert()
            mush_walk7 = pygame.image.load('runner assets/mushroom walk/mushroom_walk7.png').convert()
            mush_walk8 = pygame.image.load('runner assets/mushroom walk/mushroom_walk8.png').convert()
            mush_walk1 = pygame.transform.scale(mush_walk1, (72, 72))
            mush_walk2 = pygame.transform.scale(mush_walk2, (72, 72))
            mush_walk3 = pygame.transform.scale(mush_walk3, (72, 72))
            mush_walk4 = pygame.transform.scale(mush_walk4, (72, 72))
            mush_walk5 = pygame.transform.scale(mush_walk5, (72, 72))
            mush_walk6 = pygame.transform.scale(mush_walk6, (72, 72))
            mush_walk7 = pygame.transform.scale(mush_walk7, (72, 72))
            mush_walk8 = pygame.transform.scale(mush_walk8, (72, 72))
            self.frames = [mush_walk1, mush_walk2, mush_walk3, mush_walk4, mush_walk5, mush_walk6, mush_walk7, mush_walk8]
            y_pos = 643

            self.speed = 12

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(1300, 1600), y_pos))

    def animation_frame(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_frame()
        self.rect.x -= self.speed

    def delete(self):
        if self.rect.x <= -100:
            self.kill()


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'score: {current_time}', False, 'black')
    score_rect = score_surface.get_rect(center = (640, 120))
    screen.blit(score_surface, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 7

            if obstacle_rect.bottom == 643:
                screen.blit(mush_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else: return[]

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()

        loss_Sound = pygame.mixer.Sound('runner assets/audio/loss.mp3')
        loss_Sound.play()
        bg_Music.play(loops=-1)

        return False
    else: return True


# -- initialize window
pygame.init()
screen = pygame.display.set_mode((1280,720)) # middle is 640 x 360
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('runner assets/monocraft.ttf', 50)
game_active = False
start_time = 0

game_Music = pygame.mixer.Sound('runner assets/audio/RUN.mp3')
bg_Music = pygame.mixer.Sound('runner assets/audio/Title.mp3')
bg_Music.set_volume(.3)
bg_Music.play(loops = -1)

player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()


# -- bg fg
bg_surface = pygame.image.load('runner assets/background.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (1280, 720))

# -- fg
fg_surface = pygame.image.load('runner assets/dirt block.png').convert_alpha()
fg_surface = pygame.transform.scale(fg_surface, (80, 80))

# score text
text_surface = test_font.render('SCORE: 0', False, 'Black')
text_rect = text_surface.get_rect(center = (640, 200))
text_rect.center = (640, 200)

# start screen
title_frame1 = pygame.image.load('runner assets/title/title frame 1.png').convert_alpha()
title_frame2 = pygame.image.load('runner assets/title/title frame 2.png').convert_alpha()
title_frame1 = pygame.transform.scale(title_frame1, (1280, 720))
title_frame2 = pygame.transform.scale(title_frame2, (1280, 720))

title_frame = [title_frame1, title_frame2]
title_frames_index = 0
title_surface = title_frame[title_frames_index]


# obstacle timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1000)

# -- fg
fg_surface_width = 80
fg_count = 18
# fg_x_positions is a list of all x positions the fg blocks should be in
fg_x_positions = [i * (fg_surface_width) for i in range(fg_count)]



# -- event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))

        else:
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                game_active = True

                bg_Music.stop()
                title_select = pygame.mixer.Sound('runner assets/audio/Title select.mp3')
                title_select.play()


                game_Music.set_volume(.3)
                game_Music.play(loops= -1)

                start_time = int(pygame.time.get_ticks() / 1000)


    # -- if playing game, blit
    if game_active:
        # blit bg
        screen.blit(bg_surface,(0,0))

        # blit fg
        for i in range(fg_count):
            # moves the fg by 2px each frame
            fg_x_positions[i] -= 15

            # If the fg_surface has moved off the screen to the left, remove it and add a new one on the right
            if fg_x_positions[i] < -80:
                fg_x_positions[i] = max(fg_x_positions) + 60
                fg_count += 1
                fg_x_positions.append(fg_x_positions[i] + 60)

        for x in fg_x_positions:
            screen.blit(fg_surface, (x, 640))


        # blit score
        score = display_score()


        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()

        game_active = collision_sprite()

    else:
        title_frames_index += 0.1
        if title_frames_index >= len(title_frame):
            title_frames_index = 0
        title_surface = title_frame[int(title_frames_index)]
        screen.blit(title_surface, (0, 0))

        if pygame.mixer.get_busy() == True:
            game_Music.stop()
            bg_Music.set_volume(.3)



    # update everything
    pygame.display.update()
    clock.tick(60)
