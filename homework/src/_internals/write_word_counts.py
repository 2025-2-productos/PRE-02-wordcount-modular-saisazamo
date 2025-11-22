import os

def write_count_words(counter, output_folder):
    # create the directory output/ if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # write the word counts to a file
    output_path = os.path.join(output_folder, "wordcount.tsv")
    with open(output_path, "w", encoding="utf-8") as f:
        for key, value in sorted(counter.items()):
            f.write(f"{key}\t{value}\n")