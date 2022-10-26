from django.db import models

class Yarik(models.Model):
    ac_manufacturer_choices = [('AIRBUS', 'AIRBUS'), ('EMBRAER', 'EMBRAER'), ('BOEING', 'BOEING')]
    engine_family_choice = [('CFM56-5B', 'CFM56-5B'), ('CF34-8E', "CF34-8E"), ('CFM56-7', 'CFM56-7')]
    engine_type_choice = [('CFM56-5B4', 'CFM56-5B4'), ('CF34-8E5', 'CF34-8E5'), ('CFM56-7B27/B1', 'CFM56-7B27/B1'),
                            ('CFM56-7B26', 'CFM56-7B26'), ('CFM56-5B3', 'CFM56-5B3')]
    manufacturer_choice = [('CFM INTERNATIONAL', 'CFM INTERNATIONAL'), ('GE AIRCRAFT ENGINES', 'GE AIRCRAFT ENGINES')]
    aircraft_family_choice = [('A320', 'A320'), ('EMBRAER RJ', 'EMBRAER RJ'), ('B737', 'B737')]
    aircraft_type_choice = [('A320-200', 'A320-200'), ('ERJ170', 'ERJ170'), ('B737-800', 'B737-800'), ('A321-200', 'A321-200')]
    ac_manufacturer_choices = [('AIRBUS', 'AIRBUS'), ('EMBRAER', 'EMBRAER'), ('BOEING', 'BOEING')]
    aircraft_grp_choise =  [('A320-214', 'A320-214'), ('EMBRAER 170-100', 'EMBRAER 170-100'), ('B737-83N', 'B737-83N'), ('B737-8LP', 'B737-8LP'), ('A321-211', 'A321-211'),
                            ('B737-8Q8', 'B737-8Q8'), ('B737-8ZS', 'B737-8ZS'), ('B737-8GJ', 'B737-8GJ'), ('B737-BCF', 'B737-BCF')]
    flight_phase_choise = [('TAKEOFF', 'TAKEOFF'), ('CRUISE', 'CRUISE')]

    true_false_choice = [(0.0, 0.0), (1.0, 1.0)]
    n1_modifier_choice = [(0.0, 0.0), (1.0, 1.0), (2.0, 2.0), (3.0, 3.0), (4.0, 4.0), (5.0, 5.0), (6.0, 6.0), (7.0, 7.0)]

    n1_modifier = models.CharField(max_length=10, choices=n1_modifier_choice, verbose_name="n1 modifier", null=True, blank=True)
    IBE = models.CharField(max_length=10, choices=true_false_choice, verbose_name="ENG BLEED VALVE ENG 1", null=True, blank=True)
    IBP = models.CharField(verbose_name="PACK VALVE 1", null=True, blank=True, max_length=10, choices=true_false_choice)
    IAIE = models.CharField(verbose_name="ENG ANTI-ICE SETTING", null=True, blank=True, max_length=10, choices=true_false_choice)
    aircraft_family = models.CharField(choices=aircraft_family_choice, max_length=15, verbose_name="aircraft family", null=True, blank=True)
    aircraft_type = models.CharField(choices=aircraft_type_choice, max_length=15, verbose_name="aircraft type", null=True, blank=True)
    aircraft_grp = models.CharField(choices=aircraft_grp_choise, max_length=15, verbose_name="aircraft grp", null=True, blank=True)
    ac_manufacturer = models.CharField(choices=ac_manufacturer_choices, max_length=15, verbose_name="ac manufacturer", null=True, blank=True)
    flight_phase = models.CharField(max_length=15, choices=flight_phase_choise, verbose_name="flight_phase")
    engine_family = models.CharField(max_length=15, choices=engine_family_choice, verbose_name="engine family", null=True, blank=True)
    engine_type = models.CharField(choices=engine_type_choice, max_length=15, verbose_name="engine type", default='CFM56-5B4')
    manufacturer = models.CharField(choices=manufacturer_choice, max_length=30, verbose_name="manufacturer", null=True, blank=True)


    flight_datetime = models.TextField(verbose_name="flight_datetime", null=True, blank=True)
    engine_id = models.TextField(verbose_name="engine_id", null=True, blank=True)
    aircraft_id = models.TextField(verbose_name="aircraft id", null=True, blank=True)
    engine_position = models.IntegerField(verbose_name="engine position", null=True, blank=True)
    number_blades = models.FloatField(verbose_name="number blades", null=True, blank=True)
    ZHPTAC = models.FloatField(verbose_name="HPT ACTIVE CLEARANCE CNTL", null=True, blank=True)
    ZLPTAC = models.FloatField(verbose_name="LPT ACTIVE CLEARANCE CNTL", null=True, blank=True)
    ZPCN12 = models.FloatField(verbose_name="N1 INDICATED", null=True, blank=True)
    ZPCN25 = models.FloatField(verbose_name="N2 (HIGH SPEED ROTOR)", null=True, blank=True)
    ZPHSF = models.FloatField(verbose_name="PHASE ANGLE", null=True, blank=True)
    ZPHSR = models.FloatField(verbose_name="PHASE ANGLE (REAR)", null=True, blank=True)
    ZPN12R = models.FloatField(verbose_name="CORRECTED N1 INPUT FROM FADEC (%RPM)", null=True, blank=True)
    ZPOIL = models.FloatField(verbose_name="OIL PRESSURE (PSI)", null=True, blank=True)
    ZPS3 = models.FloatField(verbose_name="PS13 (FAN OGV DISCHARGE)", null=True, blank=True)
    ZT1AB = models.FloatField(verbose_name="FAN INLET TOTAL TEMPERATURE FROM FADEC (DEG C)']", null=True, blank=True)
    ZT3 = models.FloatField(verbose_name="HPC DISCHARG TOT TEMP (DEG)", null=True, blank=True)
    ZT49 = models.FloatField(verbose_name="EGT-HPT DISCHRG TOT TMP(DEG)", null=True, blank=True)
    ZTAMB = models.FloatField(verbose_name="STATIC AIR TEMPERATURE FROM FADEC (DEG R)", null=True, blank=True)
    ZTLA = models.FloatField(verbose_name="THROTTLE LEVER ANGLE(DEG)", null=True, blank=True)
    ZTNAC = models.FloatField(verbose_name="NACELLE TEMP(DEG C)", null=True, blank=True)
    ZTOIL = models.FloatField(verbose_name="OIL TEMP (DEG C)", null=True, blank=True)
    ZVB1F = models.FloatField(verbose_name="VIB FAN/LO SPD (FAN PICKUP)", null=True, blank=True)
    ZVB1R = models.FloatField(verbose_name="VIB LPT/LOW SPD(REAR PICKUP)", null=True, blank=True)
    ZVB2F = models.FloatField(verbose_name="VIB COR/HI SPD (FAN PICKUP)", null=True, blank=True)
    ZVB2R = models.FloatField(verbose_name="VIB HPT/HI SPD (REAR PICKUP)", null=True, blank=True)
    ZVSV = models.FloatField(verbose_name="INDICATED_AIR_SPEED", null=True, blank=True)
    ZWF36 = models.FloatField(verbose_name="VAR STATOR VANES POS (VAR)", null=True, blank=True)
    IHPSOV = models.FloatField(verbose_name="PACK FLOW 1", null=True, blank=True)
    AGW = models.FloatField(verbose_name="ACTUAL GROSS WEIGHT (LB)", null=True, blank=True)
    CAS = models.FloatField(verbose_name="COMPUTED AIR SPEED (KNOTS)", null=True, blank=True)
    IAI = models.FloatField(verbose_name="WING A/I", null=True, blank=True)
    IVS12 = models.FloatField(verbose_name="ISOLATION VALVE SWITCH 1-2", null=True, blank=True)
    SAT = models.FloatField(verbose_name="STATIC AIR TEMPERATURE (SAT)", null=True, blank=True)
    ZALT = models.FloatField(verbose_name="PRESSURE ALTITUDE (FEET)", null=True, blank=True)
    ZT1A = models.FloatField(verbose_name="TOTAL AIR TEMP (DEG C)", null=True, blank=True)
    ZVIAS = models.FloatField(verbose_name="INDICATED_AIR_SPEED", null=True, blank=True)
    ZWBP1 = models.FloatField(verbose_name="PACK FLOW 1", null=True, blank=True)
    ZWBP1_8E = models.FloatField(verbose_name="CF34-8E PACK FLOW 1 - NOT USED BY BLEED ADJUSTMENT", null=True, blank=True)
    ZWBP2 = models.FloatField(verbose_name="PACK FLOW 2", null=True, blank=True)
    ZWBP2_8E = models.FloatField(verbose_name="CF34-8E PACK FLOW 2 - NOT USED BY BLEED ADJUSTMENT", null=True, blank=True)
    ZXM = models.FloatField(verbose_name="MACH", null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Все данные'
        verbose_name = "Данные"
        ordering = ['-aircraft_id']
