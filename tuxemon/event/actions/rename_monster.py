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
# Contributor(s):
#
# Adam Chevalier <chevalierAdam2@gmail.com>
#

from __future__ import annotations
from tuxemon.event.eventaction import EventAction
from tuxemon.locale import T
from typing import NamedTuple, final
from tuxemon.states.world.worldstate import WorldState
from tuxemon.states.monster import MonsterMenuState
from tuxemon.menu.input import InputMenu
from tuxemon.menu.interface import MenuItem
from tuxemon.monster import Monster


class RenameMonsterActionParameters(NamedTuple):
    pass


@final
class RenameMonsterAction(EventAction[RenameMonsterActionParameters]):
    """
    Open the monster menu and text input screens to rename a selected monster.

    Script usage:
        .. code-block::

            rename_monster

    """

    name = "rename_monster"
    param_class = RenameMonsterActionParameters

    def start(self) -> None:
        # Get a copy of the world state.
        self.session.client.get_state_by_name(WorldState)

        # pull up the monster menu so we know which one we are renaming
        menu = self.session.client.push_state(MonsterMenuState)
        menu.on_menu_selection = self.prompt_for_name

    def update(self) -> None:

        missing_monster_menu = False

        try:
            self.session.client.get_state_by_name(MonsterMenuState)
        except ValueError:
            missing_monster_menu = True

        try:
            self.session.client.get_state_by_name(InputMenu)
        except ValueError:
            if missing_monster_menu:
                self.stop()

    def set_monster_name(self, name: str) -> None:
        self.monster.name = name
        monster_menu_state = self.session.client.get_state_by_name(
            MonsterMenuState,
        )
        monster_menu_state.refresh_menu_items()

    def prompt_for_name(self, menu_item: MenuItem[Monster]) -> None:
        self.monster = menu_item.game_object

        self.session.client.push_state(
            state_name=InputMenu,
            prompt=T.translate("input_monster_name"),
            callback=self.set_monster_name,
            escape_key_exits=False,
            initial=T.translate(self.monster.slug),
        )
