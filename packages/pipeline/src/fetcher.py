"""Image fetching module"""
from typing import Tuple, Optional
import requests
from pathlib import Path

def fetch_satellite_image(
    lat: float,
    lon: float,
    sample_id: int,
    output_dir: Path
) -> Optional[Path]:
    """
    Fetch satellite image for given coordinates.
    
    Args:
        lat: Latitude
        lon: Longitude  
        sample_id: Unique identifier
        output_dir: Directory to save image
        
    Returns:
        Path to saved image or None if failed
    """
    # TODO: Implement image fetching
    print(f"Fetching image for ({lat}, {lon})...")
    return None