from policyengine_us.model_api import *


class ct_pension_annuity_subtraction_eligible(Variable):
    value_type = bool
    entity = TaxUnit
    label = "Eligible for the Connecticut pension and annuity subtraction"
    definition_period = YEAR
    defined_for = StateCode.CT

    def formula(tax_unit, period, parameters):
        ct_agi = tax_unit("ct_agi", period)
        filing_status = tax_unit("filing_status", period)
        p = parameters(period).gov.states.ct.tax.income.subtractions
        ct_pension_threshold = p.pensions_or_annuity.income_limit[
            filing_status
        ]
        return ct_agi < ct_pension_threshold
