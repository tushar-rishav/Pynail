#! /usr/bin/python
import logging
import Image
import argparse
import magic
from os import listdir, path, mkdir, curdir
from sys import argv, exit
from multiprocessing.dummy import Pool as ThreadPool


class Img:

    def __init__(self):
        self.err = False

    def thumb_gen(self, arg, key, flag):
        self.arg = arg
        self.size = tuple(map(int, self.arg.size.split(',')))
        if not flag:
            try:
                im_data = Image.open(self.arg.simg)
                im_data.thumbnail(self.size, Image.ANTIALIAS)
                im_data.save(self.arg.timg[:-1*len(im_data.format)-1] + "\
                .thumbnail", self.arg.format)
                logging.info("Thumbanails successfully created...")
            except Exception as e:
                logging.error("%s Cause: Maybe invalid \
                file format or wrong permission.", e)
        else:
            if path.isdir(self.arg.cdir):
                list_dir = listdir(self.arg.cdir)
                pool = ThreadPool(4)
                logging.info("Generating thumbnails...")
                __ = pool.map(self.pool_thumb, list_dir)
                pool.close()
                pool.join()
                if not self.err:
                    logging.info("Thumbanails successfully created...")
                else:
                    logging.error("Thumbanails not created...")
            else:
                raise Exception(self.arg.cdir+' is not a directory')

    def pool_thumb(self, i):
        f = self.arg.cdir.rstrip("/") + "/" + i
        if 'image' in magic.from_file(f, mime=True):  # extract all images
            if not path.isdir(self.arg.destination):
                mkdir(self.arg.destination)
            try:
                im_data = Image.open(f)
                im_data.thumbnail(self.size, Image.ANTIALIAS)
                dest = self.arg.destination.rstrip("/") + "/\
                " + i[:-1*len(im_data.format)-1] + ".thumbnail"
                im_data.save(dest, self.arg.format)
            except Exception as e:
                logging.error("%s Maybe invalid file format or wrong\
                permission.", e)
                self.err = True


def logger(func):
    def log():
        logging.getLogger().name = "Pynail "
        logging.getLogger().setLevel(logging.INFO)
        args = func()
        return args
    return log


@logger
def parse():
    parser = argparse.ArgumentParser(description=" \
             Multithreaded quick image processing from terminal", epilog="\
             Author:tushar.rishav@gmail.com")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-i", "--simg", help="Source path of image for \
        thumbnail",
                       type=str)
    parser.add_argument("-t", "--timg", help="Target path for thumbnail",
                        type=str)
    group.add_argument("-c", "--cdir", help="For a given directory path it\
    converts all the images into thumbnail", type=str, default=curdir)
    parser.add_argument("-d", "--destination", help="Target directory path",
                        type=str, default=curdir)
    parser.add_argument("-s", "--size", help="Size of the thumbnails\
        ", type=str, default="200,200")
    parser.add_argument("-f", "--format", help="Format of the thumbnails\
        ", type=str, default="JPEG")
    args = parser.parse_args()
    if len(argv) == 1:
        parser.print_help()
        exit(1)
    return args


def main():
    Im = Img()
    args = parse() 
    if args.simg:
        Im.thumb_gen(args, 'simg', 0)
    elif args.cdir:
        Im.thumb_gen(args, 'cdir', 1)
if __name__ == "__main__":
    main()
