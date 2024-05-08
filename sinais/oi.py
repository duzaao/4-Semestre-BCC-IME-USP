from scipy.fftpack import dct, idct
print(dct([1,2,-1],norm="ortho"))
print(idct([3,0,1],norm="ortho"))