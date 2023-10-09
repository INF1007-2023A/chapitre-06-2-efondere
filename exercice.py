#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib.colors import cnames


def list_to_dict(some_list: list) -> dict:
    out_dict = {}
    for i in range(len(some_list)):
        out_dict[some_list[i]] = i

    return out_dict


def color_name_to_hex(colors: list) -> list:
    colors_hex = []
    for color in colors:
        colors_hex.append((color, cnames[color]))

    return colors_hex


def create_list() -> list:
    out_list = []
    for i in range(0, 15):
        out_list.append(i)
    for i in range(351, 10000):
        out_list.append(i)

    return out_list


def compute_mse(model_dict: dict) -> dict:
    average_mse = {}
    for k, v in model_dict.items():
        total_err_squared = 0
        for pair in v:
            total_err_squared += (pair[0] - pair[1]) * (pair[0] - pair[1])

        average_mse[k] = total_err_squared / len(v)

    return average_mse


def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    print(f"La liste des 10000 entiers est: {create_list()}")

    model_dict = {"LR": [(90, 92), (96, 100), (20, 25), (21, -2), (3, -20)],
                  "DNN": [(100, 101), (50, 50), (1,2), (-10, -12), (-1, 7)],
                  "RF": [(10, 19), (56, 70), (1, 9), (-100, -12), (-11, 7)]}
    print(f"Le mse des différents modèles est: {compute_mse(model_dict)}")


if __name__ == '__main__':
    main()
