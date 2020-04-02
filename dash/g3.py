import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import dash_auth

##external_stylesheets = [
##    'https://codepen.io/chriddyp/pen/bWLwgP.css',
##    {
##        'href': 'https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css',
##        'rel': 'stylesheet',
##        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
##        'crossorigin': 'anonymous'
##    }
##]

app = dash.Dash(__name__)

VALID_USERNAME_PASSWORD_PAIRS =     {
    'nakul': 'nakul','chotaadmin':'admin'
}

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)
no=1
df = pd.read_csv('analysis.csv')




app.layout =  dbc.Container([
    
    
    html.Div([
    dcc.Dropdown(
        id='demo-dropdown',
        
        options=[
            {'label': 'Virat Kohli', 'value': '0'},
            {'label': 'Shah Rukh Khan', 'value': '1'},
            {'label': 'Narendra Modi', 'value': '2'},
            {'label': 'Deepika Padukone', 'value': '3'},
            {'label': 'Shreemauli Raut', 'value': '4'},
            {'label': 'James Milner', 'value': '5'},
            {'label': 'Ratan N. Tata', 'value': '6'},
            {'label': 'Hrithik Roshan', 'value': '7'},
            {'label': 'Shubham Chandak', 'value': '8'},
            {'label': 'Robert Downey Jr', 'value': '9'}

            
        ],
        value='0',searchable=False
    )],className="dash-bootstrap"),
    
    html.Div(id='dd-output-container',className='graph1'),
    html.Div([
    html.Div(id='spider1',className='graph2'),
    html.Div(id='text1',className='graph2'),
    ],className='row2'),
    html.Div([
    html.Div(id='text2',className='graph2'),
    html.Div(id='spider2',className='graph2')  
    
    ],className='row2'),
    

    #dcc.Graph(figure=fig2),
    #dcc.Graph(figure=fig3),

    
 
], style={'rowCount': 4})
app.css.config.serve_locally = False
@app.callback(
    [dash.dependencies.Output('dd-output-container', 'children'),
    dash.dependencies.Output('spider1', 'children'),
     dash.dependencies.Output('spider2', 'children'),
     dash.dependencies.Output('text1', 'children'),
     dash.dependencies.Output('text2', 'children')],    
    [dash.dependencies.Input('demo-dropdown', 'value')])
