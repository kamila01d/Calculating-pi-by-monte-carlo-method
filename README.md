# Calculating-pi-by-monte-carlo-method

This program generate Pi number by Monte Carlo method.
It has one method:
 -generator_pi(a, it)
 which takes two arguments, a is the length of the side of the square, and it is the number of iterations.
 
 Assuming that the starting point is at the point (a, a), (center of the circle), we randomly draw points
 whose coordinates belong to the set (0, a). Next, by calculating the length
 of the segment from the drawing point to the center (a, a), we check whether this length is less than 
 or equal to the radius. If so, increment the shoots.
 
