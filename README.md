# python-crux

Has two functionalites:

1) takes object name and finds it current position wrt to location given or by default the current location of the user.
```bash
crux find <objectname> <location> # by defualt it's your present location on Earth.
```

2) takes image file and gets the penumbra and umbra of the shadow image given the image file.
```bash
crux getsize <imagefilePath> <distance between object and observing plane> <distance between source and object>
```
# Incomplete tasks:

1) Getting trajectory image, plots and simulations

2) Applying a better approach in setting thresold of the circle classifier./ Other approach for detecting the penumbra and umbra more efficiently.(In progress)

3) As the oreintation of plane is not known the image of shadow is an ellipse. So instead of cirlce we should work with ellipse.


