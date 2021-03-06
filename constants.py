import os

DEFAULT_SPLIT = (0.9, 0.05, 0.05)

BATCH_SIZE = 500
N_EPOCHS = 100
LEARNING_RATE = 0.001

DATA_FOLDER_PATH = "data"
MODELS_FOLDER_PATH = "models"
BEST_LOSS_PATH = os.path.join(MODELS_FOLDER_PATH, "min_ave_val_loss.txt")
