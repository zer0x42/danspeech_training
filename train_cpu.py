import random
import numpy as np
import argparse
import torch

from deepspeech.train import train_new
from deepspeech.train import continue_training
from deepspeech.train import finetune
parser = argparse.ArgumentParser(description='DeepSpeech training')

# -- arguments to be supplied when training a new model
parser.add_argument('--conv-layers', default=2, type=int, help='Numer of conv layers')
parser.add_argument('--hidden-size', default=800, type=int, help='Hidden size of RNNs')
parser.add_argument('--hidden-layers', default=5, type=int, help='Number of RNN layers')
parser.add_argument('--rnn-type', default='gru', help='Type of the RNN. rnn|gru|lstm are supported')
parser.add_argument('--no-bidirectional', dest='bidirectional', action='store_false', default=True,
                    help='Turn off bi-directional RNNs, introduces lookahead convolution')

# -- set seeds for reproducibility
torch.manual_seed(1337)
torch.cuda.manual_seed_all(1337)

if __name__ == '__main__':
    args = parser.parse_args()

    torch.manual_seed(args.seed)
    np.random.seed(args.seed)
    random.seed(args.seed)

    # Begin training
    train_new(train_data_path='/scratch/s134843/danspeech/', validation_data_path='/scratch/s134843/danspeech/', args=args)
