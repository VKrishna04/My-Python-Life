from math import ceil


def number_of_classes_to_attend(required_percentage, attended, total_classes) -> int:
    # (required_percentage * (attended + x)) / 100 = (total_classes + x)
    num_of_classes = (required_percentage * total_classes - 100 * attended) / (
        100 - required_percentage
    )
    return ceil(num_of_classes)


def number_of_classes_to_spare(required_percentage, attended, total_classes) -> int:
    classes_can_spare = attended - (required_percentage / 100) * total_classes
    return ceil(classes_can_spare)


def main(
    choice, required_percentage, i=1, total_classes_list=None, attended_list=None
) -> None:
    num_of_classes = []
    while choice:
        if total_classes_list is not None and attended_list is not None:
            total_classes = total_classes_list[i - 1]
            attended = attended_list[i - 1]
        else:
            total_classes = int(
                input("Please enter the total number of classes taken       : ")
            )
            attended = int(
                input("Please enter the number of classes you have attended : ")
            )

        if (attended / total_classes) > required_percentage * 0.01:
            num_of_classes.append(
                -1
                * number_of_classes_to_spare(
                    required_percentage, attended, total_classes
                )
            )
            print(
                f"You have sufficient number of classes and are above the necessary mark.\nBut if curious you have to attend {-1*num_of_classes[-1]} to spare."
            )
        else:
            num_of_classes.append(
                -1
                * number_of_classes_to_attend(
                    required_percentage, attended, total_classes
                )
            )
            print(
                f"You have to attend {num_of_classes[-1]} classes to reach {required_percentage} mark."
            )
        if i is not None:

            i -= 1
            if i == 0:
                choice = False

        else:
            choice = input("If you wish to continue press nothing: ") == ""

        print("")
    print("\n\nDone!\n\n")
    i = 1
    for num in num_of_classes:
        if num < 0:
            print(f"{i}. You have to {-1*num_of_classes[-1]} classes to spare.")
        elif num > 0:
            print(
                f"{i}. You have to attend {num} class(es) to reach {required_percentage} mark.\n"
            )
        else:
            print(
                f"{i}. Keep Attending all the classes from now onwards to maintain the mark.\n"
            )
        i += 1


if __name__ == "__main__":
    required_percentage = 75
    choice = True  # to run infinite loop

    testing = True
    if testing:
        i = 9
        total_classes_list = [15, 71, 60, 38, 34, 36, 11, 50, 8]
        attended_list = [11, 61, 45, 31, 27, 32, 10, 42, 5]

        main(choice, required_percentage, i, total_classes_list, attended_list)
    main(
        choice,
        required_percentage,
    )
