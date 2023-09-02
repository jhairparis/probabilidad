def percentage_view(val, settings):
    if settings["percentage"] == True:
        return "{:.0%}".format(val)
    else:
        return val
