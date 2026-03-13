# Phishing URL Detection

A machine learning project that classifies URLs as **Phishing** or **Legitimate** using Logistic Regression. The project achieves ~96% accuracy on the test set.

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Features Extracted](#features-extracted)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model](#model)
- [Evaluation](#evaluation)
- [License](#license)

## Overview

This project implements a phishing URL detection system using machine learning techniques. It extracts relevant features from URLs and trains a Logistic Regression model to classify them as phishing or legitimate. The system is designed to be easy to use and provides high accuracy in detecting malicious URLs.

## Dataset

- **Source:** [Phishing Site URLs - Kaggle](https://www.kaggle.com/datasets/mohamedouledhamed/phishing-site-urls)
- **File:** `phishing_site_urls.csv` (contains URL and Label columns)
- **Classes:** 
  - Phishing: ~156,422 URLs
  - Legitimate: ~392,924 URLs
- **Total Samples:** ~549,346 URLs

## Features Extracted

The following features are extracted from each URL to train the model:

| Feature | Description |
|---------|-------------|
| Root domain | Extracted using tldextract library |
| URL region | Country mapping using ccTLD (Country Code Top-Level Domain) |
| IP address | Presence of IP address in the URL |
| Free domain | Hosted on free platforms like blogspot, github.io, etc. |
| Suspicious words | Contains words like login, bank, paypal, etc. |
| HTTPS | Whether the URL uses SSL encryption |
| Abnormal URL | Hostname is present in the URL path |
| Short URL | Created using URL shortening services |
| Special characters | Count of special characters (@, ?, -, etc.) |
| URL depth | Number of path segments in the URL |
| Tokenized text | NLTK tokenization with Snowball stemmer |

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Steps

```bash
# Clone the repository
git clone <repo-url>
cd webDectection_logistic_regress

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

1. **Download the dataset** from [Kaggle](https://www.kaggle.com/datasets/mohamedouledhamed/phishing-site-urls) and place `phishing_site_urls.csv` in the project directory.

2. **Open the Jupyter notebook** and run all cells:
   ```bash
   jupyter notebook WebDetection_by_Prince_chukwuemeka.ipynb
   ```

3. **First run setup:** Execute the pip install and NLTK download cells to set up dependencies.

4. **Model output:** The trained pipeline is saved as `train_model.pkl`.

## Project Structure

```
webDectection_logistic_regress/
├── WebDetection_by_Prince_chukwuemeka.ipynb   # Main notebook with complete workflow
├── phishing_site_urls.csv                     # Dataset (download from Kaggle)
├── train_model.pkl                            # Saved model (after training)
├── requirements.txt                           # Project dependencies
└── README.md                                  # Project documentation
```

## Model

- **Algorithm:** Logistic Regression
- **Vectorization:** CountVectorizer with custom regex tokenizer
- **Pipeline:** Text → CountVectorizer → LogisticRegression
- **Accuracy:** ~96% on test set

## Evaluation

The model is evaluated using standard classification metrics:

- **Accuracy:** 96%
- **Precision:** High for both classes
- **Recall:** High for both classes
- **F1-Score:** Balanced performance

A detailed classification report and confusion matrix are available in the Jupyter notebook.

## License

MIT License

## Contributors

- Prince Chukwuemeka
