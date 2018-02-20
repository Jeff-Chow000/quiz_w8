
r"""
Create a txt file trainval.txt from a dataset with images and annotations.

"""

import tensorflow as tf
import os

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string(
    'dataset_dir',
    None,
    'The directory where the images files are saved.')

tf.app.flags.DEFINE_string(
    'trainval_dir',
    None,
    'The directory where the images files are saved.')

def _get_filenames_and_classes(dataset_dir):
    """Returns a list of  names.

    Args:
      dataset_dir: A directory containing a set of subdirectories representing
        class names. Each subdirectory should contain PNG or JPG encoded images.

    Returns:
      A list of image file paths, relative to `dataset_dir` and the list of
      subdirectories, representing class names.
    """
    image_root = os.path.join(dataset_dir, 'images')
    image_names = []
    print(image_root)
    for filename in os.listdir(image_root):
        print(filename) 
        (shotname,extension) = os.path.splitext(filename)
        image_names.append(shotname)
    return sorted(image_names)

def _write_trainval(trainval_dir,image_names):
    trainval_dir = os.path.join(trainval_dir, 'trainval.txt')
    f = open(trainval_dir,'w')
    print(image_names)
    for i in image_names:
    	f.write(i+'\n')
    f.close()

def main(_):
    image_names = _get_filenames_and_classes(FLAGS.dataset_dir)
    _write_trainval(FLAGS.trainval_dir,image_names)

if __name__ == '__main__':
    tf.app.run()



