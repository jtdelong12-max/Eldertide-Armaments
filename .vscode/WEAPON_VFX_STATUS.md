# Weapon VFX Status Report

## Summary

**Total Weapons**: 15  
**Weapons with VFX Files**: 6 (40%)  
**Weapons Missing VFX**: 9 (60%)

---

## ✅ Weapons WITH VFX Files

These weapons have dedicated MultiEffectInfo VFX files:

| # | Weapon Name | VFX File | UUID |
|---|-------------|----------|------|
| 1 | **Dawnblade** | Weapon_Dawnblade_*.lsf.lsx | `5da5cf33-66ec-4272-8000-894328c0af59` |
| 2 | **CelestialHuntress** | Weapon_CelestialHuntress_*.lsf.lsx | `b4d0fd4f-d9fa-4193-a303-1d970b364ad3` |
| 3 | **DemonsRuin** | Weapon_DemonsRuin_*.lsf.lsx | `1fe2a97e-200f-4f4b-ab72-8054818f87ea` |
| 4 | **ShadowOfMorpheus** | Weapon_ShadowOfMorpheus_*.lsf.lsx | `267ce8f3-a204-41a1-b05f-338792cf17f4` |
| 5 | **Excalibur** | Weapon_Excalibur_*.lsf.lsx | `e25bcfdf-9365-4959-955d-a42864174724` |
| 6 | **Moonveil** | Weapon_Moonveil_*.lsf.lsx | `cd50f25e-1d08-40fe-960b-1552a18d709a` |

### ⚠️ Important Note
**NONE of these weapons currently apply their VFX in-game!**

The VFX files exist, but the weapons don't have:
- `OnEquipFunctors` to apply VFX status
- `OnUnequipFunctors` to remove VFX status
- VFX status entries in Status files

**Action Needed**: Add OnEquipFunctors to these 6 weapons to activate their VFX.

---

## ❌ Weapons WITHOUT VFX Files

These weapons have no dedicated VFX files yet:

| # | Weapon Name | Type | Rarity | Theme |
|---|-------------|------|--------|-------|
| 1 | **RighteousAvenger** | Rapier | Very Rare | Bleeding/Command |
| 2 | **JudgmentOfAnubis** | Unknown | Unknown | Egyptian/Death |
| 3 | **BloodmoonFang** | Unknown | Unknown | Blood/Moon |
| 4 | **Ridgebreaker** | Unknown | Unknown | Earth/Breaking |
| 5 | **EladrinReach** | Unknown | Unknown | Fey/Magic |
| 6 | **TheDreamweaver** | Unknown | Unknown | Dream/Psychic |
| 7 | **Wildheart** | Unknown | Unknown | Nature/Primal |
| 8 | **WrathOfAsmodeus** | Unknown | Unknown | Infernal/Devil |
| 9 | **Aetherius** | Unknown | Unknown | Ethereal/Arcane |

---

## Recommended Actions

### Immediate: Activate Existing VFX (6 Weapons)

For each weapon with a VFX file, you need to:

1. **Create VFX Status Entry** (in Status files):
```bg3txt
new entry "WEAPON_NAME_VFX"
type "StatusData"
data "StatusType" "BOOST"
data "DisplayName" "hYOUR_HANDLE;1"
data "Description" "hYOUR_HANDLE;1"
data "Icon" "Action_Generic_Magic"
data "StatusEffect" "VFX-UUID-FROM-FILE"
data "StatusPropertyFlags" "DisableOverhead;DisableCombatlog;DisablePortraitIndicator"
```

2. **Add to Weapon Entry**:
```bg3txt
data "OnEquipFunctors" "ApplyEquipmentStatus(MainHand, WEAPON_NAME_VFX)"
data "OnUnequipFunctors" "RemoveStatus(WEAPON_NAME_VFX)"
```

### Priority Order for Activating Existing VFX

#### High Priority (Legendary Weapons)
1. **Dawnblade** - Fire sword, already has fire VFX
2. **Excalibur** - Holy sword, has golden glow VFX
3. **Moonveil** - Magic sword, has blue glow VFX

#### Medium Priority
4. **ShadowOfMorpheus** - Shadow weapon, has dark VFX
5. **DemonsRuin** - Demonic weapon, has infernal VFX
6. **CelestialHuntress** - Celestial bow, has heavenly VFX

---

## Adding VFX to the 9 Weapons Without VFX

