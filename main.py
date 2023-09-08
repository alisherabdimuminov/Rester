#!/usr/bin/python3

import argparse, re, requests
from rich import print_json


class ResterArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-u', '--url', help='Enter valid URL. Example: https://example.com/api/v1/posts/', type=self.URL, required=True)
        self.parser.add_argument('-m', '--method', help='Choice GET or POST', type=self.METHOD, default='GET')
        self.parser.add_argument('-H', '--headers', type=self.JSON, default={})
        self.parser.add_argument('-j', '--json', type=self.JSON, default={})
        self.parser.add_argument('-d', '--data', type=self.JSON, default={})
        self.parser.add_argument('-l', '--load', type=self.FILE)
        self.parser.add_argument('-t', '--timeout', type=self.TIMEOUT, default=20)
        self.args = self.parser.parse_args()


    def URL(self, arg_value, pat=re.compile(
        r"^https?://"
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE
    )):
        if not pat.match(arg_value):
            raise argparse.ArgumentTypeError("Invalid URL")
        return arg_value
    
    def METHOD(self, arg_value):
        if not arg_value in ['POST', 'GET', 'PUT', 'PATCH', 'DELETE']:
            raise argparse.ArgumentTypeError("Invalid method. Enter 'GET', 'POST', 'PATCH', 'PUT' or 'DELETE'")
        return arg_value
    
    def JSON(self, arg_value):
        try:
            value = eval(arg_value)
            return value
        except:
            raise argparse.ArgumentTypeError("Invalid headers")
        
    def FILE(self, arg_value):
        import os, pathlib
        if os.path.isfile(arg_value):
            if pathlib.Path(arg_value).suffix == '.json':
                return arg_value
            raise argparse.ArgumentTypeError("File does not JSON file.")
        raise argparse.ArgumentTypeError("File does not exists. Please enter correct file path.")
    
    def TIMEOUT(self, arg_value):
        try:
            time = int(arg_value)
            if time > 0 and time < 20:
                return arg_value
            raise argparse.ArgumentTypeError("The value must be between 1 and 20")
        except:
            raise argparse.ArgumentTypeError("Value must be INT.")
    


class Rester:
    def __init__(self, args):
        self.args = args
        self.get()
        self.post()
        self.put()
        self.patch()
        self.delete()
    
    def get(self):
        if self.args.method == 'GET':
            try:
                res = requests.get(url=self.args.url, headers=self.args.headers, timeout=self.args.timeout, json=self.args.json)
                try:
                    _ = res.json()
                    print_json(res.text)
                except:
                    print(res.text)
            except:
                print("400 Not found")
        return

    def post(self):
        if self.args.method == 'POST':
            try:
                res = requests.post(url=self.args.url, headers=self.args.headers, timeout=self.args.timeout, json=self.args.json, data=self.args.data)
                try:
                    _ = res.json()
                    print_json(res.text)
                except:
                    print(res.text)
            except:
                print("400 Not found")
        return
    
    def put(self):
        if self.args.method == 'PUT':
            try:
                res = requests.put(url=self.args.url, headers=self.args.headers, timeout=self.args.timeout, json=self.args.json, data=self.args.data)
                try:
                    _ = res.json()
                    print_json(res.text)
                except:
                    print(res.text)
            except:
                print("400 Not found")
        return

    def patch(self):
        if self.args.method == 'PATCH':
            try:
                res = requests.patch(url=self.args.url, headers=self.args.headers, timeout=self.args.timeout, json=self.args.json, data=self.args.data)
                try:
                    _ = res.json()
                    print_json(res.text)
                except:
                    print(res.text)
            except:
                print("400 Not found")
        return
    
    def delete(self):
        if self.args.method == 'DELETE':
            try:
                res = requests.delete(url=self.args.url, headers=self.args.headers, timeout=self.args.timeout)
                try:
                    _ = res.json()
                    print_json(res.text)
                except:
                    print(res.text)
            except:
                print("400 Not found")
        return
    
terminal = ResterArgumentParser()
rester = Rester(terminal.args)



