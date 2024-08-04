import random
import string
import csv

# Function to summarize text

def summarize_text(text):
    return f'Text contains {len(text.split())} words and {len(text.splitlines())} lines.'

# Function to compute average from CSV

def compute_average_from_csv(file_path, column_index):
    total = 0
    count = 0
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            if row:
                total += float(row[column_index])
                count += 1
    return total / count if count > 0 else 0

# Function to generate random password

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Main function to execute all functionalities

def main():
    # Sample text summarization
    sample_text = "This is a sample text file. It contains a few lines of text to demonstrate the summarization function."
    print('Text Summary:', summarize_text(sample_text))

    # CSV average computation
    average = compute_average_from_csv('data.csv', 1)
    print(f'Average score from CSV: {average}')

    # Random password generation
    password = generate_random_password(12)
    print('Generated Password:', password)

if __name__ == '__main__':
    main()