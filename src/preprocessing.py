import pandas as pd
from sklearn.preprocessing import StandardScaler

# Список признаков для кластеризации (те же, что вы использовали для Radar Chart)
FEATURE_COLUMNS = [
    'Time Spent Online (hrs/weekday)', 
    'Time Spent Online (hrs/weekend)', 
    'Likes and Reactions', 
    'Click-Through Rates (CTR)'
]

def select_and_scale_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Выбирает необходимые признаки и масштабирует их с использованием StandardScaler.

    Args:
        df: Исходный DataFrame.

    Returns:
        DataFrame с масштабированными признаками.
    """
    # 1. Выбор признаков
    features_df = df[FEATURE_COLUMNS]
    
    # 2. Инициализация и обучение масштабировщика
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(features_df)
    
    # 3. Преобразование обратно в DataFrame
    scaled_df = pd.DataFrame(scaled_data, columns=FEATURE_COLUMNS)
    
    return scaled_df, scaler # Возвращаем и данные, и обученный скейлер (чтобы можно было его сохранить!)

def get_cluster_means(df: pd.DataFrame, cluster_labels: pd.Series) -> pd.DataFrame:
    """
    Рассчитывает средние значения признаков для каждого кластера.

    Args:
        df: Исходный DataFrame с признаками.
        cluster_labels: Метки кластеров (результат KMeans.labels_).

    Returns:
        DataFrame со средними значениями признаков для каждого кластера.
    """
    # Создаем новый столбец с метками кластеров
    df_with_clusters = df.copy()
    df_with_clusters['Cluster'] = cluster_labels
    
    # Группируем и находим средние значения
    cluster_means_df = df_with_clusters.groupby('Cluster')[FEATURE_COLUMNS].mean()
    
    return cluster_means_df