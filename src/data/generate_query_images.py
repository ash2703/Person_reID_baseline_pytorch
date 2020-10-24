import os.path as osp
import os
import cv2
from tqdm import tqdm
import random
from shutil import copyfile

def mkdirs(d):
  if not osp.exists(d):
    os.makedirs(d)

gallery_root = '/content/data_v3_shard2/gallery'
query_root = '/content/data_v3_shard2/query'
mkdirs(query_root)

for root, dirs, files in tqdm(os.walk(gallery_root)):
  if len(dirs) == 0 and len(files) > 5:
    samples = random.sample(files, 5)
    for img in samples:
      dst_path = root.replace("gallery", "query")
      mkdirs(dst_path)
      copyfile(osp.join(root, img), osp.join(dst_path, img))