# Sentiment-Analysis-on-Movie-Reviews

I developed this Python script to perform **sentiment analysis on IMDb movie reviews** using **Logistic Regression**. The goal was to classify reviews as **Positive, Negative, or Neutral** by applying machine learning techniques. 

### Steps Involved:

1. **Loading the Dataset** – I imported a CSV file containing thousands of labeled movie reviews.
2. **Text Preprocessing** – The raw text was cleaned by converting it to lowercase, removing numbers, punctuation, and stopwords to ensure only meaningful words remained.
3. **Feature Extraction with TF-IDF** – I used **TF-IDF (Term Frequency-Inverse Document Frequency) Vectorization** to convert the cleaned text into numerical feature vectors, which measure the importance of words in each review relative to the entire dataset.
4. **Splitting the Data** – The dataset was divided into **training and testing sets** to evaluate model performance.
5. **Training the Model** – I used **Logistic Regression**, a widely used classification algorithm, to train the model on labeled data.
6. **Evaluating the Model** – The model was tested on unseen data to measure its accuracy and effectiveness in differentiating between sentiments.
7. **Creating a Prediction Function** – I wrote a function to process new movie reviews and predict their sentiment using the trained model.

### Results and Applications:

After training, the model achieved a reasonable accuracy score, demonstrating its ability to classify reviews effectively. To showcase its functionality, I included a **sample review** and displayed its predicted sentiment. 

This script can be applied to **automated review analysis, social media monitoring, or customer feedback classification**. Future improvements could include experimenting with different machine learning models, increasing the dataset size, or refining text preprocessing techniques. With further optimizations, it could serve as the foundation for advanced **Natural Language Processing (NLP) applications**.

This project was an exciting way to apply machine learning techniques to text data and build a practical sentiment analysis model. 
