def estimative(num_hours, hourly_wage, tax_bracket):
    pay_pretax = num_hours * hourly_wage
    pay_aftertax = pay_pretax * (1 - tax_bracket)
    return (pay_aftertax)

payment = estimative(80, 24, 0)
print(payment)


def get_pay(num_hours):
    pay_pretax = num_hours * 15
    pay_aftertax = pay_pretax * (1 - .12)
    return pay_aftertax

pay_fulltime = get_pay(40)
print(pay_fulltime)