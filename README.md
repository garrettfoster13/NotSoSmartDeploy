# NotSoSmartDeploy

## POC for decrypting PDQ SmartDeploy credentials

Prior to version 3.0.2046, PDQ SmartDeploy used static, hard-coded, universal encryption keys for credential storage. More information can be found in this blog [HKLM\SYSTEM\Setup\sMarTdEpLoY –  The (Static) Keys to Abusing PDQ SmartDeploy](https://specterops.io/blog/2025/08/12/hklmsystemsetupsmartdeploy-the-static-keys-to-abusing-pdq-smartdeploy/).

## Installation

Requirements

```
uv
```

Install

```
git clone https://github.com/username/project-name.git
cd project-name
uv sync
```

## Usage
```
uv run decrypt.py -h
v0.0.1 by @unsigned_sh0rt
usage: decrypt.py [-h] [-f {hex,base64}] ciphertext

Decrypt SmartDeploy encrypted creds prior to 3.0.2046

positional arguments:
  ciphertext

options:
  -h, --help            show this help message and exit
  -f, --format {hex,base64}
                        Data format (hex or base64)


```