### Option 1: Reuse Existing VFX (Fastest)

Match weapons to existing VFX based on theme:

| Weapon | Suggested VFX | Why |
|--------|---------------|-----|
| **WrathOfAsmodeus** | DemonsRuin VFX | Both infernal/demonic |
| **BloodmoonFang** | Scarlet Mist VFX | Blood theme |
| **JudgmentOfAnubis** | Shadow/Necrotic VFX | Death/underworld theme |
| **Wildheart** | Nature-themed spell VFX | Primal/natural |
| **TheDreamweaver** | Dream Echo VFX | Psychic/dream theme |
| **Aetherius** | Moonveil VFX | Ethereal/arcane |
| **EladrinReach** | Celestial/Magic VFX | Fey magic |
| **Ridgebreaker** | Earth/Stone VFX | Breaking/impact |
| **RighteousAvenger** | Holy Strike VFX | Justice/righteousness |

### Option 2: Create New VFX Files (Custom)

Copy and modify existing VFX files:
1. Pick a similar weapon's VFX file
2. Copy to new file with weapon name
3. Generate new UUID for main effect
4. Optionally change EffectResourceGuid for different look
5. Create status and apply to weapon

---

## Quick Fix: Activate Dawnblade VFX (Example)

### Step 1: Create Status
Add to a Status file:
```bg3txt
new entry "DAWNBLADE_VFX"
type "StatusData"
data "StatusType" "BOOST"
data "DisplayName" "h[GENERATE_HANDLE];1"
data "Description" "h[GENERATE_HANDLE];1"
data "Icon" "Action_Generic_Magic"
data "StatusEffect" "5da5cf33-66ec-4272-8000-894328c0af59"
data "StatusPropertyFlags" "DisableOverhead;DisableCombatlog;DisablePortraitIndicator"
```

### Step 2: Modify Weapon Entry
Find "ELDER_Weapon_Dawnblade" entry, add after line 24:
```bg3txt
data "OnEquipFunctors" "ApplyEquipmentStatus(MainHand, DAWNBLADE_VFX)"
data "OnUnequipFunctors" "RemoveStatus(DAWNBLADE_VFX)"
```

### Step 3: Localization
Generate handles for DisplayName and Description with `Ctrl+Shift+P` → `BG3: Generate Handle`

---

## Implementation Checklist

### Phase 1: Activate Existing VFX
- [ ] Create status entries for 6 weapons with VFX files
- [ ] Add OnEquipFunctors/OnUnequipFunctors to weapons
- [ ] Generate localization handles
- [ ] Test in-game

### Phase 2: Add VFX to Remaining Weapons
- [ ] Identify theme for each weapon
- [ ] Match to existing VFX or create new
- [ ] Create status entries
- [ ] Apply to weapons
- [ ] Test

### Phase 3: Polish
- [ ] Verify all VFX display correctly
- [ ] Check VFX positioning on different weapon types
- [ ] Ensure VFX remove properly on unequip
- [ ] Add lore-appropriate descriptions

---

## Estimated Work

### Activate Existing VFX (6 weapons)
- **Time**: 30-60 minutes
- **Difficulty**: Easy
- **Files to Edit**: 2 (Status file + Weapon file)
- **Lines to Add**: ~15 lines per weapon = 90 lines total

### Add VFX to Remaining (9 weapons)
- **Time**: 1-3 hours (depending on custom vs reuse)
- **Difficulty**: Easy if reusing, Medium if creating new
- **Files to Create/Edit**: 3+ per weapon
- **Estimated**: 135-200 lines total

---

## Templates Ready to Use

All templates available in:
- [VFX_EXAMPLES.md](VFX_EXAMPLES.md) - Copy-paste examples
- [VFX_WEAPON_GUIDE.md](VFX_WEAPON_GUIDE.md) - Detailed guide
- Snippets: `weaponvfxstatus` and `weaponwithvfx`

---

## Next Steps

1. **Start with Dawnblade** - It's the flagship weapon with existing VFX
2. **Test the workflow** - Make sure VFX applies and removes correctly
3. **Batch activate** - Apply to remaining 5 weapons with VFX files
4. **Plan remaining 9** - Decide which VFX to use for each
5. **Implement and test** - Add VFX to all weapons

---

**Would you like me to create the status entries and weapon modifications for the 6 weapons that already have VFX files?**
