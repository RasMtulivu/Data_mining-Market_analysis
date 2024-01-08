import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

def read_data_from_csv(file_path):
    try:
        # Read data from Market_Basket_Optimization 
        data = pd.read_csv(file_path, delimiter=',')

        return data if data is not None else pd.DataFrame()  # Return an empty DataFrame if data is None
    except Exception as e:
        print(f"Error reading Market_Basket file: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

def generate_association_rules(data, min_support=0.05, min_confidence=0.3):
    # Convert the data to one-hot encoding and fill missing values with 0
    one_hot_encoded = pd.get_dummies(data, dummy_na=False).fillna(0)

    # Use Apriori algorithm to find frequent itemsets
    frequent_itemsets = apriori(one_hot_encoded, min_support=min_support, use_colnames=True)
    print(frequent_itemsets)

    # Generate association rules
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)

    return rules

def main():
    # Input the file path of the Excel dataset
   # file_path = "C:/Users/The Poet/Documents/Mining_Assignment/Market_Basket_Optimisation.csv"
    file_path ="C:/Users/YoungBlood/Desktop/dataminingcat2/Mining_Assignment/Market_Basket_Optimisation.csv"
    
    # Read data from Excel
    data = read_data_from_csv(file_path)

    if data.empty:
        print("The dataset is empty or could not be loaded. Exiting.")
        return
    
    # Input the minimum support and confidence
    min_support = float(input("Enter the minimum support (e.g., 0.01): "))
    min_confidence = float(input("Enter the minimum confidence (e.g., 0.8): "))
    
    # Generate association rules
    rules = generate_association_rules(data, min_support, min_confidence)
    
    # Display the resulting rules
    print("\nAssociation Rules:")
    print(rules)

if __name__ == "__main__":
    main()
