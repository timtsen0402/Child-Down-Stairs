import pygame,math,random # type: ignore

# initialization

pygame.init()
screen_size = (600,800)
screen = pygame.display.set_mode(screen_size)
assets_path, sound_path = "assets_CDS/", "sound_CDS/"
black,  white,    yellow,  red, blue, green,  gray = \
 (0, 0, 0),(255, 255, 255), (128,128,0), (255,0,0), (0,0,128),  (0,128,0), (128,128,128)
sound_play = True # default sound on
# sounds setting
touchSound = pygame.mixer.Sound(sound_path+"AHH.wav")
deadSound = pygame.mixer.Sound(sound_path+"dead.wav")
getHP_sound = pygame.mixer.Sound(sound_path+"getHP_sound.wav")
squeezeSound = pygame.mixer.Sound(sound_path+"squeeze.wav")
startingSound = pygame.mixer.Sound(sound_path+"start.wav")
restartSound = pygame.mixer.Sound(sound_path+"restart.wav")
level_upSound = pygame.mixer.Sound(sound_path+"level_up.wav")
muteSound = pygame.mixer.Sound(sound_path+"mute.wav")
evil_laughSound = pygame.mixer.Sound(sound_path+"gasp.wav")
lengthenSound = pygame.mixer.Sound(sound_path+"lengthen.wav")
endSound = pygame.mixer.Sound(sound_path+"end.wav")
get_gold_sound = pygame.mixer.Sound(sound_path+"get_gold.wav")
magicSound = pygame.mixer.Sound(sound_path+"magic.wav")
fartSound = pygame.mixer.Sound(sound_path+"fart.wav")
tweetSound = pygame.mixer.Sound(sound_path+"tweet.wav")
fallingSound = pygame.mixer.Sound(sound_path+"fallingDown.wav")
sadSound = pygame.mixer.Sound(sound_path+"sad.wav")
# assets setting
# background surface
bkgd = (pygame.transform.scale(pygame.image.load(assets_path+"stairs2.jfif"), (600, 730))).convert()
start_bkgd = (pygame.transform.scale(pygame.image.load(assets_path+"start_bkgd.jpeg"), screen_size)).convert()
end_drawing = (pygame.transform.scale(pygame.image.load(assets_path+"dead.png"),(522,480) )).convert()
end_drawing2 = (pygame.transform.scale(pygame.image.load(assets_path+"dead2.png"),(522,480) )).convert()
whiteboard = (pygame.transform.scale(pygame.image.load(assets_path+"whiteboard.jpg"), (600, 70))).convert()
# character surface
character = (pygame.transform.scale(pygame.image.load(assets_path+"man.png"), (50,50))).convert()
character_happy = (pygame.transform.scale(pygame.image.load(assets_path+"happy_man.png"), (50,50))).convert()
character_muscle = (pygame.transform.scale(pygame.image.load(assets_path+"muscle.png"), (50,50))).convert()
character_squeeze1 = (pygame.transform.scale(pygame.image.load(assets_path+"standing_man.png"), (80,30))).convert()
character_squeeze2 = (pygame.transform.scale(pygame.image.load(assets_path+"standing_man.png"), (30,80))).convert()
character_flip = pygame.transform.flip(character,True,False).convert()
sound_off =  (pygame.transform.scale(pygame.image.load(assets_path+"sound-off.png"), (50, 50))).convert()
font = pygame.font.Font(assets_path+"Olympus Mount.ttf",50)

# CLASS
class Tool:
    def show_text(self, textX, textY, string, color):
        text = font.render(string, True, color)
        screen.blit(text, (textX, textY))

    def distanceMeasuring(self,cen1,cen2):
        x, y = cen1[0] - cen2[0], cen1[1] - cen2[1]
        return math.hypot(x, y)

    def sound_on_off(self,sound):
        if sound_play is True:
            sound.play()

class Character:
    def __init__(self, surface= character, size = (50,50), speed = 5):
        self.surface = surface
        self.size = size
        self.speed = speed

        self.x_change, self.y_change = 0, 0
        self.x, self.y = (275,200)

    def show_character(self):
        screen.blit(self.surface,(self.x,self.y))

    def move_character(self):
        self.x += self.x_change

