import pandas as pd
import numpy as np
import joblib
import json
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# 1. تحميل الداتا
df = pd.read_csv("notebooks/data/train.csv")

# 2. تحديد الأعمدة المطلوبة
numeric_features = ["GrLivArea", "BedroomAbvGr", "FullBath", "TotalBsmtSF", "GarageCars"]
categorical_features = ["MSZoning", "Neighborhood", "HouseStyle"]
target = "SalePrice"

# تنظيف البيانات
df = df.dropna(subset=[target])
X = df[numeric_features + categorical_features]
y = df[target]

# 3. إعداد الـ Pipeline
preprocessor = ColumnTransformer([
    ("num", Pipeline([
        ("impute", SimpleImputer(strategy="median")),
        ("scale", StandardScaler())
    ]), numeric_features),
    ("cat", Pipeline([
        ("impute", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ]), categorical_features)
])

model = Pipeline([
    ("prep", preprocessor),
    ("reg", RandomForestRegressor(n_estimators=100, random_state=42))
])

# 4. التدريب
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)

# 5. حفظ الموديل وأسماء الأماكن للباك إند
joblib.dump(model, "house_price.pkl")
json.dump(sorted(df["Neighborhood"].dropna().unique().tolist()), open("locations.json", "w"))

print("Done training and exporting model successfully!")
