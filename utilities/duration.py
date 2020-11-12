import os
import cv2
import shutil

original_dataset = "/media/theo/Data/PycharmProjects/Video-Summarization/DATA/Video/"
new_dataset_name = "/Video_small/"


def crawl_directory(directory):
    """Crawling data directory
        Args:
            directory (str) : The directory to crawl
        Returns:
            tree (list)     : A list with all the filepaths
    """
    tree = []
    subdirs = [folder[0] for folder in os.walk(directory)]

    for subdir in subdirs:
        files = next(os.walk(subdir))[2]
        for _file in files:
            tree.append(os.path.join(subdir, _file))
    return tree

def get_duration(filename):

    cap = cv2.VideoCapture(filename)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # duration = frame_count/fps

    return frame_count, fps


# 15 minutes = 900 seconds
if __name__ == '__main__':
    original_tree = crawl_directory(original_dataset)
    for filename in original_tree:
        frame_count, fps = get_duration(filename)
        if fps!= 0:
            duration = frame_count/fps
            if (duration <=  900):
                destination = filename.replace("/Video/", new_dataset_name)
                dst_dir = os.path.join(*destination.split(os.sep)[-3:-1])
                if not os.path.exists(dst_dir):
                    print("{0}Creation".format(dst_dir))
                    os.makedirs(dst_dir)
                # print(filename)
                shutil.copy(filename, destination)