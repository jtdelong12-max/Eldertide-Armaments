# Adding VFX to Modded Weapons - Complete Guide

## Overview

Your mod already has VFX infrastructure set up! You have:
- 📁 `EldertideVFX/` - VFX mod folder
- 📁 `MultiEffectInfos/` - Over 100 VFX definition files
- ✅ Existing weapons with VFX (Dawnblade, Moonveil, Excalibur, etc.)

## VFX Integration Methods

### Method 1: Passive/Status VFX (Always Active)
Best for: Glowing weapons, auras, ambient effects

### Method 2: Attack VFX (On Hit/Cast)
Best for: Attack effects, spell-like weapon abilities

### Method 3: Conditional VFX (Triggered)
Best for: Effects that activate under specific conditions

---

## Method 1: Passive Weapon VFX (Glowing Effect)

### Step 1: Create MultiEffectInfo File

**Location**: `EldertideArmament/Public/EldertideArmament/MultiEffectInfos/`

**Example**: `Weapon_MyWeapon_[UUID].lsf.lsx`

```xml
<?xml version="1.0" encoding="utf-8"?>
<save>
	<version major="4" minor="0" revision="9" build="323" lslib_meta="v1,bswap_guids" />
	<region id="MultiEffectInfos">
		<node id="MultiEffectInfos">
			<!-- MAIN UUID: Use BG3 Mod Helper to generate -->
			<attribute id="UUID" type="guid" value="YOUR-VFX-UUID-HERE" />
			<attribute id="Name" type="LSString" value="Weapon_MyWeapon_StatusEffect" />
			<children>
				<!-- VFX Effect 1: Glow/Aura -->
				<node id="EffectInfo">
					<attribute id="UUID" type="guid" value="EFFECT-UUID-1" />
					<!-- Effect from game's VFX library -->
					<attribute id="EffectResourceGuid" type="guid" value="GAME-VFX-RESOURCE-UUID" />
					<attribute id="DetachSource" type="bool" value="False" />
					<attribute id="DetachTarget" type="bool" value="False" />
					<attribute id="KeepRotation" type="bool" value="False" />
					<attribute id="KeepScale" type="bool" value="True" />
					<attribute id="MainHand" type="bool" value="False" />
					<attribute id="OffHand" type="bool" value="False" />
					<attribute id="BindSourceTo" type="FixedString" value="SourceEntity" />
					<attribute id="BindTargetTo" type="FixedString" value="TargetEntity" />
					<attribute id="Pivot" type="FixedString" value="Target" />
					<attribute id="Enabled" type="bool" value="True" />
					<children>
						<!-- Where VFX attaches on weapon -->
						<node id="TargetBone">
							<attribute id="Value" type="LSString" value="DummyFX" />
						</node>
					</children>
				</node>
			</children>
		</node>
	</region>
</save>
```

### Step 2: Create Status Entry in Stats

**Location**: `Stats/Generated/Data/Status_*.txt`

```bg3txt
new entry "MY_WEAPON_VFX"
type "StatusData"
data "StatusType" "BOOST"
data "DisplayName" "hYOUR_HANDLE_HERE;1"
data "Description" "hYOUR_HANDLE_HERE;1"
data "Icon" "Action_Generic_Magic"
data "StackId" "MY_WEAPON_VFX"
data "StackType" "Overwrite"
data "StatusEffect" "YOUR-VFX-UUID-HERE"  // Same as MultiEffectInfo UUID
data "RemoveEvents" "OnEquipWeaponOffHand;OnUnEquipWeaponOffHand"
data "RemoveConditions" ""
data "StatusPropertyFlags" "DisableOverhead;DisableCombatlog;DisablePortraitIndicator"
```

### Step 3: Apply Status to Weapon

**Location**: `Stats/Generated/Data/Spells_Eldertide_Weapons.txt`

```bg3txt
new entry "ELDER_Weapon_MyWeapon"
type "Weapon"
using "_BaseWeapon"
data "RootTemplate" "YOUR-WEAPON-UUID"
data "Damage Type" "Slashing"
data "Damage" "1d8"
// ... other stats ...

// Apply VFX status on equip
data "OnEquipFunctors" "ApplyEquipmentStatus(MainHand, MY_WEAPON_VFX)"
data "OnUnequipFunctors" "RemoveStatus(MY_WEAPON_VFX)"
```

