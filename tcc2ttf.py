import fontforge
import os

def convert_ttc_to_ttf(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".ttc"):
                ttc_file_path = os.path.join(root, file)
                try:
                    # Get the list of fonts in the TTC file
                    fonts = fontforge.fontsInFile(ttc_file_path)
                    
                    # Iterate over each font in the collection
                    for index, fontname in enumerate(fonts):
                        font = fontforge.open(f"{ttc_file_path}({index})")
                        ttf_file_path = os.path.join(root, f"{file[:-4]}_{fontname}.ttf")
                        font.generate(ttf_file_path)
                        font.close()
                        print(f"Converted: {ttc_file_path} -> {ttf_file_path}")
                except Exception as e:
                    print(f"Failed to convert {ttc_file_path}: {e}")

# Update the folder path with your actual folder path
folder_path = r"C:\Users\user\Documents\GayHub\fonts\original"  # Use raw string
convert_ttc_to_ttf(folder_path)
