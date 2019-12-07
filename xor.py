#!/usr/bin/python
import argparse, sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='XOR input file an output result into STDOUT')
    parser.add_argument('--key', type=str, help='XOR key', required=True)
    parser.add_argument('--input', type=argparse.FileType('rb'), default=sys.stdin, help='Input file')
    args = parser.parse_args()

    flag = args.input.read()
    for n, c in enumerate(flag):
        current_key = args.key[n % len(args.key)]
        sys.stdout.write(chr(ord(c) ^ ord(current_key)))
    args.input.close()
