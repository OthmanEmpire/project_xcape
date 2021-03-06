"""
Responsible for containing all the scenes in game.
"""

import pygame as pg

import xcape.common.settings as settings
import xcape.components.dialogue as dialogue
from xcape.common.loader import ZONE1_RESOURCES, ZONE2_RESOURCES
from xcape.common.scene import BaseScene
from xcape.components.render import RenderComponent, Dialogue
from xcape.entities.bosses import PigBoss
from xcape.entities.players import PlayerOne
from xcape.entities.scene import (
    Wall, SPlatform, DPlatform, MPlatform, Switch, Door, Spike, Decoration, Spear
)


class JailScene01(BaseScene):

    LEVEL_NUM = 1

    def __init__(self, screen):
        super().__init__(screen)

        self.players = self.addPlayers()
        self.walls = self.addWalls()
        self.sPlatforms = self.addSPlatforms()
        self.switches = self.addSwitches()
        self.doors = self.addDoors()

        self.elapsed = 0
        self.origin = pg.time.get_ticks()

        image = ZONE1_RESOURCES["levels"]["solo_jail_01"][0]
        self.render = RenderComponent(self)
        self.render.add("background", image)
        self.render.state = "background"

        self.dialogue = Dialogue(self.screen)
        self.dialogue.add(dialogue.JAIL_SOLO_1, 10, 410, "caption")

    def __str__(self):
        return "solo_jail_scene_01"

    def handleEvent(self, event):
        [p.handleEvent(event) for p in self.players]

        if event.type == self.SCENE_EVENT:
            [d.handleEvent(event) for d in self.doors]

    def update(self):
        self.elapsed = pg.time.get_ticks() - self.origin
        self.render.update()

        [w.update() for w in self.walls]
        [d.update() for d in self.doors]
        [s.update() for s in self.switches]
        [p.update() for p in self.sPlatforms]
        [p.update() for p in self.players]

        self.dialogue.update()
        if 5000 > self.elapsed >= 0:
            self.dialogue.index = 0
        else:
            self.dialogue.index = None

    def draw(self, camera=None):
        self.screen.fill(settings.COLOURS["black_red"])
        self.render.draw(camera)

        [w.draw(camera) for w in self.walls]
        [d.draw(camera) for d in self.doors]
        [s.draw(camera) for s in self.switches]
        [p.draw(camera) for p in self.sPlatforms]
        [p.draw(camera) for p in self.players]
        self.dialogue.draw()

    def addPlayers(self):
        spawn = (100, 0)
        player = [PlayerOne(self.screen)]
        player[0].rect.center = spawn
        return player

    def addWalls(self):
        assets = ZONE1_RESOURCES["walls"]
        boundaries = \
        [
            Wall(0, 10, 8, "v", assets["boundary_left"], self.screen),
            Wall(19, 478, 4, "h", assets["boundary_bot"], self.screen),
            Wall(320, 478, 5, "h", assets["boundary_bot"], self.screen),
            Wall(628, 138, 6, "v", assets["boundary_right"], self.screen),
            Wall(164, 138, 8, "h", assets["boundary_top"], self.screen),
            Wall(160, 138, 1, "v", assets["corner_top_left"], self.screen),
            Wall(160, 10, 2, "v", assets["boundary_right"], self.screen),
            Wall(628, 138, 1, "v", assets["upper_corner_right"], self.screen),
            Wall(0, 478, 1, "h", assets["inner_corner_left"], self.screen),
            Wall(628, 478, 1, "h", assets["inner_corner_right"], self.screen),
            Wall(240, 478, 1, "h", assets["inner_corner_right"], self.screen),
            Wall(240, 426, 1, "h", assets["corner_bot_right"], self.screen),
            Wall(308, 426, 1, "h", assets["corner_bot_left"], self.screen),
            Wall(320, 478, 1, "h", assets["inner_corner_left"], self.screen)
        ]

        obstacles = \
        [
            Wall(48, 418, 1, "h", assets["block_left"], self.screen),
            Wall(108, 418, 1, "h", assets["block_right"], self.screen),
            Wall(170, 450, 1, "h", assets["block_small"], self.screen),
        ]
        return boundaries + obstacles

    def addSPlatforms(self):
        platforms = \
        [
            SPlatform(475, 330, 1, self.screen),
            SPlatform(240, 255, 2, self.screen)
        ]
        return platforms

    def addSwitches(self):
        switches = \
        [
            Switch(295, 376, 1, self.screen),
            Switch(524, 280, 2, self.screen),
            Switch(295, 205, 3, self.screen)
        ]
        return switches

    def addDoors(self):
        door1 = Door(547, 370, 1, self.screen)
        door1.switchesWaiting = [1, 2, 3]
        return [door1]


