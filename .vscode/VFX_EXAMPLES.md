# Quick VFX Examples - Copy & Paste Templates

## Example 1: Fire Glow Weapon (Like Dawnblade)

### MultiEffectInfo File
**Location**: `MultiEffectInfos/Weapon_FireGlow_[YOUR-UUID].lsf.lsx`

```xml
<?xml version="1.0" encoding="utf-8"?>
<save>
	<version major="4" minor="0" revision="9" build="323" lslib_meta="v1,bswap_guids" />
	<region id="MultiEffectInfos">
		<node id="MultiEffectInfos">
			<attribute id="UUID" type="guid" value="YOUR-VFX-UUID-HERE" />
			<attribute id="Name" type="LSString" value="Weapon_FireGlow_StatusEffect" />
			<children>
				<node id="EffectInfo">
					<attribute id="UUID" type="guid" value="YOUR-EFFECT-UUID-HERE" />
					<!-- Fire glow effect from game -->
					<attribute id="EffectResourceGuid" type="guid" value="2d88a905-4148-0a2c-3187-0f56d9dbefeb" />
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

### Status Entry
**Add to**: `Stats/Generated/Data/Status_*.txt`

```bg3txt
new entry "FIRE_WEAPON_VFX"
type "StatusData"
data "StatusType" "BOOST"
data "DisplayName" "hYOUR-HANDLE;1"
data "Description" "hYOUR-HANDLE;1"
data "Icon" "Action_Generic_Magic"
data "StackId" "FIRE_WEAPON_VFX"
data "StackType" "Overwrite"
data "StatusEffect" "YOUR-VFX-UUID-HERE"
data "RemoveEvents" "OnEquipWeaponOffHand;OnUnEquipWeaponOffHand"
data "StatusPropertyFlags" "DisableOverhead;DisableCombatlog;DisablePortraitIndicator"
```

### Weapon Entry
**Add to**: `Stats/Generated/Data/Spells_Eldertide_Weapons.txt`

```bg3txt
new entry "ELDER_Weapon_FireBlade"
type "Weapon"
using "_BaseWeapon"
data "RootTemplate" "YOUR-WEAPON-ROOT-UUID"
data "Damage Type" "Slashing"
data "Damage" "1d8"
data "Rarity" "Rare"
data "Weapon Group" "MartialMeleeWeapon"
data "Weapon Properties" "Melee;Dippable;Magical;Versatile"
data "Proficiency Group" "Longswords;MartialWeapons"
data "OnEquipFunctors" "ApplyEquipmentStatus(MainHand, FIRE_WEAPON_VFX)"
data "OnUnequipFunctors" "RemoveStatus(FIRE_WEAPON_VFX)"
data "Unique" "1"
```

---

## Example 2: Lightning Weapon (Like Thor Fury)

### Reuse Existing VFX
**No new MultiEffectInfo needed!** Reference existing file.

### Status Entry
```bg3txt
new entry "LIGHTNING_WEAPON_VFX"
type "StatusData"
data "StatusType" "BOOST"
data "DisplayName" "hYOUR-HANDLE;1"
data "Description" "hYOUR-HANDLE;1"
data "Icon" "Spell_Evocation_ChainLightning"
data "StackId" "LIGHTNING_WEAPON_VFX"
data "StackType" "Overwrite"
data "StatusEffect" "561cc499-2e43-45aa-8baf-545da42c121b"  // Thor Fury VFX UUID
data "StatusPropertyFlags" "DisableOverhead;DisableCombatlog;DisablePortraitIndicator"
```

### Weapon Entry
```bg3txt
new entry "ELDER_Weapon_LightningBlade"
type "Weapon"
using "_BaseWeapon"
data "RootTemplate" "YOUR-WEAPON-ROOT-UUID"
data "Damage Type" "Slashing"
data "Damage" "1d8"
data "DefaultBoosts" "WeaponDamage(1d4,Lightning);WeaponProperty(Magical);WeaponEnchantment(2)"
data "Rarity" "Legendary"
data "OnEquipFunctors" "ApplyEquipmentStatus(MainHand, LIGHTNING_WEAPON_VFX)"
data "OnUnequipFunctors" "RemoveStatus(LIGHTNING_WEAPON_VFX)"
```

---

## Example 3: Holy Glow Weapon

### Status Entry (Using Generic Dawnblade VFX)
```bg3txt
new entry "HOLY_WEAPON_VFX"
type "StatusData"
data "StatusType" "BOOST"
data "DisplayName" "hYOUR-HANDLE;1"
data "Description" "hYOUR-HANDLE;1"
data "Icon" "Action_Paladin_LayOnHands"
data "StatusEffect" "00278d5d-c193-4ae2-9cd1-2402c12a7181"  // Generic Dawnblade VFX
data "StatusPropertyFlags" "DisableOverhead;DisableCombatlog;DisablePortraitIndicator"
```

---

## Example 4: Magic Weapon with Attack VFX

### Weapon with Spell-like Attack
```bg3txt
new entry "ELDER_Weapon_MagicBlade"
type "Weapon"
using "_BaseWeapon"
data "RootTemplate" "YOUR-WEAPON-ROOT-UUID"
data "Damage Type" "Slashing"
data "Damage" "1d8"
data "DefaultBoosts" "WeaponDamage(1d6,Force);WeaponProperty(Magical);WeaponEnchantment(2)"
data "BoostsOnEquipMainHand" "UnlockSpell(Target_PommelStrike);UnlockSpell(ELDER_Target_MagicSlash)"
data "OnEquipFunctors" "ApplyEquipmentStatus(MainHand, MAGIC_WEAPON_VFX)"
data "OnUnequipFunctors" "RemoveStatus(MAGIC_WEAPON_VFX)"

