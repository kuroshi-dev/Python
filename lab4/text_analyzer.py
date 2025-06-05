def find_sequences(text, min_words=3, min_repeats=5, max_words=7):
    """
    Find repeated sequences of words in text with memory optimization.

    Args:
        text (str): Input text to analyze
        min_words (int): Minimum words in sequence
        min_repeats (int): Minimum repetitions required
        max_words (int): Maximum words in sequence to limit memory usage

    Returns:
        dict: Sequences and their counts
    """
    words = text.lower().split()
    sequences = {}
    total_words = len(words)

    for length in range(min_words, min(max_words + 1, total_words)):
        for i in range(total_words - length + 1):
            sequence = ' '.join(words[i:i + length])

            if sequence in sequences and sequences[sequence] < 0:
                continue

            count = 0
            for j in range(total_words - length + 1):
                if ' '.join(words[j:j + length]) == sequence:
                    count += 1
                    if count >= min_repeats:
                        sequences[sequence] = count
                        break

            if count < min_repeats:
                sequences[sequence] = -1

    return {seq: count for seq, count in sequences.items() if count > 0}

def analyze_text(file_path):
    try:
        chars_with_spaces = 0
        chars_without_spaces = 0
        words = []
        
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                chars_with_spaces += len(line)
                chars_without_spaces += len(line.strip())

                line_words = [word.strip('.,!?:;()[]{}«»—-"\'') 
                            for word in line.lower().split()]
                words.extend([w for w in line_words if w])

        word_frequency = {}
        for word in words:
            word_frequency[word] = word_frequency.get(word, 0) + 1

        text = ' '.join(words)
        repeated_sequences = find_sequences(text, max_words=7)
        
        return {
            'chars_with_spaces': chars_with_spaces,
            'chars_without_spaces': chars_without_spaces,
            'total_words': len(words),
            'unique_words': len(set(words)),
            'single_occurrence': sum(1 for count in word_frequency.values() if count == 1),
            'repeated_sequences': repeated_sequences
        }
            
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def main():
    file_path = 'book.txt'
    
    results = analyze_text(file_path)
    if results:
        print("Text Analysis Results:")
        print("-" * 50)
        print(f"Characters (with spaces): {results['chars_with_spaces']}")
        print(f"Characters (without spaces): {results['chars_without_spaces']}")
        print(f"Total words: {results['total_words']}")
        print(f"Unique words: {results['unique_words']}")
        print(f"Words occurring once: {results['single_occurrence']}")
        
        print("\nRepeated sequences (>3 words, >5 times):")
        print("-" * 50)
        
        sequences = results['repeated_sequences']
        if sequences:
            # Show only top 20 most frequent sequences
            sorted_sequences = sorted(sequences.items(),
                                   key=lambda x: (-x[1], x[0]))[:20]
            for sequence, count in sorted_sequences:
                print(f"Occurrences: {count}")
                print(f"Sequence: {sequence}")
                print("-" * 30)
        else:
            print("No sequences matching the criteria found")

if __name__ == "__main__":
    main()