class JailScene02(BaseScene):

    LEVEL_NUM = 2

    def __init__(self, screen):
        super().__init__(screen)

        self.players = self.addPlayers()
        self.walls = self.addWalls()
        self.dPlatforms = self.addDPlatforms()
        self.mPlatforms = self.addMPlatforms()
        self.switches = self.addSwitches()
        self.doors = self.addDoors()
        self.spikes = self.addSpikes()
        self.decorations = self.addDecorations()

        self.elapsed = 0
        self.origin = pg.time.get_ticks()

        image = ZONE1_RESOURCES["levels"]["solo_jail_02"][0]
        self.render = RenderComponent(self)
        self.render.add("idle", image)
        self.render.state = "idle"

        self.dialogue = Dialogue(self.screen)
        self.dialogue.add(dialogue.JAIL_SOLO_2, 10, 410, "caption")

    def __str__(self):
        return "solo_jail_scene_02"

    def handleEvent(self, event):
        [p.handleEvent(event) for p in self.players]

        if event.type == self.SCENE_EVENT:
            [d.handleEvent(event) for d in self.doors]

    def update(self):
        self.elapsed = pg.time.get_ticks() - self.origin
        self.render.update()

        [d.update() for d in self.decorations]
        [w.update() for w in self.walls]
        [s.update() for s in self.switches]
        [d.update() for d in self.doors]
        [s.update() for s in self.spikes]
        [p.update() for p in self.mPlatforms]
        [p.update() for p in self.dPlatforms]
        [p.update() for p in self.players]

        self.dialogue.update()
        if 5000 > self.elapsed >= 0:
            self.dialogue.index = 0
        else:
            self.dialogue.index = None

    def draw(self, camera=None):
        self.screen.fill(settings.COLOURS["black_red"])
        self.render.draw(camera)

        [d.draw(camera) for d in self.decorations]
        [w.draw(camera) for w in self.walls]
        [s.draw(camera) for s in self.switches]
        [d.draw(camera) for d in self.doors]
        [s.draw(camera) for s in self.spikes]
        [p.draw(camera) for p in self.mPlatforms]
        [p.draw(camera) for p in self.dPlatforms]
        [p.draw(camera) for p in self.players]
        self.dialogue.draw()

    def addPlayers(self):
        spawn = (70, 510)
        player = [PlayerOne(self.screen)]
        player[0].rect.center = spawn
        return player

    def addWalls(self):
        wall = ZONE1_RESOURCES["walls"]
        platWall = [wall["plat_top"][0],
                    wall["plat_mid"][0],
                    wall["plat_bot"][0]]

        boundaries = \
        [
            Wall(0, 50, 8, "v", wall["boundary_left"], self.screen),
            Wall(0, 548, 15, "h", wall["boundary_bot"], self.screen),
            Wall(0, 548, 1, "h", wall["inner_corner_left"], self.screen),
            Wall(952, 50, 8, "v", wall["boundary_right"], self.screen),
            Wall(952, 548, 1, "h", wall["inner_corner_right"], self.screen)
        ]

        obstacles = \
        [
            Wall(210, 300, 1, "h", wall["block_left"], self.screen),
            Wall(265, 300, 1, "h", wall["block_right"], self.screen),

            Wall(435, 490, 1, "h", wall["block_left"], self.screen),
            Wall(490, 490, 1, "h", wall["block_right"], self.screen),

            Wall(655, 300, 1, "h", wall["block_left"], self.screen),
            Wall(710, 300, 1, "h", wall["block_right"], self.screen),

            Wall(770, 105, 2, "v", platWall, self.screen),
        ]

        return boundaries + obstacles

    def addDPlatforms(self):
        platforms = \
        [
            DPlatform(170, 450, 1, self.screen),
            DPlatform(60, 330, 0, self.screen),
        ]
        return platforms

    def addMPlatforms(self):
        vImage = ZONE1_RESOURCES["platforms"]["moving_vertical"]
        hImage = ZONE1_RESOURCES["platforms"]["moving_horizontal"]

        platforms = \
        [
            # MPlatform((150, 260), (350, 260), 10, 0, self.screen, hImage),
            MPlatform((340, 450), (600, 450), 8, 0, self.screen, hImage),
            MPlatform((340, 300), (600, 300), 8, 0, self.screen, hImage),
            MPlatform((660, 350), (660, 435), 0, 0, self.screen, vImage),
            MPlatform((660, 435), (660, 530), 0, 0, self.screen, vImage),
        ]
        return platforms

    def addSwitches(self):
        switches = \
        [
            Switch(250, 200, 1, self.screen),
            Switch(480, 200, 2, self.screen),
            Switch(480, 430, 3, self.screen),
            Switch(700, 200, 4, self.screen),
        ]
        return switches

    def addDoors(self):
        door1 = Door(865, 440, 1, self.screen)
        door1.switchesWaiting = [1, 2, 3, 4]
        return [door1]

    def addSpikes(self):
        assets = ZONE1_RESOURCES["traps"]
        spikes = \
        [
            Spike(325, 525, 5, "h", assets["spike_up"][0], self.screen),
            Spike(550, 525, 5, "h", assets["spike_up"][0], self.screen),
        ]
        return spikes

    def addDecorations(self):
        deco = ZONE1_RESOURCES["decorations"]
        decorations = \
        [
            Decoration(778, 81, deco["skull"][0], self.screen)
        ]
        return decorations


