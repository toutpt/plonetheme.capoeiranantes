
profile_id = 'profile-plonetheme.capoeiranantes:default'


def common(context):
    """Apply default profile"""

    context.runAllImportStepsFromProfile(profile_id)
