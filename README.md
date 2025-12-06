# 🥔 Potato Disease Classification (Deep Learning + Streamlit)

This project is a **Potato Disease Classification Web App** built using **TensorFlow/Keras** and deployed with **Streamlit**.  
The model can classify potato leaf images into three categories:

- **Healthy**
- **Early Blight**
- **Late Blight**

The app allows users to **upload an image** or **take a picture using their camera**, and the system will predict the disease along with the **model confidence score**.

---

## 📂 Dataset

The dataset used for training comes from the **PlantVillage Dataset** on Kaggle.  
For this project, only the following subsets were used:

- `Potato___healthy`
- `Potato___Early_blight`
- `Potato___Late_blight`

This dataset contains thousands of high-quality, labeled plant leaf images widely used for agricultural disease detection research.

---

## 🧠 Model Training

The model was built using **TensorFlow Keras** with the following setup:

- **Architecture:** Convolutional Neural Network (CNN)
- **Optimizer:** Adam (chosen for stable and fast convergence)
- **Loss Function:** Categorical Crossentropy
- **Epochs:** **15**
- **Final Training Performance:**  
  - **Accuracy:** `0.9730`  
  - **Loss:** `0.0514`

These results indicate that the model is well-optimized and performs strongly on the classification task.

---

## 🌐 Web Application (Streamlit)

The web interface is built with **Streamlit**, providing a simple and clean user experience.

Live Demo : https://styfie-potato-disease-classification-app-f88a8h.streamlit.app/ 

### ✔ Features
- Upload a potato leaf image
- Take a picture using webcam
- Model predicts whether the leaf is:
  - **Healthy**
  - **Early Blight**
  - **Late Blight**
- Displays **prediction confidence**
- Responsive, minimalistic UI

---

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/repo-name.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## 📁 Project Structure

```
📦 Potato Disease Classification
 ┃ 1.keras
 ┣ app.py
 ┣ requirements.txt
 ┗ README.md
```

---

## 📜 License

This project is for educational and research purposes.
