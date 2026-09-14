\# Fake News Detector



A Python-based news verification tool that checks a news claim against \*\*live news sources and Wikipedia\*\* and provides a simple prediction based on source availability and keyword matching.



\## Features



\* Accepts a news claim through the terminal

\* Extracts important keywords from the user's input

\* Searches for related articles using \*\*NewsAPI\*\*

\* Retrieves relevant information from \*\*Wikipedia\*\*

\* Compares keywords from the claim with retrieved sources

\* Calculates a source-match score

\* Classifies the claim as:



&#x20; \* \*\*Likely REAL\*\*

&#x20; \* \*\*UNCERTAIN\*\*

&#x20; \* \*\*Likely FAKE\*\*

\* Displays the number of sources and processing time



\## How It Works



The program follows a simple verification pipeline:



```text

User enters a news claim

&#x20;         ↓

Keyword extraction

&#x20;         ↓

&#x20;     ┌───────────────┐

&#x20;     ↓               ↓

&#x20;  NewsAPI         Wikipedia

&#x20;     ↓               ↓

&#x20;     └───────┬───────┘

&#x20;             ↓

&#x20;      Source comparison

&#x20;             ↓

&#x20;       Match score

&#x20;             ↓

&#x20;      Final prediction

```



\### 1. Keyword Extraction



The program removes a small set of common stopwords and keeps up to six keywords from the user's input.



\### 2. NewsAPI Search



The extracted keywords are used to search NewsAPI. Up to five related articles are retrieved, using their titles and descriptions as source text.



\### 3. Wikipedia Search



The program also searches Wikipedia and retrieves the summary of the first matching result when available.



\### 4. Source Matching



The keywords from the original news claim are compared against the retrieved sources.



A source contributes to the match score when at least two keywords from the claim are found in that source.



\### 5. Prediction



The final result is based on the number of available news sources and the match score.



| Condition                                   | Prediction  |

| ------------------------------------------- | ----------- |

| No news sources found                       | Likely FAKE |

| Match score ≥ 4 and at least 4 news sources | Likely REAL |

| Match score ≥ 2                             | UNCERTAIN   |

| Otherwise                                   | Likely FAKE |



> \*\*Note:\*\* This is a rule-based verification approach, not a trained machine-learning classifier. The predictions should therefore be treated as an indication rather than definitive fact-checking.



\## Technologies Used



\* \*\*Python\*\*

\* \*\*Requests\*\* — for making NewsAPI requests

\* \*\*Wikipedia\*\* — for retrieving Wikipedia information

\* \*\*Regular Expressions (re)\*\* — for text processing

\* \*\*Time\*\* — for measuring processing time

\* \*\*NewsAPI\*\* — live news source

\* \*\*Wikipedia\*\* — reference source



\## Project Structure



```text

fake\_news\_detector/

│

├── main.py

├── fake\_news\_dataset.csv

├── requirements.txt

└── README.md

```



\## Dataset



The repository includes `fake\_news\_dataset.csv`, containing news-related records with fields including:



\* `title`

\* `text`

\* `date`

\* `source`

\* `author`

\* `category`

\* `label`



The current `main.py` does \*\*not\*\* train a machine-learning model using this dataset. The dataset is included as part of the project for reference and potential future development.



\## Installation



Clone the repository:



```bash

git clone https://github.com/trina-shihi/fake\_news\_detector.git

cd fake\_news\_detector

```



Install the required Python packages:



```bash

pip install -r requirements.txt

```



\## NewsAPI Setup



This project requires a NewsAPI key.



1\. Create an account on NewsAPI.

2\. Obtain your API key.

3\. Open `main.py`.

4\. Replace:



```python

NEWS\_API\_KEY = "YOUR\_API\_KEY"

```



with your own API key.



\*\*Do not commit your personal API key to GitHub.\*\*



\## Running the Project



Run:



```bash

python main.py

```



The program will ask:



```text

Enter news (or type exit):

```



Enter a news claim to analyze.



To stop the program, type:



```text

exit

```



\## Example



```text

Enter news (or type exit): A major event happened today



===== RESULT =====

DEBUG API STATUS: ok

DEBUG Articles Found: 5

Total Sources: 6

Prediction: ⚠️ UNCERTAIN

Match Score: 3

Time Taken: 1.234 sec

```



\*The output will vary depending on the news query and currently available sources.\*



\## Limitations



\* The system relies on the availability of external sources.

\* Lack of news coverage does not necessarily mean that a claim is fake.

\* Keyword matching can produce false positives or false negatives.

\* Wikipedia results depend on the quality and availability of matching pages.

\* The system does not perform semantic or deep factual verification.

\* Results can change as live news sources change.



\## Future Improvements



\* Train and integrate a machine-learning model using the included dataset

\* Use TF-IDF or transformer-based text representations

\* Improve semantic similarity between claims and sources

\* Add more reliable fact-checking sources

\* Develop a graphical or web-based interface

\* Add confidence scores

\* Improve source ranking and verification logic

\* Add automated evaluation using the provided dataset



\## License



This project is intended for educational and learning purposes.



