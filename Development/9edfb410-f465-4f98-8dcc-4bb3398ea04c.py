# Standardize the features
scaler = StandardScaler()
features = ['compute_environment_type_AWS_LAMBDA', 'compute_environment_type_AWS_SAGEMAKER', 'execution_duration']
features_scaled = scaler.fit_transform(data[features])


