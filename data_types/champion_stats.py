from data_types.data_type_base import DataTypeBase

class ChampionStats(DataTypeBase):
    ability_haste: float
    ability_power: float
    armor: float
    armor_penetration_flat: float
    armor_penetration_percent: float
    attack_damage: float
    attack_range: float
    attack_speed: float
    bonus_armor_penetration_percent: float
    bonus_magic_penetration_percent: float
    crit_chance: float
    crit_damage: float
    current_health: float
    heal_shield_power: float
    health_regen_rate: float
    life_steal: float
    magic_lethality: float
    magic_penetration_flat: float
    magic_penetration_percent: float
    magic_resist: float
    max_health: float
    move_speed: float
    omnivamp: float
    physical_lethality: float
    physical_vamp: float
    resource_max: float
    resource_regen_rate: float
    resource_type: str
    resource_value: float
    spell_vamp: float
    tenacity: float

    def parse(self, target_dict: dict):
        self.ability_haste = target_dict['abilityHaste']
        self.ability_power = target_dict['abilityPower']
        self.armor = target_dict['armor']
        self.armor_penetration_flat = target_dict['armorPenetrationFlat']
        self.armor_penetration_percent = target_dict['armorPenetrationPercent']
        self.attack_damage = target_dict['attackDamage']
        self.attack_range = target_dict['attackRange']
        self.attack_speed = target_dict['attackSpeed']
        self.bonus_armor_penetration_percent = target_dict['bonusArmorPenetrationPercent']
        self.bonus_magic_penetration_percent = target_dict['bonusMagicPenetrationPercent']
        self.crit_chance = target_dict['critChance']
        self.crit_damage = target_dict['critDamage']
        self.current_health = target_dict['currentHealth']
        self.heal_shield_power = target_dict['healShieldPower']
        self.health_regen_rate = target_dict['healthRegenRate']
        self.life_steal = target_dict['lifeSteal']
        self.magic_lethality = target_dict['magicLethality']
        self.magic_penetration_flat = target_dict['magicPenetrationFlat']
        self.magic_penetration_percent = target_dict['magicPenetrationPercent']
        self.magic_resist = target_dict['magicResist']
        self.max_health = target_dict['maxHealth']
        self.move_speed = target_dict['moveSpeed']
        self.omnivamp = target_dict['omnivamp']
        self.physical_lethality = target_dict['physicalLethality']
        self.physical_vamp = target_dict['physicalVamp']
        self.resource_max = target_dict['resourceMax']
        self.resource_regen_rate = target_dict['resourceRegenRate']
        self.resource_type = target_dict['resourceType']
        self.resource_value = target_dict['resourceValue']
        self.spell_vamp = target_dict['spellVamp']
        self.tenacity = target_dict['tenacity']
