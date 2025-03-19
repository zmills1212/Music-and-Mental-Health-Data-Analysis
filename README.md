# Music and Mental Health: An Exploratory Data Analysis

This project investigates the correlation between music listening habits and various mental health indicators, using a dataset from Kaggle. 
The goal is to explore the role music plays in an individual's quality of life and overall mental well-being, specifically focusing on its impact on stress, anxiety, depression, and other related attributes.

## Dataset

The dataset used in this analysis is the "MXMH Survey Results" dataset available on Kaggle: [https://www.kaggle.com/datasets/catherinerasgaitis/mxmh-survey-results](https://www.kaggle.com/datasets/catherinerasgaitis/mxmh-survey-results)

This dataset includes information on:

* Music genres listened to
* Levels of depression, anxiety, and OCD
* Age
* Hours of music listening per day
* And other relevant mental health attributes

## Research Questions

1. How much does music play a role in a person's quality of life and overall mental health?
2. How does the duration of music listening throughout the day affect one's mental health?  Does listening to more music improve or decrease different mental health indicators?
3. What is the relationship between hours of music listened to and mental health rankings (high vs. low)?
4. What is the age range of the participants in this study?

## Methodology

This analysis was conducted using Python and Jupyter Notebooks. The following steps were taken:

1. **Data Cleaning and Preprocessing:**  nitial data preparation involved several steps using the pandas library. Missing values were identified and removed using df.dropna(inplace=True). Duplicate entries in the dataset were also removed using df.drop_duplicates(inplace=True). The data types of the columns were inspected using df.info(). Additionally, code for identifying potential outliers using z-scores was implemented, although the final handling of outliers isn't explicitly visible in this view.
2. **Exploratory Data Analysis (EDA):** Exploratory Data Analysis was performed to understand the dataset's characteristics. This included visualizing the age distribution of participants using a histogram (as seen in a previous screenshot), which showed a concentration in the late teens and early twenties.
3. **Data Visualization:** Matplotlib was used to create visualizations to identify patterns and relationships. This included the aforementioned age distribution histogram, as well as two horizontal bar plots comparing average music listening hours for individuals with low and extreme mental health rankings. A pie chart also illustrated the overall reported effects of music on mental health.
4. **Analysis and Interpretation:** The core analysis involved examining the relationships between music listening habits and mental health indicators. This included the use of pivot tables to analyze the correlation between the frequency of listening to specific genres like rock and reported depression levels. The findings suggested that music genre, particularly rock versus Lofi, and the frequency of listening can be associated with different mental health outcomes.

## Key Findings

* The genres of music people listen to directly affect their mental health. For example, listeners of rock music showed a tendency towards higher levels of mental health challenges compared to listeners of genres like Lofi.
* Music with softer beats and positive messages, such as pop and Lofi, were associated with improved quality of life.
* A correlation was observed between higher music listening duration and insomnia.

## Conclusion

This project revealed a significant correlation between music genre and mental health, with listeners of slower-paced genres like Lofi reporting better mental well-being compared to those who favored rock music. This supports the notion that music plays a substantial role in perceived quality of life. Interestingly, higher music consumption was also associated with increased insomnia. To gain a more nuanced understanding, future research should incorporate demographic data such as sex, location, and pre-existing mental health conditions.



## Files

* `music_mental_health.ipynb`: Jupyter Notebook containing the code and analysis. 
* `data/mxmh_survey_results.csv`: The dataset used in the analysis.
* `README.md`: This file.

## How to Run the Code

1. Clone the repository: `git clone https://github.com/your-username/your-repository.git`
2. Install the necessary libraries: Run `pip install pandas numpy matplotlib` in your terminal or command prompt.
3. Open and run the Jupyter Notebook: `jupyter notebook music_mental_health.ipynb`


