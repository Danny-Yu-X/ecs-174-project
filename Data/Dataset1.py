import kagglehub

# Download latest version
path = kagglehub.dataset_download("seryouxblaster764/fgvc-aircraft")

print("Path to dataset files:", path)