---

## Method 2: Attack VFX (Weapon Actions)

### Add VFX to Weapon Attacks

**In your weapon action spells**:

```bg3txt
new entry "ELDER_Target_MyWeaponAttack"
type "SpellData"
data "SpellType" "Target"
using "Target_MainHandAttack"
// ... other properties ...

// VFX on prepare, cast, and hit
data "PrepareEffect" "YOUR-PREPARE-VFX-UUID"    // Shows during windup
data "CastEffect" "YOUR-CAST-VFX-UUID"          // Shows on swing
data "TargetEffect" "YOUR-HIT-VFX-UUID"         // Shows on impact
```

### Common Game VFX Resource UUIDs

#### Fire Effects
- Fire Glow: `2d88a905-4148-0a2c-3187-0f56d9dbefeb`
- Fire Trail: `5a5abb8e-e5c1-6005-5c9a-51cda9ca47ff`

#### Magic Effects  
- Blue Glow: `d8818a51-bad4-4ed5-8d01-4d53c7fbc579`
- Purple Aura: Various in your existing files
- Holy Light: Check `Generic_Dawnblade_*.lsf.lsx`

#### Elemental
- Lightning: Check `ThorFury_*.lsf.lsx`
- Ice/Frost: Check game resources
- Poison: Check `Venomstrike_*.lsf.lsx`

---

## Method 3: Conditional VFX via Passives

### Create a Passive that Applies VFX

```bg3txt
new entry "Passive_ELDER_MyWeapon_Effect"
type "PassiveData"
data "DisplayName" "hYOUR_HANDLE;1"
data "Description" "hYOUR_HANDLE;1"
data "Icon" "Icon_Passive_Generic"
data "Properties" "IsHidden"  // Or "Highlighted" to show in UI
data "StatsFunctorContext" "OnStatusApply"
data "Conditions" "StatusId('MY_WEAPON_VFX')"
data "StatsFunctors" "ApplyStatus(MY_WEAPON_VFX, 100, -1)"
```

### Apply Passive to Weapon

```bg3txt
data "PassivesOnEquip" "Passive_ELDER_MyWeapon_Effect"
```

---

## Targeting Specific Weapon Bones

### Common Weapon Attachment Points

| Bone Name | Location | Best For |
|-----------|----------|----------|
| `DummyFX` | Main effect point | General glows |
| `Dummy_FX_01` | Blade/head | Blade effects |
| `Dummy_FX_02` | Handle | Grip effects |
| `VFXBone` | Center | Centered effects |
| `Root` | Base of weapon | Base auras |

### Example: Multi-Point VFX

```xml
<node id="EffectInfo"> <!-- Blade Glow -->
	<attribute id="UUID" type="guid" value="EFFECT-UUID-1" />
	<attribute id="EffectResourceGuid" type="guid" value="BLADE-VFX" />
	<children>
		<node id="TargetBone">
			<attribute id="Value" type="LSString" value="Dummy_FX_01" />
		</node>
	</children>
</node>

<node id="EffectInfo"> <!-- Handle Glow -->
	<attribute id="UUID" type="guid" value="EFFECT-UUID-2" />
	<attribute id="EffectResourceGuid" type="guid" value="HANDLE-VFX" />
	<children>
		<node id="TargetBone">
			<attribute id="Value" type="LSString" value="Dummy_FX_02" />
		</node>
	</children>
</node>
```

---

## Step-by-Step: Add Glow to Existing Weapon

### Example: Add Lightning VFX to a Weapon

