import os
import wandb

NAME = "chica_crop_flip"
PATH = "expr/results/chica_crop_flip"
VIDEO_FILE = "video_ref.mp4"
IMG = "reference.jpg"

def upload():
  config = {
    "dataset" : "afhq",
    "type" : "eval-video", 
    "examples" : "chica_sample_flip"
  }
  wandb.init(project="stargan", entity="stacey", name=NAME, config=config)
  wandb.log( { #"video" : wandb.Video(os.path.join(PATH, VIDEO_FILE)), 
             "ref image" : wandb.Image(os.path.join(PATH, IMG))})

upload()
