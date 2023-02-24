import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

class DataAnalysis:
    
    def __init__(self, data):
        self.data = data
        
    def load_data(self, file_path):
        self.data = pd.read_csv(file_path)
        
    def view_data(self, num_rows=5):
        return self.data.head(num_rows)
        
    def summary_statistics(self):
        return self.data.describe()
        
    def missing_values(self):
        return self.data.isnull().sum()
        