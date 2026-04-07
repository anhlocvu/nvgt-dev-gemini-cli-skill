import os
import requests
import argparse
from urllib.parse import urlparse

# Audio Asset Manager for NVGT Projects
# Finds and downloads audio assets automatically based on AI-provided links.

def download_file(url, target_folder):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        
    filename = os.path.basename(urlparse(url).path)
    if not filename:
        filename = "downloaded_asset.wav"
        
    filepath = os.path.join(target_folder, filename)
    
    print(f"Downloading {url} to {filepath}...")
    try:
        response = requests.get(url, stream=True, timeout=15)
        response.raise_for_status()
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Successfully downloaded: {filename}")
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

def search_advice():
    # Placeholder for the AI to get search advice for better results
    print("For better audio game assets, search for:")
    print("- 'SFX footstep grass wav'")
    print("- 'ambient forest loop wav'")
    print("- 'UI click mechanical wav'")
    print("Sites recommended: Freesound.org, OpenGameArt.org, Soniss GDC (for large packs)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NVGT Asset Manager")
    parser.add_argument("--download", help="URL of the asset to download")
    parser.add_argument("--target", default="sounds", help="Target folder for assets")
    parser.add_argument("--advice", action="store_true", help="Get search advice")
    
    args = parser.parse_args()
    
    if args.advice:
        search_advice()
    
    if args.download:
        download_file(args.download, args.target)