class JailScene03(BaseScene):

    LEVEL_NUM = 3

    def __init__(self, screen):
        super().__init__(screen)

        self.players = self.addPlayers()
        self.walls = self.addWalls()
        self.mPlatforms = self.addMPlatforms()
        self.switches = self.addSwitches()
        self.doors = self.addDoors()
        self.spikes = self.addSpikes()

        self.elapsed = 0
        self.origin = pg.time.get_ticks()

        image = ZONE1_RESOURCES["levels"]["solo_jail_03"][0]
        self.render = RenderComponent(self)
        self.render.add("idle", image)
        self.render.state = "idle"

        self.dialogue = Dialogue(self.screen)
        self.dialogue.add(dialogue.JAIL_SOLO_3, 10, 410, "caption")

    def __str__(self):
        return "solo_jail_scene_03"

    def handleEvent(self, event):
        [p.handleEvent(event) for p in self.players]

        if event.type == self.SCENE_EVENT:
            [d.handleEvent(event) for d in self.doors]

    def update(self):
        self.elapsed = pg.time.get_ticks() - self.origin
        self.render.update()

        [w.update() for w in self.walls]
        [s.update() for s in self.switches]
        [d.update() for d in self.doors]
        [s.update() for s in self.spikes]
        [p.update() for p in self.mPlatforms]
        [p.update() for p in self.players]

        self.dialogue.update()
        if 5000 > self.elapsed >= 0:
            self.dialogue.index = 0
        else:
            self.dialogue.index = None

    def draw(self, camera=None):
        self.screen.fill(settings.COLOURS["black_red"])
        self.render.draw(camera)

        [w.draw(camera) for w in self.walls]
        [s.draw(camera) for s in self.switches]
        [d.draw(camera) for d in self.doors]
        [s.draw(camera) for s in self.spikes]
        [p.draw(camera) for p in self.mPlatforms]
        [p.draw(camera) for p in self.players]
        self.dialogue.draw()

    def addPlayers(self):
        spawn = (315, 128)
        player = [PlayerOne(self.screen)]
        player[0].rect.center = spawn
        return player

    def addWalls(self):
        wall = ZONE1_RESOURCES["walls"]
        pillar = ZONE1_RESOURCES["pillars"]

        pillarWall = [pillar["steel_top"][0],
                      pillar["steel_mid"][0],
                      pillar["steel_bot"][0]]
        platWall = [wall["plat_top"][0],
                    wall["plat_mid"][0],
                    wall["plat_bot"][0]]
        blockWall = [wall["block_left"][0],
                     wall["block_mid"][0],
                     wall["block_right"][0]]

        boundaries = \
            [
                Wall(739, 0, 5, "h", wall["boundary_top"], self.screen),
                Wall(99, 0, 5, "h", wall["boundary_top"], self.screen),
                Wall(0, 64, 7, "v", wall["boundary_left"], self.screen),
                Wall(1102, 60, 7, "v", wall["boundary_right"], self.screen),

                Wall(587, 367, 2, "v", wall["boundary_left"], self.screen),
                Wall(507, 367, 2, "v", wall["boundary_right"], self.screen),
            ]

        obstacles = \
            [
                Wall(363, 48, 6, "v", pillarWall, self.screen),
                Wall(738, 48, 6, "v", pillarWall, self.screen),

                Wall(167, 182, 2, "h", blockWall, self.screen),
                Wall(735, 182, 2, "h", blockWall, self.screen),

                Wall(543, 198, 1, "h", wall["block_small"], self.screen),
                Wall(575, 363, 1, "v", wall["corner_bot_left"], self.screen),
                Wall(507, 363, 1, "h", wall["corner_bot_right"], self.screen),

                Wall(375, 423, 1, "v", platWall, self.screen),
                Wall(703, 423, 1, "v", platWall, self.screen),
            ]

        return boundaries + obstacles

    def addMPlatforms(self):
        vImage = ZONE1_RESOURCES["platforms"]["moving_vertical"][0]
        hImage = ZONE1_RESOURCES["platforms"]["moving_horizontal"][0]

        platforms = \
            [
                MPlatform((83, 250), (240, 400), 0, 3, self.screen, vImage),
                MPlatform((1035, 250), (250, 400), 0, 3, self.screen, vImage),
                MPlatform((215, 325), (310, 325), 3, 0, self.screen, hImage),
                MPlatform((849, 372), (950, 372), 3, 0, self.screen, hImage),
                MPlatform((420, 279), (700, 685), 3, 0, self.screen, hImage),
            ]
        return platforms

    def addSwitches(self):
        switches = \
            [
                Switch(565, 146, 1, self.screen),
                Switch(565, 305, 2, self.screen),
            ]
        return switches

    def addDoors(self):
        door1 = Door(795, 74, 1, self.screen)
        door1.switchesWaiting = [1, 2]
        return [door1]

    def addSpikes(self):
        assets = ZONE1_RESOURCES["traps"]
        spikes = \
            [
                Spike(415, 190, 2, "v", assets["spike_left"][0], self.screen),
                Spike(711, 190, 2, "v", assets["spike_right"][0], self.screen),

                Spike(45, 590, 16, "h", assets["spike_up"][0], self.screen),
                Spike(765, 590, 16, "h", assets["spike_up"][0], self.screen),
            ]
        return spikes


