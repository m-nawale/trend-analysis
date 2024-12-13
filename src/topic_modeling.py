import pandas as pd
import gensim
from gensim import corpora
from gensim.models.ldamodel import LdaModel
import os

def load_preprocessed_data():
    """Load the preprocessed dataset."""
    data_path = os.path.join('..', 'data', 'preprocessed_data.xlsx')
    df = pd.read_excel(data_path)
    return df['Processed_Title'] + " " + df['Processed_Abstract']

def prepare_corpus(texts):
    """Prepare dictionary and corpus for LDA model."""
    # Tokenize the text
    tokenized_texts = [text.split() for text in texts]

    # Create a dictionary
    dictionary = corpora.Dictionary(tokenized_texts)

    # Filter out extreme cases (rare and common words)
    dictionary.filter_extremes(no_below=2, no_above=0.5)

    # Create a corpus (bag of words representation)
    corpus = [dictionary.doc2bow(text) for text in tokenized_texts]

    return dictionary, corpus

def build_lda_model(corpus, dictionary, num_topics=5):
    """Build and train the LDA model."""
    lda_model = LdaModel(
        corpus=corpus,
        id2word=dictionary,
        num_topics=num_topics,
        random_state=42,
        passes=10,
        alpha='auto',
        per_word_topics=True
    )
    return lda_model

def display_topics(lda_model, dictionary, num_words=10):
    """Display the topics and their associated keywords."""
    topics = lda_model.print_topics(num_words=num_words)
    for topic in topics:
        print(f"Topic {topic[0]}: {topic[1]}")

def main():
    # Load the preprocessed data
    texts = load_preprocessed_data()

    # Prepare the dictionary and corpus
    dictionary, corpus = prepare_corpus(texts)

    # Build the LDA model
    lda_model = build_lda_model(corpus, dictionary)

    # Display the topics
    print("\nTopics Identified:")
    display_topics(lda_model, dictionary)

    # Save the model and dictionary
    model_path = os.path.join('..', 'data', 'lda_model')
    dictionary_path = os.path.join('..', 'data', 'dictionary')
    lda_model.save(model_path)
    dictionary.save(dictionary_path)
    print(f"\nLDA model and dictionary saved to {model_path} and {dictionary_path}")

if __name__ == "__main__":
    main()
