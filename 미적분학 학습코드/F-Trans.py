import numpy as np
import matplotlib.pyplot as plt

# 주어진 함수의 푸리에 변환
def F(omega):
    if omega == 0:
        return 2  # 주파수 0에서 불연속점이 있으므로 따로 처리
    else:
        return 2 * np.sin(omega) / omega

# 주어진 함수와 진폭의 그래프
x_values = np.linspace(-5, 5, 1000)
f_values = [1 if abs(x) < 1 else 0 for x in x_values]
F_amplitude = [abs(F(omega)) for omega in np.fft.fftshift(np.fft.fftfreq(len(x_values)))]

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(x_values, f_values, label='f(x)')
plt.title('Given Function $f(x)$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(np.fft.fftshift(np.fft.fftfreq(len(x_values))), F_amplitude, label='$|F(\omega)|$')
plt.title('Amplitude of the Fourier Transform $|F(\omega)|$')
plt.xlabel('Frequency (Hz)')
plt.ylabel('|F(omega)|')
plt.legend()

plt.tight_layout()
plt.show()
