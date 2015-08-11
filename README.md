# Pynail
Creating thumbnails efficiently using Multiprocessing.


##Installation
```sh
	python setup.py install
```

## Usage

For creating thumbnail of single image

```sh
 pynail -i 'source_img_path' -t 'target_img_path' -s 'width,height' -f 'format'

```

For creating thumbnail of all images in an entire directory

```sh
  pynail -c 'source_dir_path' -d 'target_dir_path' -s 'width,height' -f 'format'

```

## Example
```sh
  pynail -c /home/tushar/ -d /home/tushar/ -s "300,300" -f "png"
```

## License
![gpl](https://cloud.githubusercontent.com/assets/7397433/9025904/67008062-3936-11e5-8803-e5b164a0dfc0.png)
