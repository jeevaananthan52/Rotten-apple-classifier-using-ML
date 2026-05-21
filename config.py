config = {
    "size": 224,                          # Input image size (VGG16 default: 224x224)
    "number_of_class": 1,                 # Binary classification: 1 output neuron
    "activation": "sigmoid",             # Sigmoid for binary classification
    "loss": "binary_crossentropy",        # Loss for binary classification
    "batch": 32,                          # Batch size
    "epochs": 50,                         # Max training epochs
    "stopping_patience": 10,             # Early stopping patience
    "train_path": "data/train",          # Path to training data directory
    "test_path": "data/test",            # Path to test data directory
    "save_path": "checkpoints/best_weights.h5"  # Path to save best model weights
}
