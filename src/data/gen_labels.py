#generate train.txt file containing all training image path
import os

image_files = []
root = "../../"
os.chdir(root)
with open("src/data/train.txt", "w") as outfile:
  for dirname, dir, filenames in os.walk(os.path.join("", "shards/data_v3_shard1/train")):
    if dirname.endswith("img1"):
      filenames.sort()
      for file in filenames:
        image = os.path.join(dirname,file)
        outfile.write(image)
        outfile.write("\n")
outfile.close()