#### 1. Generate UUIDs
```
Ctrl+Shift+P → BG3: Generate UUID
- Main VFX UUID: abc12345-xxxx-xxxx-xxxx-xxxxxxxxxxxx
- Effect UUID: def67890-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

#### 2. Create MultiEffectInfo
**File**: `MultiEffectInfos/Weapon_Lightning_abc12345-xxxx-xxxx-xxxx-xxxxxxxxxxxx.lsf.lsx`

```xml
<?xml version="1.0" encoding="utf-8"?>
<save>
	<version major="4" minor="0" revision="9" build="323" lslib_meta="v1,bswap_guids" />
	<region id="MultiEffectInfos">
		<node id="MultiEffectInfos">
			<attribute id="UUID" type="guid" value="abc12345-xxxx-xxxx-xxxx-xxxxxxxxxxxx" />
			<attribute id="Name" type="LSString" value="Weapon_Lightning_Effect" />
			<children>
				<node id="EffectInfo">
					<attribute id="UUID" type="guid" value="def67890-xxxx-xxxx-xxxx-xxxxxxxxxxxx" />
					<attribute id="EffectResourceGuid" type="guid" value="561cc499-2e43-45aa-8baf-545da42c121b" />
					<attribute id="DetachSource" type="bool" value="False" />
					<attribute id="DetachTarget" type="bool" value="False" />
					<attribute id="KeepRotation" type="bool" value="False" />
					<attribute id="KeepScale" type="bool" value="True" />
					<attribute id="BindSourceTo" type="FixedString" value="SourceEntity" />
					<attribute id="BindTargetTo" type="FixedString" value="TargetEntity" />
					<attribute id="Pivot" type="FixedString" value="Target" />
					<attribute id="Enabled" type="bool" value="True" />
					<children>
						<node id="TargetBone">
							<attribute id="Value" type="LSString" value="DummyFX" />
						</node>
					</children>
				</node>
			</children>
		</node>
	</region>
</save>
```

#### 3. Create Status
**File**: `Stats/Generated/Data/Status_*.txt`

```bg3txt
new entry "LIGHTNING_WEAPON_VFX"
type "StatusData"
data "StatusType" "BOOST"
data "DisplayName" "hYOUR_HANDLE;1"
data "Description" "hYOUR_HANDLE;1"
data "Icon" "Action_Generic_Magic"
data "StatusEffect" "abc12345-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
data "StatusPropertyFlags" "DisableOverhead;DisableCombatlog;DisablePortraitIndicator"
```

#### 4. Apply to Weapon
```bg3txt
new entry "ELDER_Weapon_LightningBlade"
type "Weapon"
using "_BaseWeapon"
data "RootTemplate" "YOUR-WEAPON-UUID"
// ... other stats ...
data "OnEquipFunctors" "ApplyEquipmentStatus(MainHand, LIGHTNING_WEAPON_VFX)"
data "OnUnequipFunctors" "RemoveStatus(LIGHTNING_WEAPON_VFX)"
```

---

## Working with Existing VFX

### Browse Your VFX Library

You already have 100+ MultiEffectInfo files! Look in:
- `MultiEffectInfos/Weapon_*.lsf.lsx` - Weapon-specific VFX
- `MultiEffectInfos/ThorFury_*.lsf.lsx` - Lightning effects
- `MultiEffectInfos/DreamEcho_*.lsf.lsx` - Magic effects  
- `MultiEffectInfos/Generic_*.lsf.lsx` - Generic effects

### Reuse Existing VFX

Instead of creating new VFX files, reference existing ones:

```bg3txt
// Use Dawnblade's fire VFX
data "StatusEffect" "5da5cf33-66ec-4272-8000-894328c0af59"

// Use Thor Fury's lightning VFX  
data "StatusEffect" "561cc499-2e43-45aa-8baf-545da42c121b"

// Use Moonveil's glow VFX
data "StatusEffect" "cd50f25e-1d08-40fe-960b-1552a18d709a"
```

---

## VFX Properties Explained

### EffectResourceGuid
- References game's VFX assets
- You can't create new ones without modding VFX files
- Use existing game UUIDs or your custom VFX mod

### BindSourceTo / BindTargetTo
- `SourceEntity` - Effect follows the caster
- `TargetEntity` - Effect follows the target
- `SourceWeaponBone` - Attaches to weapon

### Pivot
- `Target` - Effect centers on target
- `Source` - Effect centers on source

### DetachSource / DetachTarget
- `True` - Effect stays in place when entity moves
- `False` - Effect follows entity

### KeepScale / KeepRotation
- Controls whether effect maintains original size/rotation
- Usually `True` for weapon effects

---

## Testing Your VFX

### 1. In-Game Testing
```bash
# Build your mod (if using build tools)
# Or manually copy to BG3 mods folder
```

### 2. Check in Character Creator
- Equip weapon
- VFX should appear immediately if using `OnEquipFunctors`

### 3. Test Attacks
- Use weapon action
- Check for PrepareEffect, CastEffect, TargetEffect

### 4. Debug Issues
- **VFX not showing?** Check UUID matches in MultiEffectInfo and Status
- **Wrong position?** Try different TargetBone values
- **Effect too big/small?** Adjust KeepScale or add ScaleOverride

---

## Advanced: Layer Multiple VFX

### Stack Effects for Complex Visuals

```bg3txt
new entry "MULTI_VFX_WEAPON"
type "StatusData"
data "StatusType" "BOOST"
data "StatusEffect" "VFX-UUID-1;VFX-UUID-2;VFX-UUID-3"  // Multiple UUIDs
```

### Conditional VFX Changes

```bg3txt
// Apply different VFX based on conditions
data "StatsFunctorContext" "OnAttack"
data "Conditions" "IsInSunlight()"
data "StatsFunctors" "ApplyStatus(SUNLIGHT_VFX)"

