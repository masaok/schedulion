import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from sklearn.metrics import precision_recall_fscore_support

complete_data_train = pd.read_csv('WP_data_train.csv')
complete_data_test = pd.read_csv('WP_data_test.csv')

columns_to_drop = ['Result', 'Opponent Name', 'Location_Semi-Away', 'Location_Semi-Home']
label_name = 'Result'

# Get the names of the features based on columns_to_drop
feature_names = complete_data_train.drop(columns_to_drop, axis=1).columns

x_train = complete_data_train[feature_names].values.astype(float)
y_train = complete_data_train[label_name].values.reshape(-1,1).astype(float).reshape((-1,))
x_test = complete_data_test[feature_names].values.astype(float)
y_test = complete_data_test[label_name].values.reshape(-1,1).astype(float).reshape((-1,))

if torch.cuda.is_available():
  device = 'cuda'
else:
  device = 'cpu'

class Net(nn.Module):
    def __init__(self, num_input, num_output):
      super().__init__()
      self.fc1 = nn.Linear(num_input, num_output)
      self.out = nn.Sigmoid()

    def forward(self, x):
      x = self.out(self.fc1(x))
      return x

model = Net(x_train.shape[1], 1).to(device)

x_train = torch.Tensor(x_train)
y_train = torch.Tensor(y_train)
x_test = torch.Tensor(x_test)
y_test = torch.Tensor(y_test)

loss_fn = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.0001)

n_epochs = 1000 # change this to 100 or 1000 so it doesn't take too long
epoch_print_index = n_epochs//10
BATCH_SIZE = 10
for epoch in range(n_epochs):
  for i in range(x_train.shape[0]//BATCH_SIZE):
    start_index = i * BATCH_SIZE
    end_index = start_index + BATCH_SIZE
    x_batch_train = x_train[start_index:end_index]
    optimizer.zero_grad() # Reset gradients to 0
    pred_y = model(x_batch_train).view(x_batch_train.shape[0])
    loss = loss_fn(pred_y, y_train[start_index:end_index])
    loss.backward() # Compute gradients
    optimizer.step() # Update model parameters

  if epoch % epoch_print_index == epoch_print_index-1:
    print('epoch:', epoch+1,', loss=',loss.item())
    
with torch.no_grad():
  y_train_pred = model(x_train).view(x_train.shape[0])
  train_loss = loss_fn(y_train_pred, y_train)
  y_test_pred = model(x_test).view(x_test.shape[0])
  test_loss = loss_fn(y_test_pred, y_test)

  y_train_pred_class = y_train_pred.round()
  y_test_pred_class = y_test_pred.round()

  accuracy_train = (y_train_pred_class.eq(y_train).sum())/float(y_train.shape[0])
  accuracy_test = (y_test_pred_class.eq(y_test).sum())/float(y_test.shape[0])

# Determine accuracy using rounded accuracy
print('Neural Net model\'s train and test accuracy')
print("Training Accuracy:", accuracy_train.item()) # 73.1
print("Testing Accuracy:", accuracy_test.item()) # 73.7

print('Neural Net model\'s train and test precision, recall, and F1 scores')
precision_train, recall_train, f1_train, _ = precision_recall_fscore_support(y_train, y_train_pred_class)
print("Training:") 
print("\tPrecision: ", precision_train) 
print("\tRecall: ", recall_train) 
print("\tf1: ", f1_train) 

precision_test, recall_test, f1_test, _ = precision_recall_fscore_support(y_test, y_test_pred_class)
print("Testing:") 
print("\tPrecision: ", precision_test) 
print("\tRecall: ", recall_test) 
print("\tf1: ", f1_test) 