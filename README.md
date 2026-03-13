# Phishing URL Detection

A machine learning project that classifies URLs as **Phishing** or **Legitimate** using Logistic Regression. 

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

## Image Recognition Feature

The image recognition module provides functionality to analyze images from URLs and extract visual features that may indicate phishing attempts. This module uses a pre-trained MobileNetV2 model from TensorFlow/Keras for image classification.

### Features

1. **Image Download**: Download images from URLs
2. **Image Classification**: Classify images using pre-trained MobileNetV2 (ImageNet)
3. **Feature Extraction**: Extract visual features from images
4. **URL Image Analysis**: Analyze all images from a given URL

### Usage

```python
from image_recognition import ImageRecognizer

# Create an instance of the image recognizer
recognizer = ImageRecognizer()

# Analyze images from a URL
url = "https://example.com"
results = recognizer.analyze_url_images(url, max_images=5)

# Print results
print(f"Total images found: {results['total_images']}")
print(f"Images analyzed: {results['analyzed_images']}")

for i, img_analysis in enumerate(results['images']):
    print(f"\nImage {i + 1}: {img_analysis['url']}")
    print("Classification:")
    for item in img_analysis['classification']:
        print(f"  {item['rank']}. {item['label']} ({item['score']:.2f})")
    print("Features:")
    for key, value in img_analysis['features'].items():
        print(f"  {key}: {value}")
```

### New Requirements

To use the image recognition feature, you need to install additional dependencies:

```bash
pip install tensorflow>=2.10.0
pip install pillow>=9.3.0
```

These dependencies are also included in `requirements.txt`.

## License

MIT
