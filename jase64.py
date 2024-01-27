#!/usr/bin/env python3
import json
import base64
import sys
import argparse

def encode_base64(data):
    if isinstance(data, dict):
        return {k: encode_base64(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [encode_base64(element) for element in data]
    elif isinstance(data, str):
        return base64.b64encode(data.encode()).decode()
    else:
        return data

def decode_base64(data):
    if isinstance(data, dict):
        return {k: decode_base64(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [decode_base64(element) for element in data]
    elif isinstance(data, str):
        try:
            return base64.b64decode(data).decode()
        except Exception:
            return data
    else:
        return data

def main():
    parser = argparse.ArgumentParser(description='Encode or decode all string values in a JSON file using Base64.')
    parser.add_argument('file', type=str, help='Path to the JSON file.')
    parser.add_argument('--encode', action='store_true', help='Encode the JSON values.')
    parser.add_argument('--decode', action='store_true', help='Decode the JSON values.')

    args = parser.parse_args()

    with open(args.file, 'r') as file:
        json_data = json.load(file)

    if args.encode:
        result = encode_base64(json_data)
    elif args.decode:
        result = decode_base64(json_data)
    else:
        print("Error: Please specify either --encode or --decode option.")
        sys.exit(1)

    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()