class JailScene04(BaseScene):

    LEVEL_NUM = 4

    def __init__(self, screen):
        super().__init__(screen)

        self.players = self.addPlayers()
        self.bosses = self.addBosses()
        self.bosses[0].target(self.players)

        self.walls = self.addWalls()
        self.mPlatforms = self.addMPlatforms()
        self.switches = self.addSwitches()
        self.doors = self.addDoors()
        self.spikes = self.addSpikes()
        self.dPlatforms = self.addDPlatforms()
        self.decorations = self.addDecorations()

        self.elapsed = 0
        self.origin = pg.time.get_ticks()

        image = ZONE1_RESOURCES["levels"]["solo_jail_04"]
        self.render = RenderComponent(self)
        self.render.add("background", image)
        self.render.state = "background"

        self.dialogue = Dialogue(self.screen)
        self.dialogue.add(dialogue.JAIL_SOLO_1, 10, 410, "caption")

        self.messageCutScene("transition", "pig_cutscene")
        self.messageMenu("transition", "blank_menu")

    def __str__(self):
        return "solo_jail_scene_04"

    def handleEvent(self, event):
        [p.handleEvent(event) for p in self.players]

        if event.type == self.SCENE_EVENT:
            [d.handleEvent(event) for d in self.doors]

    def update(self):
        self.elapsed = pg.time.get_ticks() - self.origin
        self.render.update()

        [d.update() for d in self.decorations]
        [w.update() for w in self.walls]
        [s.update() for s in self.switches]
        [d.update() for d in self.doors]
        [s.update() for s in self.spikes]
        [p.update() for p in self.dPlatforms]
        [p.update() for p in self.mPlatforms]
        [p.update() for p in self.players]
        [b.update() for b in self.bosses]

        self.dialogue.update()
        if 5000 > self.elapsed >= 0:
            self.dialogue.index = 0
        else:
            self.dialogue.index = None

    def draw(self, camera=None):
        self.screen.fill(settings.COLOURS["black_red"])
        self.render.draw(camera)

        [d.draw(camera) for d in self.decorations]
        [w.draw(camera) for w in self.walls]
        [s.draw(camera) for s in self.switches]
        [d.draw(camera) for d in self.doors]
        [s.draw(camera) for s in self.spikes]
        [p.draw(camera) for p in self.dPlatforms]
        [p.draw(camera) for p in self.mPlatforms]
        [p.draw(camera) for p in self.players]
        [b.draw(camera) for b in self.bosses]
        self.dialogue.draw()

    def addPlayers(self):
        spawn = (250, 200)
        player = [PlayerOne(self.screen)]
        player[0].rect.center = spawn
        return player

    def addBosses(self):
        b1Spawn = (670, 260)
        b1 = PigBoss(self.screen)
        b1.rect.center = b1Spawn
        bosses = [b1]
        return bosses

    def addWalls(self):
        wall = ZONE1_RESOURCES["walls"]
        pillar = ZONE1_RESOURCES["pillars"]
        pillarWall = [pillar["steel_top"][0],
                      pillar["steel_mid"][0],
                      pillar["steel_bot"][0]]
        blockWall = [wall["block_left"][0],
                     wall["block_mid"][0],
                     wall["block_right"][0]]

        boundaries = \
            [
                Wall(12, 288, 3, "v", wall["boundary_left"], self.screen),
                Wall(4, 52, 1, "v", wall["boundary_left"], self.screen),
                Wall(4, 0, 1, "h", wall["upper_corner_left"], self.screen),
                Wall(0, 116, 1, "h", wall["corner_top_right"], self.screen),
                Wall(52, 0, 6, "h", wall["boundary_top"], self.screen),
                Wall(432, 0, 1, "h", wall["corner_top_right"], self.screen),
                Wall(0, 236, 1, "v", wall["corner_bot_left"], self.screen),
            ]

        obstacles = \
            [
                Wall(139, 288, 2, "h", blockWall, self.screen),
                Wall(3411, 304, 2, "h", blockWall, self.screen),

                Wall(3, 167, 2, "v", pillarWall, self.screen),
                Wall(3359, 217, 3, "v", pillarWall, self.screen),

                Wall(494, 256, 1, "h", wall["block_small"], self.screen),
                Wall(632, 169, 1, "h", wall["block_small"], self.screen),
                Wall(805, 126, 1, "h", wall["block_small"], self.screen),
                Wall(805, 304, 1, "h", wall["block_small"], self.screen),
                Wall(1021, 230, 1, "h", wall["block_small"], self.screen),
                Wall(974, 384, 1, "h", wall["block_small"], self.screen),
                Wall(3347, 302, 1, "h", wall["block_small"], self.screen),

                Wall(1692, 116, 2, "h", wall["boundary_bot"], self.screen),
                Wall(1632, 168, 2, "v", wall["boundary_right"], self.screen),
                Wall(1780, 168, 2, "v", wall["boundary_left"], self.screen),
                Wall(1692, 296, 2, "h", wall["boundary_top"], self.screen),

                Wall(1632, 116, 1, "h", wall["corner_bot_right"], self.screen),
                Wall(1632, 296, 1, "h", wall["corner_top_left"], self.screen),
                Wall(1768, 116, 1, "h", wall["corner_bot_left"], self.screen),
                Wall(1776, 296, 1, "h", wall["corner_top_right"], self.screen),

                Wall(1936, 224, 1, "h", wall["block_small"], self.screen),
                Wall(2144, 373, 1, "h", wall["block_small"], self.screen),
            ]

        return boundaries + obstacles

    def addMPlatforms(self):
        vImage = ZONE1_RESOURCES["platforms"]["moving_vertical"]
        hImage = ZONE1_RESOURCES["platforms"]["moving_horizontal"]

        platforms = \
            [
                MPlatform((1187, 304), (1407, 325), 4, 0, self.screen, hImage),

                MPlatform((2309, 337), (2437, 325), 4, 0, self.screen, hImage),
                MPlatform((2558, 304), (2686, 325), 4, 0, self.screen, hImage),
                MPlatform((2696, 346), (2950, 325), 4, 0, self.screen, hImage),

                MPlatform((3049, 232), (3049, 406), 0, 4, self.screen, vImage),
                MPlatform((3144, 195), (3049, 344), 0, 4, self.screen, vImage),
                MPlatform((3289, 195), (3049, 330), 0, 4, self.screen, vImage),

            ]
        return platforms

    def addDPlatforms(self):
        platforms = \
        [
            DPlatform(1517, 126, 1, self.screen),
            DPlatform(1517, 216, 1, self.screen),
            DPlatform(1517, 305, 1, self.screen),
        ]
        return platforms

    def addSwitches(self):
        switches = \
            [
                Switch(822, 92, 1, self.screen),
                Switch(822, 263, 2, self.screen),
                Switch(992, 350, 3, self.screen),
                Switch(1296, 250, 4, self.screen),
                Switch(2610, 240, 5, self.screen),
                Switch(3138, 143, 6, self.screen),
            ]
        return switches

    def addDoors(self):
        door1 = Door(3579, 196, 1, self.screen)
        door1.switchesWaiting = [1, 2, 3, 4, 5, 6]
        return [door1]

    def addSpikes(self):
        spike = ZONE1_RESOURCES["traps"]
        spikes = \
            [
                Spike(3362, 195, 2, "h", spike["spike_up"][0], self.screen),
            ]
        return spikes

    def addDecorations(self):
        deco = ZONE1_RESOURCES["decorations"]
        decorations = \
        [
            Decoration(416, 112, deco["torch"], self.screen),
            # Decoration(2176, 140, deco["torch"], self.screen),
            Decoration(1308, 143, deco["torch"], self.screen),
            Decoration(2182, 143, deco["torch"], self.screen),
            Decoration(3486, 143, deco["torch"], self.screen),
        ]
        return decorations


