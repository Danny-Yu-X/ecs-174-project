import kagglehub

# Download latest version
path = kagglehub.dataset_download("ahnuf05/aeroscan-military-aircraft-classification")

print("Path to dataset files:", path)