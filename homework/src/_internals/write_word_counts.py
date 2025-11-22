import os

def write_count_words(counter):
    # create the directory output/ if it doesn't exist
    output_dir = "data/output/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # write the word counts to a file
    output_file = os.path.join(output_dir, "results.tsv")
    with open(output_file, "w", encoding="utf-8") as f:
        for key, value in sorted(counter.items()):
            f.write(f"{key}\t{value}\n")