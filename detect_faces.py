import boto3
import json
import os

# Create Rekognition client
rekognition = boto3.client(
    "rekognition",
    region_name=os.environ["AWS_REGION"]
)

bucket = os.environ["S3_BUCKET_NAME"]
image = "employee.jpg"

# Detect faces
response = rekognition.detect_faces(
    Image={
        "S3Object": {
            "Bucket": bucket,
            "Name": image
        }
    },
    Attributes=["ALL"]
)

faces = response["FaceDetails"]

print("Number of Faces:", len(faces))

results = []

for i, face in enumerate(faces, start=1):

    confidence = face["Confidence"]

    print(f"Face {i} Confidence: {confidence:.2f}%")

    results.append({
        "FaceNumber": i,
        "Confidence": round(confidence, 2)
    })

# Save output
with open("result.json", "w") as f:
    json.dump(results, f, indent=4)

print("Results saved to result.json")
