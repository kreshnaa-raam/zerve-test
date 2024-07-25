# Dropping columns with more than 80% missing values
threshold = 0.8
data = df[df.columns[df.isnull().mean() < threshold]]

# Fill missing values with appropriate methods (mean, median, mode, or specific value)
data['execution_time'].fillna(data['execution_time'].mean(), inplace=True)


# Example: One-hot encoding for 'status' column
data = pd.get_dummies(data, columns=['status', 'compute_environment_type', 'language'], drop_first=True)

# Feature Engineering
# Example: Create a new feature for execution duration
data['execution_duration'] = (pd.to_datetime(data['ended_at']) - pd.to_datetime(data['started_at'])).dt.total_seconds()

# Drop original datetime columns if not needed
data.drop(['started_at', 'ended_at'], axis=1, inplace=True)

# Normalization of features
scaler = StandardScaler()
numerical_cols = ['execution_time', 'execution_duration']
data[numerical_cols] = scaler.fit_transform(data[numerical_cols])

# Transformed dataset
data.dropna(inplace=True)
data['update_duration'] = (pd.to_datetime(data['time_updated']) - pd.to_datetime(data['time_created'])).dt.total_seconds()

data.drop(columns=['time_created', 'time_updated'], inplace=True)

print(data.isnull().sum())