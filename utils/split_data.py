"""This file contains the code necessary to split a given file in three files, one containig the training data, one containig the validation data and one containing the testing data."""

import random
import argparse


def split_file(
    input_file_path,
    train_output_path,
    val_output_path,
    test_output_path,
    train_ratio=0.7,
    val_ratio=0.15,
    seed=None,
):
    if seed is not None:
        random.seed(seed)

    with open(input_file_path, "r") as input_file:
        train_file = open(train_output_path, "w")
        val_file = open(val_output_path, "w")
        test_file = open(test_output_path, "w")

        for line in input_file:
            # determine which file to write to based on the random ratio
            rand_value = random.random()
            if rand_value < train_ratio:
                output_file = train_file
            elif rand_value < train_ratio + val_ratio:
                output_file = val_file
            else:
                output_file = test_file

            output_file.write(line)

        train_file.close()
        val_file.close()
        test_file.close()

        print("[+] splitting complete.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="split the data in a file in training, validation and testing data"
    )
    parser.add_argument("file", type=str, help="the name of the target file")
    args = parser.parse_args()

    data_dir = "quickdraw_data/"
    target_file = args.file

    print("[+] commencing splitting...")
    split_file(
        data_dir + target_file,
        data_dir + "train_" + target_file,
        data_dir + "val_" + target_file,
        data_dir + "test_" + target_file,
        train_ratio=0.70,
        val_ratio=0.15,
    )
