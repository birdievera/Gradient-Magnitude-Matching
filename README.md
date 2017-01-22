### Gradient Magnitude Matching

Matches the template to the image given using the magnitude of gradients. Scipy's match_template uses a fast NCC (faster than my own) in order to match the two. 

*Note*: The template and image contain lots of noise to demonstrate the accuracy of magnitude of gradients.

**Find Waldo Experiment!**

Using the image:

![alt text](https://github.com/birdievera/Gradient-Magnitude-Matching/blob/master/waldoNoise.png "Waldo and friends")

Our template is:

![alt text](https://github.com/birdievera/Gradient-Magnitude-Matching/blob/master/templateNoise.png "Waldo")

And the results of our match are:

![alt text](https://github.com/birdievera/Gradient-Magnitude-Matching/blob/master/template_match.png "Where's Waldo?")