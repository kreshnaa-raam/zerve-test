cols = ['execution_time','update_duration', 'status_PENDING', 'status_RUNNING', 'status_STOPPED',
'status_STOP_REQUESTED', 'status_SUCCEEDED','compute_environment_type_AWS_LAMBDA',       
'compute_environment_type_AWS_SAGEMAKER', 'language_PYTHON',
'language_R', 'language_RMARKDOWN', 'language_SQL','execution_duration']

corr_matrix = data[cols].corr()

#  heatmap of the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()
