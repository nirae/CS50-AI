import os
import sys
import cv2
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from random import randrange

from traffic import load_data

def plot_image(i, predictions_array, img):
    true_label = i
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'green'
    else:
        color = 'red'

    plt.xlabel(
        "{} {:2.0f}% ({})".format(
            predicted_label,
            100 * np.max(predictions_array),
            true_label
        ),
        color=color
    )


def main():

    model = tf.keras.models.load_model('model')

    images = []

    for category in range(43):
        files = [f for f in os.listdir(os.path.join('gtsrb', str(category))) if os.path.isfile(os.path.join('gtsrb', str(category), f))]
        i = randrange(len(files))
        path = os.path.join('gtsrb', str(category), files[i])
        image = cv2.imread(path)
        resized = cv2.resize(image, (30, 30))
        images.append(resized)

    predictions = []
    for i, image in enumerate(images):
        prediction = model.predict(np.asarray([image]))
        predictions.append(prediction)

    num_rows = 11
    num_cols = 4
    num_images = num_rows * num_cols
    plt.figure(figsize=(2 * 2 * num_cols, 2 * num_rows))
    for i, image in enumerate(images):
        plt.subplot(num_rows, 2 * num_cols, 2 * i + 1)
        plot_image(i, predictions[i], image)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()