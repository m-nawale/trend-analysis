import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
import os

# Download NLTK resources if not already present
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize Lemmatizer and Stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Define a function to clean and preprocess text
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Tokenize text
    tokens = word_tokenize(text)
    # Remove stopwords and lemmatize tokens
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return ' '.join(tokens)

def main():
    # Load the dataset
    data_path = os.path.join('..', 'data', '19th_CIRP_Conference_Papers.xlsx')
    df = pd.read_excel(data_path)

    # Preprocess Titles and Abstracts
    df['Processed_Title'] = df['Title'].apply(preprocess_text)
    df['Processed_Abstract'] = df['Abstract'].apply(preprocess_text)

    # Save the preprocessed data
    output_path = os.path.join('..', 'data', 'preprocessed_data.xlsx')
    df.to_excel(output_path, index=False)
    print(f"Preprocessed data saved to {output_path}")

if __name__ == "__main__":
    main()