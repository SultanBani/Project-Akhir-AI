import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

# 1. Load dataset
data = pd.read_csv("diabetes.csv")

# 2. Bersihkan data: ganti nilai 0 yang tidak logis dengan median
cols_to_fix = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
for col in cols_to_fix:
    median = data[col].median()
    data[col] = data[col].replace(0, median)

# 3. Pisahkan fitur dan label
X = data.drop("Outcome", axis=1)
y = data["Outcome"]
feature_names = list(X.columns)

# 4. Scaling (SVM perlu scaling agar optimal)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 5. Split data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)

# 6. Bangun model SVM yang lebih optimal
model = SVC(kernel='rbf', C=2, gamma='scale', probability=True)
model.fit(X_train, y_train)

# 7. Evaluasi model
y_pred = model.predict(X_test)
print("\n📊 Evaluasi Model:")
print("Akurasi:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")
print("\nLaporan klasifikasi:\n", classification_report(y_test, y_pred))

# 8. Prediksi data input dari user
print("\n📥 Silakan masukkan data pasien baru:")
user_input = []

for feature in feature_names:
    while True:
        try:
            value = float(input(f"{feature}: "))
            user_input.append(value)
            break
        except ValueError:
            print("⚠️ Input tidak valid. Masukkan angka yang sesuai.")

# 9. Ubah input menjadi DataFrame dan skalakan
input_df = pd.DataFrame([user_input], columns=feature_names)
input_scaled = scaler.transform(input_df)

# 10. Prediksi
prediction = model.predict(input_scaled)[0]
confidence = model.predict_proba(input_scaled)[0][prediction] * 100
result = "POSITIF Diabetes" if prediction == 1 else "NEGATIF Diabetes"

# 11. Tampilkan hasil prediksi
print(f"\n📌 Hasil prediksi: {result}")
print(f"🔎 Tingkat keyakinan model: {round(confidence, 2)}%")
