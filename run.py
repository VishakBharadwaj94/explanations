from flask import Flask,request,jsonify
import pandas as pd 
app = Flask(__name__)

df = pd.read_csv('feat_exp.csv')

@app.route("/explanations/get_data")
def get_data():

    idx = request.get_json().get('id',0)
    data = df.iloc[idx].to_dict()
    feature_values = {}
    explanation_values = {}
    for i in data.keys():
        if 'feat' in i:
            feature_values[i] = data[i]
        elif 'exp' in i:
            explanation_values[i] = data[i]

    return_dict = {
        "row_id": data['id'],
        "model_id":54,
        "id":idx,
        "explanation_type":"shap",
        "feature_count":5,
        "feature_values":feature_values,
        "explanation_values":explanation_values

    }
    return jsonify(return_dict)
    


if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)