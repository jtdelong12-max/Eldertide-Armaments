#!/usr/bin/env python3
"""
Build script for Eldertide Armaments BG3 Mod
Packs mod files into a .pak archive for Baldur's Gate 3
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

# Configuration
MOD_NAME = "EldertideArmaments"
VERSION = "1.0.0"
OUTPUT_DIR = "dist"

# Paths
ROOT_DIR = Path(__file__).parent
MODS_DIR = ROOT_DIR / "Mods" / MOD_NAME
PUBLIC_DIR = ROOT_DIR / "Public" / MOD_NAME
LOCALIZATION_DIR = ROOT_DIR / "Localization"
OUTPUT_PATH = ROOT_DIR / OUTPUT_DIR / f"{MOD_NAME}.pak"
PACKAGE_DIRS = [
    MODS_DIR,
    PUBLIC_DIR,
    LOCALIZATION_DIR,
    ROOT_DIR / "EldertideVFX",
]

# Divine CLI tool path (update this to your Divine.exe location)
# Download from https://github.com/Norbyte/lslib/releases
DIVINE_PATH = os.environ.get("DIVINE_PATH", "divine.exe")


def check_divine():
    """Check if Divine CLI tool is available"""
    if not shutil.which(DIVINE_PATH):
        print(f"ERROR: Divine CLI tool not found at '{DIVINE_PATH}'")
        print("Please download LSLib from: https://github.com/Norbyte/lslib/releases")
        print("Set DIVINE_PATH environment variable or update the script with the correct path.")
        return False
    return True


def create_output_dir():
    """Create output directory if it doesn't exist"""
    output_dir = ROOT_DIR / OUTPUT_DIR
    output_dir.mkdir(exist_ok=True)
    print(f"Output directory: {output_dir}")


def latest_source_mtime():
    """Return the newest modified time across package directories"""
    latest = 0
    for path in PACKAGE_DIRS:
        if not path.exists():
            continue
        for root, _, files in os.walk(path):
            for file in files:
                try:
                    mtime = (Path(root) / file).stat().st_mtime
                except FileNotFoundError:
                    continue
                if mtime > latest:
                    latest = mtime
    return latest


def pack_mod():
    """Pack the mod files into a .pak archive"""
    print(f"Packing {MOD_NAME} v{VERSION}...")
    
    # Ensure output directory exists
    create_output_dir()
    
    # Skip repack if sources haven't changed
    if OUTPUT_PATH.exists():
        latest_source_time = latest_source_mtime()
        if latest_source_time and OUTPUT_PATH.stat().st_mtime >= latest_source_time:
            print(f"Skipping repack: {OUTPUT_PATH.name} is already up to date.")
            return True
    
    # Remove old .pak file if it exists
    if OUTPUT_PATH.exists():
        OUTPUT_PATH.unlink()
        print(f"Removed old {OUTPUT_PATH.name}")
    
    # Build the Divine command
    # Divine.exe -g bg3 -a create-package -s <source_dir> -d <output.pak>
    cmd = [
        DIVINE_PATH,
        "-g", "bg3",
        "-a", "create-package",
        "-s", str(ROOT_DIR),
        "-d", str(OUTPUT_PATH),
        "-c", "lz4"  # Compression method (lz4 or zlib)
    ]
    
    try:
        print(f"Running command: {' '.join(cmd)}")
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        print(f"\n✓ Successfully created: {OUTPUT_PATH}")
        print(f"  Size: {OUTPUT_PATH.stat().st_size / 1024:.2f} KB")
        return True
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Failed to pack mod")
        print(f"  {e.stderr}")
        return False
    except FileNotFoundError:
        print(f"ERROR: Divine tool not found at '{DIVINE_PATH}'")
        print("Please install LSLib and update the DIVINE_PATH variable.")
        return False


def verify_structure():
    """Verify that required mod structure exists"""
    required_paths = [MODS_DIR, PUBLIC_DIR, LOCALIZATION_DIR]
    missing = []
    
    for path in required_paths:
        if not path.exists():
            missing.append(str(path))
    
    if missing:
        print("ERROR: Missing required directories:")
        for path in missing:
            print(f"  - {path}")
        return False
    
    # Check for meta.lsx
    meta_file = MODS_DIR / "meta.lsx"
    if not meta_file.exists():
        print(f"ERROR: Missing required file: {meta_file}")
        return False
    
    return True


def main():
    """Main build function"""
    print("=" * 60)
    print(f"Eldertide Armaments Build Script")
    print(f"Version: {VERSION}")
    print("=" * 60)
    print()
    
    # Verify structure
    if not verify_structure():
        print("\nBuild failed: Invalid mod structure")
        sys.exit(1)
    
    # Check for Divine tool
    if not check_divine():
        print("\nBuild failed: Divine CLI tool not available")
        print("\nNote: You can manually pack the mod using LSLib GUI:")
        print("1. Download LSLib from https://github.com/Norbyte/lslib/releases")
        print("2. Open ConverterApp.exe")
        print("3. Go to 'Package Manager' tab")
        print("4. Select game: Baldur's Gate 3")
        print("5. Select source directory and create package")
        sys.exit(1)
    
    # Pack the mod
    if pack_mod():
        print("\n" + "=" * 60)
        print("Build completed successfully!")
        print("=" * 60)
        sys.exit(0)
    else:
        print("\nBuild failed")
        sys.exit(1)


if __name__ == "__main__":
    main()