def update_output(value):

    no = int(value)
  
    X=df.loc[df.index[no],['big5_agreeableness','big5_conscientiousness','big5_extraversion','big5_neuroticism','big5_openness']]
    Y=list()
    colors = ['gold',] * 5
    k=0;
    for j in X:
        
        if j<=0.3:
            colors[k]='crimson'
        elif j>=0.7:
            colors[k]='lime'
        k=k+1;
    for i in X : Y.append(format(i,".2%"))





    fig = go.Figure(go.Bar(
            
            x=df.loc[df.index[no],['big5_agreeableness','big5_conscientiousness','big5_extraversion','big5_neuroticism','big5_openness']],
            y=['Agreeableness','Conscientiousness','Extraversion','Neuroticism','Openness'],
            orientation='h',
            marker_color=colors,
           
            text=Y,
            textposition='auto'
            )
            )
    fig.update_layout(template="plotly_dark",title_text='Personality Analysis',paper_bgcolor="#2B3E50",plot_bgcolor= "rgba(1.0, 1.0, 1.0, 0.1)")


    fig2 = go.Figure(data=go.Scatterpolar(
    r=df.loc[df.index[no],['need_love','need_self_expression','need_stability','need_closeness','need_excitement','need_harmony',]],

    theta=['Love','Self Expression','Stability','Closeness','Excitement','Harmony'],

    fill='toself'
    ))

    fig2.update_layout(polar=dict(
        radialaxis=dict(
          visible=True),
      ),
      showlegend=False,
    template="plotly_dark",title_text='Emotional Needs',paper_bgcolor="#2B3E50",
    plot_bgcolor= "rgba(1.0, 1.0, 1.0, 0.1)")

    fig3 = go.Figure(data=go.Scatterpolar(
    r=df.loc[df.index[no],['need_ideal','need_practicality','need_structure','need_curiosity','need_challenge','need_liberty']],

    theta=['Ideal','Practicality','Structure','Curiosity','Challenge','Liberty'],

    fill='toself'
    ))

    fig3.update_layout(polar=dict(
        radialaxis=dict(
          visible=True),
      ),
      showlegend=False,
    template="plotly_dark",title_text='Intellectual Needs',paper_bgcolor="#2B3E50",
    plot_bgcolor= "rgba(1.0, 1.0, 1.0, 0.1)")

    X2=df.loc[df.index[no],['need_love','need_self_expression','need_stability','need_closeness','need_excitement','need_harmony',]]
    Y2=[]       
    if X2[0]<=0.3:
        Y2.append("Does not enjoy social contact, whether one-to-one or one-to-many.")
    elif X2[0]>=0.7:
        Y2.append("Enjoy social contact, whether one-to-one or one-to-many. Any brand that is involved in bringing people together taps this need.")
    if X2[1]<=0.3:
        Y2.append("Does not Enjoy discovering and asserting their own identities.")
    elif X2[1]>=0.7:
        Y2.append("Enjoy discovering and asserting their own identities.")
    if X2[2]<=0.3:
        Y2.append("Does not care for equivalence in the physical world. They prefer new and untested paths.")
    elif X2[2]>=0.7:
        Y2.append("Seek equivalence in the physical world. They favor the sensible, the tried and tested.")
    if X2[3]<=0.3:
        Y2.append("Does not care about connection with family and friends.")
    elif X2[3]>=0.7:
        Y2.append("Relish being connected to family and setting up a home.")
    if X2[4]<=0.3:
        Y2.append("Does not have upbeat emotions and is not willing to make any effort to change things.")
    elif X2[4]>=0.7:
        Y2.append("Want to get out there and live life, have upbeat emotions, and want to have fun.")
    if X2[5]<=0.3:
        Y2.append("Tends to be unappreciative towards other people and thier feelings")
    elif X2[5]>=0.7:
        Y2.append("Appreciate other people, their viewpoints, and their feelings.")


    r1=[]
    k2=0
    for l in Y2 :r1.append(html.Tr(html.Td(l)))
    table_body = [html.Tbody(r1)]
    table = dbc.Table(
    
    table_body,
    bordered=True,
    #dark=True,
    hover=True,
    #responsive=True,
    striped=True,
    )

    X3=df.loc[df.index[no],['need_ideal','need_practicality','need_structure','need_curiosity','need_challenge','need_liberty']]
    Y3=[]       
    if X3[0]<=0.3:
        Y3.append("Expected to have no desire for perfection.")
    elif X3[0]>=0.7:
        Y3.append("Desire perfection and a sense of community.")
    if X3[1]<=0.3:
        Y3.append("Does not have a lot of desire to get the job done,also does not consider skill and efficiency.")
    elif X3[1]>=0.7:
        Y3.append("Have a desire to get the job done, a desire for skill and efficiency, which can include physical expression and experience.")
    if X3[2]<=0.3:
        Y3.append("Tends to be unorganized and does not have a structure for holding things together")
    elif X3[2]>=0.7:
        Y3.append("Exhibit groundedness and a desire to hold things together. They need things to be well organized and under control.")
    if X3[4]<=0.3:
        Y3.append("Does not like to go out of his comfort zone.")
    elif X3[4]>=0.7:
        Y3.append("Have an urge to achieve, to succeed, and to take on challenges.")
    if X3[3]<=0.3:
        Y3.append("Is unconcerned with respect to discovering new possiblities and can be ignorant.")
    elif X3[3]>=0.7:
        Y3.append("Have a desire to discover, find out, and grow.")
    if X3[5]<=0.3:
        Y3.append("Is not a liberal person,tends to remain dependent on others")
    elif X3[5]>=0.7:
        Y3.append("Have a desire for fashion and new things, as well as the need for escape.")


    r2=[]
    k3=0
    for l in Y3 :r2.append(html.Tr(html.Td(l)))
    table_body2 = [html.Tbody(r2)]
    table2 = dbc.Table(
    
    table_body2,
    bordered=True,
    #dark=True,
    hover=True,
    #responsive=True,
    striped=True,
    )

        
    return dcc.Graph(figure=fig),dcc.Graph(figure=fig2),dcc.Graph(figure=fig3),(table),table2



if __name__ == '__main__':
    app.run_server(debug=True)



        


        
   
