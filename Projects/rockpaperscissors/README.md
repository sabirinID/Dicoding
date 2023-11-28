# Proyek Akhir: Klasifikasi Gambar

<p align='center'>
  <img src='Images/rockpaperscissors.png' width='600' height='auto'>
  <br>
  Image by <a href='https://en.wikipedia.org/wiki/Rock_paper_scissors'>Wikipedia</a>
</p>

Kita telah berada di akhir pembelajaran dalam akademi ini. Kita sudah mempelajari dasar-dasar machine learning dan bagaimana jaringan saraf bekerja. Untuk bisa lulus dari akademi ini, kita harus mengirimkan submission berupa program jaringan saraf tiruan menggunakan TensorFlow. Program kita harus mampu mengenali bentuk tangan yang membentuk gunting, batu, atau kertas.

## Dataset

Dataset yang digunakan, yaitu [rockpaperscissors](https://github.com/dicodingacademy/assets/releases/download/release/rockpaperscissors.zip).

## Kriteria

- Dataset harus dibagi menjadi *train set* dan *validation set*.
- Ukuran validation set harus 40% dari total dataset (data training memiliki 1314 sampel, dan data validasi sebanyak 874 sampel).
- Harus mengimplementasikan [data augmentation(https://www.tensorflow.org/tutorials/images/data_augmentation)].
- Harus menggunakan `ImageDataGenerator`.
- Harus menggunakan model [Sequential](https://www.tensorflow.org/api_docs/python/tf/keras/Sequential).
- Harus memiliki akurasi model minimal 85%.
- Pelatihan model tidak melebihi waktu 30 menit.
- Program dikerjakan pada [Google Colaboratory](https://colab.research.google.com/).