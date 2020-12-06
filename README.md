<h1 align="center" style="position: relative;">
    <strong>AI.Billy</strong>
</h1>

<p align="center">
    AI.Billy is part of the <a href="https://github.com/billydevyt/RoboBilly/">RoboBilly</a> project.
</p>

<br/>

<p align="center">
    <img alt="Discord" src="https://img.shields.io/discord/750945243305869343?label=Basement&style=flat-square">
    <!-- <img alt="Travis (.com)" src="https://travis-ci.org/github/billydevyt/RoboBilly"> -->
    <!-- <img alt="Python" src=https://img.shields.io/github/pipenv/locked/python-version/billydevyt/RoboBilly> -->
    <img alt="Release" src=https://img.shields.io/github/v/release/billydevyt/AI-Billy?style=flat-square>
    <img alt="Heroku" src="https://img.shields.io/badge/heroku-passing-green?style=flat-square">
    <img alt="License" src="https://img.shields.io/github/license/billydevyt/AI-Billy?style=flat-square">
</p>

<p align="center">
    <a href="#building--running">Building & running</a> •
    <a href="#commands">Commands</a> •
    <a href="https://github.com/billydevyt/AI-Billy/blob/main/LICENSE">License</a> •
    <a href="#configuration">config</a> •
    <a href="#faq">FAQ</a>
</p>

## Building & running

The bot is written in **Python 3.8**, you can run it via `python bot.py` from command line or just use the `run.bat` file to run it. If you are missing packages make sure to run install mentioned ones in `requirements.txt` prior to building. Also all the files required to Launch the bot to **Heroku.com** is included.
Additionally you can use `pyinstaller` to create a binary file.

## Configuration

1. `config.json` is where all of the bot configuration will be placed. The only fields that are essential for running the bot are `token`, `prefix` and `owner_id`.

```json
{
	"token": "get it from discord developer portal.",
	"prefix": "!",
	"channel": "chat-bot",
	"startup_file": "std-startup.xml",
    "owner_id": "bot owner's id"
}
```

2. make a channel with the name you gave in `config.json` (by default it is chat-bot)

3. Now you can chat in that channel.

#Commands

|Command (aliases)|Description|
|--:|:--|
|respond(ai)|For talking to AI through a command method.|
|help|basic help command, lists all features.|

#FAQ

1. I want to add custom responses, how to do it?

- you will have to use the template in `./template` or make a new aiml file with responses.
- then copy the aiml file to `./aiml` directory. The bot reads any of the file from `./aiml` directory, so you can place it anywhere inside there.

2. New added custom reponses/modified responses are not working, why?
- If you have modified any of the aiml scripts or added new, you will have to delete the generated `brn` file(which can be found in the main directory), and run again.