class Floor:
    def __init__(self,img ,size = (150,30), speed = 2):
        self.img = img
        self.size = size
        self.speed , self.speed_init = speed , speed
        self.list = []
        self.surface = (pygame.transform.scale(pygame.image.load(assets_path + self.img), self.size)).convert()

    def set_floor_size(self,new_size):
        self.surface = (pygame.transform.scale(pygame.image.load(assets_path + self.img), new_size)).convert()

    def create_floor(self,floorType):
        if game.ifSpace() is True:
            new_floor_x = random.randint(75,525)
            new_floor = floorType.get_rect(midbottom = (new_floor_x,800))
            return  new_floor

    def move_floors(self,floors):
        for floor in floors:
            floor.centery -= self.speed
        return floors

    def draw_floors(self,floors):
        for floor in floors:
            screen.blit(self.surface,floor)

    def add_floor_to_list(self):
        self.list.append(self.create_floor(self.surface))

    def is_touch_floor(self,floor):
        for floor_x in range(int(-self.size[0]/2),int(self.size[0]/2)):
            if tool.distanceMeasuring((floor.centerx+floor_x,floor.centery-(self.size[1]/2)),(cha_1.x+cha_1.size[0]/2,cha_1.y+cha_1.size[1])) < 10 :
                return True
        return False

class Gift:
    def __init__(self, img, size = (40,40)):
        self.img = img
        self.size = size

        self.surface = (pygame.transform.scale(pygame.image.load(assets_path + self.img), size)).convert()
        self.x, self.y = random.randint(0,560) , random.randint(70,500)
        self.get_gift_time = 0

    def show_gift(self):
        screen.blit(self.surface, (self.x, self.y))

    def if_gifts_finish(self):
        if game.score - adrenaline.get_gift_time > 5:   cha_1.speed = 5
        if game.score - double_arrow.get_gift_time > 5:
            for floorType in floor_list:     floorType.set_floor_size(floorType.size)
        if game.score - hourglass.get_gift_time > 5:
            for floorType in floor_list:     floorType.speed = normal_floor.speed_init + game.num_of_touchFloor // 2000
        if (game.score - fat.get_gift_time > 5) and swallow.get_gift_time == 0:  game.gravity = 0.1
        if (game.score - swallow.get_gift_time > 5) and fat.get_gift_time == 0:  game.gravity = 0.1

class Adrenaline(Gift):
    def __init__(self):  super().__init__('adrenaline.png')
    def if_touch(self):
        if tool.distanceMeasuring((self.x + 20, self.y + 20),(cha_1.x + 25, cha_1.y + 50)) < 60:
            game.gift_choice = random.choice(gift_list)
            game.gift_choice.x, game.gift_choice.y = random.randint(0, 560), random.randint(70, 500)
            self.get_gift_time = game.score
            game.show_gift_delay = game.score
            cha_1.speed = 10
            cha_1.surface = character_muscle
            tool.sound_on_off(evil_laughSound)

class Double_Arrow(Gift):
    def __init__(self):  super().__init__('double-arrow.png')
    def if_touch(self):
        if tool.distanceMeasuring((self.x + 20, self.y + 20),(cha_1.x + 25, cha_1.y + 50)) < 60:
            game.gift_choice = random.choice(gift_list)
            game.gift_choice.x, game.gift_choice.y = random.randint(0, 560), random.randint(70, 500)
            self.get_gift_time = game.score
            game.show_gift_delay = game.score
            tool.sound_on_off(lengthenSound)
            for floorType in floor_list:    floorType.set_floor_size((200,30))


class Hourglass(Gift):
    def __init__(self):  super().__init__('hourglass.png')
    def if_touch(self):
        if tool.distanceMeasuring((self.x + 20, self.y + 20),(cha_1.x + 25, cha_1.y + 50)) < 60:
            game.gift_choice = random.choice(gift_list)
            game.gift_choice.x, game.gift_choice.y = random.randint(0, 560), random.randint(70, 500)
            self.get_gift_time = game.score
            game.show_gift_delay = game.score
            tool.sound_on_off(magicSound)
            for floorType in floor_list:      floorType.speed = 1


