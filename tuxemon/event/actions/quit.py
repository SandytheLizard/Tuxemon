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


class QuitActionParameters(NamedTuple):
    pass


@final
class QuitAction(EventAction[QuitActionParameters]):
    """
    Completely quit the game.

    Script usage:
        .. code-block::

            quit

    """

    name = "quit"
    param_class = QuitActionParameters

    def start(self) -> None:
        # TODO: API
        self.session.client._wants_to_exit = True
        self.session.client.exit = True
        self.session.client.done = True