class ForestScene01(BaseScene):

    LEVEL_NUM = 5

    def __init__(self, screen):
        super().__init__(screen)

        self.players = self.addPlayers()

        self.walls = self.addWalls()
        self.mPlatforms = self.addMPlatforms()
        self.switches = self.addSwitches()
        self.doors = self.addDoors()
        self.spikes = self.addSpikes()
        self.spears = self.addSpears()
        self.dPlatforms = self.addDPlatforms()
        self.decorations = self.addDecorations()

        self.elapsed = 0
        self.origin = pg.time.get_ticks()

        image = ZONE2_RESOURCES["levels"]["solo_forest_01"]
        self.render = RenderComponent(self)
        self.render.add("background", image)
        self.render.state = "background"

        self.dialogue = Dialogue(self.screen)
        self.dialogue.add(dialogue.JAIL_SOLO_1, 10, 410, "caption")

    def __str__(self):
        return "solo_forest_scene_01"

    def handleEvent(self, event):
        [p.handleEvent(event) for p in self.players]

        if event.type == self.SCENE_EVENT:
            [d.handleEvent(event) for d in self.doors]

    def update(self):
        self.elapsed = pg.time.get_ticks() - self.origin
        self.render.update()

        [d.update() for d in self.decorations]
        [w.update() for w in self.walls]
        [s.update() for s in self.switches]
        [d.update() for d in self.doors]
        [s.update() for s in self.spikes]
        [s.update() for s in self.spears]
        [p.update() for p in self.dPlatforms]
        [p.update() for p in self.mPlatforms]
        [p.update() for p in self.players]
        [b.update() for b in self.bosses]

        self.dialogue.update()
        if 5000 > self.elapsed >= 0:
            self.dialogue.index = 0
        else:
            self.dialogue.index = None

    def draw(self, camera=None):
        self.screen.fill(settings.COLOURS["dark_blue"])
        self.render.draw(camera)

        [d.draw(camera) for d in self.decorations]
        [w.draw(camera) for w in self.walls]
        [s.draw(camera) for s in self.switches]
        [d.draw(camera) for d in self.doors]
        [s.draw(camera) for s in self.spikes]
        [s.draw(camera) for s in self.spears]
        [p.draw(camera) for p in self.dPlatforms]
        [p.draw(camera) for p in self.mPlatforms]
        [p.draw(camera) for p in self.players]
        [b.draw(camera) for b in self.bosses]
        self.dialogue.draw()

    def addPlayers(self):
        spawn = (400, 900)
        player = [PlayerOne(self.screen)]
        player[0].rect.center = spawn
        return player

    def addWalls(self):
        wall = ZONE2_RESOURCES["walls"]
        pillar = ZONE2_RESOURCES["pillars"]
        platWall = [wall["plat_top"][0],
                    wall["plat_mid"][0],
                    wall["plat_bot"][0]]
        pillarWall = [pillar["steel_top"][0],
                      pillar["steel_mid"][0],
                      pillar["steel_bot"][0]]

        boundaries = \
        [
            Wall(0, 962, 4, "h", wall["ground"], self.screen),
            Wall(0, 1074, 4, "h", wall["ground_clean"], self.screen),

            Wall(675, 962, 4, "h", wall["ground"], self.screen),
            Wall(1550, 962, 5, "h", wall["ground"], self.screen),

            Wall(675, 1074, 12, "h", wall["ground_clean"], self.screen),
            # Wall(0, 500, 6, "v", pillarWall, self.screen),
        ]
        boundaries[0].render.shrinkBy = (0, -50)

        obstacles = \
        [
            Wall(0, 898, 1, "h", wall["single_plat"], self.screen),
            Wall(160, 898, 1, "h", wall["single_plat"], self.screen),
            Wall(288, 770, 1, "h", wall["single_plat"], self.screen),

            Wall(-32, 770, 4, "h", wall["block_mid"], self.screen),
            Wall(224, 770, 1, "h", wall["block_right"], self.screen),

            Wall(288, 898, 1, "h", wall["corner_top_right"], self.screen),
            Wall(224, 898, 1, "h", wall["corner_top_left"], self.screen),
            Wall(224, 834, 1, "h", wall["corner_bot_right"], self.screen),
            Wall(288, 834, 1, "h", wall["corner_bot_left"], self.screen),

            Wall(192, 738, 1, "h", wall["block_small"], self.screen),
            Wall(96, 930, 1, "h", wall["block_small"], self.screen),

            Wall(875, 850, 1, "h", wall["block_small"], self.screen),
            Wall(1050, 750, 1, "h", wall["block_small"], self.screen),
            Wall(1325, 1010, 1, "h", wall["block_small"], self.screen),

            Wall(1815, 706, 2, "v", platWall, self.screen),
            #Wall(210, 300, 1, "h", wall["block_left"], self.screen),
            #Wall(265, 300, 1, "h", wall["block_right"], self.screen),

            #Wall(435, 490, 1, "h", wall["block_left"], self.screen),
            #Wall(490, 490, 1, "h", wall["block_right"], self.screen),

            #Wall(655, 300, 1, "h", wall["block_left"], self.screen),
            #Wall(710, 300, 1, "h", wall["block_right"], self.screen),

            #Wall(770, 105, 2, "v", platWall, self.screen),
        ]

        return boundaries + obstacles

    def addDPlatforms(self):
        platforms = \
        [
            DPlatform(1550, 800, 1, self.screen, zoneArtwork=2),
            #DPlatform(60, 330, 0, self.screen, zoneArtwork=2),
        ]
        return platforms

    def addMPlatforms(self):
        vImage = ZONE2_RESOURCES["platforms"]["moving_vertical"]
        hImage = ZONE2_RESOURCES["platforms"]["moving_horizontal"]

        platforms = \
        [
            MPlatform((1000, 710), (1300, 260), 9, 0, self.screen, hImage),
            #MPlatform((1000, 450), (600, 450), 8, 0, self.screen, hImage),
            #MPlatform((340, 300), (600, 300), 8, 0, self.screen, hImage),
            #MPlatform((660, 350), (660, 435), 0, 0, self.screen, vImage),
            #MPlatform((660, 435), (660, 530), 0, 0, self.screen, vImage),
        ]
        return platforms

    def addSwitches(self):
        switches = \
        [
            Switch(1070, 650, 1, self.screen, zoneArtwork=2),
            Switch(1070, 900, 2, self.screen, zoneArtwork=2),
            Switch(1600, 750, 3, self.screen, zoneArtwork=2),
            #Switch(1600, 900, 3, self.screen, zoneArtwork=2),
            #Switch(700, 200, 4, self.screen, zoneArtwork=2),
        ]
        return switches

    def addDoors(self):
        door1 = Door(1710, 854, 1, self.screen, zoneArtwork=2)
        door1.switchesWaiting = [1, 2, 3]
        return [door1]

    def addSpikes(self):
        assets = ZONE2_RESOURCES["traps"]
        spikes = \
        [
            Spike(1175, 1050, 18, "h", assets["spike_up"][0], self.screen),
            Spear(1340, 963, self.screen),
            #Spike(550, 525, 5, "h", assets["spike_up"][0], self.screen),
        ]
        x_axis = 798
        for x in range(4):
            spikes.append(Spear(x_axis, 915, self.screen))
            x_axis += 64
        return spikes

    def addDecorations(self):
        deco = ZONE2_RESOURCES["decorations"]
        x_axis = 0
        x_axis2 = 675
        x_axis3 = 1550

        decorations = \
        [
            Decoration(732, 456, deco["moon"][0], self.screen)
        ]
        for x in range(4):
            decorations.append(Decoration(x_axis, 950, deco["grass"][0], self.screen))
            x_axis += 125
        for x in range(4):
            decorations.append(Decoration(x_axis2, 950, deco["grass"][0], self.screen))
            x_axis2 += 125
        for x in range(5):
            decorations.append(Decoration(x_axis3, 950, deco["grass"][0], self.screen))
            x_axis3 += 125
        return decorations

    def addSpears(self):
        spears = \
        [
            #Spear(1370, 946, self.screen),
            #Spear(862, 915, self.screen),
            #Spear(926, 915, self.screen),
            #Spear(0, 915, self.screen),
        ]

        return spears
        