class Gold(Gift):
    def __init__(self):  super().__init__('gold.png')
    def if_touch(self):
        if tool.distanceMeasuring((self.x + 20, self.y + 20), (cha_1.x + 25, cha_1.y + 50)) < 60:
            game.gift_choice = random.choice(gift_list)
            game.gift_choice.x, game.gift_choice.y = random.randint(0, 560), random.randint(70, 500)
            self.get_gift_time = game.score
            game.show_gift_delay = game.score
            tool.sound_on_off(get_gold_sound)

class Fat(Gift):
    def __init__(self):  super().__init__('fat.png')
    def if_touch(self):
        if tool.distanceMeasuring((self.x + 20, self.y + 20), (cha_1.x + 25, cha_1.y + 50)) < 60:
            game.gift_choice = random.choice(gift_list)
            game.gift_choice.x, game.gift_choice.y = random.randint(0, 560), random.randint(70, 500)
            self.get_gift_time = game.score
            game.show_gift_delay = game.score
            swallow.get_gift_time = 0
            game.gravity = 0.3
            tool.sound_on_off(fartSound)

class Swallow(Gift):
    def __init__(self):  super().__init__('swallow.png')
    def if_touch(self):
        if tool.distanceMeasuring((self.x + 20, self.y + 20), (cha_1.x + 25, cha_1.y + 50)) < 60:
            game.gift_choice = random.choice(gift_list)
            game.gift_choice.x, game.gift_choice.y = random.randint(0, 560), random.randint(70, 500)
            self.get_gift_time = game.score
            game.show_gift_delay = game.score
            fat.get_gift_time = 0
            self.G = 0
            game.gravity = 0.03
            tool.sound_on_off(tweetSound)

