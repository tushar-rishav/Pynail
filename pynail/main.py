#! /usr/bin/python
import Image
import argparse
import magic
from os import listdir, path, mkdir
from sys import argv, exit
from multiprocessing.dummy import Pool as ThreadPool


class Img:

    def __init__(self):
        pass

    def thumb_gen(self, arg, key, flag):
        self.arg = vars(arg)[key]
        self.size = tuple(map(int, self.arg[2][1:-1].split(',')))
        if not flag:    # thumbnail for an individual image
            try:
                im_data = Image.open(arg[0])
                im_data.thumbnail(self.size, Image.ANTIALIAS)
                im_data.save(self.arg[1] + ".thumbnail", self.arg[3])
            except Exception as e:
                print e
        else:
            if path.isdir(self.arg[0]):
                _ = listdir(self.arg[0])
                pool = ThreadPool(4)
                print "Generating thumbnails..."
                __ = pool.map(self.pool_thumb, _)
                pool.close()
                pool.join()
                print "Thumbanails successfully created..."
            else:
                raise Exception(arg[0]+' is not a directory')

    def pool_thumb(self, i):
        f = self.arg[0].rstrip("/") + "/" + i
        if 'image' in magic.from_file(f, mime=True):  # extract all images
            if not path.isdir(self.arg[1]):
                mkdir(self.arg[1])
            try:
                im_data = Image.open(f)
                im_data.thumbnail(self.size, Image.ANTIALIAS)
                __ = self.arg[1].rstrip("/") + "/"
                + i[:-1*len(im_data.format)-1] + ".thumbnail"
                im_data.save(__, self.arg[3])
            except Exception as e:
                print e


def main():
    Im = Img()
    parser = argparse.ArgumentParser(description=" \
             Multithreaded quick image processing from terminal", epilog="Author:\
              tushar.rishav@gmail.com")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-i", "--image", nargs=4, help="Create a thumbnail.",
                       type=str)
    group.add_argument("-d", "--dir", nargs=4, help="Create a thumbnail\
     of all the images in a directory. ",
                       type=str)
    args = parser.parse_args()
    if len(argv) == 1:
        parser.print_help()
        exit(1)
    if args.image:
        Im.thumb_gen(args, 'image', 0)
    elif args.dir:
        Im.thumb_gen(args, 'dir', 1)
if __name__ == "__main__":
    main()
