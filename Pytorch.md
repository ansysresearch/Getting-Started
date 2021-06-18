# Pytorch guidelines

- moving tensors to GPU: Instead of using `x = x.cuda()`, use `x = x.to(device)` where device is for example `device = torch.device('cuda')`. The benefit will be when you need to choose a specific GPU for multi-GPU training.

- test time: during training, when you're evaluating the model on the test set, make sure to wrap it within a `with torch.no_grad()` context manager. Notice that this must be **together** with `model.eval()`. 
