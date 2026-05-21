# 🍎 Rotten Apple Classifier

A deep learning model for binary classification of apples as **fresh** or **rotten**, built using transfer learning with VGG16 pretrained on ImageNet.

---

## 📁 Project Structure

```
rotten-apple-classifier/
├── model.py          # VGG16Classifier class definition
├── train.py          # Entry point to train the model
├── config.py         # Hyperparameters and paths
├── requirements.txt  # Python dependencies
└── README.md
```

---

## 🧠 Model Architecture

- **Base Model:** VGG16 (pretrained on ImageNet, top layers removed)
- **Pooling:** GlobalAveragePooling2D
- **Output:** Dense(1, activation='sigmoid') — binary classification
- **Loss:** Binary Crossentropy
- **Optimizer:** Adam

---

## 📦 Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/rotten-apple-classifier.git
cd rotten-apple-classifier
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 📂 Dataset Structure

Organize your dataset as follows:

```
data/
├── train/
│   ├── fresh/
│   │   ├── img1.jpg
│   │   └── ...
│   └── rotten/
│       ├── img1.jpg
│       └── ...
└── test/
    ├── fresh/
    └── rotten/
```

> **Note:** 30% of the training data is automatically used for validation.

---

## ⚙️ Configuration

Edit `config.py` to adjust hyperparameters:

| Parameter           | Default                        | Description                        |
|---------------------|--------------------------------|------------------------------------|
| `size`              | 224                            | Input image size (px)              |
| `batch`             | 32                             | Batch size                         |
| `epochs`            | 50                             | Maximum training epochs            |
| `stopping_patience` | 10                             | Early stopping patience            |
| `train_path`        | `data/train`                   | Path to training data              |
| `test_path`         | `data/test`                    | Path to test data                  |
| `save_path`         | `checkpoints/best_weights.h5`  | Where to save best model weights   |

---

## 🚀 Training

```bash
python train.py
```

The training pipeline includes:
- **Data Augmentation:** rotation, zoom, flips, shifts
- **Learning Rate Reduction:** on plateau
- **Early Stopping:** restores best weights
- **Model Checkpointing:** saves best weights automatically

---

## 📊 Callbacks

| Callback             | Monitors    | Behavior                                     |
|----------------------|-------------|----------------------------------------------|
| `ReduceLROnPlateau`  | `val_loss`  | Reduces LR by 10x if no improvement for 3 epochs |
| `EarlyStopping`      | `val_loss`  | Stops training if no improvement for 10 epochs   |
| `ModelCheckpoint`    | `val_loss`  | Saves best weights to `checkpoints/`             |

---

## 🛠️ Requirements

- Python 3.8+
- TensorFlow 2.10+
- Keras 2.10+

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
