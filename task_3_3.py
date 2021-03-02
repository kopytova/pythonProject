def thesaurus(*list_names):
    dict_names = {}
    for name in list_names:
        if name[0] not in dict_names:
            dict_names[name[0]] = [name]
        else:
            dict_names[name[0]] += [name]

    return dict_names



output = thesaurus('Елисей', 'Анна', 'Дмитрий',
                   'Сергей', 'Екатерина', 'Юрий',
                   'Ярослав', 'Константин', 'Светлана')

print(output)
