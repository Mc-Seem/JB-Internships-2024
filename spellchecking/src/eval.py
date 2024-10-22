import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from Levenshtein import distance as levenshtein_distance

# 1. Accuracy
def accuracy(correct_word: pd.Series, predicted_word: pd.Series) -> float:
    """
    Calculate the accuracy of the spell checker.
    
    Args:
        correct_word (pd.Series): Series containing the correct words.
        predicted_word (pd.Series): Series containing the predicted words.
        
    Returns:
        float: Accuracy score (proportion of correct predictions).
    """
    correct = np.where(correct_word == predicted_word, 1, 0)
    return accuracy_score(correct, [1] * correct_word.shape[0])

# 2. Precision
def precision(correct_word: pd.Series, predicted_word: pd.Series, original_word: pd.Series) -> float:
    """
    Calculate the precision of the spell checker, focusing on the corrections made.
    
    Precision is the ratio of correct corrections made to the total corrections suggested.
    
    Args:
        correct_word (pd.Series): Series containing the correct words.
        predicted_word (pd.Series): Series containing the predicted words.
        original_word (pd.Series): Series containing the original (possibly misspelled) words.
        
    Returns:
        float: Precision score. Returns 0 if no corrections were made.
    """
    corrections_made = original_word != predicted_word
    correct_corrections = (correct_word == predicted_word) & corrections_made

    if corrections_made.sum() == 0:  # No corrections were made, so precision is undefined
        return 0.0
    
    return correct_corrections.sum() / corrections_made.sum()

# 3. Recall
def recall(correct_word: pd.Series, predicted_word: pd.Series, original_word: pd.Series) -> float:
    """
    Calculate the recall of the spell checker, focusing on correcting misspelled words.
    
    Recall is the ratio of correctly corrected misspelled words to the total misspelled words.
    
    Args:
        correct_word (pd.Series): Series containing the correct words.
        predicted_word (pd.Series): Series containing the predicted words.
        original_word (pd.Series): Series containing the original (possibly misspelled) words.
        
    Returns:
        float: Recall score. Returns 0 if no misspelled words are present.
    """
    misspelled_words = original_word != correct_word
    correct_corrections = (correct_word == predicted_word) & misspelled_words

    if misspelled_words.sum() == 0:  # No misspelled words
        return 0.0
    
    return correct_corrections.sum() / misspelled_words.sum()

# 4. F1-Score
def f1(precision: float, recall: float) -> float:
    """
    Calculate the F1 score, the harmonic mean of precision and recall.
    
    The F1 score balances precision and recall, giving an overall measure of performance.
    
    Args:
        precision (float): The precision score.
        recall (float): The recall score.
        
    Returns:
        float: F1 score. Returns 0 if precision + recall is 0 (to avoid division by zero).
    """
    if precision + recall == 0:
        return 0.0
    return 2 * (precision * recall) / (precision + recall)

# 5. Levenshtein Distance
def avg_levenshtein(correct_word: pd.Series, predicted_word: pd.Series) -> float:
    """
    Calculate the average Levenshtein distance between the correct and predicted words.
    
    Levenshtein distance measures the number of single-character edits required to 
    change the predicted word into the correct word.
    
    Args:
        correct_word (pd.Series): Series containing the correct words.
        predicted_word (pd.Series): Series containing the predicted words.
        
    Returns:
        float: Average Levenshtein distance across all word pairs.
    """
    together = pd.concat([correct_word, predicted_word], axis=1)
    together.columns = ['correct_word', 'predicted_word']
    levenshtein = together.apply(lambda row: levenshtein_distance(row['predicted_word'], row['correct_word']), axis=1)
    return levenshtein.mean()

# 6. Correction Time
def avg_time(correction_time: pd.Series) -> float:
    """
    Calculate the average time taken for word corrections.
    
    Args:
        correction_time (pd.Series): Series containing the correction times for each word.
        
    Returns:
        float: Average correction time.
    """
    return correction_time.mean()
