# BG3 Modding Extensions - Complete Setup Guide

## ✅ Installed & Configured Extensions

### 1. **BG3 Mod Helper** (`ghostboats.bg3-mod-helper` v2.2.63)
**Purpose**: Core BG3 modding tool for UUID/Handle generation and localization management

**Configuration**:
- ✅ Mod name, UUID, and author configured
- ✅ Localization path set to English folder
- ✅ Auto-update for .loca.xml files enabled

**Commands** (Ctrl+Shift+P):
- `BG3: Generate UUID` - Creates a new UUID
- `BG3: Generate Handle` - Creates localization handle (h + UUID)
- `BG3: Insert UUID` - Inserts UUID at cursor
- `BG3: Insert Handle` - Inserts handle at cursor

---

### 2. **BG3 Text Support** (`chromosome16.bg3-text-support` v0.0.6)
**Purpose**: Language support and syntax highlighting for BG3 .txt files

**Configuration**:
- ✅ File associations set (*.txt → bg3txt)
- ✅ Tab size: 4 spaces
- ✅ Word wrap disabled for better readability
- ✅ Syntax highlighting configured

**Features**:
- Syntax highlighting for BG3 stats files
- Code snippets for common BG3 structures
- IntelliSense support for keywords

---

### 3. **BG3 TXT Formatter** (`fierrof.bg3txt-formatter` v1.0.2)
**Purpose**: Format and align BG3 text files

**Configuration**:
- ✅ Formatter enabled
- ✅ Indent size: 4 spaces
- ✅ Data alignment enabled
- ⚠️ Format on save disabled (to prevent unwanted changes)

**Usage**:
- Right-click → "Format Document" or Ctrl+Shift+I
- Aligns "data" statements for better readability

---

### 4. **BG3 GUID Infos** (`fallenstar.bg3guidinfos` v1.1.4)
**Purpose**: Shows information about GUIDs/UUIDs when hovering

**Configuration**:
- ✅ Extension enabled
- ℹ️ BG3 data path not set (optional - set if you have BG3 unpacked data)

**Features**:
- Hover over UUIDs to see information
- Works with .lsx, .xml, and .json files
- Helps identify game resources by GUID

**Optional Setup**:
To enable full GUID lookup, set your BG3 data path:
```json
"bg3guidinfos.bg3DataPath": "/path/to/BG3/Data"
```

---

### 5. **BG3 SE Snippets** (`fallenstar.bg3-se-snippets` v1.0.7)
**Purpose**: Code snippets for BG3 Script Extender

**Configuration**:
- ✅ Snippets available in Lua files
- ✅ Custom snippets added for common BG3 patterns

**Features**:
- Event listener snippets
- Script Extender API snippets
- Works with Lua files for SE modding

**Common Snippets**:
- `listener` - Creates an event listener
- `event` - Basic event structure
- `api` - SE API call template

---

### 6. **GitHub Copilot** (v1.388.0 + Chat v0.36.1)
**Purpose**: AI-powered code completion and chat assistance

**Configuration**:
- ✅ Enabled for most file types
- ⚠️ Disabled for XML files (to prevent XML corruption)
- ✅ Enabled for BG3 txt files and Markdown

**Best Practices**:
- Use for boilerplate code generation
- Ask in chat for BG3 modding patterns
- Disable for sensitive XML editing

---

## 📝 Custom Workspace Features

### Code Snippets
Custom snippets added in `.vscode/snippets.code-snippets`:
- `entry` - BG3 TXT stats entry
- `data` - Data line
- `status` - Status entry
- `spell` - Spell entry
- `passive` - Passive entry
- `armor` - Armor/jewelry entry
- `loca` - Localization entry
- `node` - LSX node
- `attr` - LSX attribute

### File Associations
- `.lsx` → XML
- `.loca`, `.loca.xml` → XML  
- `.txt` → bg3txt

### Syntax Highlighting
Custom colors configured for:
- Keywords (purple)
- Operators (orange)
- Strings (light blue)
- Types (teal)
- Comments (green, italic)

---

## 🔧 Quick Actions

### Generate New Item
1. Open Stats file (e.g., `Armor.txt`)
2. Type `armor` and press Tab
3. Press Ctrl+Shift+P → "BG3: Generate UUID"
4. Paste UUID in RootTemplate field
5. Press Ctrl+Shift+P → "BG3: Generate Handle" for DisplayName
6. Handle auto-added to localization files

### Format BG3 TXT File
1. Open any .txt file
2. Right-click → "Format Document"
3. Or press: Ctrl+Shift+I

### Lookup GUID
1. Hover over any UUID/GUID
2. Extension shows information if available

---

## ⚙️ Recommended Settings

### File Exclusions
The following are excluded from search:
- `**/node_modules`
- `**/bower_components`
- `**/.git`
- `**/tools/Packed` (pre-compiled tools)

### Editor Behavior
- Format on save: **Disabled** (prevents XML corruption)
- Detect indentation: **Disabled** (enforces consistent spacing)
- Insert spaces: **Enabled** (no tabs)

---

## 🚀 Common Workflows

### Creating a New Spell
```plaintext
1. Open: Stats/Generated/Data/Spells_*.txt
2. Type: spell [Tab]
3. Fill in spell details
4. Generate handles for name/description
5. Localization auto-updates
```

### Creating a New Ring/Amulet
```plaintext
1. Open: Stats/Generated/Data/Armor.txt
2. Type: armor [Tab]
3. Generate UUID for RootTemplate
4. Set stats and properties
5. Generate handles for DisplayName
6. Create RootTemplate in RootTemplates folder
```

### Adding Localization
```plaintext
1. Generate handle: Ctrl+Shift+P → BG3: Generate Handle
2. Extension auto-adds to .loca.xml files
3. Open: Localization/English/*.loca.xml
4. Find your handle
5. Add text between <content> tags
```

---

## 🛠️ Troubleshooting

### Extension Not Working
1. Reload window: Ctrl+Shift+P → "Developer: Reload Window"
2. Check Extensions panel for updates
3. Verify settings in `.vscode/settings.json`

### Formatter Issues
- Disable auto-format: `"editor.formatOnSave": false`
- Format manually only when needed
- Check indent size matches file (4 for .txt, 2 for .xml)

### GUID Info Not Showing
- Set `bg3guidinfos.bg3DataPath` if you have unpacked BG3 data
- Extension works best with actual game data path

---

## 📚 Additional Resources

### BG3 Modding Wiki
- https://bg3.wiki/

### Script Extender Documentation
- Required for SE snippets extension
- Check Script Extender GitHub for API docs

### Larian Studios Modding Resources
- Official modding tools and documentation

---

## 🎯 Next Steps

1. ✅ All extensions configured
2. ✅ Custom snippets ready
3. ✅ File associations set
4. ✅ Syntax highlighting active

**You're ready to mod!** Open any .txt or .lsx file to see syntax highlighting and use snippets.
