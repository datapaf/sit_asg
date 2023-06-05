# Code Summarization with Strcuture-induced Transformer. ASG Modification.

This is a version of [Strcuture-induced Transformer](https://arxiv.org/pdf/2012.14710.pdf) modified to accept Abstract Semantic Graph(ASG) as a structural input feature. 

Note: The modification is available only for Python.

## Dependency

```bash
pip install -r requirements.txt
```

## Data

For reproducing the results, you can download the tokens from [here](https://drive.google.com/file/d/1iVR0WsEs3v9NLKEjBmQnaLuqccK2pyl5/view?usp=sharing) and put `python` the `data` directory.

To prepare the ASG adjacency matrices, unpack `adjacency.zip` archive:

```bash
cd sit_asg
unzip adjacency.zip
```

Unpack `lines.zip` archive to prepare lines vectors:

```bash
cd sit_asg
unzip lines.zip
```

## Quick Start

**Training**

```bash
cd main
python train.py --dataset_name python --model_name YOUR_MODEL_NAME
```

See the log through:

```bash
vi ../modelx/YOUR_MODEL_NAME.txt
```


**Testing**

```bash
python test.py --dataset_name python --beam_size 5 --model_name YOUR_MODEL_NAME
```

**Acknowledgement:** The implementation is based on https://github.com/gingasan/sit3.

## Some Files Descriptions

`absent_asg.txt` - contains id of the source code samples that have no corresponding ASG adjacency matrices

`with_zero_matrices.txt` - contains id of the source code samples that have zero matrices because of having `with` statement

`wrong_lines.txt` - contains id of the source code samples that have incorrect corresponding lines vector

`zero_matrices.txt` - contains id of the source code samples that have zero ASG adjacency matrices

`ignore_guids.txt` - contains id of the source code samples (`absent_asg.txt` + `with_zero_matrices.txt` + `wrong_lines.txt`) to ignore while training and testing
