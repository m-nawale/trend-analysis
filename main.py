import nltk

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("punkt_tab")

from src.preprocessing import main as preprocess_main
from src.topic_modeling import main as topic_modeling_main
from src.visualization import main as visualization_main

def main():
    print("Starting the Trend Analysis Project...")

    # Step 1: Preprocessing
    print("\nStep 1: Preprocessing")
    preprocess_main()

    # Step 2: Topic Modeling
    print("\nStep 2: Topic Modeling")
    topic_modeling_main()

    # Step 3: Visualization
    print("\nStep 3: Visualization")
    visualization_main()

    print("\nAll steps completed successfully!")

if __name__ == "__main__":
    main()