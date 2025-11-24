#!/usr/bin/env python3

# We don't actually use Path yet, so you can remove this import if you want
# from pathlib import Path 

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib


def train_and_save(model_path: str = "model.pkl") -> None:
    # 1) Load the iris dataset
    data = load_iris()
    X, y = data.data, data.target  # X = features, y = labels

    # 2) Split into train/test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,      # 20% for testing, 80% for training
        random_state=42     # fixed seed for reproducibility
    )

    # 3) Create and train the model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # 4) Evaluate on the test set
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Test accuracy: {acc:.3f}")

    # 5) Save the trained model
    joblib.dump(model, model_path)
    print(f"Saved model to {model_path}")


if __name__ == "__main__":
    train_and_save()
