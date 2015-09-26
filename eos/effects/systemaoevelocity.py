# systemAoeVelocity
#
# Used by:
# Celestials named like: Black Hole Effect Beacon Class (6 of 6)
runTime = "early"
type = ("projected", "passive")
def handler(fit, beacon, context):
    fit.modules.filteredChargeMultiply(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                       "aoeVelocity", beacon.getModifiedItemAttr("aoeVelocityMultiplier"))
