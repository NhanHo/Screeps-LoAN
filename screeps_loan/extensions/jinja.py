from flask import session
from screeps_loan import app
import screeps_loan.models.alliances as alliances_model

alliance_query = alliances_model.AllianceQuery()
app.jinja_env.globals.update(get_name_from_shortname=alliance_query.find_by_shortname)


import screeps_loan.models.users as users
app.jinja_env.globals.update(get_name_from_user_id=users.user_name_from_db_id)



import screeps_loan.models.invites as invites
def user_has_invites():
    my_invites = invites.get_invites_by_user(session['my_id'])
    return len(my_invites) > 0

app.jinja_env.globals.update(has_invites=user_has_invites)
