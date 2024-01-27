# jase64
jase64 is a simple tool to encode and decode base64 in json values.

## Installation
asdf plugin add jase64 https://github.com/ogontaro/asdf-jase64.git

## Usage
```shell
cat data.json
#{
#  "key": "value",
#  "key2": "dmFsdWU="
#}
jase64 --encode data.json
#{
#    "foo": "Zm9vZm9v",
#    "bar": "YmFyYmFy"
#}

jase64 --encode data.json > data_encoded.json
jase64 --decode data_encoded.json
#{
#    "hoge": "fuga",
#    "joy": "full"
#}
```
