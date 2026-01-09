# Eldertide Armaments

A Baldur's Gate 3 mod that introduces a collection of custom armaments for your adventures in the Forgotten Realms.

## Overview

Eldertide Armaments is a mod for Baldur's Gate 3 (Patch 7 compatible) that adds unique weapons and armor to the game. This mod is designed to work with the In-Game Mod Manager introduced in Patch 7.

## Installation

### Using In-Game Mod Manager (Recommended)
1. Download the latest `.pak` file from the releases page
2. Place the `.pak` file in your BG3 Mods folder:
   - Windows: `%LOCALAPPDATA%\Larian Studios\Baldur's Gate 3\Mods`
   - Steam Deck/Linux: `~/.local/share/Larian Studios/Baldur's Gate 3/Mods`
3. Launch Baldur's Gate 3
4. Open the In-Game Mod Manager from the main menu
5. Enable "Eldertide Armaments"
6. Start or continue your game

### Manual Installation (Legacy)
1. Download the latest `.pak` file
2. Place it in your BG3 Mods folder (see paths above)
3. The mod will be automatically loaded by the game

## Development

### Prerequisites
- Python 3.7 or higher
- LSLib Divine CLI tool ([Download here](https://github.com/Norbyte/lslib/releases))

### Building the Mod
1. Clone this repository
2. Install LSLib and set the `DIVINE_PATH` environment variable:
   ```bash
   export DIVINE_PATH=/path/to/divine.exe
   ```
3. Run the build script:
   ```bash
   python build.py
   ```
4. The packed mod will be created in the `dist/` folder

### Project Structure
```
Eldertide-Armaments/
├── Mods/
│   └── EldertideArmaments/
│       └── meta.lsx              # Mod metadata and configuration
├── Public/
│   └── EldertideArmaments/
│       └── [PAK]_EldertideArmaments/  # Public assets
├── Localization/
│   └── English/                  # Localization files
├── build.py                      # Build script to pack the mod
├── .gitignore                    # Git ignore file
└── README.md                     # This file
```

## Legacy Migration

### Migrating from Pre-Patch 7 Versions

If you're upgrading from a version of this mod created before Baldur's Gate 3 Patch 7, please note the following changes:

#### In-Game Mod Manager Support
Patch 7 introduced a built-in mod manager. Eldertide Armaments now includes proper `meta.lsx` configuration to ensure compatibility with this new system. The mod will appear in the in-game mod list with its full name and description.

#### UUID Changes
The mod now uses a standardized UUID system required by the In-Game Mod Manager. If you had a previous version installed:
1. Disable or remove the old version from your Mods folder
2. Install the new version
3. Launch the game and enable the mod through the In-Game Mod Manager

#### Save Game Compatibility
- Save games from previous versions should remain compatible
- However, we recommend starting a new playthrough if you experience any issues
- Always backup your save files before updating mods

#### ModFixer/LSLib Users
If you previously used external tools like ModFixer or manual LSLib packing:
- These tools are still compatible but no longer necessary
- The In-Game Mod Manager handles load order automatically
- You can safely switch to using the in-game system

### Troubleshooting Legacy Issues

**Issue**: Mod doesn't appear in In-Game Mod Manager
- **Solution**: Ensure you've removed any old versions and only the new `.pak` file is in your Mods folder

**Issue**: Duplicate items or conflicts
- **Solution**: Check that no legacy versions are still active. Only one version should be installed.

**Issue**: Save game shows missing mod content
- **Solution**: Re-enable the mod through the In-Game Mod Manager and load your save again

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This mod is provided as-is for the Baldur's Gate 3 community.

## Credits

- Built for Baldur's Gate 3 Patch 7
- Uses LSLib by Norbyte

## Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the BG3 modding community forums
- Ensure you're running the latest version of Baldur's Gate 3