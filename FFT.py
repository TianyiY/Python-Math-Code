# !/usr/bin/python
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def triangle_wave(size, T):
    t = np.linspace(-1, 1, size, endpoint=False)
    y = np.abs(t)
    y = np.tile(y, T) - 0.5
    x = np.linspace(0, 2*np.pi*T, size*T, endpoint=False)
    return x, y


def sawtooth_wave(size, T):
    t = np.linspace(-1, 1, size)
    y = np.tile(t, T)
    x = np.linspace(0, 2*np.pi*T, size*T, endpoint=False)
    return x, y


def triangle_wave2(size, T):
    x, y = sawtooth_wave(size, T)
    return x, np.abs(y)


def non_zero(f):
    f1 = np.real(f)
    f2 = np.imag(f)
    eps = 1e-4
    return f1[(f1 > eps) | (f1 < -eps)], f2[(f2 > eps) | (f2 < -eps)]


if __name__ == "__main__":
    np.set_printoptions(suppress=True)

    x = np.linspace(0, 2*np.pi, 16, endpoint=False)
    print 'time-domain sampling：', x
    y = np.sin(2*x) + np.sin(3*x + np.pi/4) + np.sin(5*x)
    # y = np.sin(x)

    N = len(x)
    print 'Number of sampling：', N
    print 'Original signal：', y
    f = np.fft.fft(y)
    print 'frequency-domain signal：', f/N
    a = np.abs(f/N)
    print 'amplitude of frequency：', a

    iy = np.fft.ifft(f)
    print 'restore signal by inverse FFT：', iy
    print 'Imaginary number：', np.imag(iy)
    print 'Real number：', np.real(iy)
    print 'similarity of original signal and restored signal ：', np.allclose(np.real(iy), y)

    plt.subplot(211)
    plt.plot(x, y, 'go-', lw=2)
    plt.title('time-domain signal', fontsize=15)
    plt.grid(True)
    plt.subplot(212)
    w = np.arange(N) * 2*np.pi / N
    print 'frequency-domain sampling：', w
    plt.stem(w, a, linefmt='r-', markerfmt='ro')
    plt.title('frequency-domain signal', fontsize=15)
    plt.grid(True)
    plt.show()

    # triangle/sawtooth wave
    x, y = triangle_wave(20, 5)
    # x, y = sawtooth_wave(20, 5)
    N = len(y)
    f = np.fft.fft(y)
    # print 'original frequency-domain signal：', np.real(f), np.imag(f)
    print 'original frequency-domain signal：', non_zero(f)
    a = np.abs(f / N)

    # np.real_if_close
    f_real = np.real(f)
    eps = 0.3 * f_real.max()
    print eps
    f_real[(f_real < eps) & (f_real > -eps)] = 0
    f_imag = np.imag(f)
    eps = 0.3 * f_imag.max()
    print eps
    f_imag[(f_imag < eps) & (f_imag > -eps)] = 0
    f1 = f_real + f_imag * 1j
    y1 = np.fft.ifft(f1)
    y1 = np.real(y1)
    # print 'restored frequency-domain signal：', np.real(f1), np.imag(f1)
    print 'restored frequency-domain signal：', non_zero(f1)

    plt.figure(figsize=(8, 8), facecolor='w')
    plt.subplot(311)
    plt.plot(x, y, 'g-', lw=2)
    plt.title('triangle wave', fontsize=15)
    plt.grid(True)
    plt.subplot(312)
    w = np.arange(N) * 2*np.pi / N
    plt.stem(w, a, linefmt='r-', markerfmt='ro')
    plt.title('frequency-domain signal', fontsize=15)
    plt.grid(True)
    plt.subplot(313)
    plt.plot(x, y1, 'b-', lw=2, markersize=4)
    plt.title('triangle restored signal', fontsize=15)
    plt.grid(True)
    plt.tight_layout(1.5, rect=[0, 0.04, 1, 0.96])
    plt.suptitle('FFT and frequency-domain filtering', fontsize=17)
    plt.show()
