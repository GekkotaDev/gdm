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

from typing import Final
from typing_extensions import Annotated

import pathlib

import asyncer
import typer
import yaml

from pydantic import BaseModel

from returns.io import IO, IOResult, IOFailure, IOSuccess
from returns.trampolines import Trampoline, trampoline

__all__ = ("install",)


SPEC_FILE: Final[str] = "gdm_spec.yaml"


@trampoline
def resolve_gdm_spec_path(
    current_working_directory: IO[pathlib.Path],
) -> IOResult[IO[pathlib.Path], IOError]:
    gdm_spec_file_path = current_working_directory.map(
        lambda path: path / "gdm_spec.yaml"
    )
    parent_directory = current_working_directory.map(lambda path: path.parent)

    if gdm_spec_file_path.map(lambda path: path.exists()) == IO(True):
        return IOSuccess(gdm_spec_file_path)

    if IO(current_working_directory) == parent_directory:
        return IOFailure(IOError())

    return Trampoline(resolve_gdm_spec_path, parent_directory)()


@asyncer.syncify
async def install(
    dependencies: Annotated[list[str], typer.Argument()],
):
    current_working_directory = IO(pathlib.Path.cwd())
    gdm_spec_path = resolve_gdm_spec_path(current_working_directory)
