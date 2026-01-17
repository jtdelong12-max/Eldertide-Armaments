# ✨ VFX Setup Complete!

## What You Have

Your mod is **already VFX-ready** with:
- ✅ 100+ existing VFX files in `MultiEffectInfos/`
- ✅ Working weapon VFX examples (Dawnblade, Moonveil, Excalibur, etc.)
- ✅ Complete VFX infrastructure
- ✅ New code snippets for quick VFX creation
- ✅ Comprehensive documentation

---

## 📖 Documentation Created

### 1. [VFX_WEAPON_GUIDE.md](.vscode/VFX_WEAPON_GUIDE.md)
**Complete reference guide** covering:
- All 3 VFX integration methods
- MultiEffectInfo file structure
- Status creation and weapon integration
- Weapon bone targeting
- Testing and troubleshooting
- 500+ lines of detailed documentation

### 2. [VFX_EXAMPLES.md](.vscode/VFX_EXAMPLES.md)
**Ready-to-use templates** including:
- 6 complete working examples
- Fire glow weapon
- Lightning weapon
- Holy weapon
- Magic weapon with attack VFX
- Conditional VFX (changes based on environment)
- Multi-layer complex VFX
- Quick reference table of existing VFX UUIDs

### 3. Updated Snippets
**New code snippets** in `.vscode/snippets.code-snippets`:
- `weaponvfx` - Complete MultiEffectInfo template
- `weaponvfxstatus` - VFX status entry
- `weaponwithvfx` - Weapon with VFX support

---

## 🚀 Quick Start (3 Steps!)

### Step 1: Pick Existing VFX
Browse your `MultiEffectInfos/` folder:
```bash
ls MultiEffectInfos/Weapon_*.lsf.lsx
```

Popular choices:
- `Weapon_Dawnblade_*.lsf.lsx` - Fire glow
- `Weapon_Moonveil_*.lsf.lsx` - Blue magic  
- Thor Fury files - Lightning
- Excalibur files - Holy light

### Step 2: Create Status Entry

Type `weaponvfxstatus` + Tab in any .txt file:

```bg3txt
new entry "MY_WEAPON_VFX"
type "StatusData"
data "StatusType" "BOOST"
data "DisplayName" "hYOUR-HANDLE;1"
data "Description" "hYOUR-HANDLE;1"
data "StatusEffect" "UUID-FROM-VFX-FILE"  // Copy from chosen VFX file
data "StatusPropertyFlags" "DisableOverhead;DisableCombatlog;DisablePortraitIndicator"
```

### Step 3: Add to Weapon

In your weapon entry:
```bg3txt
data "OnEquipFunctors" "ApplyEquipmentStatus(MainHand, MY_WEAPON_VFX)"
data "OnUnequipFunctors" "RemoveStatus(MY_WEAPON_VFX)"
```

**Done!** Test in-game by equipping the weapon.

---

## 📋 VFX Methods Available

### Method 1: Passive/Always-On VFX
Best for: Glowing weapons, auras, ambient effects
- Weapon glows when equipped
- Simple to implement
- See Example 1-2 in VFX_EXAMPLES.md

### Method 2: Attack VFX
Best for: Attack effects, spell-like abilities
- VFX on windup, cast, and hit
- Uses PrepareEffect, CastEffect, TargetEffect
- See Example 4 in VFX_EXAMPLES.md

### Method 3: Conditional VFX
Best for: Dynamic effects triggered by conditions
- Changes based on environment (sunlight, etc.)
- Uses passives and conditions
- See Example 5 in VFX_EXAMPLES.md

---

## 🎨 Your Existing VFX Library

### Weapon Effects (Already in Your Mod)
| VFX Name | UUID | Effect |
|----------|------|--------|
| Dawnblade | `5da5cf33-66ec-4272-8000-894328c0af59` | 🔥 Fire |
| Moonveil | `cd50f25e-1d08-40fe-960b-1552a18d709a` | 🔵 Blue Magic |
| Excalibur | `e25bcfdf-9365-4959-955d-a42864174724` | ✨ Holy |
| Thor Fury | `561cc499-2e43-45aa-8baf-545da42c121b` | ⚡ Lightning |
| Shadow of Morpheus | `267ce8f3-a204-41a1-b05f-338792cf17f4` | 🌑 Shadow |
| Demon's Ruin | `1fe2a97e-200f-4f4b-ab72-8054818f87ea` | 🔴 Demonic |
| Celestial Huntress | `b4d0fd4f-d9fa-4193-a303-1d970b364ad3` | ⭐ Celestial |

