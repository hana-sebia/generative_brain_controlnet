""" Script to create train, validation and test data lists with paths to t1w and flair images. """
from pathlib import Path
import os
import random

import pandas as pd


def create_datalist(files):

    data_list = []
    for image_path in files:
        for i in range(30):
            fus_path = Path(image_path).parent / "fUS" / image_path.replace("ULM.png",f'01_rest_slice-{i}_fUS.png')
            data_list.append({"ULM": "ULM/" + str(image_path), "fUS": str(fus_path)})

    return pd.DataFrame(data_list)


def main():
    output_dir = Path("outputs/ids/")
    output_dir.mkdir(parents=True, exist_ok=True)

    data_dir_ulm = Path("data/ULM")
    

    # List all image files in the directory
    image_files = [f for f in os.listdir(data_dir_ulm) if f.endswith(".png")]

    # Shuffle the list of image files randomly
    random.shuffle(image_files)


    # Calculate the number of images for each split
    num_train = 25
    num_validate = 5
    num_test = 5


    data_df = create_datalist(image_files[0:num_train])
    data_df.to_csv(output_dir / "train.tsv", index=False, sep="\t")

    data_df = create_datalist(image_files[num_train:num_train + num_validate])
    data_df.to_csv(output_dir / "validation.tsv", index=False, sep="\t")

    data_df = create_datalist(image_files[num_train + num_validate:len(image_files)])
    data_df.to_csv(output_dir / "test.tsv", index=False, sep="\t")


if __name__ == "__main__":
    main()