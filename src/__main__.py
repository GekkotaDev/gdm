# fmt: off
"""
    Godot Dependency Manager. Simple, robust CLI for add-on management
    Copyright (C) 2025 gekkotadev

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
# fmt: on

import typer

from .commands.install import install


app = typer.Typer()

app.command()(install)


if __name__ == "__main__":
    typer.run(app)