Plus 100+ more spell and effect VFX!

---

## 💡 Common Use Cases

### Add Fire Glow to Sword
```bg3txt
// Reuse Dawnblade VFX
data "StatusEffect" "5da5cf33-66ec-4272-8000-894328c0af59"
```

### Add Lightning to Weapon
```bg3txt
// Reuse Thor Fury VFX
data "StatusEffect" "561cc499-2e43-45aa-8baf-545da42c121b"
```

### Add Holy Light to Weapon
```bg3txt
// Reuse Excalibur VFX
data "StatusEffect" "e25bcfdf-9365-4959-955d-a42864174724"
```

### Add Blue Magic Glow
```bg3txt
// Reuse Moonveil VFX
data "StatusEffect" "cd50f25e-1d08-40fe-960b-1552a18d709a"
```

---

## 🔧 Code Snippets Usage

### Create New VFX File
1. Create new .lsx file in MultiEffectInfos/
2. Type `weaponvfx` + Tab
3. Fill in UUIDs (use BG3 Mod Helper)
4. Choose EffectResourceGuid from existing VFX

### Create VFX Status
1. Open any Stats .txt file
2. Type `weaponvfxstatus` + Tab
3. Fill in the UUIDs
4. Done!

### Create Weapon with VFX
1. Type `weaponwithvfx` + Tab
2. Fill in weapon stats
3. Specify VFX status name
4. Complete!

---

## 📚 Documentation Index

| Guide | Purpose | Lines |
|-------|---------|-------|
| [VFX_WEAPON_GUIDE.md](VFX_WEAPON_GUIDE.md) | Complete reference | 500+ |
| [VFX_EXAMPLES.md](VFX_EXAMPLES.md) | Copy-paste templates | 400+ |
| [QUICK_REFERENCE.md](QUICK_REFERENCE.md) | Quick commands | Updated |
| [EXTENSIONS_GUIDE.md](EXTENSIONS_GUIDE.md) | Extension docs | Comprehensive |

---

## 🎯 Next Steps

### Beginner: Use Existing VFX
1. Pick a VFX from your library
2. Create status entry (copy from examples)
3. Add OnEquipFunctors to weapon
4. Test!

### Intermediate: Customize Existing VFX
1. Copy existing MultiEffectInfo file
2. Change UUID (generate new one)
3. Optionally change EffectResourceGuid
4. Create new status pointing to it
5. Apply to weapon

### Advanced: Layer Multiple VFX
1. Create MultiEffectInfo with multiple EffectInfo nodes
2. Each can have different VFX on different bones
3. Create status referencing main UUID
4. Achieve complex visual effects

---

## 🐛 Troubleshooting Quick Fixes

### VFX Not Showing
```bash
# Check these:
1. UUID matches in Status and MultiEffectInfo ✓
2. Enabled="True" in MultiEffectInfo ✓
3. OnEquipFunctors in weapon ✓
4. Weapon equipped in MainHand ✓
```

### VFX Wrong Position
```xml
<!-- Try different bones -->
<attribute id="Value" type="LSString" value="DummyFX" />
<!-- or -->
<attribute id="Value" type="LSString" value="Dummy_FX_01" />
```

### VFX Stays After Unequip
```bg3txt
data "OnUnequipFunctors" "RemoveStatus(YOUR_VFX_STATUS)"
```

---

## ⚡ Pro Tips

1. **Start with existing VFX** - Don't create new ones yet
2. **Test one weapon first** - Get workflow down
3. **Use snippets** - Save tons of typing
4. **Hover UUIDs** - BG3 GUID Infos shows info
5. **Format regularly** - Ctrl+Shift+I keeps files clean

---

## 🎮 Testing Checklist

- [ ] Weapon entry has OnEquipFunctors
- [ ] Status entry created with correct UUID
- [ ] MultiEffectInfo file exists (or reusing existing)
- [ ] UUIDs match between status and VFX file
- [ ] Localization handles generated
- [ ] Tested in Character Creator
- [ ] Tested combat with weapon
- [ ] VFX appears on equip
- [ ] VFX disappears on unequip

---

**You're all set to add stunning VFX to your weapons!** 

Start with [VFX_EXAMPLES.md](VFX_EXAMPLES.md) for ready-to-use templates.

See [VFX_WEAPON_GUIDE.md](VFX_WEAPON_GUIDE.md) for complete documentation.

Press `Ctrl+Shift+P` → type `BG3` for all mod helper commands!
