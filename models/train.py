import mlflow
import mlflow.pytorch
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import argparse


class ToyDataset(Dataset):
def __init__(self, n=1000):
self.x = torch.randn(n, 10)
self.y = (self.x.sum(dim=1) > 0).long()
def __len__(self): return len(self.x)
def __getitem__(self, idx): return self.x[idx], self.y[idx]


class SimpleModel(nn.Module):
def __init__(self):
super().__init__()
self.fc = nn.Linear(10, 2)
def forward(self, x): return self.fc(x)


if __name__ == '__main__':
parser = argparse.ArgumentParser()
parser.add_argument('--epochs', type=int, default=5)
args = parser.parse_args()
mlflow.set_tracking_uri('http://mlflow:5000')
with mlflow.start_run():
ds = ToyDataset(2000)
dl = DataLoader(ds, batch_size=64, shuffle=True)
model = SimpleModel()
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.CrossEntropyLoss()
for epoch in range(args.epochs):
total = 0
for xb, yb in dl:
logits = model(xb)
loss = loss_fn(logits, yb)
opt.zero_grad(); loss.backward(); opt.step()
total += loss.item()
mlflow.log_metric('epoch_loss', total, step=epoch)
mlflow.pytorch.log_model(model, 'model')


print('Training complete')
