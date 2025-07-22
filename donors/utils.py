def _normalize_blood_group_string(blood_group):
    blood_group = blood_group.strip().upper()
    if 'A+' in blood_group or 'A(VE+)' in blood_group or 'এ পজেটিভ' in blood_group or 'এ+' in blood_group or 'A (+) POSITIVE' in blood_group or 'A(+)' in blood_group or 'A(+VE)' in blood_group or 'A (+)' in blood_group or 'A (+VE).' in blood_group or 'A +VE' in blood_group or 'A POJETIVE' in blood_group or 'A POSITIVE' in blood_group or 'A(+)' in blood_group or 'A(+) POSITIVE' in blood_group or 'A(+)VE' in blood_group or 'A(+VE)' in blood_group or 'এ (+)' in blood_group:
        return 'A+'
    elif 'A-' in blood_group or 'A(VE-)' in blood_group or 'এ নেগেটিভ' in blood_group or 'A (-) NEGATIVE' in blood_group or 'A(-)' in blood_group or 'A(-VE)' in blood_group or 'A (-) VE' in blood_group or 'A - (A NEGETIVE)' in blood_group or 'A - VE' in blood_group or 'A NAGATIVE' in blood_group or 'A NEGATIVE' in blood_group or 'A NEGETIVE' in blood_group or 'A(-) NEGATIVE' in blood_group or 'A(-) VE' in blood_group or 'A=' in blood_group:
        return 'A-'
    elif 'B+' in blood_group or 'B(VE+)' in blood_group or 'বি পজেটিভ' in blood_group or 'বি+' in blood_group or 'B (+) POSITIVE' in blood_group or 'B(+)' in blood_group or 'B(+VE)' in blood_group or 'B (+)' in blood_group or 'B (+VE) POSITIVE' in blood_group or 'B +VE' in blood_group or 'B POSITIVE' in blood_group or 'B(+VE )' in blood_group or 'B±' in blood_group or 'বি + পসিটিভ' in blood_group:
        return 'B+'
    elif 'B-' in blood_group or 'B(VE-)' in blood_group or 'বি নেগেটিভ' in blood_group or 'B (-) NEGATIVE' in blood_group or 'B(-)' in blood_group or 'B(-VE)' in blood_group or 'B (-)' in blood_group or 'B -' in blood_group or 'B -VE' in blood_group or 'B NEGATIVE' in blood_group or 'B NEGETIVE' in blood_group or 'B(-) NEGATIVE' in blood_group or 'B(-) VE' in blood_group or 'B(-)B NEGATIVE' in blood_group or 'বি নেগ' in blood_group or 'বি -' in blood_group:
        return 'B-'
    elif 'AB+' in blood_group or 'AB(VE+)' in blood_group or 'এবি পজেটিভ' in blood_group or 'AB (+) POSITIVE' in blood_group or 'AB(+)' in blood_group or 'AB(+VE)' in blood_group or 'AB (+VE)' in blood_group or 'AB +VE' in blood_group or 'AB POSITIVE' in blood_group or 'এবি +' in blood_group:
        return 'AB+'
    elif 'AB-' in blood_group or 'AB(VE-)' in blood_group or 'এবি নেগেটিভ' in blood_group or 'AB (-) NEGATIVE' in blood_group or 'AB(-)' in blood_group or 'AB(-VE)' in blood_group or 'AB (-)' in blood_group or 'AB -' in blood_group or 'AB - (NEGATIVE)' in blood_group or 'AB - (VE)' in blood_group or 'AB NEGATIVE' in blood_group or 'Ab-' in blood_group:
        return 'AB-'
    elif 'O+' in blood_group or 'O(VE+)' in blood_group or 'ও পজিটিভ' in blood_group or 'ও+' in blood_group or '0+' in blood_group or '0+(VE)' in blood_group or '0+VE' in blood_group or 'O (+) POSITIVE' in blood_group or 'O (+)' in blood_group or 'O (+VE)' in blood_group or 'O + (POSTIVIE)' in blood_group or 'O +(VE)' in blood_group or 'O +VE' in blood_group or 'O POSITIVE' in blood_group or 'O POSITIVE (+VE)' in blood_group or 'O(+)' in blood_group or 'O(+)VE)' in blood_group or 'O(+VE)' in blood_group or 'O*' in blood_group or 'OH' in blood_group or 'O‌+' in blood_group or 'ও পজেটিভ' in blood_group:
        return 'O+'
    elif 'O-' in blood_group or 'O(VE-)' in blood_group or 'ও নেগেটিভ' in blood_group or 'O NEGATIVE' in blood_group or 'O (-) NEGATIVE' in blood_group or 'O(-)' in blood_group or 'O(-VE)' in blood_group or '0(-)' in blood_group or '0-VE' in blood_group or 'O (-)' in blood_group or 'O (-) VE' in blood_group or 'O (-VE)' in blood_group or 'O -' in blood_group or 'O - ( NEGATIVE)' in blood_group or 'O - (NEGATIVE)' in blood_group or 'O - NEGETIVE' in blood_group or 'O NEGATIVE (-)' in blood_group or 'ও-' in blood_group:
        return 'O-'
    elif 'ALL' in blood_group or 'সব গ্রুপ' in blood_group or 'ANY' in blood_group:
        return 'ALL'
    return 'NA'

def normalize_donor_data(donor_data):
    processed_data = []
    for row in donor_data:
        blood_group = _normalize_blood_group_string(row.get('blood_group', ''))
        if blood_group:
            row['blood_group'] = blood_group
            processed_data.append(row)
    return processed_data
