import pandas as pd
import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
from Levenshtein import distance as levenshtein_distance

# 1. Accuracy
def accuracy(correct_word, predicted_word) -> float:
    """
    Calculate the accuracy of the spell checker.
    
    Args:
        df (pd.DataFrame): DataFrame containing 'correct_word' and 'predicted_word'.
        
    Returns:
        float: Accuracy score.
    """
    correct = np.where(correct_word == predicted_word, 1, 0)
    return accuracy_score(correct, [1] * correct_word.shape[0])


# 2. Precision
def precision(correct_word, predicted_word, original_word) -> float:
    corrections_made = original_word != predicted_word
    correct_corrections = (correct_word == predicted_word) & corrections_made

    if corrections_made.sum() == 0:  # No corrections were made, so precision is undefined
        return 0
    
    return correct_corrections.sum() / corrections_made.sum()



# 3. Recall
def recall(correct_word, predicted_word, original_word) -> float:
    misspelled_words = original_word != correct_word
    correct_corrections = (correct_word == predicted_word) & misspelled_words

    if misspelled_words.sum() == 0:  # No misspelled words
        return 0
    
    return correct_corrections.sum() / misspelled_words.sum()



# 4. F1-Score
def f1(precision, recall) -> float:
    """
    Calculate the F1 score of the spell checker.
    
    Args:
        df (pd.DataFrame): DataFrame containing 'correct_word' and 'predicted_word'.
        
    Returns:
        float: F1 score.
    """
    return 2 * (precision * recall) / (precision + recall)


# 5. Levenshtein Distance
def avg_levenshtein(correct_word, predicted_word) -> float:
    """
    Calculate the average Levenshtein distance between the correct words and predicted words.
    
    Args:
        df (pd.DataFrame): DataFrame containing 'correct_word' and 'predicted_word'.
        
    Returns:
        float: Average Levenshtein distance.
    """
    together = pd.concat([correct_word, predicted_word], axis=1)
    together.columns = ['correct_word', 'predicted_word']
    levenshtein = together.apply(lambda row: levenshtein_distance(row['predicted_word'], row['correct_word']), axis=1)
    return levenshtein.mean()


# 6. Correction Time
def avg_time(correction_time) -> float:
    """
    Calculate the average correction time.
    
    Args:
        df (pd.DataFrame): DataFrame containing 'correction_time'.
        
    Returns:
        float: Average correction time.
    """
    return correction_time.mean()
