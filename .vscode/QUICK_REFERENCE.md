# BG3 Modding - Quick Reference

## 🎮 Installed Extensions (All Configured)

| Extension | Version | Status |
|-----------|---------|--------|
| BG3 Mod Helper | 2.2.63 | ✅ Configured |
| BG3 Text Support | 0.0.6 | ✅ Configured |
| BG3 TXT Formatter | 1.0.2 | ✅ Configured |
| BG3 GUID Infos | 1.1.4 | ✅ Configured |
| BG3 SE Snippets | 1.0.7 | ✅ Configured |

---

## ⌨️ Essential Commands

### BG3 Mod Helper
| Command | Shortcut | Description |
|---------|----------|-------------|
| Generate UUID | `Ctrl+Shift+P` → BG3: Generate UUID | Creates UUID, copies to clipboard |
| Generate Handle | `Ctrl+Shift+P` → BG3: Generate Handle | Creates h+UUID, auto-updates .loca |
| Insert UUID | `Ctrl+Shift+P` → BG3: Insert UUID | Inserts UUID at cursor |
| Insert Handle | `Ctrl+Shift+P` → BG3: Insert Handle | Inserts handle at cursor |

### Formatting
| Command | Shortcut | Description |
|---------|----------|-------------|
| Format Document | `Ctrl+Shift+I` or Right-click | Formats BG3 .txt files |
| Format Selection | `Ctrl+K Ctrl+F` | Formats selected code |

### Navigation
| Command | Shortcut | Description |
|---------|----------|-------------|
| Go to Symbol | `Ctrl+Shift+O` | Jump to entries in current file |
| Find in Files | `Ctrl+Shift+F` | Search across workspace |
| Quick Open | `Ctrl+P` | Quick file navigation |

---

## 📝 Code Snippets (Type and press Tab)

### BG3 TXT Files
- `entry` → New stats entry
- `data` → Data line
- `armor` → Armor/jewelry entry
- `spell` → Spell entry
- `status` → Status entry
- `passive` → Passive entry
- `weaponwithvfx` → Weapon with VFX support
- `weaponvfxstatus` → Weapon VFX status

### XML/LSX Files
- `node` → LSX node
- `attr` → LSX attribute
- `loca` → Localization entry
- `weaponvfx` → Complete weapon VFX MultiEffectInfo

---

## 📂 File Structure

```
EldertideArmament/
├── Localization/English/      ← Localization files (.loca.xml)
├── Mods/EldertideArmament/    ← Mod metadata
│   └── meta.lsx               ← Mod info (UUID, version)
└── Public/EldertideArmament/
    ├── Stats/Generated/       ← Stats files (.txt)
    │   ├── Equipment.txt
    │   ├── ItemCombos.txt
    │   ├── TreasureTable.txt
    │   └── Data/
    │       ├── Armor.txt      ← Rings, amulets, armor
    │       ├── Passive_*.txt  ← Passive abilities
    │       ├── Spells_*.txt   ← Spells
    │       └── Status_*.txt   ← Status effects
    ├── RootTemplates/         ← Item templates (.lsx)
    ├── MultiEffectInfos/      ← Visual effects (.lsx)
    └── GUI/                   ← Icons (.lsx)
```

---

## � Quick Actions

### Generate New Item
```
Open: Stats/Generated/Data/Armor.txt
Type: armor [Tab]
Ctrl+Shift+P → Generate UUID → Paste in RootTemplate
Ctrl+Shift+P → Generate Handle → Use for DisplayName
Edit localization in: Localization/English/Items_*.loca.xml
Create RootTemplate: RootTemplates/[uuid].lsx
```

### Add VFX to Weapon
```
1. Browse MultiEffectInfos/ folder for existing VFX
2. Copy UUID from filename
3. Create status: weaponvfxstatus [Tab]
4. Add to weapon: OnEquipFunctors and OnUnequipFunctors
5. Test in-game!

See: .vscode/VFX_WEAPON_GUIDE.md for full guide
See: .vscode/VFX_EXAMPLES.md for copy-paste examples
```

### Add New Spell
```
Open: Stats/Generated/Data/Spells_*.txt
Type: spell [Tab]
Fill in spell properties
Generate handles for name/description
Add to TooltipExtras if needed
```

### Format Stats File
```
Open any .txt file
Ctrl+Shift+I
Aligns all data lines
```

---

## 🎨 File Types & Languages

| Extension | Language | Purpose |
|-----------|----------|---------|
| `.lsx` | XML | Game data structures |
| `.loca.xml` | XML | Localization/translations |
| `.txt` | bg3txt | Stats definitions |
| `.lsf.lsx` | XML | Compiled LSF files |

---

## ⚙️ Settings Summary

- **Format on Save**: Disabled (prevents XML corruption)
- **Tab Size**: 4 for .txt, 2 for .xml
- **Auto-update Localization**: Enabled
- **Syntax Highlighting**: Custom colors for BG3 files
- **Copilot**: Enabled for .txt, disabled for .xml

---

## 🔍 Hover Features

- **UUIDs/GUIDs**: Hover to see information (BG3 GUID Infos)
- **Keywords**: Hover for snippets (BG3 Text Support)
- **Properties**: Context-aware suggestions

---

## 📚 Configuration Files

| File | Purpose |
|------|---------|
| `.vscode/settings.json` | All extension settings |
| `.vscode/snippets.code-snippets` | Custom code snippets |
| `.vscode/extensions.json` | Recommended extensions |
| `.vscode/EXTENSIONS_GUIDE.md` | Detailed extension docs |
| `.vscode/VFX_WEAPON_GUIDE.md` | Complete VFX guide |
| `.vscode/VFX_EXAMPLES.md` | Copy-paste VFX examples |

---

## 💡 Pro Tips

1. **Use snippets**: Type shortcut + Tab instead of writing from scratch
2. **Format regularly**: Keep .txt files aligned with Ctrl+Shift+I
3. **Hover GUIDs**: Check what UUIDs reference before changing
4. **Command Palette**: Ctrl+Shift+P is your friend for all BG3 commands
5. **Auto-localization**: Handles are automatically added to .loca files

---

## 🚨 Important Notes

- ⚠️ **Never** format XML files with external tools (can corrupt them)
- ✅ **Always** use BG3 Mod Helper to generate UUIDs (ensures uniqueness)
- ✅ **Keep** localization files in English folder (extension looks there)
- ✅ **Use** provided snippets for consistency
- ⚠️ **Disable** format on save for XML files

---

**All extensions are configured and ready!** Press Ctrl+Shift+P and type "BG3" to see available commands.
