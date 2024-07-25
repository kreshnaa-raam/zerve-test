anomalies = data[data['anomaly_score'] == -1]

# Plotting the anomalies
plt.figure(figsize=(12, 6))
sns.scatterplot(data=data, x='execution_time', y='execution_duration', hue='anomaly_score', palette=['red', 'blue'])
plt.title('Anomalies Detected by Isolation Forest')
plt.xlabel('Execution Time')
plt.ylabel('Execution Duration')
plt.legend(title='Anomaly', labels=['Normal', 'Anomaly'])
plt.show()

print("Anomalies detected:")
print(anomalies)