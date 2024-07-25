model_filename = "isolation_forest_model.joblib"
joblib.dump(isolation_forest, model_filename)

scaler_filename = "scaler.joblib"
joblib.dump(scaler, scaler_filename)