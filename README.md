# 🌟 User Segmentation ML Project (K-Means Clustering)

## 🎯 Project Goal

The primary objective of this project is to perform **user segmentation** based on their behavioral data (online activity, engagement, and click-through rates). By using the **K-Means clustering** algorithm, the project creates clear, actionable user profiles to enhance targeted advertising and personalize marketing strategies.

---

## ⚙️ Methodology

This project follows a professional, modular structure:

1.  **Data Preprocessing:** Key behavioral features are extracted and standardized using `StandardScaler` to prepare the data for clustering.
2.  **Modular Code:** Preprocessing logic (scaling, feature selection, and cluster mean calculation) is centralized in the **`src/preprocessing.py`** module for code cleanliness and reusability.
3.  **Clustering:** The K-Means algorithm is applied to segment the user base into **5 distinct clusters**.
4.  **Model Persistence:** The trained $K$-Means model and the fitted scaler are saved using `joblib` into the **`models/`** directory for future deployment.
5.  **Visualization:** A **Radar Chart** is used to visually compare the profiles of the five identified user segments.

---

## 📊 Key Findings (Segment Profiles)

The analysis resulted in five clearly defined user segments, each named based on their most defining characteristics:

| Cluster | Name | Key Characteristics | Marketing Recommendations |
| :---: | :--- | :--- | :--- |
| **0** | **Weekend Warriors** | High activity on weekends, moderate overall engagement. | Schedule peak advertising during Saturday and Sunday. |
| **1** | **Engaged Professionals** | Balanced week/weekend activity, **highest overall likes/reactions**. | Focus on high-quality content; steady ad budget throughout the week. |
| **2** | **Low-Key Users** | Consistently low metrics across all features. | Target with "cold" lead generation funnels focusing on initial awareness. |
| **3** | **Active Explorers** | High weekday and weekend activity, **high Click-Through Rates (CTR)**. | Use action-oriented ads that encourage immediate interaction. |
| **4** | **Budget Browsers** | Low recorded income, moderate online activity. | Focus campaigns heavily on discounts, sales, and promotional offers. |

### Segment Comparison (Radar Chart)

The Radar Chart below visually demonstrates the strengths and weaknesses of each segment across the key behavioral metrics.

*\[**Insert your Plotly Radar Chart Image here**]*

---

## 📂 Project Structure

The repository adheres to a standard data science project layout, ensuring clarity and reproducibility:

User_Segmentation_ML/
├── data/
│   └── user_profiles_for_ads.csv          # Raw input user data for segmentation
│
├── models/
│   ├── kmeans_model.joblib                # Trained K-Means clustering model
│   └── data_scaler.joblib                 # Fitted StandardScaler for feature scaling
│
├── notebooks/
│   └── user_segmentation_analysis.ipynb   # Main exploratory analysis & modeling notebook
│
├── src/
│   └── preprocessing.py                   # Reusable functions (cleaning, scaling, feature prep)
│
├── .gitignore                             # Ignore venv/, models/, checkpoints, etc.
├── requirements.txt                       # Python dependencies for the project
└── README.md                              # Project description and usage instructions

