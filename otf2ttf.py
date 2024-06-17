import fontforge
import os

def convert_otf_to_ttf(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".otf"):
                otf_file_path = os.path.join(root, file)
                ttf_file_path = os.path.join(root, file[:-4] + ".ttf")
                try:
                    font = fontforge.open(otf_file_path)
                    font.generate(ttf_file_path)
                    font.close()
                    print(f"Converted: {otf_file_path} -> {ttf_file_path}")
                except Exception as e:
                    print(f"Failed to convert {otf_file_path}: {e}")

# Update the folder path with your actual folder path
folder_path = r"C:\Users\user\Documents\GayHub\fonts\original"  # Use raw string
convert_otf_to_ttf(folder_path)
