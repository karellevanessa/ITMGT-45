import math

def savings(gross_pay, tax_rate, expenses):
    after_tax = math.floor(gross_pay * (1 - tax_rate))
    remaining = after_tax - expenses
    return remaining

def material_waste(total_material, material_units, num_jobs, job_consumption):
    total_consumption = num_jobs * job_consumption
    waste = total_material - total_consumption
    return f"{waste}{material_units}"

def interest(principal, rate, periods):
    final_value = principal * (1 + (rate * periods))
    return math.floor(final_value)