// Custom weapon action with VFX
new entry "ELDER_Target_MagicSlash"
type "SpellData"
data "SpellType" "Target"
using "Target_MainHandAttack"
data "Cooldown" "OncePerShortRest"
data "SpellSuccess" "TARGET:DealDamage(MainMeleeWeapon, MainMeleeWeaponDamageType);TARGET:DealDamage(2d6,Force);ExecuteWeaponFunctors(MainHand)"
data "DisplayName" "hYOUR-HANDLE;1"
data "Description" "hYOUR-HANDLE;1"
data "Icon" "Action_Generic_Magic"
data "PrepareEffect" "cd50f25e-1d08-40fe-960b-1552a18d709a"  // Moonveil glow on windup
data "CastEffect" "06d915e4-c520-4060-ab02-b1a3e2e7da99"     // Cast flash
data "TargetEffect" "57fe6957-0cad-4d39-b735-69aa7f7059e2"   // Hit impact
```

---

## Example 5: Conditional VFX (Changes in Sunlight)

### Two Different VFX Statuses
```bg3txt
new entry "DAYLIGHT_WEAPON_VFX"
type "StatusData"
data "StatusType" "BOOST"
data "DisplayName" "hYOUR-HANDLE-DAY;1"
data "Description" "hYOUR-HANDLE-DAY;1"
data "StatusEffect" "00278d5d-c193-4ae2-9cd1-2402c12a7181"  // Holy glow
data "StatusPropertyFlags" "DisableOverhead;DisableCombatlog;DisablePortraitIndicator"

new entry "DARKNESS_WEAPON_VFX"
type "StatusData"
data "StatusType" "BOOST"
data "DisplayName" "hYOUR-HANDLE-NIGHT;1"
data "Description" "hYOUR-HANDLE-NIGHT;1"
data "StatusEffect" "267ce8f3-a204-41a1-b05f-338792cf17f4"  // Shadow effect
data "StatusPropertyFlags" "DisableOverhead;DisableCombatlog;DisablePortraitIndicator"
```

### Passive that Switches VFX
```bg3txt
new entry "Passive_ELDER_DayNight_Weapon"
type "PassiveData"
data "DisplayName" "hYOUR-HANDLE;1"
data "Description" "hYOUR-HANDLE;1"
data "Icon" "Icon_Passive_Generic"
data "Properties" "Highlighted"
data "StatsFunctorContext" "OnTurn"
data "Conditions" "IsInSunlight()"
data "StatsFunctors" "RemoveStatus(DARKNESS_WEAPON_VFX);ApplyStatus(DAYLIGHT_WEAPON_VFX)"

new entry "Passive_ELDER_DayNight_Weapon_Shadow"
type "PassiveData"
data "StatsFunctorContext" "OnTurn"
data "Conditions" "not IsInSunlight()"
data "StatsFunctors" "RemoveStatus(DAYLIGHT_WEAPON_VFX);ApplyStatus(DARKNESS_WEAPON_VFX)"
```

### Weapon Entry
```bg3txt
data "PassivesOnEquip" "Passive_ELDER_DayNight_Weapon;Passive_ELDER_DayNight_Weapon_Shadow"
```

---

## Example 6: Multi-Layer VFX (Complex Visual)

### MultiEffectInfo with Multiple Effects
```xml
<?xml version="1.0" encoding="utf-8"?>
<save>
	<version major="4" minor="0" revision="9" build="323" lslib_meta="v1,bswap_guids" />
	<region id="MultiEffectInfos">
		<node id="MultiEffectInfos">
			<attribute id="UUID" type="guid" value="YOUR-MAIN-VFX-UUID" />
			<attribute id="Name" type="LSString" value="Weapon_Complex_Effect" />
			<children>
				<!-- Effect 1: Blade Glow -->
				<node id="EffectInfo">
					<attribute id="UUID" type="guid" value="EFFECT-1-UUID" />
					<attribute id="EffectResourceGuid" type="guid" value="2d88a905-4148-0a2c-3187-0f56d9dbefeb" />
					<attribute id="KeepScale" type="bool" value="True" />
					<attribute id="Enabled" type="bool" value="True" />
					<children>
						<node id="TargetBone">
							<attribute id="Value" type="LSString" value="Dummy_FX_01" />
						</node>
					</children>
				</node>
				
				<!-- Effect 2: Handle Aura -->
				<node id="EffectInfo">
					<attribute id="UUID" type="guid" value="EFFECT-2-UUID" />
					<attribute id="EffectResourceGuid" type="guid" value="d8818a51-bad4-4ed5-8d01-4d53c7fbc579" />
					<attribute id="KeepScale" type="bool" value="True" />
					<attribute id="Enabled" type="bool" value="True" />
					<children>
						<node id="TargetBone">
							<attribute id="Value" type="LSString" value="Dummy_FX_02" />
						</node>
					</children>
				</node>
				
				<!-- Effect 3: Trailing Particles -->
				<node id="EffectInfo">
					<attribute id="UUID" type="guid" value="EFFECT-3-UUID" />
					<attribute id="EffectResourceGuid" type="guid" value="5a5abb8e-e5c1-6005-5c9a-51cda9ca47ff" />
					<attribute id="KeepScale" type="bool" value="True" />
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

