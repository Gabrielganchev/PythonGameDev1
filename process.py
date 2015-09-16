import pygame, sys, classes, random
def process(bug, FPS, total_frames):

    # PROCESSING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
# makes the game close   when event is quit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                classes.BugProjectile.fire = not classes.BugProjectile.fire
# goes for the E key is pressed and witchers the from spear to frost
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:

        bug.image = pygame.image.load("images/hero2.png")
        bug.velx = 5
        classes.Bug.going_right = True
    elif keys[pygame.K_a]:
        bug.image = pygame.image.load("images/hero2fliped.png")

        bug.velx = -5
        classes.Bug.going_right = False
    else:
        bug.velx = 0

    if keys[pygame.K_w]:
        bug.jumping = True

    if keys[pygame.K_SPACE]:
        def direction():

            if classes.Bug.going_right:
                p.velx = 8
            else:
                p.image = pygame.transform.flip(p.image, True, False)
                p.velx = -8
        if (classes.BugProjectile.fire):

            p = classes.BugProjectile(bug.rect.x, bug.rect.y,True, "images/spears.png")
            direction()
        else:
            p = classes.BugProjectile(bug.rect.x, bug.rect.y,False, "images/frost.png")
            direction()



    spawn(FPS, total_frames)
    collisions()

def spawn (FPS, total_frames):
    four_seconds = FPS * 4
    if total_frames % four_seconds == 0:
        r = random.randint(1, 2)
        x = 1
        if r == 2:
            x = 640 - 40
        classes.Enemy(x, 130, "images/enemybug1.png")



def collisions():

    for fly in classes.Enemy.List:

        projectiles = pygame.sprite.spritecollide(fly,classes.BugProjectile.List, True)

        for projectile in projectiles:

            fly.health = 0

            if projectile.if_this_variable_is_true_then_fire:
                pass

            else:

                if fly.velx > 0:

                    fly.image = pygame.image.load("images/frozenbug1.png")
                elif fly.velx < 0:
                    fly.image = pygame.image.load("images/frozenbug1.png")

            projectile.rect.x = 2 * -projectile.rect.width
            projectile.destroy()


