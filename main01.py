def panel_calc(f_length, f_width, p_length, p_width, box_amount):
    floor_field = f_length * f_width
    panel_field = p_length * p_width

    return round (((floor_field/panel_field) * 1.1) / box_amount)


print(panel_calc(4,4,0.2, 1, 10))


