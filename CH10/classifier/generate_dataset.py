from src import datasets
import params

def main():
    the_dataset = datasets.Shapes(params.Shapes)

    for shape in the_dataset.x_list:
        print()
        the_dataset.print_shape(shape)

if __name__ == '__main__':
    main()