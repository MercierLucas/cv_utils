import cv2
import os

from cvutils.loaders import list_files_in_dir_recursive

class ImageDataset:

    def __init__(self, dataset_dir, verbose=False) -> None:
        self.verbose = verbose
        images_path = list_files_in_dir_recursive(dataset_dir)
        self.images, self.labels = self._load(images_path)
        

    def _load(self, images_path):
        images = []
        labels = []
        n_images = len(images_path)
        for (i, path) in enumerate(images_path):
            if self.verbose:
                print(f'Processing {(i + 1)}/{n_images}')
            image = cv2.imread(path)
            name =  os.path.dirname(path).split('\\')[-1]
            labels.append(name)
            images.append(image)

        return images, labels


    def __getitem__(self, idx):
        return self.images[idx], self.labels[idx]

    
    def __next__(self):
        self.curr_idx += 1

        if self.curr_idx == len(self.labels):
            raise StopIteration

        return self[self.curr_idx]


    def __iter__(self):
        self.curr_idx = -1
        return self
