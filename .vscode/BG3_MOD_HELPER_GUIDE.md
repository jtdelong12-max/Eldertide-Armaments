# BG3 Mod Helper - Quick Reference

## Setup Complete ✓

Your workspace is now configured for BG3 Mod Helper with the following settings:
- **Mod Name**: EldertideArmament
- **Mod UUID**: 22b848d1-5fff-4f76-a4f8-8461721e6112
- **Author**: Proxeuz
- **Localization Path**: EldertideArmament/Localization/English

## Key Features & Commands

### 1. UUID Generation
- **Command Palette**: `BG3: Generate UUID`
- **Usage**: Generates a new UUID and copies it to clipboard
- **Use for**: Creating new items, spells, effects, etc.

### 2. Handle Generation
- **Command Palette**: `BG3: Generate Handle`
- **Usage**: Generates a new handle (h followed by UUID) and copies it to clipboard
- **Use for**: Creating localization entries

### 3. Auto-Update Localization
- **Enabled by default** in your settings
- When you generate a new handle, the extension will automatically add it to your .loca.xml files
- Location: `EldertideArmament/Localization/English/*.loca.xml`

### 4. Insert UUID/Handle
- **Command Palette**: 
  - `BG3: Insert UUID` - Generates and inserts a UUID at cursor
  - `BG3: Insert Handle` - Generates and inserts a handle at cursor

### 5. File Association Support
Your workspace is configured to recognize:
- `.lsx` files as XML
- `.loca` and `.loca.xml` files as XML
- `.txt` files as BG3 text format

## Recommended Workflow

### Creating a New Item/Spell/Effect:

1. **Generate UUID**: Use `Ctrl+Shift+P` → `BG3: Generate UUID`
2. **Paste into your .lsx file** where needed
3. **Generate Handle**: Use `Ctrl+Shift+P` → `BG3: Generate Handle` for localization
4. **Add Localization**: The handle is automatically added to your .loca.xml files
5. **Fill in the details** in the appropriate localization file

### Working with Existing Files:

- Open any `.lsx` file to see syntax highlighting
- The extension will help with XML formatting
- Use the command palette to quickly insert UUIDs and handles

## Additional Extensions Installed

- **BG3 Text Support** (`chromosome16.bg3-text-support`): Provides language support for BG3 .txt files
- Syntax highlighting for BG3-specific file types
- Code snippets for common BG3 modding patterns

## Tips

1. **Always use the extension to generate UUIDs** - ensures proper format and uniqueness
2. **Handles are automatically prefixed with 'h'** - this is BG3's standard format
3. **Keep your localization files organized** by type (Items, Spells, Weapons, etc.)
4. **The mod folder structure is already correct** - follow the existing pattern when adding new files

## Need More Extensions?

Other useful BG3 modding extensions available:
```vscode-extensions
fierrof.bg3txt-formatter,fallenstar.bg3guidinfos,fallenstar.bg3-se-snippets
```

## Troubleshooting

If commands don't appear:
1. Reload VS Code: `Ctrl+Shift+P` → `Developer: Reload Window`
2. Check extension is enabled: Extensions panel → Search "bg3"
3. Verify settings: `.vscode/settings.json` should have your mod configuration

## Command Palette Access

Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) and type "BG3" to see all available commands.
