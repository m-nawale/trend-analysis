import os
import gensim
import pyLDAvis
import pyLDAvis.gensim

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
    # Load model and dictionary
    lda_model, dictionary = load_model_and_dictionary()

    # Prepare the visualization
    vis_data = prepare_visualization(lda_model, dictionary)

    # Save the visualization to an HTML file
    vis_path = os.path.join('..', 'data', 'lda_visualization.html')
    pyLDAvis.save_html(vis_data, vis_path)

    print(f"Visualization saved to {vis_path}")
    print("Open the HTML file in a browser to explore the topics interactively.")

if __name__ == "__main__":
    main()