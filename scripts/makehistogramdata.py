import skimage as ski
import numpy as np
import scipy
from skimage.morphology import disk
from skimage.segmentation import find_boundaries
from scipy.ndimage import convolve


def HoCS(B, min_scale, max_scale, increment, num_bins):
    '''
    Computes a histogram of curvature scale for the shape in the binary image B.  
    Boundary fragments due to holes are ignored.
    :param B: A binary image consisting of a single foreground connected component.
    :param min_scale: smallest scale to consider (minimum 1)
    :param max_scale: largest scale to consider (max_scale > min_scale)
    :param increment:  increment on which to compute scales between min_scale and max_scale
    :param num_bins: number of bins for the histogram at each scale
    :return: 1D array of histograms concatenated together in order of increasing scale.
    '''

    B_padded = np.pad(B, (max_scale+1, max_scale+1), 'constant')

    boundary = find_boundaries(B_padded, connectivity=2, mode='outer')
    boundary_indices = boundary.nonzero()
    boundary_indices = np.stack((boundary_indices[0], boundary_indices[1]), axis=-1)

    histograms = np.zeros(((max_scale - min_scale) // increment + 1,num_bins))
    
    for radius in range(min_scale, max_scale+1, increment):
        kernel = disk(radius)
        num_kernel_pixels = kernel.sum()
        data = []
        for i in boundary_indices:
            # Center mask about (i[0],i[1])
            #print(f'x: {i[0]} | y: {i[1]}')
            data.append(
                (B_padded
                  [i[0] - radius - 0: i[0] + radius + 1, 
                   i[1] - radius - 0: i[1] + radius + 1] & kernel).sum()
                / num_kernel_pixels
            )
            #print(max(data))
        histograms[((radius - min_scale) // increment) - 1,:],_ =  np.histogram(data, bins=num_bins, range=(0,1.0), density=True)
    #return histograms[0,:] / num_bins
    return np.concatenate(histograms) / num_bins

if __name__ == '__main__':
    print("Running script")