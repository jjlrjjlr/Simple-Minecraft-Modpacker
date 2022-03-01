#!/bin/python3
# Simple Minecraft Modpacker
# ========
# Simple program for bundling mods into separate packs for
# client, server, and singleplayer (client+server). With plans to
# eventually turn this script into a full mod manager with the ability
# to package, distribute, and update mods in a simple and easy to
# maintain format.
# ========
# TODO:
#   * Add config file handling.
#   * Figure out a way to auto-unpack
#   * Add update checker
#   * Create system for downloading mods from curseforge needed for modpack (maybe...)
#   * Create user friendly UI for managing mods
#   * Create .mcrate file format, based off of .tar.gz, for distributing modpacks
# ========
# Copyright 2022  jjlrjjlr (https://github.com/jjlrjjlr)

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.

#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ------------

from os import path, makedirs, listdir
from sys import argv
import tempfile
from rich import print as rprint
import argparse
import shutil