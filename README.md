# Phishing URL Detection

A machine learning project that classifies URLs as **Phishing** or **Legitimate** using Logistic Regression. Built by Prince Chukwuemeka.

## Overview

This project extracts features from URLs and trains a Logistic Regression model to detect phishing websites. The model achieves ~96% accuracy on the test set.

## Dataset

- **Source:** [Phishing Site URLs - Kaggle](https://www.kaggle.com/datasets/mohamedouledhamed/phishing-site-urls)
- **File:** `phishing_site_urls.csv` (URL, Label columns)
- **Classes:** Phishing (~156k), Legitimate (~393k)

## Features Extracted

| Feature | Description |
|---------|-------------|
| Root domain | Extracted using tldextract |
| URL region | ccTLD to country mapping |
| IP address | Presence of IP in URL |
| Free domain | Hosted on blogspot, github.io, etc. |
| Suspicious words | login, bank, paypal, etc. |
| HTTPS | URL uses SSL |
| Abnormal URL | Hostname present in URL |
| Short URL | URL shortening service |
| Special characters | Count of @, ?, -, etc. |
| URL depth | Path segment count |
| Tokenized text | NLTK tokenization + Snowball stemmer |

## Installation

```bash
# Clone the repository
git clone <repo-url>
cd webDectection_logistic_regress

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

1. **Download the dataset** from [Kaggle](https://www.kaggle.com/datasets/mohamedouledhamed/phishing-site-urls) and place `phishing_site_urls.csv` in the project directory.

2. **Open the notebook** and run all cells:
   ```bash
   jupyter notebook WebDetection_by_Prince_chukwuemeka.ipynb
   ```

3. **First run:** Execute the pip install and NLTK download cells to set up dependencies.

4. **Model output:** The trained pipeline is saved as `train_model.pkl`.

## Project Structure

```
webDectection_logistic_regress/
├── WebDetection_by_Prince_chukwuemeka.ipynb   # Main notebook
├── phishing_site_urls.csv                     # Dataset (download from Kaggle)
├── train_model.pkl                            # Saved model (after training)
├── requirements.txt
└── README.md
```

## Model

- **Algorithm:** Logistic Regression
- **Vectorization:** CountVectorizer with custom regex tokenizer
- **Pipeline:** Text → CountVectorizer → LogisticRegression

## License

MIT