data "StatsFunctorContext" "OnAttack"  
data "Conditions" "not IsInSunlight()"
data "StatsFunctors" "ApplyStatus(SHADOW_VFX)"
```

---

## Quick Reference: Your Existing VFX

### Weapon VFX in Your Mod
| File | Effect Type | Color |
|------|-------------|-------|
| Weapon_Dawnblade | Fire glow | Orange/Red |
| Weapon_Moonveil | Magic glow | Blue |
| Weapon_Excalibur | Holy light | Gold/White |
| Weapon_DemonsRuin | Dark energy | Red/Black |
| Weapon_ShadowOfMorpheus | Shadow | Purple/Black |
| Weapon_CelestialHuntress | Celestial | Blue/White |

### Copy and Modify
1. Find a VFX file with similar effect to what you want
2. Copy the file with a new name
3. Change the UUID (use BG3 Mod Helper)
4. Optionally change EffectResourceGuid for different look
5. Reference new UUID in your weapon status

---

## Code Snippets

### BG3 VFX MultiEffectInfo Snippet

Add to `.vscode/snippets.code-snippets`:

```json
"BG3 Weapon VFX": {
  "scope": "xml",
  "prefix": "weaponvfx",
  "body": [
    "<?xml version=\"1.0\" encoding=\"utf-8\"?>",
    "<save>",
    "\t<version major=\"4\" minor=\"0\" revision=\"9\" build=\"323\" lslib_meta=\"v1,bswap_guids\" />",
    "\t<region id=\"MultiEffectInfos\">",
    "\t\t<node id=\"MultiEffectInfos\">",
    "\t\t\t<attribute id=\"UUID\" type=\"guid\" value=\"${1:vfx-uuid}\" />",
    "\t\t\t<attribute id=\"Name\" type=\"LSString\" value=\"${2:Weapon_Name_Effect}\" />",
    "\t\t\t<children>",
    "\t\t\t\t<node id=\"EffectInfo\">",
    "\t\t\t\t\t<attribute id=\"UUID\" type=\"guid\" value=\"${3:effect-uuid}\" />",
    "\t\t\t\t\t<attribute id=\"EffectResourceGuid\" type=\"guid\" value=\"${4:game-vfx-uuid}\" />",
    "\t\t\t\t\t<attribute id=\"KeepScale\" type=\"bool\" value=\"True\" />",
    "\t\t\t\t\t<attribute id=\"Enabled\" type=\"bool\" value=\"True\" />",
    "\t\t\t\t\t<children>",
    "\t\t\t\t\t\t<node id=\"TargetBone\">",
    "\t\t\t\t\t\t\t<attribute id=\"Value\" type=\"LSString\" value=\"DummyFX\" />",
    "\t\t\t\t\t\t</node>",
    "\t\t\t\t\t</children>",
    "\t\t\t\t</node>",
    "\t\t\t</children>",
    "\t\t</node>",
    "\t</region>",
    "</save>"
  ],
  "description": "BG3 Weapon VFX MultiEffectInfo template"
}
```

---

## Need Help?

### Common Issues

1. **VFX not appearing**: Check Status and MultiEffectInfo UUIDs match
2. **VFX in wrong spot**: Try different TargetBone values
3. **VFX flickers**: Check Enabled="True" in MultiEffectInfo
4. **VFX stays after unequip**: Add proper RemoveStatus in OnUnequipFunctors

### Next Steps

1. Choose a weapon to add VFX to
2. Pick an existing VFX file to copy/reference
3. Create status entry
4. Apply to weapon with OnEquipFunctors
5. Test in-game!

---

**You're ready to add VFX to your weapons!** Start with existing VFX files and modify them for your needs.
