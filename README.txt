=======
Pynail
=======
Creating thumbnails efficiently using Multiprocessing.

=============
Installation
=============
```sh
	python setup.py install
```
========
Usage
========
For creating thumbnail of single image

```sh
  pynail -i 'source_img_path' 'target_img_path' '(width,height)' 'format'
```

For creating thumbnail of all images in an entire directory

```sh
  pynail -d 'source_dir_path' 'target_dir_path' '(width,height)' 'format'
```
========
Example
========
```sh
  pynail -d "/home/tushar/Desktop/Garbage/Images/Mytrip/Munnar" "/home/tushar/Desktop/thumby" "(400,400)" "JPEG"
```
=======
License
=======
![gpl](https://cloud.githubusercontent.com/assets/7397433/9025904/67008062-3936-11e5-8803-e5b164a0dfc0.png)
