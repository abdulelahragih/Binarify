# Binarify
A simple Python script that converts any file to its binary representation and from its binary representation back to the actual file. I just created it for fun

## Requirements

- Python 3.x

## Usage

The script can be run from the command line with the following syntax:

```bash
python binarify.py {-c, -b} source_file output_file
```
-  Use `-c` to compile a file to its actual binary format, and `-b` to get the binary representation of a file in text format.
- `source_file` is the path to the source file you want to convert.
- `output_file` is the name of the output file where the result will be saved.

For example, to get the binary representation of a file named `example.jpg`, you would run:

```bash
python binarify.py -b path/to/file/example.jpg binary.txt
```

And to compile a file from its binary representation to its actual form, you would run:

```bash
python binarify.py -c path/to/file/binary.txt image.jpg 
```

## TODO
- [ ] allow output file to accept file name or path. For now, it only accepts a file name and it is stored in the same path as the source file
## License

This project is licensed under the terms of the MIT license.

