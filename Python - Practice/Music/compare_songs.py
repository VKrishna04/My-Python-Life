import csv


# Function to read songs from yt.md
def read_yt_songs(filepath):
    yt_songs = set()
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip() and not line.strip().isdigit() and ":" not in line:
                yt_songs.add(line.strip())
    return yt_songs


# Function to read songs from prime.csv
def read_prime_songs(filepath):
    prime_songs = set()
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            prime_songs.add(row[0].strip())
    return prime_songs


# Main function to compare songs
def compare_songs(yt_filepath, prime_filepath):
    yt_songs = read_yt_songs(yt_filepath)
    prime_songs = read_prime_songs(prime_filepath)

    # Debug print statements
    print("YT Songs:", yt_songs)
    print("Prime Songs:", prime_songs)

    # Songs in prime.csv but not in yt.md
    unique_prime_songs = prime_songs - yt_songs

    print("Songs in prime.csv but not in yt.md:")
    for song in unique_prime_songs:
        print(song)


# File paths
yt_filepath = "/V:/Code/My Python Life/Python - Practice/Music/yt.md"
prime_filepath = "/V:/Code/My Python Life/Python - Practice/Music/prime.csv"

# Compare songs
compare_songs(yt_filepath, prime_filepath)
