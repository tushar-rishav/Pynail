# Pynail
Creating thumbnails efficiently using Multiprocessing. (Work under progress :grin: )



## Usage
For creating thumbnail of single image
```sh
  python main.py -i 'source_img_path' 'target_img_path' '(width,height)' 'format'
```
For creating thumbnail of all images in an entire directory
```sh
  python main.py -d 'source_dir_path' 'target_dir_path' '(width,height)' 'format'
```
## Example
```sh
  sudo ./main.py -d "/home/tushar/Desktop/Garbage/Images/Mytrip/Munnar" "/home/tushar/Desktop/thumby" "(400,400)" "JPEG"
  ```

## License
![gpl](https://cloud.githubusercontent.com/assets/7397433/9025904/67008062-3936-11e5-8803-e5b164a0dfc0.png)
