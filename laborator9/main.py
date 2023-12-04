import matplotlib.pyplot as plt
from dictlearn import DictionaryLearning
from dictlearn import methods
from matplotlib import image
from sklearn.feature_extraction.image import extract_patches_2d
from sklearn.feature_extraction.image import reconstruct_from_patches_2d
import numpy as np
from sklearn.preprocessing import normalize
from matplotlib import pyplot


# Exercitiul 1
imagine = image.imread("cat.png")
print("Dimensiune imagine:", imagine.shape)
imagine = imagine[:,:,0]
pixeli = 8 # dimensiune patch
s = 6 # grad de sparsitate
numar_patchuri = 1000 # numar de patchuri
numar_atomi = 256 # numar de atomi
iteratii = 50 # numar de iteratii


deviatie = 0.075 # deviatia standard
imagine_noisy = imagine + deviatie*np.random.randn(imagine.shape[0],imagine.shape[1])

patchuri_Ynoisy = extract_patches_2d(imagine_noisy, (pixeli,pixeli))
print("Dimensiune patchuri:", patchuri_Ynoisy.shape)
patchuri_Ynoisy = patchuri_Ynoisy.reshape(patchuri_Ynoisy.shape[0], -1)
print("Dimensiune patchuri reshape:", patchuri_Ynoisy.shape)
patchuri_transpuse = patchuri_Ynoisy.transpose()
print("Dimensiune patchuri transpus:", patchuri_transpuse.shape)
patchuri_mean = np.mean(patchuri_transpuse, axis=0)
patchuri_no_mean = patchuri_transpuse - patchuri_mean
print("Dimensiune patchuri fara medie:", patchuri_no_mean.shape)

patchuri_random = patchuri_no_mean[:,np.random.choice(patchuri_no_mean.shape[1],numar_patchuri)]
print("Patchuri aleatoare:", patchuri_random)

# Exercitiul 2

dictionar_initial = np.random.random(size=(pixeli*pixeli, numar_atomi))
dictionar_initial = normalize(dictionar_initial, axis=0, norm="max")

dl = DictionaryLearning(n_components=numar_atomi,max_iter=iteratii,fit_algorithm='ksvd',n_nonzero_coefs=s,code_init=None,
                        dict_init=dictionar_initial,params=None,data_sklearn_compat=False)
dl.fit(patchuri_random)
dictionar = dl.D_

# Exercitiul 3

coeficienti, err = methods.omp(patchuri_random, dictionar, n_nonzero_coefs=s)


patchuri_compresate, err = methods.omp(coeficienti, dictionar, n_nonzero_coefs=s)

patchuri_compresate = patchuri_compresate + patchuri_mean

imagine_reconstruita = reconstruct_from_patches_2d(coeficienti, coeficienti.shape[0])
# Exercitiul 4
plt.imshow(imagine)
plt.imshow(imagine_noisy)
plt.imshow(imagine_reconstruita)

def SNR_imagine(img1, img2):
    mse = np.mean((img1 - img2) ** 2)
    if(mse == 0):
        return 0
    max_pixel = 255
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr

print("SNR imagine cu zgomot:", SNR_imagine(imagine, imagine_noisy))
print("SNR imagine reconstruita:", SNR_imagine(imagine, imagine_reconstruita))
