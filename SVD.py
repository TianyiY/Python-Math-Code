import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def restore1(sigma, u, v, K):
    m = len(u)
    n = len(v)
    a = np.zeros((m, n))
    for k in range(K):
        uk = u[:, k].reshape(m, 1)
        vk = v[k].reshape(1, n)
        a += sigma[k] * np.dot(uk, vk)
    a[a < 0] = 0
    a[a > 255] = 255
    # a = a.clip(0, 255)
    return np.rint(a).astype('uint8')


def restore2(sigma, u, v, K):
    m = len(u)
    n = len(v)
    a = np.zeros((m, n))
    for k in range(K+1):
        for i in range(m):
            a[i] += sigma[k] * u[i][k] * v[k]
    a[a < 0] = 0
    a[a > 255] = 255
    return np.rint(a).astype('uint8')


if __name__ == "__main__":
    A = Image.open("lena.png", 'r')
    a = np.array(A)
    print a.shape
    K = 20
    u_r, sigma_r, v_r = np.linalg.svd(a[:, :, 0])
    print u_r.shape, sigma_r.shape, v_r.shape
    print len(u_r), len(v_r)
    u_g, sigma_g, v_g = np.linalg.svd(a[:, :, 1])
    u_b, sigma_b, v_b = np.linalg.svd(a[:, :, 2])
    plt.figure(figsize=(10,10), facecolor='w')

    for k in range(1, K+1):
        R = restore1(sigma_r, u_r, v_r, k)
        print R.shape
        G = restore1(sigma_g, u_g, v_g, k)
        B = restore1(sigma_b, u_b, v_b, k)
        I = np.stack((R, G, B), 2)

        plt.subplot(4, 5, k)
        plt.imshow(I)
        plt.axis('off')
        plt.title('SV:{}'.format(k))

    plt.suptitle(u'SVD and Image Decomposition', fontsize=20)
    plt.tight_layout(2)
    plt.subplots_adjust(top=0.9)
    plt.show()
