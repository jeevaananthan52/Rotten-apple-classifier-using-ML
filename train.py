from model import VGG16Classifier
from config import config


def main():
    print("Initializing Rotten Apple Classifier...")
    classifier = VGG16Classifier(config)

    print("Building model...")
    classifier.create_model()
    classifier.model.summary()

    print("Starting training...")
    classifier.train_model()

    print("Training complete!")


if __name__ == "__main__":
    main()
