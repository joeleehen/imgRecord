WIP for album art thingy

[Here's the video tutorial](https://www.youtube.com/watch?v=6i8kzqvh94E&t=622s)

### Authentication
I generated a personal access token and I'm passing this into any GET requests. This can be changed but works for now

## Alternative Search Methods
A few records don't have a barcode to scan. I need to implement a string search to still display these albums

### RGB matrix
I'm pretty sure adafruit has an rgb matrix setup script that I can curl into and run in a bash script. [see here for example, lines 32-42](https://github.com/ryanwa18/spotipi/blob/3acaf931d21adbdd54342e6cee137fb1f4cd9eda/setup.sh)

The link above (and the whole repo) will be valuable for building this jawn

[RGB matrix](https://www.adafruit.com/product/2026)

[RGB bonnet](https://www.adafruit.com/product/2026) (out of stock rn)

NOTE: instead of soldering, edit **/config/rgb_options.ini** and change `"adafruit-hat-pwm"` to `"adafruit-hat"`

compatible with any raspberry pi with a 40-pin GPIO pin header

### TODO:
- [ ] Get Raspberry pi, RGB matrix, RGB bonnet, solder the pins
- [ ] assemble
- [ ] write python code to get images from discogs
- [ ] write python code to display image to RGB matrix
- [ ] edit getImg to allow searching by artist and title
- [ ] create HTML landing page (needs camera button to scan barcode and text fields to enter artist and title)
- [ ] what python packages do I need? rbgmatrix, requests(?), PIL:Image(?),
- [ ] figure out how to pass API pulls to python functions (bash scripting? how do search queries come in?)
