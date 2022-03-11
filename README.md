# Explanation of how to use the code
The code is submitted through a jupyter notebook, with the extension *.ipynb*.

To be able to look at it, here are the steps to follow:

# 1) clone the git repository locally

```bash
torchserve --start --model-store serving/model_store --models corner_detection.mar --ncs --ts-config serving/config.properties
```
