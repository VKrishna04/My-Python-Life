import pandas as pd
import os

# Get the current working directory
current_directory = os.getcwd()
print("Current Directory:", current_directory)

# Load the prime.csv file
prime_csv_path = os.path.join(current_directory, "prime.csv")
if not os.path.exists(prime_csv_path):
    raise FileNotFoundError(f"The file '{prime_csv_path}' does not exist.")

prime_df = pd.read_csv(
    prime_csv_path,
    delimiter="\t",
    header=None,
    names=["Title", "Artist", "Album", "Duration"],
)

# Load the yt.md file
yt_md_path = os.path.join(current_directory, "yt.md")
if not os.path.exists(yt_md_path):
    raise FileNotFoundError(f"The file '{yt_md_path}' does not exist.")

with open(yt_md_path, "r") as file:
    yt_content = file.read()

# Extract track titles from yt.md
yt_titles = []
for line in yt_content.split("\n"):
    if line.strip() and not line.startswith(
        (
            " ",
            "\t",
            "&",
            "(",
            "[",
            "]",
            "•",
            "feat.",
            "Explicit",
            "Original",
            "Motion",
            "Picture",
            "Soundtrack",
            "Lyrics",
        )
    ):
        yt_titles.append(line.strip())

# Extract track titles from prime.csv
prime_titles = prime_df["Title"].tolist()

# Find the difference
tracks_not_in_yt = [title for title in prime_titles if title not in yt_titles]

# Print the tracks that are in prime.csv but not in yt.md
print("Tracks in prime.csv but not in yt.md:")
for track in tracks_not_in_yt:
    print(track)
