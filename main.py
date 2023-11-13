
import numpy as np
import face_recognition
import cv2
import os
from mtcnn import MTCNN
def process_known_images(known_images_path):
    known_faces = []
    known_names = []

    for image_name in os.listdir(known_images_path):
        image_path = os.path.join(known_images_path, image_name)
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)

        if len(face_locations) == 1:
            face_encoding = face_recognition.face_encodings(image, known_face_locations=face_locations)[0]
            known_faces.append(face_encoding)
            known_names.append(image_name.split(".")[0])

    return known_faces, known_names

def classify_unknown_images(unknown_images_path, known_faces, known_names):
    detector = MTCNN()

    for unknown_image_name in os.listdir(unknown_images_path):
        unknown_image_path = os.path.join(unknown_images_path, unknown_image_name)
        unknown_image = cv2.imread(unknown_image_path)
        rgb_unknown_image = cv2.cvtColor(unknown_image, cv2.COLOR_BGR2RGB)

        faces = detector.detect_faces(rgb_unknown_image)
        if len(faces) == 1:
            face_coordinates = faces[0]['box']
            face = unknown_image[face_coordinates[1]:face_coordinates[1] + face_coordinates[3],
                                 face_coordinates[0]:face_coordinates[0] + face_coordinates[2]]
            rgb_face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
            face_encoding = face_recognition.face_encodings(rgb_face)[0]
            # 比对
            matches = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.5)
            if True in matches:
                first_match_index = matches.index(True)
                name = known_names[first_match_index]
                print(f"Match found! The person in {unknown_image_name} is {name}")
            else:
                print(f"No match found for {unknown_image_name} (unknown person).")
        else:
            print(f"No or multiple faces detected in {unknown_image_name}.")

if __name__ == '__main__':
    known_images_path = "./known_images/"
    unknown_images_path = "./images/"

    known_faces, known_names = process_known_images(known_images_path)
    classify_unknown_images(unknown_images_path, known_faces, known_names)
