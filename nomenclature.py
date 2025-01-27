import torch
from models import *
from datasets import *
from evaluators import MultimodalEvaluator

device = torch.device("cuda")

DATASETS = {
    #"reddit": RedditDataset,
    "twitter": TwitterDataset,
}

EVALUATORS = {
    "multimodal-evaluator": MultimodalEvaluator,
}

MODELS = {
    "T-M2S": TM2S,
    "SingleModal": SingleModal,
    "tlstm": TimeLSTM
}
