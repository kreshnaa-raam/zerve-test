isolation_forest = IsolationForest(contamination=0.1, random_state=42)

# Fit the model
data['anomaly_score'] = isolation_forest.fit_predict(features_scaled)