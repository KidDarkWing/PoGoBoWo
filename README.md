PoGoWoBo
========
[![Build Status](https://travis-ci.org/BoBeR182/PoGoBoWo.svg?branch=master)](https://travis-ci.org/BoBeR182/PoGoBoWo)

Bitcoin: 1HJ5kY14HMTjE3DfTEDr9YkRMxCS5PHPta

## USE WITH CAUTION! 
Niantic may ban you if you run the bot while signed in through your phone.
Softbans will happen if you teleport around the world too much.
Just wait some time between switching locations or spin 40 Pokestops.

### Important Announcement
If your bot stops working all of a sudden and doesn't move, input your latitude and longitude manually in pokebot.py. This happened because there is a limit to how many calls you can make for the API. If the bot is getting JSON errors and you you are 100% sure your config is right, check to see if the servers are down at https://go.jooas.com/

### Features
+ Incubate eggs. Use stepsize less than 3.
+ CLI based to run on VPS
+ Auto evolve
+ Auto transfer
+ Auto catch
+ Auto spin pokestop
+ Auto top up pokeballs
+ Google API for location
+ Multi account support (just add more entries in config.json)
+ Includes a basic web UI to monitor your bot

### Instructions
1. Fork/Clone project. `git clone https://github.com/BoBeR182/PoGoBoWo`.
2. Change into the directory `cd PoGoBoWo`.
3. You need to install Python version 2.7 and have pip installed; (I recommend setting up a VirtualEnv)
4. Install the dependencies with: `pip install -r requirements.txt`
5. Create a Google Maps Directions API key and activate it:
    1. Create it here: https://console.developers.google.com/projectselector/apis/credentials
    2. Then activate it here (select your project on the dropdown menu): https://console.developers.google.com/apis/api/directions_backend/overview?project=_
6. Then `cp config.json.example config.json` file.
7. Edit the file with your username, location, password, Google API, and anything else you want to change.
8. If you login into Pokemon Go with Google: `python pokebot.py -i 0` and `python pokebot.py -i 1` if you use Pokemon Trainer's Club.
9. When running the bot for the first time add `--cache` to the end.
10. ???
11. Profit.

99. You can now open your browser and navigate to `http://localhost:3001` and checkout your bot's progress.  
You can change the port by changing the `PORT` env var. eg start your bot with `PORT=8080 python pokebot.py -i 0`.

## Contibuting and TODO

Feel free to contribute code, all you need to do is run `tox` before a commit or check with TravisCI.
`pip install tox`

+ We need user freindly documentation in the wiki.
+ We need more awesome options to make it more bot like and faster, or more human like and slower.
+ Auto lucky egg
+ Detect softban and go to pokestop first.
+ Auto Gym
+ Anything else?
