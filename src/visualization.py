import os
import pandas as pd
import pyLDAvis
import pyLDAvis.gensim_models
from gensim.models.ldamodel import LdaModel
from gensim.corpora import Dictionary

def load_model_and_dictionary():
    """Load the LDA model and dictionary."""
    model_path = os.path.join('..', 'data', 'lda_model')
    dictionary_path = os.path.join('..', 'data', 'dictionary')

    lda_model = gensim.models.LdaModel.load(model_path)
    dictionary = gensim.corpora.Dictionary.load(dictionary_path)

    return lda_model, dictionary

def prepare_visualization(lda_model, dictionary):
    """Prepare data for PyLDAvis."""
    corpus = [dictionary.doc2bow(text.split()) for text in dictionary.values()]
    vis_data = pyLDAvis.gensim.prepare(lda_model, corpus, dictionary)
    return vis_data

def main():
    # Dynamically resolve the base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(BASE_DIR, 'data')

    # Load the LDA model and dictionary
    model_path = os.path.join(data_dir, 'lda_model')
    dictionary_path = os.path.join(data_dir, 'dictionary')

    print("Loading the LDA model and dictionary...")
    lda_model = LdaModel.load(model_path)
    dictionary = Dictionary.load(dictionary_path)

    # Load the corpus
    preprocessed_data_path = os.path.join(data_dir, 'preprocessed_data.xlsx')
    df = pd.read_excel(preprocessed_data_path)
    tokenized_text = [text.split() for text in df['Processed_Title'] + ' ' + df['Processed_Abstract']]
    corpus = [dictionary.doc2bow(text) for text in tokenized_text]

    # Generate the visualization
    print("Generating visualization...")
    vis = pyLDAvis.gensim_models.prepare(lda_model, corpus, dictionary)
    vis_path = os.path.join(data_dir, 'lda_visualization.html')
    pyLDAvis.save_html(vis, vis_path)

    print(f"Visualization saved to {vis_path}")
    print("Open the HTML file in a browser to explore the topics interactively.")

if __name__ == "__main__":
    main()