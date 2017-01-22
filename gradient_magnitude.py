from pylab import *
import numpy as np
import scipy as sp
from scipy.ndimage import imread
from scipy.misc import imsave
from scipy.signal import convolve2d as conv
from scipy.ndimage import gaussian_gradient_magnitude
import matplotlib.pyplot as plt
from skimage import data
from skimage.feature import match_template

def compute_gradmag(I1, I2, sigmas):
    '''
    Find best gradient magnitude for images
    '''
    for sigma in sigmas:
        grad_mag = gaussian_gradient_magnitude(I1, sigma, mode='constant', cval = 0)
        imsave("templatenoise_gradient_"+str(sigma)+".jpg", grad_mag)
    
    for sigma in sigmas:
        grad_mag = gaussian_gradient_magnitude(I2, sigma, mode='constant', cval = 0)
        imsave("waldonoise_gradient_"+str(sigma)+".jpg", grad_mag)
    
def NCC(image, template):
    '''
    Returns result of normalized cross-correlation for the image and template
    '''
    product = np.mean((image - image.mean()) * (template - template.mean()))
    stds = image.std() * template.std()    
    return product/stds

def match(img, tmpl):
    # get edges from the magnitude of gradients (7 for the template is sufficient
    # to remove noise and 9 is sufficient to remove noise for the full image)
    grad_mag = gaussian_gradient_magnitude(tmpl, 7, mode='constant', cval = 0)
    Img_grad_mag = gaussian_gradient_magnitude(img, 9, mode='constant', cval = 0)
    
    # fast NCC with the template and image
    result = match_template(Img_grad_mag, grad_mag)
    
    # find peak
    ij = np.unravel_index(np.argmax(result), result.shape)
    x, y = ij[::-1] 
    
    plot(img, tmpl, x, y, result)
    
    
def plot(img, tmpl, x, y, result):
    fig, (ax1, ax2, ax3) = plt.subplots(ncols = 3, figsize = (8, 3))
    
    ax1.imshow(tmpl, cmap='gray')
    ax1.set_axis_off()
    ax1.set_title('template')
    
    ax2.imshow(img, cmap='gray')
    ax2.set_axis_off()
    ax2.set_title('image')
    # highlight matched region
    rect = plt.Rectangle((x,y), tmpl.shape[1], tmpl.shape[0], 
                         edgecolor='r', facecolor='none')
    ax2.add_patch(rect)
    
    ax3.imshow(result, cmap='gray')
    ax3.set_axis_off()
    ax3.set_title('match template')
    ax3.autoscale(False)
    ax3.plot(x, y, 'o', markeredgecolor='r', markerfacecolor='none', markersize=7)
    
    show()
    plt.savefig("template_match.png", facecolor=fig.get_facecolor())    

if __name__ == "__main__":
    tmpl = imread("templatenoise.png", mode='L')
    img = imread("waldonoise.png", mode='L')    
    
    #sigmas = [0.5, 2, 5, 10, 30] 
    #compute_gradmag(tmpl, img, sigmas)
    
    match(img, tmpl)
       
    