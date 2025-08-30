def calculate_accuracy(y_true, y_pred):
    correct = sum(y_true == y_pred)
    return correct / len(y_true) if len(y_true) > 0 else 0
