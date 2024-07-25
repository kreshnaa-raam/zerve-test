new_data_dict = {
    'compute_environment_type_AWS_LAMBDA': [1, 1, 0],
    'compute_environment_type_AWS_SAGEMAKER': [0, 0, 1],
    'execution_duration': [400.0, 600.0, 200.0]
}

new_data = pd.DataFrame(new_data_dict)

scaler_filename = 'scaler.joblib'
anomaly_model = 'isolation_forest_model.joblib'

loaded_scaler = joblib.load(scaler_filename)
loaded_model = joblib.load(anomaly_model)

new_data_scaled = loaded_scaler.transform(new_data)

anomaly_scores = loaded_model.predict(new_data_scaled)

new_data['anomaly_score'] = anomaly_scores