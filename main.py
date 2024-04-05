def letter_count(text):
    letter_counts = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
    return letter_counts


def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
        print(f"--- Begin Report of {file_path} ---")
        print(f"Total number of words: {len(file_contents.split())}.")
        letter_counts = letter_count(file_contents)
        sorted_letter_counts = sorted(
            letter_counts.items(), key=lambda x: x[1], reverse=True
        )

        for letter, count in sorted_letter_counts:
            print(
                f"The '{letter}' character was found {count} times.")
        print("--- End Report ---")


main()
