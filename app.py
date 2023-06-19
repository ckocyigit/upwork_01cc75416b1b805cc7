from arizonaCourt import ArizonaCCCH
from maricopaCourt import MaricopaJCCH

arizonaccch = ArizonaCCCH("https://www.superiorcourt.maricopa.gov/docket/CivilCourtCases/caseSearchResults.asp")
maricopajcch = MaricopaJCCH("https://justicecourts.maricopa.gov/app/courtrecords/caseSearchResults")

print(arizonaccch.search(lastName="Peter"))
