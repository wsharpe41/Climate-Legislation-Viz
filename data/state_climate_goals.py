class EmissionTarget:
    def __init__(self, year: int, reduction_percent: float, ghg: str = "CO2e", reference_year: int = None):
        self.year = year
        self.reduction_percent = reduction_percent
        self.ghg = ghg
        self.reference_year = reference_year

class ClimatePolicy:
    def __init__(self, state: str, exists: bool, targets: list[EmissionTarget] = []):
        self.state = state
        self.exists = exists
        self.targets = targets
    

ALL_POLICIES = {
    "AK" : ClimatePolicy(state="Alaska", exists=False),
    "AL" : ClimatePolicy(state="Alabama", exists=False),
    "AR" : ClimatePolicy(state="Arkansas", exists=False),
    "AS" : ClimatePolicy(state="American Samoa", exists=False),
    "AZ" : ClimatePolicy(state="Arizona", exists=False),
    "CA" : ClimatePolicy(state="California", exists=True,targets=[
        EmissionTarget(year=2030, reduction_percent=40, ghg="CO2e", reference_year=1990),
        EmissionTarget(year=2045, reduction_percent=100, ghg="CO2e", reference_year=1990),
        ]),
    "CO": ClimatePolicy(state="Colorado", exists=True,targets=[
        EmissionTarget(year=2025, reduction_percent=26, ghg="CO2e", reference_year=2005),
        EmissionTarget(year=2030, reduction_percent=50, ghg="CO2e", reference_year=2005),
        EmissionTarget(year=2050, reduction_percent=90, ghg="CO2e", reference_year=2005),
        ]),
    "CT": ClimatePolicy(state="Connecticut", exists=True,targets=[
        EmissionTarget(year=2030, reduction_percent=45, ghg="CO2e", reference_year=2001),
        EmissionTarget(year=2050, reduction_percent=80, ghg="CO2e", reference_year=2001),
    ]),
    "DC": ClimatePolicy(state="District of Columbia", exists=True,targets=[
        EmissionTarget(year=2030, reduction_percent=60, ghg="CO2e", reference_year=2006),
        EmissionTarget(year=2045, reduction_percent=100, ghg="CO2e", reference_year=2006),
    ]),
    "DE": ClimatePolicy(state="Delaware", exists=True,targets=[
        EmissionTarget(year=2025, reduction_percent=26, ghg="CO2e", reference_year=2005)
    ]),
    "FL": ClimatePolicy(state="Florida", exists=False),
    "FM": ClimatePolicy(state="Federated States of Micronesia", exists=False),
    "FO": ClimatePolicy(state="Faroese", exists=False),
    "GA": ClimatePolicy(state="Georgia", exists=False),
    "GU": ClimatePolicy(state="Guam", exists=False),
    "HI": ClimatePolicy(state="Hawaii", exists=True,targets=[
        EmissionTarget(year=2030, reduction_percent=50, ghg="CO2e", reference_year=2005),
        EmissionTarget(year=2045, reduction_percent=101, ghg="CO2e", reference_year=2005),
    ]),
    "IA": ClimatePolicy(state="Iowa", exists=False),
    "ID": ClimatePolicy(state="Idaho", exists=False),   
    "IL": ClimatePolicy(state="Illinois", exists=True,targets=[
        EmissionTarget(year=2030, reduction_percent=26, ghg="CO2e", reference_year=2005),]),
    "IN": ClimatePolicy(state="Indiana", exists=False),
    "KS": ClimatePolicy(state="Kansas", exists=False),
    "KY": ClimatePolicy(state="Kentucky", exists=False),
    "LA": ClimatePolicy(state="Louisiana", exists=True,targets=[
        EmissionTarget(year=2025, reduction_percent=26, ghg="CO2e", reference_year=2005),
        EmissionTarget(year=2030, reduction_percent=40, ghg="CO2e", reference_year=2005),
        EmissionTarget(year=2050, reduction_percent=100, ghg="CO2e", reference_year=2005)]),
    "MA": ClimatePolicy(state="Massachusetts", exists=True,targets=[
        EmissionTarget(year=2025, reduction_percent=33, ghg="CO2e", reference_year=1990),
        EmissionTarget(year=2030, reduction_percent=50, ghg="CO2e", reference_year=1990),
        EmissionTarget(year=2040, reduction_percent=75, ghg="CO2e", reference_year=1990),
        EmissionTarget(year=2050, reduction_percent=100, ghg="CO2e", reference_year=1990),
    ]),
    "MD": ClimatePolicy(state="Maryland", exists=True,targets=[
        EmissionTarget(year=2031, reduction_percent=40, ghg="CO2e", reference_year=2006),
        EmissionTarget(year=2045, reduction_percent=100, ghg="CO2e", reference_year=2006),]),
    "ME": ClimatePolicy(state="Maine", exists=True,targets=[
        EmissionTarget(year=2030, reduction_percent=45, ghg="CO2e", reference_year=1990),
        EmissionTarget(year=2045, reduction_percent=100, ghg="CO2e", reference_year=1990),]),
    "MH": ClimatePolicy(state="Marshall Islands", exists=False),
    "MI": ClimatePolicy(state="Michigan", exists=True,targets=[
        EmissionTarget(year=2025, reduction_percent=28, ghg="CO2e", reference_year=2005),
        EmissionTarget(year=2050, reduction_percent=100, ghg="CO2e", reference_year=2005),
        ]),
    "MN": ClimatePolicy(state="Minnesota", exists=True,targets=[
        EmissionTarget(year=2025, reduction_percent=30, ghg="CO2e", reference_year=2005),
        EmissionTarget(year=2050, reduction_percent=80, ghg="CO2e", reference_year=2005),
    ]),
    "MO": ClimatePolicy(state="Missouri", exists=False),
    "MP": ClimatePolicy(state="Northern Mariana Islands", exists=False),
    "MS": ClimatePolicy(state="Mississippi", exists=False),
    "MT": ClimatePolicy(state="Montana", exists=False),
    "NC": ClimatePolicy(state="North Carolina", exists=True,targets=[
        EmissionTarget(year=2025, reduction_percent=40, ghg="CO2e", reference_year=2005),
        EmissionTarget(year=2030, reduction_percent=50, ghg="CO2e", reference_year=2005),
        EmissionTarget(year=2050, reduction_percent=100, ghg="CO2e", reference_year=2005),
        ]),
    "ND": ClimatePolicy(state="North Dakota", exists=False),
    "NE": ClimatePolicy(state="Nebraska", exists=False),
    "NH": ClimatePolicy(state="New Hampshire", exists=False),
    "NJ": ClimatePolicy(state="New Jersey", exists=True,targets=[
        EmissionTarget(year=2030, reduction_percent=50, ghg="CO2e", reference_year=2006),
        EmissionTarget(year=2050, reduction_percent=80, ghg="CO2e", reference_year=2006),
    ]),
    "NM": ClimatePolicy(state="New Mexico", exists=True,targets=[
        EmissionTarget(year=2030, reduction_percent=45, ghg="CO2e", reference_year=2005),]
    ),
    "NV": ClimatePolicy(state="Nevada", exists=True,targets=[
        EmissionTarget(year=2025, reduction_percent=28, ghg="CO2e", reference_year=2005),
        EmissionTarget(year=2030, reduction_percent=45, ghg="CO2e", reference_year=2005),
        EmissionTarget(year=2050, reduction_percent=100, ghg="CO2e", reference_year=2005),]),
    "NY": ClimatePolicy(state="New York", exists=True,targets=[
        EmissionTarget(year=2030, reduction_percent=40, ghg="CO2e", reference_year=1990),
        EmissionTarget(year=2050, reduction_percent=100, ghg="CO2e", reference_year=1990)]),
    "OH": ClimatePolicy(state="Ohio", exists=False),
    "OK": ClimatePolicy(state="Oklahoma", exists=False),
    "OR": ClimatePolicy(state="Oregon", exists=True,targets=[
        EmissionTarget(year=2030, reduction_percent=45, ghg="CO2e", reference_year=1990),
        EmissionTarget(year=2050, reduction_percent=75, ghg="CO2e", reference_year=1990)]),
    "PA": ClimatePolicy(state="Pennsylvania", exists=True,targets=[
        EmissionTarget(year=2025,reduction_percent=26, ghg="CO2e", reference_year=2005),
        EmissionTarget(year=2050,reduction_percent=80, ghg="CO2e", reference_year=2005),]),
    "PR": ClimatePolicy(state="Puerto Rico", exists=False),
    "PW": ClimatePolicy(state="Palau", exists=False),
    "RI": ClimatePolicy(state="Rhode Island", exists=True,targets=[
        EmissionTarget(year=2030, reduction_percent=45, ghg="CO2e", reference_year=1990),
        EmissionTarget(year=2040, reduction_percent=80, ghg="CO2e", reference_year=1990),
        EmissionTarget(year=2050, reduction_percent=100, ghg="CO2e", reference_year=1990)]),
    "SC": ClimatePolicy(state="South Carolina", exists=False),
    "SD": ClimatePolicy(state="South Dakota", exists=False),
    "TN": ClimatePolicy(state="Tennessee", exists=False),
    "TX": ClimatePolicy(state="Texas", exists=False),
    "UM": ClimatePolicy(state="United States Minor Outlying Islands", exists=False),
    "UT": ClimatePolicy(state="Utah", exists=False),
    "VA": ClimatePolicy(state="Virginia", exists=True,targets=[
        EmissionTarget(year=2045, reduction_percent=100, ghg="CO2e", reference_year=2005),]),
    "VI": ClimatePolicy(state="Virgin Islands", exists=False),
    "VT": ClimatePolicy(state="Vermont", exists=True,targets=[
        EmissionTarget(year=2025, reduction_percent=26, ghg="CO2e", reference_year=1990),
        EmissionTarget(year=2030, reduction_percent=40, ghg="CO2e", reference_year=1990),
        EmissionTarget(year=2050, reduction_percent=80, ghg="CO2e", reference_year=1990)]),
    "WA": ClimatePolicy(state="Washington", exists=True,targets=[
        EmissionTarget(year=2030, reduction_percent=45, ghg="CO2e", reference_year=1990),
        EmissionTarget(year=2040, reduction_percent=70, ghg="CO2e", reference_year=1990),
        EmissionTarget(year=2050, reduction_percent=95, ghg="CO2e", reference_year=1990)]),
    "WI": ClimatePolicy(state="Wisconsin", exists=True,targets=[
        EmissionTarget(year=2025, reduction_percent=26, ghg="CO2e", reference_year=2005),]),
    "WV": ClimatePolicy(state="West Virginia", exists=False),
    "WY": ClimatePolicy(state="Wyoming", exists=False),
}
