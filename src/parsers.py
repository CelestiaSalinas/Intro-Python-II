def name_in_list(srch_for, list):
    found = []
    for i in list:
        if i.name.find(srch_for) != -1:
            found.append(i)
    if len(found) == 0:
        return {"find_any": False, "more_spec": False, "found": found}
    elif len(found) == 1:
        return {"find_any": True, "more_spec": False, "found": found}
    else:
        return {"find_any": True, "more_spec": True, "found": found}