---

## Quick Reference: VFX Resource UUIDs from Your Mod

### Weapon VFX (Can Reuse)
| Name | UUID | Effect Type |
|------|------|-------------|
| Dawnblade | `5da5cf33-66ec-4272-8000-894328c0af59` | Fire glow |
| Moonveil | `cd50f25e-1d08-40fe-960b-1552a18d709a` | Blue magic |
| Excalibur | `e25bcfdf-9365-4959-955d-a42864174724` | Holy light |
| Thor Fury | `561cc499-2e43-45aa-8baf-545da42c121b` | Lightning |
| Witcher Quen | `32ee5119-7775-4eb2-a292-4ef8a297db28` | Yellow shield |
| Witcher Igni | `e445e849-e220-4763-8d7f-34b8485f8277` | Fire |
| Shadow | `267ce8f3-a204-41a1-b05f-338792cf17f4` | Dark aura |
| Generic Dawnblade | `00278d5d-c193-4ae2-9cd1-2402c12a7181` | Golden glow |
| Generic Moonveil | `6edd2b2a-045e-433b-b135-cb091bc77c32` | Blue aura |

### Spell VFX (For Attack Effects)
| Name | UUID | Use For |
|------|------|---------|
| Holy Strike | `825de76e-2f1d-4e1a-a75d-ff602e9039a9` | Radiant attacks |
| Bat Swarm | `70d6ecde-3900-4c26-aeac-42889855b461` | Necrotic effects |
| Scarlet Mist | `0c568348-b13c-45ca-9270-01d6309ddfbe` | Blood effects |
| Dream Echo Blue | `7e2e80d8-db62-4298-b741-1859ebb83526` | Psychic/blue |
| Dream Echo Purple | `6a657db7-b508-4729-8fac-5653ebb0408b` | Psychic/purple |

---

## Workflow: Add VFX to Existing Weapon

### Step 1: Choose VFX
Browse `MultiEffectInfos/` folder, pick a VFX you like

### Step 2: Create Status
```bg3txt
new entry "MY_WEAPON_VFX"
type "StatusData"
data "StatusType" "BOOST"
data "StatusEffect" "UUID-FROM-MULTIEFFECTINFO-FILE"
data "StatusPropertyFlags" "DisableOverhead;DisableCombatlog;DisablePortraitIndicator"
```

### Step 3: Apply to Weapon
Find your weapon entry, add:
```bg3txt
data "OnEquipFunctors" "ApplyEquipmentStatus(MainHand, MY_WEAPON_VFX)"
data "OnUnequipFunctors" "RemoveStatus(MY_WEAPON_VFX)"
```

### Step 4: Test
Load game, equip weapon, see VFX!

---

## Pro Tips

1. **Start Simple**: Use existing VFX first before creating new ones
2. **Copy Similar**: Find a weapon with similar VFX, copy and modify
3. **Test Bones**: Try different TargetBone values if VFX position is wrong
4. **Layer Effects**: Combine multiple VFX for complex visuals
5. **Performance**: Don't overload with too many effects (2-3 max per weapon)

---

## Troubleshooting

### VFX Not Showing
- ✅ Check UUID matches between Status and MultiEffectInfo
- ✅ Verify `Enabled="True"` in MultiEffectInfo
- ✅ Check weapon has OnEquipFunctors

### VFX in Wrong Position
- Try different TargetBone: `DummyFX`, `Dummy_FX_01`, `VFXBone`
- Check weapon model has that bone (not all weapons have all bones)

### VFX Stays After Unequip
- Add OnUnequipFunctors with RemoveStatus
- Check RemoveEvents in status definition

### VFX Too Big/Small
- Adjust `KeepScale` to `False`
- Add `UseScaleOverride="True"` and scale attributes

---

**Pick an example, replace UUIDs, and you're ready to go!**

Use `Ctrl+Shift+P` → `BG3: Generate UUID` for all UUID placeholders.
