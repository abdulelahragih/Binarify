import argparse
import os

CHUNK_SIZE = 1024 * 1024 * 10  # 10 MB


def get_output_path(source_file_path: str, output_file_name: str) -> str:
    directory = os.path.dirname(source_file_path)
    return os.path.join(directory, output_file_name)


def read_in_chunks(file_object, chunk_size):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


def process_to_binary(data: bytes) -> str:
    return ''.join([bin(byte)[2:].zfill(8) for byte in data])


def process_to_byte(data: str) -> bytes:
    return bytes(int(data[i:i + 8], 2) for i in range(0, len(data), 8))


def convert_file_to_binary(source_file_path: str, output_file_name: str):
    output_path = get_output_path(source_file_path, output_file_name)
    with open(source_file_path, "rb") as fin, open(output_path, "w") as fout:
        for data in read_in_chunks(fin, CHUNK_SIZE):
            fout.write(process_to_binary(data))
    print(f"Binary representation of the file is saved in {output_path}")


def compile_to_file(source_file_path: str, output_file_name: str):
    output_path = get_output_path(source_file_path, output_file_name)
    with open(source_file_path, "r") as fin, open(output_path, "wb") as fout:
        for data in read_in_chunks(fin, CHUNK_SIZE):
            fout.write(process_to_byte(data))
    print(f"File is compiled to actual binary representation and saved in {output_path}")


def main():
    parser = argparse.ArgumentParser(description='This script converts a file to binary representation and vice versa.')

    parser.add_argument("-c", "--compile", nargs=2, dest="compile",
                        metavar=("source_file", "output_file"),
                        help="Compile a file to binary representation."
                        )
    parser.add_argument("-b", "--binary", nargs=2, dest="binarify",
                        metavar=("source_file", "output_file"),
                        help="Get binary representation of a file."
                        )
    args = parser.parse_args()
    if args.compile:
        compile_to_file(*args.compile)
    elif args.binarify:
        convert_file_to_binary(*args.binarify)


if __name__ == "__main__":
    main()
