# Bloody Rebuilded Swords Integration Plan

## Overview
The Bloody Rebuilded mod contains several demonic/blood-themed swords with spectacular VFX. These can be integrated into Eldertide Armaments with **combat-only VFX activation**.

## Available Weapons from Bloody Rebuilded

### One-Handed Variants
1. **BloodyAllegiance_Aluve** - Longsword (Force damage)
2. **BloodyAllegiance_Big** - Longsword variant (Light, NotSheathable)
3. **BloodyAllegiance_Big_Sheatable** - Sheathable version
4. **BloodyAllegiance_Giant_Onehand** - Large one-handed variant
5. **BloodyAllegiance_Giant_Onehand_Mage** - Legendary mage variant
6. **BloodyAllegiance_Silver_OneHand** - Silver variant
7. **BloodyAllegiance_Silver_OneHand_NoSheat** - Non-sheathable silver
8. **BloodyAllegiance_Silver_OneHand_Magic** - Legendary magic silver
9. **BloodyAllegiance_Rapier** - Rapier variant

### Two-Handed Variants
10. **BloodyAllegiance_Giant_Twohand** - Greatsword (2d8 Force)
11. **BloodyAllegiance_Crusher_TwoHand** - Crusher greatsword

## Key Features of Bloody Weapons

### Scaling Enchantment
- Levels 1-4: +2 enchantment
- Levels 5-9: +3 enchantment
- Levels 10+: +5 enchantment

### Unique Mechanics
1. **ItemReturnToOwner()** - Weapon returns when thrown
2. **Force Damage** - Ignores most resistances
3. **Life Steal on Crit** - Regain HP equal to DamageDone/8 on critical hits
4. **Soul Torment System** - Unique soul-catching mechanic
5. **Terror Abilities** - Fear-based attacks

### Special Abilities Unlocked
- `Target_Duo_Demonic` - Dual attack
- `Zone_Cleave_Demonic` - AoE cleave
- `Target_Heart_Demonic` - Heart strike
- `Zone_Fear_Demonic2` - Fear AoE
- `TerrorOnslaught_Original_Demon` - Terror onslaught
- `Awok_Terror_Demonic` - Awakened terror

## Combat-Only VFX System

### How It Works
The Bloody mod uses a smart system where VFX is tied to combat status:

1. **On Equip**: Applies `MAINHANDATTACK_Melee_Standart` status
   - This status includes: `StatusEffect "875f06ca-91f6-4125-933d-1589edf3902d"`
   - StatusPropertyFlags: `DisableOverhead;DisableCombatlog;DisablePortraitIndicator`
   - VFX activates automatically in combat

2. **Toggle System**: Uses `Toggled_MainMagic_Apply` passive
   - Allows switching between melee and ranged VFX
   - Player can toggle on/off

3. **Impact VFX**: Uses `Melee_Impact_Status`
   - Applied on weapon hits via WeaponFunctors
   - Creates hit effects on enemies

### Key Status Entry
```
new entry "MAINHANDATTACK_Melee_Standart"
type "StatusData"
data "StatusType" "BOOST"
data "DisplayName" "h23612148g0b1dg4d30g9830g02f8e603a2af;1"
data "Description" "hfff0b8b7g85cag4a81gafcag7dff4bdd61d5;1"
data "Icon" "Demon_MainMelee"
data "Boosts" "AttackSpellOverride(...)"
data "StatusEffect" "875f06ca-91f6-4125-933d-1589edf3902d"
data "StatusPropertyFlags" "DisableOverhead;DisableCombatlog;DisablePortraitIndicator"
data "Passives" "MeleeStance_Passive"
```

## Integration Options

### Option 1: Full Integration (Recommended)
Copy all weapons as new entries in Eldertide with "ELDER_" prefix:
- Rename: `BloodyAllegiance_X` → `ELDER_Weapon_BloodyAllegiance_X`
- Update RootTemplate UUIDs (generate new ones)
- Copy all VFX files to Eldertide MultiEffectInfos
- Copy status entries and passives
- Add Eldertide-style localization

**Pros:**
- Full control over weapons
- Can customize damage/abilities
- Integrate with Eldertide lore
- Combat-only VFX works automatically

**Cons:**
- Requires copying many files
- Need to generate new UUIDs

### Option 2: Select Favorites
Choose 2-3 best variants to add:
- Recommended: Silver_OneHand, Giant_Twohand, Rapier
- Simpler integration
- Less file copying

