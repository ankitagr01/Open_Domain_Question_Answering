# Open_Domain_Question_Answering
Build a statistical or deep neural model for Question Answering either utilizing both the provided Wikidata Knowledge Graph and Wikipedia Text Corpus or just a single knowledge source. Any existing methods/libraries could be utilized. In this project, I have implemented an End-to-End Memory Net using Keras. Later, trained the model for 100 epochs on Facebook's bAbI dataset which has 1000 questions for training and 1000 for test. Also, the dataset has an array of text passages ranging from Single Fact Evidence to Multihop Reasoning based corpus.

# Execution Instructions
Clone the repository
Install the project dependencies: "pip install -r requirements.txt"
In the "qa_model.py" file set the hyperparameters (lstm_size, epochs, batch size, model type) accordingly.
Run the model: "python qa_model.py"
Assess model performance using the test questions in Test Questions file

# Author
Ankit Agrawal
