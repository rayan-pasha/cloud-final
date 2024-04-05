import pandas as pd
from google.cloud import storage
import matplotlib.pyplot as plt
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./cloud-implementation-417919-81c811a23020.json"


def download_data(bucket_name, source_blob_name, destination_file_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print(f'Blob {source_blob_name} downloaded to {destination_file_name}.')


def main():
    bucket_name = 'cloud_highd'
    source_blob_name = 'data/01_tracksMeta.csv'
    destination_file_name = '01_tracksMeta.csv'

    download_data(bucket_name, source_blob_name, destination_file_name)

    df = pd.read_csv(destination_file_name)

    # Filter Data off drivingDirection
    df_direction_1 = df[df['drivingDirection'] == 1]
    df_direction_2 = df[df['drivingDirection'] == 2]

    # Plot graphs for each direction
    plt.figure(figsize=(10, 6))

    # Plot for drivingDirection == 1
    plt.subplot(1, 2, 1)
    plt.plot(df_direction_1['minDHW'], df_direction_1['minTHW'], 'bo')
    plt.xlabel('minDHW')
    plt.ylabel('minTHW')
    plt.title('Driving Direction 1')
    plt.grid(True)

    # Plot for drivingDirection == 2
    plt.subplot(1, 2, 2)
    plt.plot(df_direction_2['minDHW'], df_direction_2['minTHW'], 'ro')
    plt.xlabel('minDHW')
    plt.ylabel('minTHW')
    plt.title('Driving Direction 2')
    plt.grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
