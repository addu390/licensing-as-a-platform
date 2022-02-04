# Database model constants
STATUS = "status"
PLAN = "plan"
FEATURE = "feature"
ACTIVATION_DATE = "activation_date"
EXPIRY_DATE = "expiry_date"
LICENSE = "license"

# Enum constants
TRIAL = "TRIAL"
IN_PROGRESS = "IN_PROGRESS"
BLOCKED = "BLOCKED"
ACTIVE = "ACTIVE"
EXPIRED = "EXPIRED"
IN_ACTIVE = "IN_ACTIVE"
REGULAR = "REGULAR"
CUSTOM = "CUSTOM"
LIMIT = "LIMIT"
SWITCH = "SWITCH"

LICENSE_STATUS = (
    (TRIAL, 'Trial License'),
    (IN_PROGRESS, 'License activation in progress'),
    (BLOCKED, 'License Blocked'),
    (ACTIVE, 'License Activated'),
    (EXPIRED, 'License Validity Expired')
)

BASE_STATUS = (
    (ACTIVE, "Active"),
    (IN_ACTIVE, "In Active"),
)

PLAN_TYPE = (
    (REGULAR, "Regular"),
    (CUSTOM, "Custom"),
)

FEATURE_TYPE = (
    (LIMIT, "Limit"),
    (SWITCH, "Switch"),
)
