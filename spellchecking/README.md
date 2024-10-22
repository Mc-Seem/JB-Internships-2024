#JetBrains 

>**This section hosts my solution for Task 2 of the Spellchecking assignment by JetBrains.**

I hereby provide a list of my chosen spellcheckers and evaluation methods, with a brief explanation. I also attach a table with ready results.

### Spellchecking tool selection

In my work, I have mostly considered spellcheckers that can correct a word without knowing the context. This is due to difficulties during experimenting phase, when I found out most of more sophisticated tools with context window require much more compute and are often more vague with their predictions. Limiting the scope has also enabled me to gather a bigger evaluation dataset.

- **PySpellChecker**: A basic spellchecker that uses a frequency-based dictionary to suggest corrections.
- **SymSpellPy**: A fast, memory-efficient spellchecker that uses precompiled edit-distance dictionaries.
- **PyEnchant**: A wrapper for the Enchant spellchecking library that supports multiple languages and dictionaries.
- **TextBlob**: A simple text-processing library with built-in spellchecking functionality.
- **LanguageTool**: A more sophisticated grammar and spellchecking tool that works across multiple languages and can handle basic context.

### Evaluation metric selection

- **Accuracy**
	- A typical metric for classification problems in ML. In our case, it allows us to measure how many times the word was correct exactly as it should have been.
- **Precision**
	- Reflects how many of the corrected words were truly incorrect. It’s crucial for a spellchecker to avoid changing words that were already correct, which this metric captures.
- **Recall**
	- Indicates how many of the misspelled words were successfully corrected. It helps measure the tool's effectiveness in identifying and correcting errors.
- **F1 Score**
	- Simply the harmonic mean of precision and recall. This metric provides a balance between precision and recall, offering a single measure of overall performance.
- **Levenshtein distance**
	- Measures the similarity between the suggested word and the correct word by counting the minimum number of edits (insertions, deletions, or substitutions) required to change one word into the other. A lower Levenshtein distance indicates a closer match.
- **Correction time**
	- Measures the average time taken to propose a correction. This is critical for user experience, as users typically expect instant feedback from their spellchecker.

### Results

| Spellchecker   | Accuracy | Precision | Recall   | F1       | Avg. Levenshtein | Avg. Time |
| -------------- | -------- | --------- | -------- | -------- | ---------------- | --------- |
| PySpellChecker | 0.450793 | 0.400328  | 0.358359 | 0.378183 | 2.456240         | 0.135717  |
| SymSpellPy     | 0.454041 | 0.474363  | 0.355447 | 0.406385 | 1.838465         | 0.000058  |
| PyEnchant      | 0.429972 | 0.373253  | 0.331930 | 0.351381 | 2.052495         | 0.024769  |
| TextBlob       | 0.411412 | 0.435170  | 0.321383 | 0.369720 | 1.916735         | 0.086484  |
| LanguageTool   | 0.457597 | 0.421233  | 0.366827 | 0.392152 | 1.901484         | 0.024247  |

### Conclusion

In accordance with the table provided above, I hereby conclude that the best spellchecking tool from the selection is SymSpellPy. It is considerably faster than its competitors, while providing the closest result to the correct word. Its precision and recall are the highest among the group, and the accuracy is on par with LanguageTool.

##### Post-work thoughts

Regardless of the outcome of this submission, thank you for allowing to work on this project and for the time spent assessing it. It has been great fun to explore this side of NLP.

