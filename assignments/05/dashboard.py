import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from recommender import recommender
from user import user

import time
ratings_file = 'ratings.csv'

class Question:
    def __init__(self):
        r = recommender()
        u = user(len(r.md.gname_idx_map))
        self.r = r
        self.u = u

        self.no = 0
        self.uid = max(self.r.md.users.user_id.values) + 1
        m = self.r.get_random_movie()
        self.movie_id = m[0]
        self.movie_name = m[1]

    def update(self,rating):
        self.no += 1
        if self.no == 1:
            return

        rating = float(rating)
        self.u.rate(self.movie_id,self.r.md.mg_map,rating)
        self.r.md.add_rating(self.uid,self.movie_id,rating)

        m = None
        if self.no <= 7:
            m = self.r.recommended_movie(self.u)
        else:
            m = self.r.finally_reco_movie(self.u)
        self.movie_id = m[0]
        self.movie_name = m[1]








def start_app():

    css = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=css)
    question = Question()
    setAppLayout(app,question)
    app.run_server(debug=True)




def getLayout(question):

    return html.Div(style={'text-align':'center','color':'green'},children=[
            html.H1('Welcome to my recommendation system'),
            html.H3(' Please rate the following movies!'),
            html.Div(style = {'width': '20%','margin-left': 'auto','margin-right': 'auto','text-align': 'left'},
                children=[
                    html.H4(id='head', children='Question '+ str(question.no) + ':'),
                    html.Div(children='Movie name: ' + question.movie_name),
                    'Rating: ',
                    dcc.Input(
                        id='txt_rating',
                        placeholder='Rate here!',
                        type='text',
                        value=''
                    ),
                    html.Div(id='dum', children=''),
                    html.Button('Next', id='btnNext',style={'margin-top':'5px'})
                ]),
        ])

def getEndLayout(question):
    return html.Div(style={'text-align':'center','color':'green'},children=[
            html.H1('You will most likely like "' + question.movie_name + '"')
        ])



def setAppLayout(app,question):

    app.layout = html.Div(id ='page-content',children=getLayout(question))

    @app.callback(
    Output(component_id='page-content', component_property='children'),
    [Input('btnNext', 'n_clicks')],
    [State('txt_rating', 'value')]
    )
    def rate(n_clicks, value):
        question.update(value)
        if question.no == 8:
            return getEndLayout(question)

        return getLayout(question)




if __name__ == '__main__':
    start_app()