TRIAL = "TRIAL"
IN_PROGRESS = "IN_PROGRESS"
BLOCKED = "BLOCKED"
ACTIVE = "ACTIVE"
EXPIRED = "EXPIRED"

IN_ACTIVE = "IN_ACTIVE"

STATUS = "status"
PACKAGE = "package"
ACTIVATION_DATE = "activation_date"
EXPIRY_DATE = "expiry_date"
LICENSE = "license"

LICENSE_STATUS = (
    ("TRIAL", 'Trial License'),
    ("IN_PROGRESS", 'License activation in progress'),
    ("BLOCKED", 'License Blocked'),
    ("ACTIVE", 'License Active'),
    ("EXPIRED", 'License Validity Expired')
)

BASE_STATUS = (
    ("ACTIVE", "Active"),
    ("IN_ACTIVE", "In Active"),
)
