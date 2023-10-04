def calc_imc():
    weight = int(Element('weight').value)
    height = float(Element('height').value)
    imc_el = Element('imc')
    imc_description_el = Element('imc-description')

    imc = round(weight / (height ** 2),1)

    imc_el.write(imc)
    imc_description_el.write(imc_description(imc, imc_el, imc_description_el))

def imc_description(imc, imc_el, imc_description_el):
    msg = ''
    imc_el.remove_class('text-success')
    imc_description_el.remove_class('text-success-emphasis')
    imc_el.remove_class('text-warning')
    imc_description_el.remove_class('text-warning-emphasis')
    imc_el.remove_class('text-danger')
    imc_description_el.remove_class('text-danger-emphasis')

    if imc <= 18.5:
        msg = 'Abaixo do peso'
        imc_el.add_class('text-warning')
        imc_description_el.add_class('text-warning-emphasis')
    elif 18.6 <= imc <= 24.9:
        msg = 'Peso ideal'
        imc_el.add_class('text-success')
        imc_description_el.add_class('text-success-emphasis')
    elif 25 <= imc <= 29.9:
        msg = 'Levemente acima do peso'
        imc_el.add_class('text-warning')
        imc_description_el.add_class('text-warning-emphasis')
    elif 30 <= imc <= 34.9:
        msg = 'Obesidade grau I'
        imc_el.add_class('text-warning')
        imc_description_el.add_class('text-warning-emphasis')
    elif 35 <= imc <= 39.9:
        msg = 'Obesidade grau II (Severa)'
        imc_el.add_class('text-danger')
        imc_description_el.add_class('text-danger-emphasis')
    else:
        msg = 'Obesidade grau III (Grave)'
        imc_el.add_class('text-danger')
        imc_description_el.add_class('text-danger-emphasis')
    return msg