#
# Tuxemon
# Copyright (c) 2014-2017 William Edwards <shadowapex@gmail.com>,
#                         Benjamin Bean <superman2k5@gmail.com>
#
# This file is part of Tuxemon
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import annotations
from tuxemon.event.eventaction import EventAction
from typing import NamedTuple, final


class TeleportFaintActionParameters(NamedTuple):
    pass


@final
class TeleportFaintAction(EventAction[TeleportFaintActionParameters]):
    """
    Teleport the player to the point in the teleport_faint variable.

    Usually used to teleport to the last visited Tuxcenter, as when
    all monsters in the party faint.

    Script usage:
        .. code-block::

            teleport_faint

    """

    name = "teleport_faint"
    param_class = TeleportFaintActionParameters

    def start(self) -> None:
        player = self.session.player

        # Start with the default value, override if game variable exists
        teleport = ["healing_center.tmx", 7, 10]
        if "teleport_faint" in player.game_variables:
            teleport = player.game_variables["teleport_faint"].split(" ")

        # Start the screen transition
        # self.game.event_engine.execute_action("screen_transition", [.3])

        # Call the teleport action
        self.session.client.event_engine.execute_action("teleport", teleport)
