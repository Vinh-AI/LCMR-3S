# T-M2S: A Time-Aware Mental State Space for Multimodal Depression Detection on Social Media

## 💿 Installation

```python
pip install -r requirements.txt
```

## 🍓 Dataset Preparation

The Twitter dataset could be downloaded [here](https://drive.google.com/open?id=11ye00sHFY5re2NOBRKreg-tVbDNrc7Xd).

Please contact the author in below referenced paper for accessing the Reddit dataset.

Uban, Ana-Sabina, Berta Chulvi, and Paolo Rosso. [Explainability of Depression Detection on Social Media: From Deep Learning Models to Psychological Interpretations and Multimodality](https://link.springer.com/chapter/10.1007/978-3-031-04431-1_13). In Early Detection of Mental Health Disorders by Social Media Monitoring, pp. 289-320. Springer, Cham, 2022.

```python
# Twitter
python extract_twitter_embeddings.py --modality image --embs clip
python extract_twitter_embeddings.py --modality image --embs dino

python extract_twitter_embeddings.py --modality text --embs roberta
python extract_twitter_embeddings.py --modality text --embs emoberta
python extract_twitter_embeddings.py --modality text --embs mentalbert
```

## 🚀 Training and Evaluating
```python
# Twitter
python main.py  --config_file configs/combos/dino_mentalbert.yaml --name fold-0-twitter-ws-128-dino-mentalbert --group tm2s --dataset twitter --fold 0 --window_size 128 --position_embeddings time2vec --mode run --epochs 200 --batch_size 256
python evaluate.py  --config_file configs/combos/dino_mentalbert.yaml --name fold-0-twitter-ws-128-dino-mentalbert --group tm2s --dataset twitter --fold 0 --window_size 128  --position_embeddings time2vec --output_dir twitter
```

## 👀 Visualization
```python
# Visualize the sentiment distribution of posts 
python visualization/sentiment_distribution.py --config_file configs/combos/clip_roberta.yaml --dataset twitter --fold 0 --window_size 128 --position_embeddings zero --kind test --weight best.ckpt

# Visualize the attention map of posts
python visualization/post_attention.py --config_file configs/combos/clip_roberta.yaml --dataset twitter --fold 0 --window_size 128 --position_embeddings zero --kind test --weight best.ckpt

# Visualize state space of depressed and non-depressed users
## Depressed Users
python visualization/state_space.py --config_file configs/combos/clip_roberta.yaml --dataset twitter --fold 0 --window_size 128 --position_embeddings zero --kind test --type Depressed --weight best.ckpt
## Non-Depressed Users
python visualization/state_space.py --config_file configs/combos/clip_roberta.yaml --dataset twitter --fold 0 --window_size 128 --position_embeddings zero --kind test --type Non-Depressed --weight best.ckpt
```

## ❤️️ Weights
Weights for DINO and MentalBERT encoders

| Window Size | Twitter | Reddit |
| ------- | ------  | ------ |
| 128 | updating...   | updating... |
| 256 | updating...   | updating... |
| 512 | updating...  | updating... |
| 1024 | updating...  | updating... |