class ForestScene02(BaseScene):

    LEVEL_NUM = 6

    def __init__(self, screen):
        super().__init__(screen)

        self.players = self.addPlayers()

        self.walls = self.addWalls()
        self.mPlatforms = self.addMPlatforms()
        self.switches = self.addSwitches()
        self.doors = self.addDoors()
        self.spikes = self.addSpikes()
        self.spears = self.addSpears()
        self.dPlatforms = self.addDPlatforms()
        self.decorations = self.addDecorations()

        self.elapsed = 0
        self.origin = pg.time.get_ticks()

        image = ZONE2_RESOURCES["levels"]["solo_forest_01"]
        self.render = RenderComponent(self)
        self.render.add("background", image)
        self.render.state = "background"

        self.dialogue = Dialogue(self.screen)
        self.dialogue.add(dialogue.FOREST_SOLO_2, 10, 410, "caption")

    def __str__(self):
        return "solo_forest_scene_02"

    def handleEvent(self, event):
        [p.handleEvent(event) for p in self.players]

        if event.type == self.SCENE_EVENT:
            [d.handleEvent(event) for d in self.doors]

    def update(self):
        self.elapsed = pg.time.get_ticks() - self.origin
        self.render.update()

        [d.update() for d in self.decorations]
        [w.update() for w in self.walls]
        [s.update() for s in self.switches]
        [d.update() for d in self.doors]
        [s.update() for s in self.spikes]
        [s.update() for s in self.spears]
        [p.update() for p in self.dPlatforms]
        [p.update() for p in self.mPlatforms]
        [p.update() for p in self.players]
        [b.update() for b in self.bosses]

        self.dialogue.update()
        if 5000 > self.elapsed >= 0:
            self.dialogue.index = 0
        else:
            self.dialogue.index = None

    def draw(self, camera=None):
        self.screen.fill(settings.COLOURS["dark_blue"])
        self.render.draw(camera)

        [d.draw(camera) for d in self.decorations]
        [w.draw(camera) for w in self.walls]
        [s.draw(camera) for s in self.switches]
        [d.draw(camera) for d in self.doors]
        [s.draw(camera) for s in self.spikes]
        [s.draw(camera) for s in self.spears]
        [p.draw(camera) for p in self.dPlatforms]
        [p.draw(camera) for p in self.mPlatforms]
        [p.draw(camera) for p in self.players]
        [b.draw(camera) for b in self.bosses]
        self.dialogue.draw()

    def addPlayers(self):
        spawn = (400, 900)
        player = [PlayerOne(self.screen)]
        player[0].rect.center = spawn
        return player

    def addWalls(self):
        wall = ZONE2_RESOURCES["walls"]
        pillar = ZONE2_RESOURCES["pillars"]
        platWall = [wall["plat_top"][0],
                    wall["plat_mid"][0],
                    wall["plat_bot"][0]]
        pillarWall = [pillar["steel_top"][0],
                      pillar["steel_mid"][0],
                      pillar["steel_bot"][0]]

        boundaries = \
        [
            Wall(0, 962, 9, "h", wall["ground"], self.screen),
            Wall(0, 1074, 9, "h", wall["ground_clean"], self.screen),
                 
            Wall(1375, 962, 6,  "h", wall["ground"], self.screen),
            Wall(1375, 1074, 6, "h", wall["ground_clean"], self.screen),
        ]
        boundaries[0].render.shrinkBy = (0, -50)

        obstacles = \
        [
            Wall(288, 706, 2,"v", platWall, self.screen),
            
            Wall(1814, 518, 1, "h", wall["corner_top_right"], self.screen),
            Wall(1750, 518, 1, "h", wall["corner_top_left"], self.screen),
            Wall(1750, 454, 1, "h", wall["corner_bot_right"], self.screen),
            Wall(1814, 454, 1, "h", wall["corner_bot_left"], self.screen),
            
        ]

        return boundaries + obstacles

    def addDPlatforms(self):
        platforms = \
        [
            
        ]
        return platforms

    def addMPlatforms(self):
        vImage = ZONE2_RESOURCES["platforms"]["moving_vertical"]
        hImage = ZONE2_RESOURCES["platforms"]["moving_horizontal"]
        x_axis = 595
        x_axis2 = 800
        y_axis = 885
        
        platforms = \
        [
            #MPlatform((595, 885), (800, 450), 8, 0, self.screen, hImage),
            #MPlatform((753, 808), (958, 300), 8, 0, self.screen, hImage),
            #MPlatform((911, 731), (1116, 435), 8, 0, self.screen, hImage),
            #MPlatform((1064, 731), (1116, 435), 8, 0, self.screen, hImage),
            #MPlatform((660, 435), (660, 530), 0, 0, self.screen, vImage),
        ]
        for x in range(6):
            platforms.append(MPlatform((x_axis, y_axis), (x_axis2, 450), 8, 0, self.screen, hImage))
            x_axis += 158
            x_axis2 += 158
            y_axis -= 77
        
        return platforms

    def addSwitches(self):
        switches = \
        [
            Switch(962, 571, 1, self.screen, zoneArtwork=2),
            #Switch(1070, 900, 2, self.screen, zoneArtwork=2),
            #Switch(1600, 750, 3, self.screen, zoneArtwork=2),
            #Switch(1600, 900, 3, self.screen, zoneArtwork=2),
            #Switch(700, 200, 4, self.screen, zoneArtwork=2),
        ]
        return switches

    def addDoors(self):
        door1 = Door(1798, 346, 1, self.screen, zoneArtwork=2)
        door1.switchesWaiting = [1]
        return [door1]

    def addSpikes(self):
        assets = ZONE2_RESOURCES["traps"]
        spikes = \
        [
            Spike(1375, 938, 25, "h", assets["spike_up"][0], self.screen),
            #Spear(1340, 963, self.screen),
            #Spike(550, 525, 5, "h", assets["spike_up"][0], self.screen),
        ]
        x_axis = 798
        for x in range(4):
            spikes.append(Spear(x_axis, 915, self.screen))
            x_axis += 64
        return spikes

    def addDecorations(self):
        deco = ZONE2_RESOURCES["decorations"]
        door = ZONE2_RESOURCES["doors"]
        x_axis = 0
        x_axis2 = 1375
        #x_axis3 = 1550

        decorations = \
        [
            Decoration(732, 456, deco["moon"][0], self.screen),
            Decoration(352, 854, door["open"][0], self.screen),
        ]
        for x in range(9):
            decorations.append(Decoration(x_axis, 950, deco["grass"][0], self.screen))
            x_axis += 125
        for x in range(6):
            decorations.append(Decoration(x_axis2, 950, deco["grass"][0], self.screen))
            x_axis2 += 125
            
        return decorations

    def addSpears(self):
        spears = \
        [
            #Spear(1370, 946, self.screen),
            #Spear(862, 915, self.screen),
            #Spear(926, 915, self.screen),
            #Spear(0, 915, self.screen),
        ]

        return spears