**Pros:**
- Faster implementation
- Cleaner mod structure
- Focus on quality over quantity

**Cons:**
- Doesn't include all variants

### Option 3: Hybrid Approach (Best Balance)
Add 4-5 weapons with different playstyles:
1. **Bloodfang** (One-hand, fast) - Based on Silver variant
2. **Crimson Reaver** (One-hand, versatile) - Based on Giant variant
3. **Soulcrusher** (Two-hand, heavy) - Based on Crusher variant
4. **Blood Rapier** (Finesse, duelist) - Based on Rapier
5. **Demonic Greatsword** (Two-hand, balanced) - Based on Twohand variant

**Pros:**
- Good variety
- Each fills a niche
- Manageable file count
- All combat-only VFX

## Required Files to Copy

### From Bloody Mod:
1. **MultiEffectInfos/** (VFX files)
   - `DefaultStatus.lsf.lsx`
   - `BloodAttackCastEffect*.lsf.lsx`
   - `HitStatusMelee*.lsf.lsx`
   - `PrepareAttack.lsf.lsx`
   - And ~20 more VFX files

2. **Status Entries**
   - `MAINHANDATTACK_Melee_Standart`
   - `Melee_Impact_Status`
   - `BloodStatusWeapon_Empty`
   - `BloodStatusWeapon_Magic`
   - Soul Torment statuses

3. **Passives**
   - `MeleeStance_Passive`
   - `Toggled_MainMagic_Apply`
   - `CritKill_Passive`
   - `CritImpactMelee_Passive`
   - `SoulsTormentApply_Status`

4. **Spells**
   - All the Demonic abilities
   - Attack overrides

5. **Localization**
   - Weapon names/descriptions
   - Ability descriptions
   - Status descriptions

## Implementation Steps

### Step 1: Prepare Files
1. Copy MultiEffectInfo VFX files to Eldertide
2. Generate new UUIDs for weapon RootTemplates
3. Copy status entries to Status_Eldertide.txt
4. Copy passive entries

### Step 2: Create Weapons
1. Add weapon entries to Spells_Eldertide_Weapons.txt
2. Use ELDER_ prefix for consistency
3. Update RootTemplate references
4. Keep combat-only VFX system intact

### Step 3: Add Localization
1. Create lore-appropriate names
2. Write descriptions matching Eldertide theme
3. Add to Weapons_EldertideArmament.loca.xml

### Step 4: Test
1. Verify VFX only activates in combat
2. Test all abilities
3. Check scaling enchantment works
4. Verify soul torment mechanics

## Combat-Only VFX vs Current System

### Current Eldertide Weapons
- VFX active **always when equipped**
- Uses simple OnEquipFunctors
- Good for constant magical weapons

### Bloody Weapons System  
- VFX active **only in combat**
- Uses status-based system
- Better for "awakening" weapons
- More dramatic/immersive

### Hybrid Approach
Could implement both:
- Keep current weapons with always-on VFX
- Add Bloody weapons with combat-only VFX
- Give players choice of VFX styles

## Recommended Implementation

### Add 5 New Weapons:

1. **Crimson Fang** (Based on Silver_OneHand)
   - One-handed, Finesse, Light
   - Force damage
   - Soul steal on crit
   - VeryRare

2. **Bloodreaver's Edge** (Based on Giant_Onehand)
   - One-handed, Versatile
   - Larger damage
   - VeryRare

3. **Soulcrusher** (Based on Crusher_TwoHand)
   - Two-handed greatsword
   - 2d8 Force damage
   - Terror abilities
   - VeryRare

4. **Crimson Duelist** (Based on Rapier)
   - Rapier, Finesse
   - Precise strikes
   - Rare

5. **Demonic Reaver** (Based on Giant_Twohand)
   - Two-handed, Heavy
   - Maximum damage
   - Legendary (magic version)

All would have:
- Combat-only VFX
- Scaling enchantments
- Soul torment mechanics
- Demonic abilities
- Life steal on crit

## Next Steps

Would you like me to:

1. **Full integration** - Add all 11 weapons with all features?
2. **Select 5 weapons** - Implement the recommended 5 above?
3. **Custom selection** - You choose which weapons to add?
4. **Preview mode** - Just add 1 weapon first to test the combat VFX system?

I can handle all the file copying, UUID generation, status creation, and localization. The combat-only VFX system will work perfectly with your mod!
