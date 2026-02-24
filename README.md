# 🎬 Movie Recommender System

A Content-Based Movie Recommender System built using **Python** and **Machine Learning**. This system suggests movies similar to a user's choice by analyzing genres, keywords, cast, crew, and overviews.

---

## 🚀 Project Overview

This project utilizes the **TMDB 5000 Movies Dataset** to build a recommendation engine. Unlike collaborative filtering (which relies on user behavior), this system focuses on the **attributes** of the movies themselves. 

If you like a movie with a specific director or theme, the system identifies other movies with the highest content overlap.

---

## 📂 Dataset Used

The project uses two primary datasets from Kaggle:
* `tmdb_5000_movies.csv`: Contains metadata like budget, genres, and overviews.
* `tmdb_5000_credits.csv`: Contains cast and crew information.

The datasets are merged on the **title** column to create a comprehensive data frame for processing.

---

## 🛠️ Technologies Used

| Category | Tools/Libraries |
| :--- | :--- |
| **Language** | Python |
| **Data Manipulation** | Pandas, NumPy |
| **Machine Learning** | Scikit-learn (CountVectorizer, Cosine Similarity) |
| **NLP** | NLTK (Stemming) |
| **Environment** | Jupyter Notebook |

---

## ⚙️ How It Works

### 1. Data Preprocessing
* **Feature Selection:** We filter for columns that truly define a movie: `movie_id`, `title`, `overview`, `genres`, `keywords`, `cast`, and `crew`.
* **Data Cleaning:** Handled missing values and duplicated entries.
* **JSON Parsing:** Converted string-based list objects (genres, keywords) into usable Python lists.
* **Refinement:** Extracted the **Top 3 cast members** and the **Director** from the crew list.

### 2. Feature Engineering
A unified **"tags"** column is created by concatenating:
* `overview` + `genres` + `keywords` + `cast` + `crew` (Director).

To ensure the model doesn't get confused by spaces in names (e.g., "Sam Worthington" vs "Sam Raimi"), spaces are removed to create unique tokens like "SamWorthington".



[Image of Content-Based Filtering workflow]


### 3. Vectorization & Similarity
* **Stemming:** Applied NLTK's PorterStemmer to reduce words to their root form (e.g., "activities" becomes "activ").
* **Bag of Words:** Used `CountVectorizer` to convert the tags into 5,000-dimensional vectors.
* **Similarity:** Calculated the distance between movie vectors using **Cosine Similarity**. 

The similarity score is calculated as:
$$\text{similarity} = \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}$$

---

## 🎯 Recommendation Function

To get recommendations, simply call the function:

```python
recommend('Avatar')

Output Example:

Aliens

Alien³

Falcon Rising

Star Trek Into Darkness

Titan A.E
