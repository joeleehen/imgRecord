WIP for album art thingy

### Authentication
- authentication required to pull image URLs; use discogs Auth Flow rather than OAuth and its libraries
- more info here: https://www.discogs.com/developers/#page:authentication,header:authentication-discogs-auth-flow
- I think use consumer key/secret rather than personal tokens for ease of use

### RGB matrix
I'm pretty sure adafruit has an rgb matrix setup script that I can curl into and run in a bash script
[see here for example, lines 32-42] (https://github.com/ryanwa18/spotipi/blob/3acaf931d21adbdd54342e6cee137fb1f4cd9eda/setup.sh)
The link above (and the whole repo) will be valuable for building this jawn

### TODO:
- [ ] Get Raspberry pi, RGB matrix, RGB bonnet, solder the pins
- [ ] assemble
- [ ] write python code/bash script (which one comes first?
- [ ] create HTML landing page
