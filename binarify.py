import binascii
import argparse

CHUNK_SIZE = 1


def get_binary_of_file(source_file_path: str, output_file_name):
    source_file_path = source_file_path.replace("\\", "/")
    output_path = "/".join(source_file_path.split(
        "/")[:len(source_file_path.split("/")) - 1]) + "/" + output_file_name
    fin = open(source_file_path, "rb")
    with open(output_path, "w") as fout:
        data = fin.read(CHUNK_SIZE)
        while data != b'':
            binary_string = bin(int(binascii.hexlify(data), 16))[2:].zfill(8)
            fout.write(binary_string)

            data = fin.read(CHUNK_SIZE)
    print("Binary representation of the file is saved in", output_path)
    fin.close()


def compile_to_actual_binary(source_file_path: str, output_file_name):
    source_file_path = source_file_path.replace("\\", "/")
    output_path = "/".join(source_file_path.split(
        "/")[:len(source_file_path.split("/")) - 1]) + "/" + output_file_name
    fin = open(source_file_path, "r")
    with open(output_path, "wb") as fout:
        data = fin.read(CHUNK_SIZE * 8)
        while data != '':
            n = int(data, 2)
            fout.write(n.to_bytes(CHUNK_SIZE, 'big'))
            data = fin.read(CHUNK_SIZE * 8)
    fin.close()
    print("File is compiled to actual binary representation and saved in", output_path)


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
        compile_to_actual_binary(args.compile[0], args.compile[1])
    elif args.binarify:
        get_binary_of_file(args.binarify[0], args.binarify[1])


if __name__ == "__main__":
    main()
