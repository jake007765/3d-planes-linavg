

import numpy as np
import csv


def plane_of_best_fit(filename):

    with open(filename) as file:
        reader = csv.reader(file)
    
        
        d = 0.01 # pre-calculated difference

        origin = None # access origin in file

        basis = None # i dont know how to find the basis of a 3d plane :(

        coefficients = None #needed, unsure of usage in the equation

        points = []     # points need to be passed in as a list. (implement w/ comprehension)

        for row in csv:
            p = [row[0], row[1], row[2]]
            points.append(p)
            

        # The method you're looking for. Calculates form of best fit in three-dimensions
        svd = np.linalg.svd(points - np.mean(points, axis=1, keepdims=True))

        # Leftmost vector from svd, representing a cross-section of the form
        vector = svd[0]

    return vector


