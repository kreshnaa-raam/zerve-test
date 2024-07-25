
def preprocess(data_dict):
    data = pd.DataFrame(data_dict)
    data = pd.get_dummies(data, columns=['compute_environment_type'], drop_first=True)
    data['execution_duration'] = (pd.to_datetime(data['ended_at']) - pd.to_datetime(data['started_at'])).dt.total_seconds()
    data.drop(columns=['started_at','ended_at'], inplace=True)
    scaler = StandardScaler()
    features = ['compute_environment_type_AWS_LAMBDA', 'compute_environment_type_AWS_SAGEMAKER', 'execution_duration']
    features_scaled = scaler.fit_transform(data[features])
    return features_scaled

def prediction(features_scaled):
    scaler_filename = 'scaler.joblib'
    anomaly_model = 'isolation_forest_model.joblib'
    loaded_scaler = joblib.load(scaler_filename)
    loaded_model = joblib.load(anomaly_model)
    new_data_scaled = loaded_scaler.transform(features_scaled)
    anomaly_scores = loaded_model.predict(new_data_scaled)
    response = {'response': anomaly_scores}
    return response


scaled = preprocess(payload['new_data'])

RESPONSE = prediction(scaled)