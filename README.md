
# GET 24
An adaptation of the arithmetical card game [24](http://en.wikipedia.org/wiki/24_Game) for the [OLPC](http://one.laptop.org/) and designed for use within the [Sugar Educational Runtime Environmentt](https://www.sugarlabs.org/).

## TABLE OF CONTENTS

- Overview
    - What is 24?
    - Operational Requirements
    - Game Features
- How to Run
    - As a Standalone Python App
    - Within the OLPC
- For Developers
    - Setup Development Environment
    - File Hierarchy
    - To-Do
- Project History
- Core Contributors
- License & Attribution



## OVERVIEW
### What is 24?
Taken from [Wikipedia](http://en.wikipedia.org/wiki/24_Game):
>The 24 Game is an arithmetical card game in which the objective is to find a way to manipulate four integers so that the end result is 24. Addition, subtraction, multiplication, or division, and sometimes other operations, may be used to make four digits from one to nine equal 24. For example, card with the numbers 4,7,8,8, a possible solution is the following: (7-(8/8))*4=24.
>
The game has been played in Shanghai since the 1960s, using ordinary playing cards.

GET 24 is a digital take on this classic mathematical card game.

### Operational Requirements
* Python 2.7.9
* PyGame ( latest version compatible with Python 2.7.x )
* *(optional)* XOPC for testing device deployment

### Game Features
* Main Menu Features
    * Play the Game
    * Launch the help menu
    * Quit the game
* Help Menu
    * An explanation of how to play the game
    * Info graphic showcasing the game assets and what they do
* Game
    * Digital variant of game play found in the card game 24
    * colorful, click-friendly environment suited for young students
    * "undo" and "reset" controls -- undo a mistake, or reset the whole game.

## HOW TO RUN
### As a Standalone Python App
Simply navigate to the directory where you downloaded GET24, and run `Game24.py` (from terminal: `$ Python ./Game24.py`)

### Within the OLPC / Sugar Environment
TODO

## FOR DEVELOPERS
GET24 is a very new, very-alpha piece of software and so likely is not ready for prime time. We encourage developers to take our code and run wild with it! Add features listed on our todo, add custom features and shoot us a pull request, do anything you like! :)

The base project is derived from the [FOSSRIT](https://github.com/FOSSRIT) [Sugar-Quickstart](https://github.com/FOSSRIT/sugar-quickstart), with the goal of compiling the project into a package for the Sugar RTE. Please visit the Sugar-Quickstart repo to learn more about building for the OLPC/Sugar RTE.

Partial code structure was also based off of work done by the [Fractionauts](https://github.com/chrisknepper/Fractionauts) team, a similar project targeted at the Sugar RTE. Thank you for your contributions!

### Setup Development Environment
The development environment does not have any particularly fancy requirements. As long as you meet the software requirements (Python 2.7.x, PyGame 2.7.x) you should be good to go. We did encounter some runtime/performance issues on various Linux distributions however have been unable to pinpoint the cause. Our core development team developed exclusively on OSX and Windows based computers.

### Important Files
Within `references/24`:

#### Game24.py
The main entry point for the application. Manages the scenes, main game loop, and event delegation to the active scene.

#### SceneBasic.py
Super Class for scenes. Each scene inherits from SceneBasic. It contains basic, essential structure used in all scenes, such as responding to scene loading / exiting.

#### SceneMenu.py
The first scene loaded by `Game24.py`. The main menu.

#### SceneHelp.py
Called by `SceneMenu.py`. This scene displays help information to the user.

#### SceneGame.py
Called by `SceneMenu.py`. This is the actual game.

#### test.py
Backend logic for application. Contains methods for generating and validating integer sets and user answers. the "AI" of the game.

### Development To-Do
* TODO
* Finish Game
* get compiling to Sugar working

## PROJECT INFORMATION
### Project History
The project was started in October, 2014 as an assignment in the [Humanitarian, Free/Open Source Software Development Course](https://hfoss-fossrit.rhcloud.com/) at the [Rochester Institute of Technology](www.rit.edu).

### Core Contributors
* [Anjali Tewari (anjalitewari)](https://github.com/anjalitewari)
* [Danny Nguyen (dxn7335)](https://github.com/dxn7335)
* [Lanxi Xing (xingnx)](https://github.com/xingnx)
* [Tom Conroy (tconroy)](https://github.com/tconroy)

### License & Attribution
Full licensing can be found within the root directory of the project, within the file `LICENSE.md`. The project is built upon the GNU GENERAL PUBLIC LICENSE Version 2, June 1991.

A special thanks to the following people, developers & resources used within this project:

* [FOSS@RIT Sugar Quickstart](https://github.com/FOSSRIT/sugar-quickstart)
    * base code structure, Sugar compiling instructions
* [Fractionauts](https://github.com/chrisknepper/Fractionauts)
    * Code structure inspiration
* [OpenGameArt.org](opengameart.org)
    * Audio assets
* [Danny Nguyen (dxn7335)](https://github.com/dxn7335)
    * Visual assets
* [PyGButton](https://github.com/asweigart/pygbutton)
    * Button library for Python
* [Remy DeCausemaker](https://github.com/decause)
    * Course Professor, fueled us with pizza at hackathons :)