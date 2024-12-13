# Trend Analysis in Machining

This project performs topic modeling on research papers to analyze trends in machining. Using natural language processing (NLP) techniques, the project extracts insights from titles, abstracts, and keywords provided in the dataset.

---

## Getting Started

### Installation

1. Clone this repository:
   ```bash
   git clone https://gitlab.kit.edu/mnawale/trend_analysis.git
Navigate to the project directory:

bash
Copy code
cd trend_analysis
Create and activate a virtual environment:

bash
Copy code
python -m venv trend_env
trend_env\Scripts\activate  # On Windows
source trend_env/bin/activate  # On macOS/Linux
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Dataset
The dataset consists of research papers related to machining. It includes the following columns:

Title: The title of the paper.
Authors: The authors of the paper.
Abstract: The abstract of the paper.
DOI: The DOI of the paper.
Ensure the dataset file 19th_CIRP_Conference_Papers.xlsx is placed in the data/ folder before running the scripts.

Project Workflow
1. Preprocessing
The preprocessing.py script cleans and prepares the dataset for topic modeling. The following steps are performed:

Convert all text to lowercase.
Remove special characters, numbers, and punctuation.
Tokenize the text into individual words.
Remove stopwords (e.g., "the," "and," "is").
Lemmatize words to their base form (e.g., "running" → "run").
Output:

A preprocessed dataset saved as preprocessed_data.xlsx in the data/ folder, with two new columns:
Processed_Title
Processed_Abstract
2. Topic Modeling
The topic_modeling.py script uses the Latent Dirichlet Allocation (LDA) algorithm to extract topics from the preprocessed dataset.

Steps:

Combine the Processed_Title and Processed_Abstract columns into a single text field.
Create a dictionary and corpus for the text data.
Apply the LDA algorithm to extract topics.
Output:

Topics and their associated keywords displayed in the terminal.
The trained LDA model and dictionary saved in the data/ folder.
3. Visualization
The visualization.py script uses PyLDAvis to create an interactive visualization of the topics.

Steps:

Load the LDA model and dictionary.
Generate a PyLDAvis visualization.
Save the visualization as lda_visualization.html in the data/ folder.
Output:

An interactive HTML file (lda_visualization.html) that allows exploration of the topics.
Project Structure
bash
Copy code
trend_analysis/
│
├── data/                      # Contains the input dataset and output files
│   ├── 19th_CIRP_Conference_Papers.xlsx
│   ├── preprocessed_data.xlsx
│   ├── lda_model
│   ├── dictionary
│   ├── lda_visualization.html
├── notebooks/                 # Jupyter notebooks for exploratory analysis
├── src/                       # Source code for the project
│   ├── preprocessing.py       # Text preprocessing
│   ├── topic_modeling.py      # Topic modeling
│   ├── visualization.py       # Visualization scripts
├── tests/                     # Unit tests for the scripts
├── README.md                  # Project documentation
├── requirements.txt           # List of dependencies
└── main.py                    # Main script to run the project
How to Run
Preprocess the dataset:

bash
Copy code
python src/preprocessing.py
Extract topics using LDA:

bash
Copy code
python src/topic_modeling.py
Visualize the topics:

bash
Copy code
python src/visualization.py
Open the visualization in a browser:

bash
Copy code
data/lda_visualization.html
Future Enhancements
Add advanced visualization tools for better topic interpretation.
Experiment with other topic modeling algorithms like BERTopic.
Create a dashboard for real-time topic analysis.
License
This project is licensed under the MIT License. See LICENSE for details.

Contact
For questions or feedback, reach out at:

Email: your-email@example.com
GitLab Profile: mnawale
yaml
Copy code

---

### **Steps to Update the README**
1. Open the `README.md` file in VS Code.
2. Replace its current content with the finalized content above.
3. Save the file (`Ctrl+S` or `Cmd+S`).

---

### **Commit and Push the Changes**
1. Stage the changes:
   ```bash
   git add README.md
Commit the changes:

bash
Copy code
git commit -m "Finalized README.md with complete project details"
Push to the remote repository:

bash
Copy code
git push