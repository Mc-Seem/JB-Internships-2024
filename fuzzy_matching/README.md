# Short Report

>Thank you for letting me work on this project. Regardless of the outcome, it has been a pleasure to read up on different similarity metrics and fuzzy matching in general.
>
>Below you may find a short report with explanation of my similarity metric choice, and some edge cases that were suggested to consider in the assignment.
>
>You may find the code itself in `main.ipynb`
### Similarity Metric Choice

For this small project, I find Jaro-Winkler similarity metric most applicable to company names for several reasons:
- **Attention to beginnings** - Winkler's addition of prefix scale to Jaro similarity metric favors strings that are similar in the beginning, rather than the end.
	- This way, "Aboba" and "Aboba Incorporated" will have similarity rating of $0.856$ even without the preprocessing, and this is what we desire.
- **Tolerance for Small Variations** - it handles minor spelling differences well, making it robust for cases where punctuation, spacing, or abbreviations (like "Co." vs. "Company") differ slightly between entries.

### Bonus: edge cases

The one edge case I noticed was full company name abbreviations. An example from my notebook would be "Procter & Gamble Co." and "P&B Co."

There are several viable approaches that I see for this case:
- During standardization phase, propose possible abbreviations to each full company name from `list_A` and check similarities with them too.
	- One of the drawbacks of such approach is that, for instance, some companies may share abbreviations if we try to do it automatically.
	- Another is that instead of receiving a ready-to-sort list of similarities we will be provided with a *set* of lists of similarities (similarity with original name and with all kinds of abbreviations that we produce), that are non-trivial to compile, since we do not know, which to give priority.
- Introduce a dictionary of known company abbreviations (and apply it during standardization)
	- This is an approach that loses us nothing, but helps eliminate mistakes with the most famous companies. For example it would translate "IBM" to "International Business Machines".
	- However, during market research, one may also deal with smaller, less known organizations, and this approach provides no solution for them.