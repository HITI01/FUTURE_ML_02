import shap
import matplotlib.pyplot as plt

def shap_explain(model, X_test):
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_test)
    plt.title("SHAP Feature Importance")
    shap.summary_plot(shap_values, X_test, plot_type='bar')
    shap.summary_plot(shap_values, X_test)
