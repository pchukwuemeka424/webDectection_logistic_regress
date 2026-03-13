import os
import io
import requests
from PIL import Image
import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
from bs4 import BeautifulSoup
import urllib.parse


class ImageRecognizer:
    """Class for image recognition and analysis"""
    
    def __init__(self):
        self.model = MobileNetV2(weights='imagenet', include_top=True)
    
    def download_image(self, url, save_path=None):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            img = Image.open(io.BytesIO(response.content)).convert('RGB')
            
            if save_path:
                os.makedirs(os.path.dirname(save_path) or '.', exist_ok=True)
                img.save(save_path)
            
            return img
        except Exception as e:
            print(f"Error downloading image: {e}")
            return None
    
    def classify_image(self, img):
        try:
            img = img.resize((224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            preprocessed = preprocess_input(img_array)
            predictions = self.model.predict(preprocessed, verbose=0)
            decoded = decode_predictions(predictions, top=5)[0]
            
            results = []
            for i, (imagenet_id, label, score) in enumerate(decoded):
                results.append({
                    'rank': i + 1,
                    'class_id': imagenet_id,
                    'label': label,
                    'score': float(score)
                })
            return results
        except Exception as e:
            print(f"Error classifying image: {e}")
            return []
    
    def extract_image_features(self, img):
        features = {}
        features['width'], features['height'] = img.size
        features['aspect_ratio'] = features['width'] / features['height']
        
        img_array = np.array(img)
        features['mean_red'] = np.mean(img_array[:, :, 0])
        features['mean_green'] = np.mean(img_array[:, :, 1])
        features['mean_blue'] = np.mean(img_array[:, :, 2])
        features['std_red'] = np.std(img_array[:, :, 0])
        features['std_green'] = np.std(img_array[:, :, 1])
        features['std_blue'] = np.std(img_array[:, :, 2])
        
        brightness = np.mean(img_array)
        features['is_bright'] = brightness > 240
        features['is_dark'] = brightness < 15
        
        return features
    
    def analyze_url_images(self, url, max_images=5):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            img_tags = soup.find_all('img', src=True)
            
            results = {'total_images': len(img_tags), 'analyzed_images': 0, 'images': []}
            
            for i, img_tag in enumerate(img_tags[:max_images]):
                img_url = img_tag['src']
                if not img_url.startswith('http'):
                    img_url = urllib.parse.urljoin(url, img_url)
                
                img = self.download_image(img_url)
                if img:
                    analysis = {
                        'url': img_url,
                        'classification': self.classify_image(img),
                        'features': self.extract_image_features(img)
                    }
                    results['images'].append(analysis)
                    results['analyzed_images'] += 1
            
            return results
        except Exception as e:
            print(f"Error analyzing images from {url}: {e}")
            return {'error': str(e)}


def main():
    print("Image Recognition Module")
    print("=" * 30)
    
    recognizer = ImageRecognizer()
    test_url = "https://example.com"
    print(f"\nAnalyzing images from: {test_url}")
    
    results = recognizer.analyze_url_images(test_url)
    
    if 'error' in results:
        print(f"Error: {results['error']}")
    else:
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


if __name__ == "__main__":
    main()
