def selector(name_list):
    selected_name = {}
    for name in name_list:
        if name.capitalize().startswith("S"):
        # if name.startswith("S") or name.startswith("s"):

        #     name_upper = name.capitalize()
        #     if name_upper in selected_name:
        #         selected_name[name_upper] += 1
        #     else:
        #         selected_name[name_upper] = 1
            selected_name[name.capitalize()] = selected_name.get(name.capitalize(), 0) + 1
    return selected_name


name_box = ['Joe', 'James', 'Kunle', 'Seyi', 'Ashley', 'Akpan', 'Segun', 'Seyi', 'Hakimi', 'Segun', 'Samuel',
         'Seyi', 'seyi', 'segun']


print(selector(name_box))
