"""
Responsible for the audio of a game object.
"""

import pygame as pg

from xcape.common.object import GameObject


class AudioComponent(GameObject):
    """
    Attaches to a game object to allow playing of audio.
    """

    def __init__(self, gameObject, enableAutoPlay=True, enableRepeat=False):
        """
        :param gameObject: GameObject instance, the instance to attach to.
        :param enableAutoPlay: Boolean, whether to play audio immediately.
        :param enableRepeat: Boolean, whether to keep repeating audio.
        """
        self.gameObject = gameObject
        self.enableRepeat = enableRepeat
        self.enableAutoPlay = enableAutoPlay

        self.stateToSound = {}
        self.stateToLink = {}
        self.timesPlayed = 0
        self.sound = None

        self.isPlaying = False
        self.shouldPlay = False

        self.origin = 0
        self.elapsed = 0
        self.delay = 0

        if self.enableAutoPlay:
            self.shouldPlay = True

        self._state = None

    def update(self):
        self.elapsed = pg.time.get_ticks() - self.origin

        if not self.isPlaying and self.shouldPlay:
            self._playSound()

        if self.isPlaying:
            if self.elapsed > 1000*self.sound.get_length() + self.delay:
                try:
                    self.state, self.delay = self.stateToLink[self.state]
                    self.timesPlayed = 0
                except KeyError:
                    if not self.enableRepeat:
                        self.shouldPlay = False

    def add(self, state, sound):
        """
        Links a sound effect to a state.

        :param state: String, the name of the state.
        :param sound: pygame.mixer.Sound, the sound effect object.
        """
        self.stateToSound[state] = sound

    def link(self, state1, state2, delay=0):
        """
        Links the given two states so that two sound effects are played
        successively, separated in time by the given delay.

        :param state1: String, the name of the state to link from.
        :param state2: String, the name of the state to link to.
        :param delay: Number, the delay between transitioning states.
        """
        self.stateToLink[state1] = (state2, delay)

    def _playSound(self):
        """
        Plays the current sound once only.
        """
        self.sound.play()
        self.timesPlayed += 1
        self.isPlaying = True
        self.shouldPlay = False
        self._resetTimer()

    def _resetTimer(self):
        """
        Resets the timer used for controlling transitioning of sound effects.
        """
        self.origin = pg.time.get_ticks()
        self.elapsed = 0

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        try:
            self.shouldPlay = True
            self.isPlaying = False
            self._resetTimer()

            self._state = value
            self.sound = self.stateToSound[value]
            _, self.delay = self.stateToLink[value]
        except KeyError:
            self.delay = 0
