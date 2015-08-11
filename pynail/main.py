#! /usr/bin/python
import Image
import argparse
import magic
from os import listdir, path, mkdir , curdir
from sys import argv, exit
from multiprocessing.dummy import Pool as ThreadPool


class Img:

    def __init__(self):
        pass

    def thumb_gen(self, arg, key, flag):
        self.arg = arg
        self.size = tuple(map(int, self.arg.size.split(',')))
        if not flag:    # thumbnail for an individual image
            try:
                im_data = Image.open(self.arg.simg)
                im_data.thumbnail(self.size, Image.ANTIALIAS)
                im_data.save(self.arg.timg[:-1*len(im_data.format)-1] + ".thumbnail", self.arg.format)
                print "Thumbanails successfully created..."
            except Exception as e:
                print "Error! Maybe invalid file format "+e
        else:
            if path.isdir(self.arg.cdir):
                _ = listdir(self.arg.cdir)
                pool = ThreadPool(4)
                print "Generating thumbnails..."
                __ = pool.map(self.pool_thumb, _)
                pool.close()
                pool.join()
                print "Thumbanails successfully created..."
            else:
                raise Exception(self.arg.cdir+' is not a directory')

    def pool_thumb(self, i):
        f = self.arg.cdir.rstrip("/") + "/" + i
        if 'image' in magic.from_file(f, mime=True):  # extract all images
            if not path.isdir(self.arg.destination):
                mkdir(self.arg.destination)         # if directory do not exist then create a new one
            try:
                im_data = Image.open(f)
                im_data.thumbnail(self.size, Image.ANTIALIAS)
                __ = self.arg.destination.rstrip("/") + "/"+ i[:-1*len(im_data.format)-1] + ".thumbnail"
                im_data.save(__, self.arg.format)
            except Exception as e:
                print e


def main():
    Im = Img()
    parser = argparse.ArgumentParser(description=" \
             Multithreaded quick image processing from terminal", epilog="Author:\
              tushar.rishav@gmail.com")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-i", "--simg", help="Source path of image for thumbnail",
                       type=str)
    parser.add_argument("-t", "--timg", help="Target path for thumbnail",
                       type=str)
    group.add_argument("-c", "--cdir", help="For a given directory path it converts all the images into thumbnail",
                       type=str, default = curdir)
    parser.add_argument("-d", "--destination", help="Target directory path",
                       type=str, default = curdir)
    parser.add_argument("-s", "--size", help="Size of the thumbnails", type=str, default="200,200" )
    parser.add_argument("-f", "--format", help="Format of the thumbnails", type=str, default="JPEG" )
    args = parser.parse_args()
    if len(argv) == 1:
        parser.print_help()
        exit(1)
    if args.simg:
        Im.thumb_gen(args, 'simg', 0)
    elif args.cdir:
        Im.thumb_gen(args, 'cdir', 1)
if __name__ == "__main__":
    main()
