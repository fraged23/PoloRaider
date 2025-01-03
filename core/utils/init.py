import os

try:
    import requests
    import json
    import time
    import re
    import webbrowser
    import colorama
    import websocket
    import platform
    import threading
    import random
    import typing
    from concurrent.futures import ThreadPoolExecutor
    import asyncio
    import aiohttp
except ImportError:
    os.system("pip install requests")
    os.system("pip install colorama") 
    os.system("pip install websocket-client")
    os.system("pip install aiohttp")
    os.system("pip install asyncio")
    os.system("pip install typing")

from colorama import(
    Fore, init, Style
)
from typing import(
    List, Tuple, Dict
)

class invite:
    webbrowser.open("https://discord.gg/x5aj3d3CFg")

init(autoreset=True)

class Colors:
    darkgrey = Fore.LIGHTBLACK_EX
    w = Fore.WHITE

class Themes:
    def __init__(self):
        self.themes = {
            'blue': {
                'main': '\033[38;5;75m',
                'second': Fore.WHITE,
                'h': Fore.WHITE
            },
            'pink': {
                'main': '\033[38;5;218m', 
                'second': Fore.LIGHTMAGENTA_EX,
                'h': Fore.WHITE
            },
            'red': {
                'main': '\033[38;5;174m',
                'second': Fore.LIGHTRED_EX,
                'h': Fore.WHITE
            },
            'green': {
                'main': '\033[38;5;121m',
                'second': Fore.LIGHTGREEN_EX,
                'h': Fore.WHITE
            },
            'yellow': {
                'main': '\033[38;5;229m',
                'second': Fore.LIGHTGREEN_EX,
                'h': Fore.WHITE
            }
        }

        self.fade = {
            'blue': ['\033[38;5;75m', '\033[38;5;74m', '\033[38;5;73m', '\033[38;5;67m', '\033[38;5;61m'],
            'pink': ['\033[38;5;218m', '\033[38;5;217m', '\033[38;5;211m', '\033[38;5;175m', '\033[38;5;174m'],
            'red': ['\033[38;5;174m', '\033[38;5;167m', '\033[38;5;166m', '\033[38;5;160m', '\033[38;5;124m'],
            'green': ['\033[38;5;121m', '\033[38;5;120m', '\033[38;5;114m', '\033[38;5;108m', '\033[38;5;107m'],
            'yellow': ['\033[38;5;229m', '\033[38;5;228m', '\033[38;5;222m', '\033[38;5;221m', '\033[38;5;220m']
        }

        self.current_theme = self.load_theme()

    def load_theme(self):
        try:
            with open('config.json', 'r') as f:
                config = json.load(f)
                return config.get('theme', 'blue')
        except:
            return 'blue'

    def save_theme(self, theme_name):
        config = {}
        try:
            with open('config.json', 'r') as f:
                config = json.load(f)
        except FileNotFoundError:
            pass
        
        config['theme'] = theme_name
        
        with open('config.json', 'w') as f:
            json.dump(config, f, indent=4)

    def get_colors(self):
        return self.themes.get(self.current_theme, self.themes['blue'])

    def get_fade(self):
        return self.fade.get(self.current_theme, self.fade['blue'])

    def change_theme(self):
        clear()
        print(ascii)
        print()
        colors = self.get_colors()
        for i, theme in enumerate(self.themes.keys(), 1):
            print(f"                                                {colors['main']}[{Colors.w}{i}{colors['main']}] > {colors['main']}[{Colors.w}{theme}{colors['main']}]")
        
        try:
            c_input = int(input(f"                                                {colors['main']}[{Colors.w}POLO{colors['main']}] {Colors.w}| {colors['main']}[{Colors.w}INPUT{colors['main']}] > "))
            theme_name = list(self.themes.keys())[c_input - 1]
            self.current_theme = theme_name
            self.save_theme(theme_name)
            return True
        except (ValueError, IndexError):
            print(f"                                                {colors['main']}[{Colors.w}Invalid choice, try again. {colors['main']}]")
            time.sleep(1)
            return False

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_tokens():
    try:
        with open('data/input/tokens.txt', 'r') as f:
            return [token.strip() for token in f.readlines() if token.strip()]
    except FileNotFoundError:
        print("Error: tokens.txt not found in data/input/")
        return []

theme = Themes()

ascii = fr"""
{theme.get_fade()[0]}                                            ________      ______      
{theme.get_fade()[1]}                                            ___  __ \________  /_____
{theme.get_fade()[2]}                                            __  /_/ /  __ \_  /_  __ \
{theme.get_fade()[3]}                                            _  ____// /_/ /  / / /_/ /
{theme.get_fade()[4]}                                            /_/     \____//_/  \____/    """

def print_logo():
    colors = theme.get_colors()
    print(ascii)
    logo = fr"""
                          {Colors.darkgrey}NOTE: SOME FEATURES ARE PAID, AND WON'T WORK ON THIS VERSION        

           {colors['main']}[{Colors.w}01{colors['main']}] {Colors.w}> Channel Spammer    {colors['main']}[{Colors.w}06{colors['main']}] {Colors.w}> Reaction Spammer     {colors['main']}[{Colors.w}11{colors['main']}] {Colors.w}> Token Checker   {colors['main']}[{Colors.w}16{colors['main']}] {Colors.w}> Status Switcher
           {colors['main']}[{Colors.w}02{colors['main']}] {Colors.w}> Reply Spammer      {colors['main']}[{Colors.w}07{colors['main']}] {Colors.w}> VC Spammer           {colors['main']}[{Colors.w}12{colors['main']}] {Colors.w}> Server Joiner   {colors['main']}[{Colors.w}17{colors['main']}] {Colors.w}> Pron Switcher
           {colors['main']}[{Colors.w}03{colors['main']}] {Colors.w}> Thread Spammer     {colors['main']}[{Colors.w}08{colors['main']}] {Colors.w}> Ghost Spammer        {colors['main']}[{Colors.w}13{colors['main']}] {Colors.w}> Server Leaver   {colors['main']}[{Colors.w}18{colors['main']}] {Colors.w}> Pass Switcher
           {colors['main']}[{Colors.w}04{colors['main']}] {Colors.w}> Group Spammer      {colors['main']}[{Colors.w}09{colors['main']}] {Colors.w}> DM Spammer           {colors['main']}[{Colors.w}14{colors['main']}] {Colors.w}> Server Checker  {colors['main']}[{Colors.w}19{colors['main']}] {Colors.w}> Bio Switcher
           {colors['main']}[{Colors.w}05{colors['main']}] {Colors.w}> Forum Spammer      {colors['main']}[{Colors.w}10{colors['main']}] {Colors.w}> Friend Req Spammer   {colors['main']}[{Colors.w}15{colors['main']}] {Colors.w}> Name Switcher   {colors['main']}[{Colors.w}20{colors['main']}] {Colors.w}> Settings"""
    print(logo)
