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
mkdirs(label_root)
seqs = [s for s in os.listdir(seq_root)] #s for s in os.listdir(seq_root)
print(seqs)
tid_curr = 0
tid_last = -1
seq_width = 720
seq_height = 1080
for seq in seqs:
    print(seq)
    # seq_info = open(osp.join(seq_root, seq, 'seqinfo.ini')).read().split("\n")
    gt_txt = osp.join(seq_root, seq, 'gt', 'gt.txt')
    gt = np.loadtxt(gt_txt, dtype=np.float64, delimiter=',')

    seq_label_root = osp.join(label_root, seq, 'img1')
    mkdirs(seq_label_root)

    for fid, tid, x, y, w, h, _, _,_ in tqdm(gt):
        fid = int(fid)
        tid = int(tid)
        if not tid == tid_last:
            tid_curr += 1
            tid_last = tid
        label_fpath = osp.join(seq_label_root, '{:06d}.txt'.format(fid))
        label_str = '0 {:d} {:d} {:d} {:d} {:d}\n'.format(
            tid_curr, int(x) , int(y) , int(w) , int(h) )
        with open(label_fpath, 'a') as f:
            f.write(label_str)
