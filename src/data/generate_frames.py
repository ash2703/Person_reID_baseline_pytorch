import os.path as osp
import os
import numpy as np
import cv2
from tqdm import tqdm

def mkdirs(d):
  if not osp.exists(d):
    os.makedirs(d)

seq_root = '/content/data_v3_shard2/images/train'
label_root = '/content/data_v3_shard2/labels/train'
gallery = '/content/data_v3_shard2/gallery'
mkdirs(gallery)
seqs = [s for s in os.listdir(seq_root)]
count = 0
for seq in seqs:
  for img_file in tqdm(os.listdir(osp.join(label_root, seq, 'img1'))):
    img_path = osp.join(label_root, seq, 'img1', img_file).replace("txt", "jpg").replace("labels","images")
    img = cv2.imread(img_path)
    gt = np.loadtxt(osp.join(label_root, seq, 'img1', img_file), ndmin = 2).astype(int)
    for person in gt:
      tid = person[1]
      mkdirs(osp.join(gallery, seq, f"{tid}"))
      x = person[2]
      y = person[3]
      w = person[4]
      h = person[5]
      try:
        cv2.imwrite(osp.join(gallery, seq, f"{tid}", f"{count}.jpg") ,img[y: y + h, x: x+ w])
        count += 1
      except:
        print("Error at: ",img_path)



