import pandas as pd
import re

def parse_birkbeck(file_path: str, counted: bool=False) -> pd.DataFrame:
    """
    Parse the Birkbeck Spelling Error Corpus into a pandas DataFrame.

    Args:
        file_path (str): Path to the Birkbeck Corpus file.

    Returns:
        pd.DataFrame: DataFrame with two columns: 'misspelled_word' and 'correct_word'.
    """
    data = []
    correct_word = None
    
    typo_pattern = re.compile(r'(.+) \d+')
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('$'):
                correct_word = line[1:]  # Remove the '$'
            elif correct_word:
                if counted:
                    line = typo_pattern.match(line).group(1)
                data.append([line, correct_word])

    df = pd.DataFrame(data, columns=['misspelled_word', 'correct_word'])

    return df
