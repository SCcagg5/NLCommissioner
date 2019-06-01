from .routesfunc import *

def setuproute(app, call):
    @app.route('/test/',            ['OPTIONS', 'POST', 'GET'], lambda x = None: call([])               )
    @app.route('/compute_one/',     ['OPTIONS', 'POST'],        lambda x = None: call([compute_one])  )
    @app.route('/compute_multi/',   ['OPTIONS', 'POST'],        lambda x = None: call([compute_multi])  )
    def base():
        return
