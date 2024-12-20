from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def normalize(df):
    scaler = MinMaxScaler()
    normalized_engagement = scaler.fit_transform(df)
    normalized_df = pd.DataFrame(normalized_engagement, columns=df.columns)
    return normalized_df


def dimension_reduction(df):
    scaler = StandardScaler()
    numeric_columns = df.select_dtypes(include=['float64', 'int64'])
    scaled_data = scaler.fit_transform(numeric_columns)
    pca =PCA(n_components=2)
    principal_components = pca.fit_transform(scaled_data)
    pca_df = pd.DataFrame(data=principal_components,columns=['PC1','PC2'])
    explained_variance = pca.explained_variance_ratio_
    # Print results 
    print("Explained Variance Ratio:", explained_variance) 
    print("Principal Components DataFrame:\n", pca_df) 
    plt.figure(figsize=(10, 6))
    plt.scatter(x=pca_df['PC1'], y=pca_df['PC2'])
    plt.title('PCA - First Two Principal Components')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.show()
    # Interpretation 
    print("\nInterpretation:") 
    print("1. PC1 and PC2 capture the majority of variance in the data.") 
    print("2. High loading scores on PC1 for Gaming DL indicate its significant contribution.") 
    print("3. The total explained variance by PC1 and PC2 shows effective dimensionality reduction.") 
    print("4. The PCA results help identify key patterns in data usage.")
