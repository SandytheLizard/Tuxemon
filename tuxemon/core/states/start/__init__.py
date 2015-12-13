#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Tuxemon
# Copyright (C) 2014, William Edwards <shadowapex@gmail.com>,
#                     Benjamin Bean <superman2k5@gmail.com>
#
# This file is part of Tuxemon.
#
# Tuxemon is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Tuxemon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Tuxemon.  If not, see <http://www.gnu.org/licenses/>.
#
# Contributor(s):
#
# William Edwards <shadowapex@gmail.com>
#
#
# core.states.start Handles the splash screen and start menu.
#
#
import logging
import pygame

from animation import Task
from core import prepare
from core import state


# Create a logger for optional handling of debug messages.
logger = logging.getLogger(__name__)
logger.debug("states.start successfully imported")


class START(state.State):
    """ The state responsible for the splash screen and start menu.
    """
    default_duration = 3

    def startup(self, params=None):
        self.animations = pygame.sprite.Group()

        # this task will skip the splash screen after some time
        task = Task(self.game.pop_state, self.default_duration)
        self.animations.add(task)

        # Set up the splash screen logos
        self.splash_pygame = {}
        self.splash_pygame['path'] = prepare.BASEDIR + "resources/gfx/ui/intro/pygame_logo.png"
        self.splash_pygame['surface'] = pygame.image.load(self.splash_pygame['path'])
        self.splash_pygame['surface'] = pygame.transform.scale(self.splash_pygame['surface'],
                                                           (self.splash_pygame['surface'].get_width() * prepare.SCALE,
                                                            self.splash_pygame['surface'].get_height() * prepare.SCALE
                                                            ))

        splash_border = prepare.SCREEN_SIZE[0] / 20     # The space between the edge of the screen
        self.splash_pygame['position'] = (splash_border,
                                          prepare.SCREEN_SIZE[1] - splash_border - self.splash_pygame['surface'].get_height())

        self.splash_cc = {}
        self.splash_cc['path'] = prepare.BASEDIR + "resources/gfx/ui/intro/creative_commons.png"
        self.splash_cc['surface'] = pygame.image.load(self.splash_cc['path'])
        self.splash_cc['surface'] = pygame.transform.scale(self.splash_cc['surface'],
                                                           (self.splash_cc['surface'].get_width() * prepare.SCALE,
                                                            self.splash_cc['surface'].get_height() * prepare.SCALE
                                                            ))
        self.splash_cc['position'] = (prepare.SCREEN_SIZE[0] - splash_border - self.splash_cc['surface'].get_width(),
                                      prepare.SCREEN_SIZE[1] - splash_border - self.splash_cc['surface'].get_height())

    def update(self, screen, keys, current_time, time_delta):
        """Update function for state.

        :param surface: The pygame.Surface of the screen to draw to.
        :param keys: List of keys from pygame.event.get().
        :param current_time: The amount of time that has passed.

        :type surface: pygame.Surface
        :type keys: Tuple
        :type current_time: Integer

        :rtype: None
        :returns: None

        """
        self.animations.update(time_delta)
        self.draw(self.game.screen)

    def get_event(self, event):
        """Processes events that were passed from the main event loop.

        :param event: A pygame key event from pygame.event.get()

        :type event: PyGame Event

        :rtype: None
        :returns: None

        """
        # Skip the splash screen if a key is pressed.
        if event.type == pygame.KEYDOWN:
            self.game.pop_state()

    def draw(self, surface):
        """Draws the start screen to the screen.

        :param Surface: Surface to draw to

        :type Surface: pygame.Surface

        :rtype: None
        :returns: None

        """
        surface.fill((15, 15, 15))
        surface.blit(self.splash_pygame['surface'], self.splash_pygame['position'])
        surface.blit(self.splash_cc['surface'], self.splash_cc['position'])