# Child Down Stairs (Game)
class CDS:
    def __init__(self):
        cha_1.__init__()
        for floorType in floor_list:     floorType.__init__(floorType.img)
        for giftType in gift_list:       giftType.__init__()
        self.SPAWNFLOOR = pygame.USEREVENT
        pygame.time.set_timer(self.SPAWNFLOOR, 700)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Escape The Anti-Gravity World !!")
        pygame.display.set_icon(pygame.image.load(assets_path+"man.png"))
        self.gift_choice = random.choice(gift_list)
        # variable definition
        self.HP = 50
        self.score = 0
        self.level, self.level_init = 1, 1
        self.level_score, self.level_score_init = 0, 0
        self.gravity = 0.1
        self.G = 0
        self.run_count, self.act_count = 0, 0
        self.oneSecond = 120
        self.num_of_touchFloor = 0
        self.show_gift_delay = 0
        # running logic part
        self.run = True
        self.game_active = False
        self.game_start = True

    def show_start_screen(self):
        screen.blit(start_bkgd, (0, 0))
        if self.run_count > 40:
            tool.show_text(10, 60, "ESCAPE THE", red)
            tool.show_text(90, 140, "ANTI-GRAVITY WORLD !!", red)
        if self.run_count > 100:
            tool.show_text(10, 490, "LEFT & RIGHT TO CONTROL ", green)
            tool.show_text(10, 545, "PRESS SPACE TO START", green)
            tool.show_text(10, 610, "PRESS ESC TO QUIT", green)
        if self.run_count > 160:
            tool.show_text(95, 750, "AUG 2021 DESIGNED BY TIM", yellow)

    def show_bkgd_screen(self):
        screen.blit(whiteboard, (0, 0))
        screen.blit(bkgd, (0, 70))
        tool.show_text(10, 20, "HP : " + str(self.HP), red)
        tool.show_text(180, 20, "SCORE : " + str(self.score), black)
        tool.show_text(405, 20, "LEVEL : " + str(self.level), blue)

    def show_end_screen(self,end_draw_img):
        screen.fill(black)
        screen.blit(end_draw_img, (50, 120))
        tool.show_text(10,  10, "GAME TIME : "+ str(self.score), white)
        tool.show_text(10, 100, "YOUR SCORE : " + str(self.score+self.level_score), white)
        tool.show_text(50, 600, "PRESS SPACE TO CONTINUE", gray)
        tool.show_text(95, 750, "AUG 2021 DESIGNED BY TIM", yellow)

    def cal_score(self):
        if self.act_count % self.oneSecond == 0:    self.score += 1

    def boundary(self):
        if cha_1.x <= 0:
            cha_1.x = 0
        if cha_1.x >= 550:
            cha_1.x = 550

    def level_up_Judgement(self):
        if self.score - hourglass.get_gift_time > 5:
            for floorType in floor_list:
                floorType.speed = floorType.speed_init + self.num_of_touchFloor // 500
        if self.num_of_touchFloor % 500 == 0 and self.num_of_touchFloor != 0:
            self.level_score = self.level_score_init + (self.num_of_touchFloor//500)*10

            self.level = self.level_init + self.num_of_touchFloor // 500
            tool.sound_on_off(level_upSound)

    def start_delay(self):
        if self.run_count > self.oneSecond / 2:
            self.cal_score()
            self.G += self.gravity
            cha_1.y += self.G
            self.damage()

    def ifSpace(self):
        if self.game_start is True:
            self.__init__()
            self.game_start = False
            self.game_active = True
            tool.sound_on_off(startingSound)
        if self.isEnd() is True:
            self.__init__()
            self.show_start_screen()
        return True


    def event_get(self):
        global sound_play, bkgd
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            # key pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cha_1.x_change = -cha_1.speed
                    cha_1.surface = (pygame.transform.scale(pygame.image.load(assets_path+"man.png"), cha_1.size)).convert()
                if event.key == pygame.K_RIGHT:
                    cha_1.x_change = cha_1.speed
                    cha_1.surface = character_flip
                if event.key == pygame.K_ESCAPE:self.run = False
                if event.key == pygame.K_SPACE: self.ifSpace()
                if event.key == pygame.K_r:     self.__init__()
                if event.key == pygame.K_e:
                    muteSound.play()
                    if sound_play is True:
                        sound_play = False
                        bkgd.blit(sound_off,(10,670))
                    else:
                        sound_play = True
                        bkgd = (pygame.transform.scale(pygame.image.load(assets_path+"stairs2.jfif"), (600, 730))).convert()
            # key released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:    cha_1.x_change = 0
            # floor spawned
            if event.type == self.SPAWNFLOOR:
                if self.game_active == True:
                ## probability => 8:3:2:1
                    self.probability = random.randrange(0,14)
                    if self.probability == 13 or ((self.score - gold.get_gift_time) < 5 and gold.get_gift_time != 0):
                        golden_floor.list.append(golden_floor.create_floor(golden_floor.surface))
                        if len(golden_floor.list) > 20: golden_floor.list.pop(0)
                    else:
                        for i in range(0,8):
                            if self.probability == i:
                                normal_floor.list.append(normal_floor.create_floor(normal_floor.surface))
                                if len(normal_floor.list) > 20 : normal_floor.list.pop(0)
                        for i in range(8,11):
                            if self.probability == i:
                                sharp_floor.list.append(sharp_floor.create_floor(sharp_floor.surface))
                                if len(sharp_floor.list) > 8 :   sharp_floor.list.pop(0)
                        for i in range(11, 13):
                            if self.probability == i:
                                bouncy_floor.list.append(bouncy_floor.create_floor(bouncy_floor.surface))
                                if len(bouncy_floor.list) > 8 :  bouncy_floor.list.pop(0)

    def if_touch_floor(self):
        cha_1.y -= normal_floor.speed + 0.5
        for floorType in floor_list:
        # normal floor
            if floorType == normal_floor:
                for floor in normal_floor.list:
                    if normal_floor.is_touch_floor(floor) is True:
                        self.num_of_touchFloor += 1
                        self.G = 0
        # sharp floor
            if floorType == sharp_floor:
                for floor in sharp_floor.list:
                    if sharp_floor.is_touch_floor(floor) is True:
                        self.num_of_touchFloor += 1
                        self.G = 0
                        if self.num_of_touchFloor % 3 == 0:
                            cha_1.surface = character_squeeze2
                            self.HP -= 1
                            tool.sound_on_off(touchSound)
        # golden floor
            if floorType == golden_floor:
                for floor in golden_floor.list:
                    if golden_floor.is_touch_floor(floor) is True:
                        self.num_of_touchFloor += 1
                        self.G = 0
                        if self.num_of_touchFloor % 5 == 0:
                            cha_1.surface = character_happy
                            self.HP += 1
                            tool.sound_on_off(getHP_sound)
        # bouncy floor
            if floorType == bouncy_floor:
                for floor in bouncy_floor.list:
                    if bouncy_floor.is_touch_floor(floor) is True:
                        self.num_of_touchFloor += 1
                        self.G = -5
                        cha_1.surface = character_squeeze1
                        tool.sound_on_off(squeezeSound)

    def show_gift_on_screen(self):
        if self.score - self.show_gift_delay >= 5:
            self.gift_choice.show_gift()
            self.gift_choice.if_touch()
            self.gift_choice.if_gifts_finish()

    def damage(self):
        if cha_1.y < 1:
            cha_1.surface = character_squeeze2
            self.HP -= 1
            cha_1.y += 10
            tool.sound_on_off(touchSound)
        if cha_1.y > 800:   self.HP = 0

    def isEnd(self):
        if self.HP <= 0 :
            if cha_1.y >= 800 :
                self.show_end_screen(end_drawing)
                tool.sound_on_off(fallingSound)
            else:
                self.show_end_screen(end_drawing2)
                touchSound.stop()
                tool.sound_on_off(sadSound)
            self.game_active = False
            return True

    def main(self):
        while self.run:
            self.clock.tick(self.oneSecond)
            self.event_get()
            if self.game_start is True:
                self.show_start_screen()
                fallingSound.stop()
                sadSound.stop()
                for floorType in floor_list:    floorType.list = []
                if self.run_count == self.oneSecond/60: restartSound.play()
            if self.game_active is True:
                # renew bkgd and character constantly
                self.show_bkgd_screen()
                cha_1.show_character()
                # determine the variable situations
                cha_1.move_character()
                self.boundary()
                self.start_delay()
                self.if_touch_floor()
                self.show_gift_on_screen()
                self.level_up_Judgement()
                # move floors
                normal_floor.list = normal_floor.move_floors(normal_floor.list)
                sharp_floor.list = sharp_floor.move_floors(sharp_floor.list)
                golden_floor.list = golden_floor.move_floors(golden_floor.list)
                bouncy_floor.list = bouncy_floor.move_floors(bouncy_floor.list)
                # draw floors
                normal_floor.draw_floors(normal_floor.list)
                sharp_floor.draw_floors(sharp_floor.list)
                golden_floor.draw_floors(golden_floor.list)
                bouncy_floor.draw_floors(bouncy_floor.list)
                self.isEnd()
                self.act_count += 1
            self.run_count += 1
            pygame.display.update()

if __name__ == '__main__' :
# create a tool
    tool = Tool()
# create a default character
    cha_1 = Character()
# create 4 floor types
    normal_floor = Floor("floor1.png")
    sharp_floor  = Floor("floor2.png")
    golden_floor = Floor("floor3.png")
    bouncy_floor = Floor("floor4.png")
    floor_list = [normal_floor,sharp_floor,golden_floor,bouncy_floor]
# create 6 gift types
    adrenaline = Adrenaline()
    double_arrow = Double_Arrow()
    hourglass = Hourglass()
    gold = Gold()
    fat = Fat()
    swallow = Swallow()
    gift_list = [adrenaline,double_arrow,hourglass,gold,fat,swallow]
# create a game
    game = CDS()
# run the game
    game.main()
