from d_Puzzle import sudokuSolverOrtools
from d_Puzzle import sudokuSolverZ3

_ = 0

grid100x100 = [
    [_, _, _, _, _, 41, 1, 47, 84, 94, 46, 69, 31, 71, 13, 36, 42, _, _, _, _, _, _, 97, 9, 39, 63, 12, 77, 19, 99, 40, 2, _, _, _, 85, 37, 24, _, _, 64, _, _, _, 53, 87, 52, 66, 16, 20, 28, 76, 8, 83, _, _, _, 98, _, _, 60, 78,
     82, _, _, _, 74, 93, 51, 43, 61, 29, 59, 26, 89, 73, _, _, _, _, _, _, 5, 75, 92, 96, 32, 23, 90, 22, 34, 10, 80, 57, _, _, _, _, _],
    [_, 18, _, _, _, _, _, 55, 85, 34, 80, 68, 66, 40, 94, _, _, _, _, _, _, 71, 69, 46, 29, 36, 4, 88, 62, 13, 39, 63, 87, 31, 9, 58, _, _, _, 81, _, 57, 77, 59, 6, 96, 82, 15, 2, 91, 5, 23, 56, 90, 75, 32, 30, 48, 24, _, 79, _,
     _, _, 1, 41, 47, 83, 100, 3, 44, 74, 11, 8, 51, 28, 33, 76, 38, _, _, _, _, _, _, 98, 67, 53, 86, 93, 26, 89, 50, _, _, _, _, _, 61, _],
    [_, _, 78, 87, _, _, _, _, 97, 39, 3, 91, 6, 33, 76, _, _, _, 83, _, _, 10, 30, 44, 35, 37, 99, 5, 34, 32, 48, 96, 72, 92, 90, 56, _, _, _, _, _, _, 85, 98, 21, 73, 93, 19, 89, 70, 49, 53, 64, 27, 86, 66, 65, 54, _, _, _, _,
     _, _, 63, 62, 88, 4, 71, 36, 41, 2, 40, 68, 45, 18, 82, 94, 100, _, _, 52, _, _, _, 51, 26, 11, 77, 57, 47, 1, _, _, _, _, 79, 12, _, _],
    [_, _, 51, 72, 63, 74, _, _, 77, 24, 14, 20, 43, 26, _, _, 21, 89, _, _, _, _, 64, 11, 16, 96, 66, 49, 65, 15, 28, 27, 8, 38, 76, 32, _, _, _, _, _, _, 23, 79, 55, 67, 90, 30, 75, 5, 68, 94, 52, 45, 88, 40, 82, 100, _, _, _,
     _, _, _, 31, 59, 97, 17, 69, 58, 19, 95, 12, 1, 47, 22, 3, 53, _, _, _, _, 85, 37, _, _, 35, 70, 80, 34, 13, 42, _, _, 46, 29, 56, 4, _, _],
    [_, _, _, 61, 73, 98, 26, _, _, 21, 96, 32, 5, _, _, 23, 48, _, _, _, _, _, 47, 95, 41, 79, 24, 84, 1, 81, 69, 62, 42, 46, 88, _, _, 71, _, _, _, _, _, 45, 68, 7, 22, 80, 50, 49, 37, 35, 99, 34, 70, 85, 19, _, _, _, _, _, 16,
     _, _, 65, 53, 27, 52, 54, 25, 87, 17, 67, 9, 63, 58, 97, _, _, _, _, _, 44, 38, _, _, 83, 15, 76, 51, _, _, 77, 74, 100, 33, _, _, _],
    [71, _, _, 36, 88, 29, 62, _, _, 56, 49, 53, 86, _, _, 2, 82, _, _, 65, _, _, _, 80, 45, 61, 67, 26, 89, 94, 34, 22, 100, 10, 98, _, _, _, _, _, 76, _, _, 33, 60, 74, 28, 11, 8, 38, 25, 39, 58, 59, 31, 97, 13, _, _, 87, _, _,
     _, _, _, 90, 5, 48, 75, 30, 72, 93, 6, 78, 91, 50, 20, _, _, _, 3, _, _, 12, 81, _, _, 79, 41, 95, 85, _, _, 35, 27, 99, 40, _, _, 66],
    [15, _, _, _, 7, 79, 82, 40, _, _, 29, 17, _, _, 100, 63, _, _, _, 58, 75, 56, _, 23, 52, 70, 48, 90, 92, 31, 5, 77, 33, 93, _, _, 30, _, _, 94, 34, _, _, _, 61, 83, 99, 32, 37, 26, 12, 84, 3, 41, 81, 6, _, _, _, 95, 91, _, _,
     28, _, _, 76, 24, 8, 50, 69, 88, 36, 42, 57, 71, 46, _, 62, 4, 65, _, _, _, 27, 9, _, _, 21, 49, _, _, 43, 14, 86, 98, _, _, _, 73],
    [2, 8, _, _, _, _, 100, 28, _, _, 18, 10, _, _, _, _, _, _, 19, 37, 93, _, _, _, 51, 60, 72, 33, 87, 74, 1, 79, 59, 67, _, _, _, _, _, 3, 31, 58, _, _, _, _, 65, 71, 39, 97, 61, 57, 78, 43, _, _, _, _, 14, 73, 81, _, _, _, _,
     _, 56, 68, 7, 80, 98, 49, 54, 66, 5, 64, _, _, _, 27, 46, 36, _, _, _, _, _, _, 62, 29, _, _, 90, 75, _, _, _, _, 23, 96],
    [27, 64, 65, 86, _, _, _, _, 52, _, 15, 81, _, _, _, _, 24, 95, 47, 41, 2, 78, _, _, _, _, 100, 7, 40, 73, 45, 18, 14, 89, _, _, _, _, 80, 26, 42, 4, 29, 62, _, _, _, _, 9, 69, 60, 11, _, _, _, _, 77, 51, 72, 67, 99, 35, _, _,
     _, _, 70, 94, 55, 85, 32, 75, 23, 48, _, _, _, _, 96, 90, 97, 63, 10, 31, _, _, _, _, 17, 71, _, 6, _, _, _, _, 91, 8, 38, 5],
    [96, 23, 5, 30, 13, 48, _, _, _, _, _, _, _, _, 78, 11, 50, 64, 44, 51, 91, 76, 27, 8, _, _, _, _, 28, 18, 86, 6, _, _, _, _, 16, 66, 52, 15, 84, 81, 3, _, 1, 47, _, _, _, _, _, _, _, _, 36, 69, _, 4, 26, 62, 98, 45, 61, 43,
     _, _, _, _, 73, 67, 80, 77, _, _, _, _, 34, 10, 37, 55, 33, 7, 40, 68, 94, 100, _, _, _, _, _, _, _, _, 25, 59, 88, 63, 39, 87],
    [16, 52, 64, 49, 86, 54, 27, 53, 29, _, 58, 9, _, 17, 25, 31, 63, 87, 97, 59, 28, _, 6, 3, 12, 95, _, _, _, _, _, _, _, _, _, 10, 18, 70, 99, 21, 30, 68, 96, _, 32, 100, 89, 56, 23, 75, 13, 46, 62, 71, 67, 4, _, 88, 69, 76,
     80, 82, 90, 7, 2, _, _, _, _, _, _, _, _, _, 37, 47, 57, 14, _, 43, 83, 91, 44, 8, 15, 5, 20, _, 84, 98, _, 65, 60, 51, 93, 74, 77, 50, 72, 33],
    [81, 89, 59, 43, 26, 57, 47, 68, 79, _, 69, 4, _, 29, 90, 71, 14, 46, 10, 67, 30, 13, 62, 36, 48, 88, 5, 61, 75, 8, 95, 92, 12, 84, _, 96, 56, 93, 41, 32, 65, 86, 52, _, 49, 98, 66, 16, 54, 27, 87, 74, 63, 25, 97, 9, _, 60,
     39, 11, 58, 6, 76, 73, 28, _, 83, 91, 72, 20, 78, 50, 77, 21, 23, 51, 35, 33, 24, 15, 94, 2, 80, 100, 82, 42, 22, _, 31, 1, _, 85, 99, 18, 70, 64, 19, 37, 7, 34],
    [73, 9, 42, 1, 45, 39, _, _, _, _, _, _, _, _, 80, 7, 94, 93, 74, 68, 16, _, 82, 52, 27, 54, 65, 64, 49, 66, 51, 2, 67, 72, _, _, 78, 86, 77, 100, 37, 90, 35, _, 18, 10, _, _, _, _, _, _, _, _, 12, 84, _, 95, 50, 21, 43, 57,
     47, 15, _, _, 19, 87, 14, 34, 79, 20, 28, 76, 8, 83, 31, 91, _, 59, 69, 62, 36, 58, 13, 6, _, _, _, _, _, _, _, _, 92, 56, 48, 96, 17, 23],
    [74, 10, 12, 55, _, _, _, _, _, _, 2, 78, _, _, _, _, 47, 33, 100, 50, 97, 63, 25, 45, 70, 58, 7, 39, 9, 59, 40, 17, 80, 48, _, _, 60, 22, 88, 11, 8, 28, 91, 44, _, _, _, _, 14, 6, 54, 86, _, _, _, _, 66, 83, 65, 37, 71, 36,
     62, 42, _, _, 13, 16, 85, 69, 38, 3, 1, 93, 52, 27, 95, 81, 4, 41, 77, 96, 90, 73, _, _, _, _, 75, 23, _, _, _, _, _, _, 21, 61, 24, 26],
    [30, 32, 21, _, _, _, 56, _, _, 23, 64, 52, 53, _, _, _, _, _, 65, 34, _, 47, 20, 76, 84, 44, 91, 83, 15, 92, 14, 43, 73, 57, 54, _, _, 36, 98, 37, 62, 42, _, _, _, _, 88, 13, 4, 46, 72, 31, 93, 77, _, _, _, _, 1, 51, 96, 8,
     17, _, _, 9, 24, 95, 25, 97, 18, 70, 55, 99, 74, 26, 60, 19, 10, _, 41, 12, _, _, _, _, _, 28, 68, 63, 94, _, _, 22, _, _, _, 2, 35, 100],
    [65, _, _, _, 11, 40, 77, _, _, 87, 36, 61, 30, _, _, 5, _, _, _, 32, 68, 22, 100, 31, 60, 2, 17, 94, 33, 80, 74, 50, 75, 59, 7, _, _, 24, 63, 25, 57, _, _, _, 39, 97, 76, 21, 73, 43, 15, 20, 8, 28, 6, 16, _, _, _, 10, 52, 49,
     86, _, _, 64, 66, 54, 27, 4, 46, 71, 96, 89, 90, 29, 69, 88, 45, 62, 48, _, _, _, 37, _, _, 19, 55, 79, 14, _, _, 13, 81, 78, _, _, _, 47],
    [33, _, _, 85, 70, 15, _, _, 38, 61, 99, 19, 37, 28, _, _, 77, _, _, 12, 71, 67, 73, 98, 89, 43, 14, 21, 26, 23, 27, 58, 4, 83, 94, 62, _, _, 46, 20, 60, _, _, 78, 93, 64, 11, 74, 36, 50, 82, 2, 22, 40, 80, 100, 45, _, _, 57,
     63, 32, _, _, 65, 1, 81, 55, 44, 84, 92, 56, 42, 75, 72, 13, 5, 30, 48, 54, 59, _, _, 24, _, _, 97, 29, 95, 35, 49, 39, _, _, 69, 10, 86, _, _, 16],
    [_, _, _, 96, _, _, _, _, 50, 80, 83, 55, 38, 8, _, _, _, _, _, _, 40, 77, 57, _, 11, 35, 78, 74, 99, 86, 64, 82, 69, 13, 65, 16, _, _, _, 52, _, _, _, 84, 33, 24, 95, 1, 19, 79, 73, 92, 47, 81, 32, 90, 48, _, _, _, 26, _, _,
     _, 98, 56, 59, 10, 3, 75, 9, 63, 97, 39, 58, 87, _, 17, 25, 85, _, _, _, _, _, _, 88, 30, 67, 45, 4, 5, _, _, _, _, 42, _, _, _],
    [_, _, 67, _, _, _, _, 14, 37, 3, 48, 75, 13, 73, 57, _, _, _, _, 62, 51, 46, 4, 29, 90, 56, 69, 32, 96, 42, 97, 47, 71, 5, 45, 79, 81, _, _, _, _, _, 9, 25, 59, 72, 17, 87, 63, 61, 18, 55, 34, 19, 35, 36, 64, 85, _, _, _, _,
     _, 33, 50, 60, 77, 11, 88, 74, 2, 22, 82, 94, 80, 100, 12, 7, 40, 68, 10, _, _, _, _, 54, 65, 49, 16, 27, 76, 44, 8, _, _, _, _, 20, _, _],
    [_, _, _, _, _, 13, 83, 17, 66, 69, 81, 42, 95, 79, 24, 1, 70, _, 88, _, _, _, _, _, _, _, 18, 10, 50, 72, 91, 44, 38, 34, 28, 15, _, _, _, _, _, _, _, 82, _, 92, _, _, 45, 7, 14, 75, _, _, 27, _, 43, _, _, _, _, _, _, _, 46,
     35, 99, 100, 61, 48, 53, 64, 49, 86, _, _, _, _, _, _, _, 11, _, 47, 78, 57, 51, 26, 74, 33, 12, 58, 97, 31, 73, _, _, _, _, _],
    [_, _, _, _, _, _, 68, 13, 100, 55, 26, 54, 14, 53, _, 65, 22, 16, 86, _, _, _, _, _, _, _, _, _, 35, 85, _, _, _, _, _, _, _, 28, 91, _, _, _, _, _, _, _, _, _, 29, _, _, 19, _, _, _, _, _, _, _, _, _, 63, 58, _, _, _, _, _,
     _, _, 52, 51, _, _, _, _, _, _, _, _, _, 84, 81, 1, 95, _, 3, 59, 12, 47, 62, 66, 71, 42, _, _, _, _, _, _],
    [_, 58, 17, _, _, _, 9, _, 87, 97, _, 24, _, 10, 27, 35, 18, 55, 37, _, _, 66, 51, 96, 54, _, _, _, _, _, _, 98, 89, 21, 44, 57, 14, 65, 26, _, _, 33, 49, 11, 78, 80, 77, _, _, _, _, _, _, 30, 42, 71, 75, 90, 92, _, _, 50, 12,
     3, 84, 91, 31, 6, 1, _, _, _, _, _, _, 45, 100, 2, 67, _, _, 16, 62, 36, 99, 46, 4, _, 60, _, 38, 68, _, 20, _, _, _, 76, 47, _],
    [_, 96, 28, 32, 92, _, _, _, _, 75, 47, 3, 1, 95, 81, 19, 41, 12, 84, _, _, 17, 9, 49, 97, 59, _, _, _, _, _, 29, 36, 4, 62, 46, 13, 48, 42, _, _, 50, 16, 99, 52, 27, 64, _, _, _, _, _, _, 14, 26, 38, 57, 43, 73, _, _, 77, 72,
     78, 51, 11, 69, 33, 60, _, _, _, _, _, 85, 34, 21, 35, 18, _, _, 76, 91, 54, 8, 15, 44, 55, 6, 83, 82, _, _, _, _, 80, 100, 7, 94, _],
    [1, 54, 15, 26, 69, 76, 81, _, _, 8, 66, 98, 88, 43, 73, 77, 61, _, 67, _, _, 3, 34, 18, 62, 94, _, _, _, _, _, _, _, _, 25, 97, 83, 59, 58, _, _, 7, 22, 40, 82, 60, 2, 68, _, 45, 24, _, 91, 6, 84, 47, 4, 20, 79, _, _, 70, 55,
     19, 10, 85, _, _, _, _, _, _, _, _, 96, 75, 32, 90, 29, _, _, 13, _, 49, 28, 27, 52, 80, 42, 65, 33, _, _, 93, 78, 72, 11, 53, 14, 51],
    [46, 11, 95, 29, 52, 6, 71, 64, _, _, 78, 57, 60, 50, 31, 51, 33, 74, 93, _, _, 1, 84, 70, 69, _, _, _, 79, 41, _, _, 7, _, _, _, 82, 68, 2, _, _, 8, 38, 20, 28, 15, _, _, 83, 90, 58, 59, _, _, 72, 39, 9, 87, 25, _, _, 73, 67,
     14, _, _, _, 99, _, _, 36, 16, _, _, _, 49, 53, 86, 13, _, _, 5, 23, 45, 48, 32, 56, 75, 30, 96, _, _, 35, 10, 77, 19, 12, 85, 18, 37],
    [98, 40, 14, 57, 89, 21, 61, 67, _, _, 17, 62, 29, 13, 42, 4, 46, 36, 69, _, _, _, 91, 20, _, _, 83, 15, 38, 44, _, _, 18, 55, 34, _, _, 99, _, _, _, 39, 31, 26, 63, 48, _, _, 87, 59, 22, 82, _, _, 2, 7, 68, 45, 32, _, _, _,
     23, _, _, 96, 30, 79, _, _, 84, 24, 47, 12, _, _, 94, 41, _, _, _, 72, 51, 33, 93, 78, 74, 77, 66, 53, _, _, 27, 49, 64, 54, 52, 16, 65, 86],
    [84, 47, 24, 12, 62, 44, 91, 79, 20, _, _, 92, 56, 5, 48, 30, 23, 99, 96, 90, _, _, _, _, _, 93, 77, 72, 74, 14, 52, _, _, 16, 64, 27, 54, 67, _, _, 13, 71, 42, 88, 4, _, _, 69, 51, 36, 8, 41, 21, _, _, 28, 3, 81, 76, 15, _,
     _, 32, 2, 100, 40, 89, _, _, 7, 57, 80, 98, 43, 66, _, _, _, _, _, 35, 38, 37, 85, 29, 10, 19, 18, 34, _, _, 25, 39, 73, 9, 58, 17, 87, 97, 83],
    [10, 37, 85, 34, 18, 35, 70, 99, 19, _, _, 82, 100, 94, 2, 45, 59, 40, 7, 80, _, _, _, _, _, 30, 57, 98, 67, 33, 93, 8, _, 60, 51, 6, 11, _, _, _, 41, 3, 95, 47, 12, _, _, 81, 84, 1, 86, 64, 54, _, _, 27, 96, 16, 52, 53, _, _,
     _, 62, 42, 66, 74, _, 13, 71, 83, 91, 78, 20, 76, _, _, _, _, _, 39, 25, 31, 97, 24, 63, 87, 17, 9, _, _, 56, 23, 48, 75, 5, 26, 32, 90, 4],
    [49, 48, 53, 66, 36, 86, 45, 16, 27, 65, _, 58, 64, 39, 52, 25, 97, 72, 9, 63, 80, _, _, _, 100, 68, 22, 40, 2, 82, 24, 75, _, 76, 5, 23, 32, _, _, 90, 85, 35, 10, 54, 19, _, 18, 17, 94, 37, 77, 69, 51, 13, _, 78, 31, 93, 33,
     60, 47, _, _, 41, 59, 81, 15, _, 83, 44, 30, 99, 71, 74, 4, 42, _, _, _, 46, 73, 57, 89, 98, 67, 21, 14, 61, 43, _, 88, 3, 6, 79, 95, 8, 70, 1, 91, 84],
    [77, 3, 74, 33, 50, 60, 93, 78, 72, 51, _, 44, 15, 6, 38, 20, 83, 8, 28, 11, 99, _, _, _, 37, 26, 55, 71, 23, 10, 88, 45, _, 79, 84, 81, 41, _, _, 12, 5, 21, 43, 75, 56, 89, 14, 92, 98, 76, 34, 85, 29, 70, 66, 48, 35, 62, 46,
     18, 65, _, _, 16, 27, 4, 80, _, 64, 52, 97, 25, 63, 58, 73, 31, _, _, _, 17, 82, 68, 7, 90, 40, 86, 100, 2, 94, _, 61, 24, 69, 57, 36, 67, 96, 59, 13, 30],
    [75, 56, 92, 5, 61, 69, 90, 30, 32, 41, _, 29, 42, 57, 14, 46, 36, 13, 71, 88, _, _, _, _, _, _, 50, 77, 53, 60, 59, 100, _, 97, _, _, _, _, 25, 63, 55, 6, 45, 15, 74, _, 83, 10, 20, 40, 44, 8, 33, 86, _, 49, 54, 76, 66, 16,
     68, 96, _, _, _, _, 2, _, 22, 64, 37, 4, 34, 18, _, _, _, _, _, _, 81, 79, 95, 84, 12, 3, 24, 1, 47, _, 87, 21, 67, 26, 31, 38, 73, 89, 43, 58],
    [83, 53, 66, 52, 49, 11, 33, 86, 16, 27, _, 7, 21, 20, 75, 76, 91, 15, 45, 44, _, 97, 31, _, _, _, _, 59, 94, 17, 61, 64, _, _, _, _, 43, 57, 67, 30, 92, 25, 78, 90, 34, _, 23, 48, 88, 96, 70, 99, 69, 35, _, 18, 85, 37, 10,
     32, 77, 56, 89, 74, _, _, _, _, 50, 72, 3, 84, 95, _, _, _, _, 47, 79, _, 68, 28, 82, 38, 100, 2, 80, 65, 8, _, 29, 13, 42, 5, 62, 55, 71, 36, 4, 46],
    [34, 63, 97, 17, 31, 87, 84, 18, 9, _, _, 8, 59, 100, 82, 40, 66, 68, 58, 38, _, 85, 70, _, 55, 78, _, _, _, _, _, _, _, _, 14, 86, 49, 19, 6, 53, 69, 46, 36, 81, 71, _, _, 42, 56, 62, 64, 60, 90, _, _, 2, 5, 98, 30, 48, 95,
     29, 79, 54, 24, 16, _, _, _, _, _, _, _, _, 43, 73, _, 21, 99, _, 91, 93, 75, 7, 83, 20, 76, 15, 45, _, _, 33, 77, 88, 94, 51, 72, 74, 50, 57],
    [_, 72, 10, 60, 77, 64, 65, 93, 78, _, _, 49, 81, 47, 41, 79, 3, 24, 1, 84, _, 61, 7, _, _, 45, 62, 80, 25, 100, 85, _, _, 18, 71, 37, 35, 89, 70, 99, 50, 5, 86, 22, 16, _, _, 27, 82, 87, 96, 88, 67, _, _, 73, 40, 57, 13, 42,
     44, 14, 33, 98, 26, 69, 46, _, _, 91, 76, 28, 8, 17, 20, _, _, 83, 39, _, 31, 58, 63, 4, 97, 34, 54, 94, 59, _, _, 19, 48, 32, 11, 75, 23, 90, 30, _],
    [_, 28, 38, 58, 81, 12, _, _, _, _, _, _, _, _, 50, 60, 74, 51, 78, 25, _, 48, 95, 41, _, 75, 44, 20, 47, 49, _, _, 5, 56, 23, 92, 8, 16, 90, _, 21, 61, 73, 3, 89, 26, 30, _, _, _, _, _, _, 17, 87, 63, 97, 46, 59, 31, _, 85,
     35, 37, 55, 99, 67, 70, _, _, 40, 45, 2, 82, 7, _, 14, 22, 53, _, 29, 69, 42, 19, 88, 62, _, _, _, _, _, _, _, _, 1, 39, 54, 86, 52, _],
    [_, 45, 82, 40, _, _, _, _, _, _, 9, 93, _, _, _, _, 39, 31, 63, 61, _, 23, 3, 90, _, _, 30, 18, 56, 5, _, _, 27, 28, 83, 20, 48, 38, 44, 96, 29, 94, 79, 1, _, _, _, _, 24, 84, 71, 21, _, _, _, _, 26, 58, 6, 25, 19, 42, 13,
     57, 88, 73, 36, 62, _, _, 54, 66, 16, 64, _, _, 86, 52, 49, _, 74, 51, 72, 46, _, _, _, _, 78, 14, _, _, _, _, _, _, 59, 35, 34, _],
    [43, _, _, _, _, _, 57, _, _, 13, 10, 99, 85, 55, _, _, _, _, 53, _, _, 4, 46, 88, 71, _, 82, 1, 36, 40, _, 34, 74, 65, 78, 12, 79, 3, 66, 84, 49, 63, _, _, _, _, 97, _, 31, 17, 93, 7, _, 52, _, _, _, _, 80, 39, 94, 48, 75, 5,
     90, 30, 45, 41, 47, _, 87, 69, 59, 91, _, 60, 51, 77, 23, _, _, 18, _, _, _, _, 21, 67, 89, 73, 83, _, _, 44, _, _, _, _, _, 8],
    [25, _, _, _, 3, _, _, _, _, 48, 73, 26, 83, 69, 4, 89, _, _, _, _, 12, 99, 38, 15, 33, 24, 6, _, _, _, _, 87, 45, 7, 82, 2, 68, 31, 21, 58, 39, _, 37, _, 35, 28, 70, _, _, 32, 11, _, _, 91, 34, 74, _, 75, _, 50, 53, 86, 100,
     1, 52, 84, 40, 80, 66, _, _, _, _, 29, 88, 65, 10, 57, 71, 36, _, _, _, _, 92, 96, 30, 22, 64, 41, 60, _, _, _, _, 14, _, _, _, 78],
    [99, _, _, _, _, _, _, _, 39, 50, 32, 56, 90, 96, 6, 92, 30, _, _, _, 21, 57, 54, 26, 67, _, _, _, _, _, 62, 46, 13, 36, 69, 42, 10, 4, 29, 88, 64, _, _, 93, 75, 59, 51, _, _, _, _, _, _, 84, 79, 12, 24, _, _, 81, 83, 76, 15,
     8, 78, 61, 71, 20, 38, 28, _, _, _, _, _, 25, 63, 58, 9, 97, _, _, _, 52, 16, 87, 27, 66, 53, 44, 40, 80, _, _, _, _, _, _, _, 22],
    [_, 21, _, _, _, _, 46, 73, 71, 36, 35, 65, 94, 52, 18, 37, 19, 34, _, _, _, _, _, _, _, _, _, _, 76, 64, 77, 72, 51, 11, _, 40, 24, 50, 33, 1, _, _, _, 80, _, _, _, _, _, _, _, _, _, _, _, _, 83, _, _, _, 87, 97, 9, 59, 25,
     _, 39, 58, 17, 31, 93, 48, _, _, _, _, _, _, _, _, _, _, 57, 43, 55, 26, 10, 6, 70, 85, 95, 91, 61, 3, _, _, _, _, 12, _],
    [_, _, _, _, _, 82, 32, 100, 7, 40, 51, 77, 74, 93, 11, 50, 78, _, _, _, _, _, _, _, _, _, 56, 92, 90, 30, 76, 88, 98, 15, 38, 83, 28, 6, 20, _, 24, _, _, _, _, _, _, _, 46, 71, 31, 25, _, _, _, _, _, _, _, 17, _, 54, 3, 66,
     21, 14, 73, 26, 84, 89, 86, 8, 62, 69, _, _, _, _, _, _, _, _, _, 99, 18, 94, 70, 34, 85, 10, 27, 52, 65, 61, 67, _, _, _, _, _],
    [37, 34, _, _, _, _, _, 19, 55, 10, 21, 43, 89, 14, 67, _, _, _, _, _, _, 12, 41, 47, 1, 84, 3, 79, 81, 24, 65, 16, 86, 53, 68, 29, 2, _, _, _, _, _, 33, 51, _, _, 50, 77, 93, 74, 6, 15, 38, 20, _, _, 91, 28, _, _, _, _, _,
     17, 58, 25, 9, 63, 59, 39, 75, 98, 30, 5, 32, 56, 92, 48, 90, _, _, _, _, _, _, 40, 64, 54, 82, 100, 7, 36, 4, _, _, _, _, _, 46, 62],
    [_, 13, 71, 53, _, _, _, _, 69, 62, 16, 90, 52, 65, _, _, _, _, 54, _, _, 94, 61, 64, 73, 82, 98, 45, 43, 22, 72, 60, 21, 33, 81, 59, _, 51, _, _, _, 85, 99, 55, 37, _, _, 28, 10, 15, 32, 30, 96, _, _, 46, 23, 92, 56, _, _, _,
     91, _, 20, 8, 50, 44, 11, 6, 26, 7, 100, 80, 2, 14, 68, 40, 57, _, _, 67, _, _, _, _, 17, 87, 63, 31, 3, 18, _, _, _, _, 41, 34, 84, _],
    [_, 27, 30, 92, 56, 23, _, _, 90, _, _, _, _, 70, _, _, 58, 75, 17, 97, _, 65, 16, 54, 19, 32, 52, 85, 66, 34, 9, 55, 95, 99, 10, 35, _, _, 37, 31, _, 88, 69, 13, 36, 84, 12, _, 42, 4, 94, 45, _, 2, 24, 68, 22, 40, 100, _, 86,
     81, _, _, 96, 47, 41, 53, 98, 79, 91, 21, 83, 6, 49, 46, 76, 15, 28, _, 38, 39, 43, 61, _, _, 8, _, _, _, _, 50, _, _, 60, 93, 78, 11, 33, _],
    [_, 98, 57, 14, 12, 1, 74, _, _, 96, 40, 45, 80, _, _, 22, 100, 7, 94, _, _, 88, 13, 62, 42, 4, 28, 86, 71, 36, 47, 61, 3, 24, 43, _, _, 41, 19, _, _, _, 63, 9, 97, 25, 39, 73, 59, 31, 51, 65, 27, 49, 54, 11, 37, 52, _, _, _,
     69, 5, _, _, 92, 48, 75, 56, 23, 85, 35, 70, 53, 18, 58, 99, 34, 55, _, _, 33, 93, 77, 26, _, _, 81, 50, 16, 8, _, _, 76, 32, 91, 6, 38, 15, _],
    [28, 15, 91, 76, 38, 20, 94, _, _, 6, 37, 47, 24, _, _, 84, 55, 1, 72, 10, _, 31, 97, 59, 17, 25, _, _, _, 87, _, _, _, _, 42, _, _, 90, 96, _, _, _, _, 68, 7, 61, 40, 82, 16, 100, 95, 79, 43, 3, 18, 19, 81, _, _, _, _, 52,
     85, _, _, 27, _, _, _, _, 50, _, _, _, 11, 33, 93, 74, 78, _, 5, 56, 71, 86, 46, _, _, 62, 35, 4, 73, _, _, 66, 53, 26, 14, 45, 21, 80],
    [64, 75, 52, 46, 66, 16, 49, 65, _, _, 56, 27, _, _, 32, 48, 53, 9, 30, _, _, 89, 40, 100, _, _, _, _, 57, 26, 25, 39, _, _, 74, _, 97, 58, 11, _, _, 87, _, 76, 91, 8, 34, 18, 44, 19, 29, 90, 88, 69, 4, 42, 36, _, 62, _, _,
     38, 60, 51, _, 77, _, _, 28, 33, 67, 96, _, _, _, _, 45, 61, 22, _, _, 24, 47, 23, 41, 59, _, _, 20, 3, _, _, 5, 55, 85, 37, 35, 81, 10, 1],
    [72, 97, 87, 31, 17, 33, 25, 58, _, _, 8, 76, _, _, 44, 91, 20, 28, 81, _, _, _, _, 83, _, _, 11, 38, 6, 77, 4, 48, 46, 71, _, _, _, _, _, _, _, 65, 53, _, 64, 45, 49, _, _, 66, 10, _, _, 98, 73, 57, _, 21, 67, _, _, _, _, _,
     _, _, 35, 18, 37, 19, 95, 47, 9, 24, _, _, 1, _, _, _, _, 32, 79, 42, 90, 69, _, _, 88, 30, _, _, 13, 100, 68, 89, 82, 29, 40, 2],
    [9, 77, 63, 11, 93, 78, 39, 50, 73, _, 34, 41, _, 18, 5, 95, 38, 83, 6, 19, 8, _, _, _, 46, 20, 76, 69, 72, 91, 80, 49, 52, 82, _, 54, 27, _, _, _, 26, 89, 98, 21, 58, 94, 43, _, _, _, _, _, _, 99, 71, 35, 1, 84, 55, 47, _, _,
     _, 24, 36, _, 42, 32, 70, 62, 12, 59, 81, 31, 97, 37, _, _, _, 87, 53, 45, 2, 13, 22, 68, 29, _, 65, 74, _, 75, 86, 96, 51, 48, 30, 56, 92, 28],
    [3, 84, 41, 47, 43, 61, 79, 24, 81, _, 42, 88, _, 4, 46, 13, 69, 62, 29, 36, _, _, _, 55, 49, 10, 37, 51, 70, 67, 8, 14, 34, 85, _, 89, 1, 73, _, _, 56, 48, 5, 32, 30, 90, 92, 75, _, _, _, _, 77, 60, 50, 86, 93, 72, 74, 33, _,
     _, 94, 80, 45, _, 7, 2, 82, 22, 20, 65, 38, 19, 64, 66, 54, _, _, _, 6, 15, 21, 91, 11, 83, 98, _, 44, 28, _, 63, 9, 58, 87, 17, 39, 25, 31, 97],
    [59, 31, 9, 39, 58, 53, 17, 87, 25, _, 57, 95, _, 21, 92, 67, 32, 69, 89, 43, _, _, _, 14, 61, 34, 85, 99, 19, 37, 54, 3, 16, 27, _, 18, 98, 64, _, _, 33, 52, 75, 65, 77, 23, 48, 96, _, _, _, _, 6, 94, 28, 83, 100, 44, 8, 91,
     _, _, 11, 93, 74, _, 72, 76, 78, 60, 22, 73, 20, 7, 86, 2, 80, _, _, _, 12, 1, 30, 41, 84, 79, 45, _, 90, 24, _, 71, 88, 46, 66, 4, 13, 62, 29, 36],
    [44, 41, 56, 91, 30, 32, 96, 3, 76, _, 77, 50, _, 27, 72, 54, 99, 11, 60, 93, 5, _, _, _, 95, 23, 81, 70, 84, 12, 68, 26, 61, 43, _, 67, 73, _, _, _, 94, 40, 57, 100, 90, 21, 7, _, _, _, _, _, _, 37, 10, 53, 87, 55, 58, 20, _,
     _, _, 49, 85, _, 52, 98, 19, 16, 6, 38, 45, 36, 1, 24, _, _, _, 34, 62, 4, 29, 69, 71, 88, 13, _, 46, 51, _, 15, 47, 59, 63, 31, 97, 39, 28, 9],
    [55, 66, 54, 10, 99, 97, 18, 37, _, _, 7, 22, _, _, 40, 80, 2, 94, 82, _, _, _, _, 6, _, _, 8, 91, 20, 38, 58, 59, 31, 25, _, _, _, _, _, _, _, 84, 24, _, 79, 1, 81, _, _, 47, 92, _, _, 32, 23, 50, _, 56, 90, _, _, _, _, _, _,
     _, 29, 88, 42, 13, 11, 72, 93, 33, _, _, 30, _, _, _, _, 43, 49, 21, 73, 67, _, _, 98, 86, _, _, 64, 19, 34, 52, 16, 65, 89, 27],
    [86, 19, 36, 27, 65, 62, 16, 52, _, _, 79, 84, _, _, 37, 34, 71, 41, 73, _, _, 25, 39, 9, _, _, _, _, 63, 58, 66, 32, _, _, 47, _, 88, 72, 13, _, _, 30, _, 60, 46, 50, 78, 51, 11, 93, 80, 40, 7, 15, 68, 14, 76, _, 82, _, _,
     33, 44, 20, _, 28, _, _, 91, 83, 100, 57, _, _, _, _, 43, 26, 94, _, _, 92, 35, 75, 56, 95, _, _, 48, 81, _, _, 53, 12, 55, 85, 90, 70, 99, 54],
    [42, 60, 29, 88, 78, 34, 69, _, _, 71, 1, 70, 33, _, _, 62, 90, 18, 85, 55, _, 100, 45, 2, 40, 67, _, _, _, 68, _, _, _, _, 86, _, _, 46, 74, _, _, _, _, 97, 27, 17, 25, 31, 72, 63, 47, 3, 79, 89, 21, 81, 84, _, _, _, _, 43,
     7, _, _, 57, _, _, _, _, 66, _, _, _, 35, 39, 77, 54, 98, _, 28, 20, 6, 10, 44, _, _, 8, 83, 64, 24, _, _, 92, 5, 32, 37, 23, 95, 48],
    [_, 46, 50, 74, 33, 72, 12, _, _, 77, 13, 15, 28, _, _, 38, 88, 91, 20, _, _, 86, 52, 66, 53, 98, 64, 65, 16, 51, 78, 90, 23, 80, 92, _, _, 56, 5, _, _, _, 4, 8, 83, 44, 71, 58, 62, 42, 67, 43, 73, 24, 95, 61, 49, 26, _, _, _,
     34, 87, _, _, 31, 21, 39, 63, 9, 55, 37, 19, 14, 27, 85, 18, 99, 70, _, _, 22, 68, 40, 32, _, _, 82, 2, 94, 75, _, _, 1, 3, 81, 84, 79, 41, _],
    [_, 67, 26, 22, 94, 73, _, _, 68, _, _, _, _, 9, _, _, 17, 59, 31, 87, _, 36, 71, 4, 88, 13, 29, 42, 46, 69, 44, 28, 6, 77, 15, 76, _, _, 83, 8, _, 70, 55, 10, 85, 18, 35, _, 34, 99, 48, 51, _, 72, 78, 5, 33, 74, 93, _, 3, 80,
     _, _, 47, 79, 12, 84, 24, 95, 90, 32, 50, 92, 60, 23, 75, 96, 64, _, 27, 53, 54, 66, _, _, 57, _, _, _, _, 61, _, _, 14, 86, 7, 98, 56, _],
    [_, 57, 40, 82, _, _, _, _, 14, 2, 44, 83, 4, 81, _, _, _, _, 12, _, _, 33, 49, 74, 72, 77, 93, 60, 78, 50, 36, 69, 79, 62, 41, 95, _, 35, _, _, _, 13, 88, 28, 29, _, _, 6, 38, 20, 65, 52, 66, _, _, 1, 16, 86, 27, _, _, _, 48,
     _, 32, 23, 75, 5, 30, 96, 63, 17, 31, 97, 59, 53, 87, 25, 58, _, _, 19, _, _, _, _, 34, 85, 3, 37, 68, 100, _, _, _, _, 43, 73, 80, _],
    [48, 5, _, _, _, _, _, 11, 92, 28, 86, 23, 51, 78, 53, _, _, _, _, _, _, 24, 79, 32, 47, 41, 96, 56, 30, 3, 57, 12, 94, 40, 2, 45, 100, _, _, _, _, _, 89, 14, _, _, 67, 43, 26, 82, 85, 97, 19, 39, _, _, 34, 9, _, _, _, _, _,
     55, 35, 70, 54, 65, 18, 99, 29, 46, 44, 13, 69, 62, 4, 71, 81, _, _, _, _, _, _, 80, 77, 60, 93, 36, 58, 20, 76, _, _, _, _, _, 87, 38],
    [_, _, _, _, _, 83, 80, 20, 23, 81, 30, 96, 61, 56, 26, 14, 75, _, _, _, _, _, _, _, _, _, 21, 73, 7, 57, 37, 65, 99, 19, 52, 70, 55, 34, 85, _, 16, _, _, _, _, _, _, _, 64, 92, 69, 13, _, _, _, _, _, _, _, 71, _, 1, 45, 94,
     40, 67, 100, 22, 68, 82, 15, 41, 3, 95, _, _, _, _, _, _, _, _, _, 9, 39, 25, 63, 97, 87, 78, 74, 93, 33, 11, 44, _, _, _, _, _],
    [_, 94, _, _, _, _, 22, 63, 40, 82, 38, 35, 91, 15, 12, 28, 6, 97, _, _, _, _, _, _, _, _, _, _, 85, 95, 90, 23, 58, 54, _, 39, 21, 92, 32, 16, _, _, _, 83, _, _, _, _, _, _, _, _, _, _, _, _, 69, _, _, _, 8, 55, 99, 96, 70,
     _, 37, 19, 81, 5, 45, 26, _, _, _, _, _, _, _, _, _, _, 64, 17, 36, 65, 42, 52, 27, 25, 72, 77, 11, 60, _, _, _, _, 78, _],
    [6, _, _, _, _, _, _, _, 88, 66, 50, 37, 8, 44, 93, 33, 60, _, _, _, 98, 16, 77, 61, 26, _, _, _, _, _, 38, 99, 70, 20, 75, 34, 86, 78, 55, 19, 22, _, _, 94, 80, 40, 57, _, _, _, _, _, _, 67, 65, 72, 25, _, _, 27, 85, 79, 95,
     4, 91, 18, 1, 3, 35, 47, _, _, _, _, _, 92, 90, 23, 56, 48, _, _, _, 63, 59, 31, 58, 9, 97, 87, 36, 46, _, _, _, _, _, _, _, 42],
    [23, _, _, _, 90, _, _, _, _, 92, 45, 25, 9, 63, 59, 58, _, _, _, _, 49, 62, 86, 81, 30, 65, 53, _, _, _, _, 68, 82, 88, 22, 100, 7, 2, 64, 4, 73, _, 26, _, 98, 56, 61, _, _, 67, 91, _, _, 1, 39, 8, _, 6, _, 44, 51, 72, 77,
     60, 33, 50, 32, 93, 74, _, _, _, _, 46, 78, 69, 13, 37, 34, 18, _, _, _, _, 96, 84, 95, 41, 40, 80, 16, _, _, _, _, 87, _, _, _, 79],
    [13, _, _, _, _, _, 15, _, _, 12, 82, 100, 22, 68, _, _, _, _, 2, _, _, 64, 36, 40, 4, _, 42, 46, 29, 71, _, 41, 66, 96, 49, 52, 45, 27, 65, 5, 17, 97, _, _, _, _, 63, _, 48, 9, 55, 58, _, 18, _, _, _, _, 19, 85, 30, 92, 56,
     90, 75, 24, 10, 34, 23, _, 60, 39, 33, 50, _, 72, 74, 93, 77, _, _, 83, _, _, _, _, 38, 91, 76, 20, 67, _, _, 89, _, _, _, _, _, 98],
    [_, 26, 20, 21, _, _, _, _, _, _, 53, 87, _, _, _, _, 27, 92, 64, 86, _, 50, 1, 78, _, _, 33, 67, 51, 93, _, _, 91, 6, 8, 28, 77, 44, 15, 83, 47, 2, 81, 95, _, _, _, _, 79, 24, 90, 56, _, _, _, _, 32, 23, 5, 3, 13, 62, 42, 38,
     54, 52, 49, 71, _, _, 73, 40, 43, 22, _, _, 89, 100, 82, _, 19, 10, 46, 34, _, _, _, _, 37, 18, _, _, _, _, _, _, 31, 58, 63, _],
    [_, 30, 58, 25, 39, 59, _, _, _, _, _, _, _, _, 71, 52, 49, 17, 36, 42, _, 5, 96, 79, _, 66, 92, 47, 32, 90, _, _, 48, 73, 67, 98, 26, 14, 61, _, 99, 18, 19, 37, 10, 35, 55, _, _, _, _, _, _, 68, 40, 80, 2, 82, 22, 45, _, 65,
     53, 69, 29, 46, 64, 86, _, _, 24, 1, 21, 3, 81, _, 41, 84, 75, _, 93, 50, 77, 11, 33, 74, _, _, _, _, _, _, _, _, 8, 20, 38, 44, 6, _],
    [_, 55, 34, 99, 46, 85, 37, 35, 10, _, _, 89, 67, 61, 19, 81, 56, 98, 26, 21, _, 39, 87, _, _, 17, 97, 58, 31, 9, 3, _, _, 50, 72, 1, 47, 12, 93, 60, 52, 49, 27, 66, 14, _, _, 64, 86, 65, 42, 33, 95, _, _, 41, 79, 11, 77, 74,
     45, 94, 40, 22, 80, 100, 82, _, _, 68, 8, 83, 15, 28, 44, _, _, 38, 76, _, 88, 71, 13, 57, 53, 29, 16, 4, 69, _, _, 48, 92, 23, 30, 96, 32, 75, 5, _],
    [50, 74, 77, 78, 72, 51, 60, 96, 33, _, _, 14, 73, 24, 83, 39, 1, 84, 46, 20, _, 70, 10, _, 99, 55, _, _, _, _, _, _, _, _, 85, 30, 40, 63, 59, 97, 38, 15, 58, 69, 44, _, _, 8, 91, 11, 81, 62, 87, _, _, 92, 28, 71, 88, 29, 25,
     7, 98, 67, 61, 89, _, _, _, _, _, _, _, _, 54, 16, _, 66, 27, _, 75, 90, 22, 48, 5, 23, 47, 56, 79, _, _, 45, 80, 68, 82, 18, 94, 95, 2, 3],
    [52, 86, 27, 16, 53, 65, 64, 49, 54, 67, _, 48, 96, 75, 3, 90, 5, 32, 79, 95, _, 8, 28, _, _, _, _, 44, 18, 83, 13, 25, _, _, _, _, 62, 80, 69, 71, 51, 78, 93, 74, 72, _, 60, 50, 6, 33, 21, 89, 61, 73, _, 43, 98, 66, 36, 26,
     57, 11, 31, 97, _, _, _, _, 87, 59, 4, 42, 85, _, _, _, _, 55, 88, _, 45, 100, 12, 82, 2, 30, 81, 68, 92, _, 84, 47, 37, 34, 41, 22, 24, 40, 1, 56],
    [24, 91, 19, 56, 42, 8, 29, 69, 44, 38, _, 72, 34, 88, 70, 57, 40, 78, 77, 85, _, _, _, _, _, _, 68, 100, 22, 7, 18, 35, _, 51, _, _, _, _, 10, 95, 23, 75, 92, 5, 96, _, 21, 3, 90, 30, 50, 16, 60, 97, _, 93, 52, 64, 53, 46,
     20, 84, _, _, _, _, 28, _, 76, 12, 31, 11, 87, 9, _, _, _, _, _, _, 61, 98, 99, 89, 14, 1, 73, 43, 26, _, 86, 27, 66, 54, 4, 65, 62, 71, 49, 39],
    [12, 81, 3, 79, 34, 95, 63, 39, 21, 47, _, 51, 19, 48, 33, 75, 54, 96, 32, 99, 4, _, _, _, 44, 62, 26, 36, 88, 52, 98, 11, _, 58, 50, 31, 17, _, _, 72, 86, 20, 59, 6, 13, 66, 8, 22, 1, 28, 30, 71, 46, 92, 69, 23, 56, 5, 42,
     90, 49, _, _, 65, 16, 78, 91, _, 53, 87, 82, 43, 73, 15, 14, 57, _, _, _, 76, 2, 80, 100, 29, 9, 45, 40, 24, 7, _, 37, 74, 85, 94, 18, 35, 10, 93, 77, 55],
    [66, 33, 16, 77, 27, 88, 72, 74, 11, 86, _, 71, 46, 36, 69, 3, 29, 4, 42, 13, 22, _, _, _, 96, 40, 45, 82, 100, 2, 15, 83, _, 44, 20, 8, 76, _, _, 18, 32, 79, 50, 92, 23, _, 56, 78, 60, 51, 89, 54, 53, 21, _, 64, 14, 65, 49,
     98, 10, _, _, 35, 73, 43, 34, _, 67, 70, 58, 9, 39, 63, 87, 17, _, _, _, 25, 55, 26, 48, 30, 19, 52, 37, 90, 5, _, 1, 95, 41, 24, 6, 47, 81, 84, 68, 12],
    [36, 71, 60, 69, 76, 46, 4, 62, 42, _, _, 31, 7, 58, 22, 100, 87, 45, 25, 40, _, _, _, _, _, 57, 13, 16, 61, 89, 41, 1, _, 3, 12, 47, 95, _, _, _, 18, 55, 70, 85, 84, _, _, 35, 99, 10, 39, 17, 59, _, _, 94, 80, 2, 97, 68, _,
     _, _, 32, 5, 75, 90, _, 96, 56, 88, 78, 74, 77, 50, _, _, _, _, _, 44, 8, 38, 6, 34, 91, 83, 20, 28, _, _, 86, 21, 27, 52, 53, 49, 66, 54, 65],
    [31, 68, 23, 75, 96, 22, 52, 80, 82, _, _, 67, 26, 89, 98, 21, 57, 43, 14, 73, _, _, _, _, _, 1, 84, 6, 3, 47, 2, _, _, 100, 32, 48, 92, 94, _, _, 25, 16, 17, 91, 9, _, _, 63, 49, 53, 78, 50, 72, _, _, 60, 74, 77, 95, 93, _,
     _, 59, 58, 44, 83, 38, _, _, 76, 10, 34, 99, 37, 55, _, _, _, _, _, 54, 65, 41, 51, 64, 56, 33, 86, 81, _, _, 29, 36, 4, 42, 62, 46, 88, 71, 13],
    [85, 61, 25, 70, 55, 99, 19, 10, _, _, 5, 11, 50, 30, 60, 56, 37, 23, 90, _, _, _, 8, 69, _, _, 46, 76, 42, 28, _, _, 93, 74, 39, _, _, 77, _, _, _, 83, 54, 64, 65, 58, _, _, 97, 41, 62, 32, _, _, 48, 13, 88, 36, 75, _, _, _,
     66, _, _, 17, 20, 52, _, _, 94, 100, 80, 40, _, _, 7, 29, _, _, _, 3, 27, 92, 89, 53, 82, 95, 49, 84, _, _, 57, 16, 72, 73, 34, 67, 44, 14],
    [20, 83, 13, 44, 8, 38, 28, 6, _, _, 59, 97, 17, 77, 39, 94, 68, 2, 80, _, _, 74, 63, 72, 93, _, _, _, 60, 29, _, _, 53, _, _, _, 65, 42, 34, _, _, 82, 62, 4, 69, 71, _, _, 33, 21, 100, 87, _, _, 7, 31, 58, 25, 40, _, _, 98,
     19, 88, _, _, _, 14, _, _, 1, 79, _, _, _, 84, 81, 12, 3, _, _, 70, 76, 16, 43, 35, 85, 10, 73, 99, _, _, 32, 56, 23, 92, 5, 30, 96, 75],
    [78, 65, 93, 64, 51, 50, 54, _, _, 53, 95, 12, 41, 84, 47, 88, 81, _, 24, _, _, 87, 58, 17, 39, 33, _, _, _, _, _, _, _, _, 37, 85, 99, 55, 16, _, _, 11, 90, 77, 48, 30, 72, 5, _, 34, 52, _, 26, 66, 63, 67, 27, 73, 43, _, _,
     100, 82, 45, 22, 80, _, _, _, _, _, _, _, _, 46, 36, 71, 44, 42, _, _, 61, _, 14, 57, 18, 23, 98, 96, 21, 28, _, _, 8, 91, 15, 76, 3, 20, 89],
    [_, 92, 100, 94, 48, _, _, _, _, 45, 6, 28, 20, 83, 91, 44, 8, 76, 15, _, _, 95, 19, 37, 34, 18, _, _, _, _, _, 7, 22, 90, 80, 82, 75, 23, 68, _, _, 14, 40, 46, 57, 2, 73, _, _, _, _, _, _, 33, 41, 24, 51, 47, 3, _, _, 71, 21,
     89, 69, 13, 62, 42, 29, _, _, _, _, _, 38, 52, 65, 16, 54, _, _, 74, 78, 79, 77, 60, 66, 93, 11, 50, 39, _, _, _, _, 97, 63, 31, 9, _],
    [_, 73, 89, _, _, _, 67, _, 2, 14, _, 18, _, 74, 55, 85, 72, 82, 34, _, _, 54, 21, 77, 64, _, _, _, _, _, _, 71, 88, 69, 36, 13, 4, 52, 62, _, _, 29, 7, 42, 94, 38, 100, _, _, _, _, _, _, 16, 76, 15, 20, 8, 28, _, _, 24, 81,
     95, 79, 3, 84, 47, 12, _, _, _, _, _, _, 32, 48, 75, 30, _, _, 97, 58, 87, 63, 22, 31, _, 39, _, 70, 51, _, 98, _, _, _, 33, 19, _],
    [_, _, _, _, _, _, 24, 59, 1, 17, 27, 38, 49, 66, _, 64, 52, 65, 16, _, _, _, _, _, _, _, _, _, 68, 56, _, _, _, _, _, _, _, 61, 89, _, _, _, _, _, _, _, _, _, 95, _, _, 37, _, _, _, _, _, _, _, _, _, 51, 74, _, _, _, _, _, _,
     _, 21, 6, _, _, _, _, _, _, _, _, _, 46, 88, 94, 62, _, 69, 13, 36, 42, 79, 22, 7, 82, _, _, _, _, _, _],
    [_, _, _, _, _, 66, 86, 27, 3, 30, 20, 85, 48, 91, 28, 83, 15, _, 38, _, _, _, _, _, _, _, 74, 93, 11, 76, 67, 89, 43, 26, 21, 14, _, _, _, _, _, _, _, 34, _, 19, _, _, 35, 18, 88, 4, _, _, 46, _, 71, _, _, _, _, _, _, _, 82,
     95, 79, 1, 41, 24, 81, 5, 90, 56, _, _, _, _, _, _, _, 59, _, 39, 45, 97, 6, 63, 58, 17, 80, 78, 73, 40, 7, _, _, _, _, _],
    [_, _, 75, _, _, _, _, 92, 62, 52, 97, 66, 58, 59, 17, _, _, _, _, 5, 18, 34, 37, 99, 85, 19, 10, 35, 55, 96, 87, 53, 64, 86, 4, 49, 69, _, _, _, _, _, 12, 39, 47, 6, 9, 29, 41, 3, 79, 76, 83, 44, 15, 26, 95, 24, _, _, _, _,
     _, 13, 71, 36, 8, 46, 20, 42, 68, 94, 7, 2, 100, 67, 40, 45, 80, 30, 14, _, _, _, _, 61, 89, 21, 57, 43, 93, 72, 51, _, _, _, _, 77, _, _],
    [_, _, _, 67, _, _, _, _, 53, 15, 65, 16, 27, 64, _, _, _, _, _, _, 41, 79, 24, _, 81, 29, 47, 75, 95, 84, 55, 97, 90, 66, 58, 5, _, _, _, 82, _, _, _, 89, 40, 43, 98, 14, 32, 57, 28, 34, 70, 93, 85, 10, 6, _, _, _, 69, _, _,
     _, 3, 7, 22, 37, 92, 100, 33, 12, 13, 62, 71, 74, _, 36, 46, 42, _, _, _, _, _, _, 50, 31, 51, 19, 96, 59, _, _, _, _, 4, _, _, _],
    [14, _, _, 7, 22, 45, _, _, 96, 57, 24, 6, 12, 41, _, _, 84, _, _, 47, 89, 49, 53, 86, 65, 64, 27, 52, 54, 70, 33, 74, 78, 29, 16, 77, _, _, 72, 50, 87, _, _, 63, 17, 31, 91, 85, 58, 25, 40, 80, 2, 100, 98, 20, 21, _, _, 43,
     60, 9, _, _, 83, 76, 4, 56, 62, 38, 99, 18, 61, 73, 93, 8, 11, 69, 66, 19, 23, _, _, 26, _, _, 48, 5, 32, 92, 71, 81, _, _, 13, 36, 3, _, _, 95],
    [26, _, _, _, 44, 28, 38, _, _, 19, 54, 60, 77, _, _, 29, _, _, _, 52, 46, 69, 78, 25, 59, 42, 87, 62, 4, 88, 63, 13, 56, 23, 48, _, _, 32, 36, 92, 79, _, _, _, 45, 95, 20, 83, 15, 81, 99, 73, 84, 47, 91, 3, _, _, _, 1, 6, 67,
     49, _, _, 53, 96, 64, 65, 27, 14, 10, 37, 55, 34, 35, 70, 43, 89, 57, 7, _, _, _, 80, _, _, 72, 100, 2, 31, _, _, 90, 97, 9, _, _, _, 17],
    [68, 70, 37, _, _, _, 43, _, _, 83, 19, 79, 18, _, _, _, _, _, 3, 81, _, 9, 22, 71, 13, 63, 36, 97, 17, 39, 46, 42, 96, 12, 93, _, _, 11, 60, 62, 88, 27, _, _, _, _, 86, 53, 52, 54, 57, 14, 82, 74, _, _, _, _, 61, 49, 5, 75,
     30, _, _, 32, 16, 31, 80, 94, 77, 85, 51, 72, 21, 4, 98, 50, 26, _, 24, 44, _, _, _, _, _, 33, 91, 56, 89, _, _, 29, _, _, _, 69, 76, 41],
    [54, 39, 79, 24, _, _, _, _, _, _, 90, 30, _, _, _, _, 92, 63, 75, 23, 44, 83, 15, 50, 6, 91, 38, 28, 8, 20, 7, 80, 40, 2, _, _, 94, 45, 73, 68, 93, 74, 11, 72, _, _, _, _, 78, 77, 27, 66, _, _, _, _, 86, 53, 37, 65, 55, 47,
     70, 18, _, _, 85, 81, 10, 35, 48, 58, 84, 41, 17, 1, 9, 3, 59, 31, 13, 29, 4, 62, _, _, _, _, 71, 88, _, _, _, _, _, _, 98, 57, 67, 61],
    [17, 1, 31, 9, 41, 81, _, _, _, _, _, _, _, _, 88, 49, 13, 42, 4, 69, 56, _, 5, 92, 32, 90, 23, 3, 48, 16, 83, 38, 76, 91, _, _, 15, 8, 75, 28, 7, 67, 21, _, 26, 82, _, _, _, _, _, _, _, _, 60, 51, _, 19, 78, 72, 61, 89, 73,
     68, _, _, 14, 45, 57, 40, 39, 29, 25, 87, 24, 97, 47, 95, _, 79, 70, 35, 96, 74, 52, 93, _, _, _, _, _, _, _, _, 65, 34, 66, 27, 85, 18],
    [69, 42, 88, 89, 60, 4, 13, 71, 36, _, 67, 21, _, 80, 43, 61, 7, 73, 22, 14, 26, 40, 66, 82, 68, 100, 94, 57, 98, 45, 70, 19, 10, 37, _, 99, 34, 85, 95, 35, 90, 96, 56, _, 92, 5, 75, 23, 55, 48, 59, 9, 39, 31, 17, 25, _, 97,
     87, 58, 74, 93, 50, 77, 11, _, 51, 78, 33, 29, 49, 15, 53, 52, 65, 86, 38, 64, 91, 20, 76, 81, 3, 27, 79, 47, 41, _, 1, 54, _, 8, 24, 62, 16, 84, 83, 28, 32, 44],
    [93, 50, 11, 51, 29, 77, 78, 72, 74, _, 100, 94, _, 98, 89, 9, 26, 57, 68, 45, 73, _, 43, 67, 7, 12, _, _, _, _, _, _, _, _, _, 24, 3, 88, 31, 41, 71, 62, 46, _, 42, 4, 13, 49, 69, 8, 75, 48, 32, 5, 22, 96, _, 30, 23, 56, 39,
     59, 25, 63, 17, _, _, _, _, _, _, _, _, _, 83, 82, 27, 6, _, 28, 34, 85, 65, 95, 10, 66, 86, _, 18, 38, _, 64, 19, 70, 35, 79, 55, 91, 53, 99],
    [82, 7, 68, 2, 80, 94, _, _, _, _, _, _, _, _, 63, 59, 9, 58, 87, 17, 67, 26, 98, 57, _, _, _, _, 14, 61, 92, 51, _, _, _, _, 23, 75, 48, 66, 46, 36, 30, _, 62, 42, _, _, _, _, _, _, _, _, 3, 95, _, 79, 12, 24, 70, 19, 37, 39,
     _, _, _, _, 99, 18, 28, 76, _, _, _, _, 44, 20, 83, 8, 16, 64, 53, 65, 86, 81, _, _, _, _, _, _, _, _, 96, 88, 74, 72, 93, 60],
    [11, 78, 33, 50, _, _, _, _, 60, _, 89, 39, _, _, _, _, 43, 14, 61, 26, 96, 84, _, _, _, _, 12, 95, 5, 1, 79, 4, 62, 42, _, _, _, _, 100, 36, 6, 54, 66, 27, _, _, _, _, 53, 83, 23, 47, _, _, _, _, 90, 32, 48, 19, 88, 58, _, _,
     _, _, 25, 13, 31, 17, 59, 82, 68, 45, _, _, _, _, 7, 63, 80, 41, 15, 2, _, _, _, _, 38, 8, _, 10, _, _, _, _, 18, 99, 55, 35],
    [76, 38, _, _, _, _, 8, 44, _, _, 11, 36, _, _, _, _, _, _, 13, 29, 70, _, _, _, 10, 99, 35, 34, 91, 55, 16, 31, 97, 87, _, _, _, _, _, 9, 63, 93, _, _, _, _, 74, 72, 17, 78, 66, 68, 86, 82, _, _, _, _, 45, 100, 7, _, _, _, _,
     _, 27, 40, 54, 53, 89, 67, 14, 61, 98, 88, _, _, _, 21, 84, 30, _, _, _, _, _, _, 56, 5, _, _, 12, 95, _, _, _, _, 57, 24],
    [70, _, _, _, 79, 24, 3, 41, _, _, 92, 5, _, _, 23, 32, _, _, _, 56, 17, 72, _, 58, 63, 87, 31, 29, 97, 62, 6, 20, 83, 8, _, _, 44, _, _, 33, 10, _, _, _, 100, 85, 37, 55, 47, 35, 43, 98, 13, 61, 57, 88, _, _, _, 28, 11, _, _,
     48, _, _, 93, 50, 51, 77, 65, 86, 52, 27, 53, 54, 66, _, 16, 64, 42, _, _, _, 21, 39, _, _, 25, 46, _, _, 94, 7, 80, 40, _, _, _, 45],
    [56, _, _, 62, 75, 9, 42, _, _, 25, 88, 34, 99, _, _, 10, 35, _, _, 18, _, _, _, 94, 82, 7, 40, 2, 41, 11, 50, 54, 17, 52, 53, _, _, _, _, _, 77, _, _, 31, 87, 22, 59, 97, 92, 58, 74, 93, 81, 51, 16, 37, 70, _, _, 78, _, _, _,
     _, _, 20, 44, 38, 15, 65, 23, 90, 4, 57, 13, 5, 29, _, _, _, 1, _, _, 96, 47, _, _, 3, 24, 66, 98, _, _, 67, 43, 61, 89, _, _, 21],
    [_, _, _, 90, 71, 52, 5, _, _, 88, 94, 2, 82, _, _, 68, 80, _, _, _, _, _, 65, 16, 76, 49, 86, 19, 13, 53, 35, 37, 85, 95, 99, _, _, 10, _, _, _, _, _, 61, 43, 57, 26, 98, 21, 89, 97, 63, 31, 58, 25, 87, 59, _, _, _, _, _, 24,
     _, _, 12, 92, 96, 79, 1, 62, 30, 32, 100, 42, 48, 36, 56, _, _, _, _, _, 50, 69, _, _, 78, 33, 72, 91, _, _, 38, 15, 44, 28, _, _, _],
    [_, _, 73, 95, 21, 14, _, _, 57, 98, 74, 33, 54, 37, _, _, 51, 70, _, _, _, _, 92, 30, 24, 48, 32, 23, 45, 75, 12, 84, 41, 81, 13, 88, _, _, _, _, _, _, 28, 38, 8, 91, 44, 65, 76, 52, 26, 36, 18, 10, 96, 55, 72, 99, _, _, _,
     _, _, _, 62, 42, 87, 69, 5, 46, 17, 31, 58, 25, 39, 11, 78, 80, _, _, _, _, 83, 20, _, _, 94, 100, 22, 6, 9, 97, _, _, 49, 66, 27, 19, _, _],
    [_, _, 48, 63, _, _, _, _, 17, 32, 76, 86, 78, 38, 15, _, _, _, 91, _, _, 42, 33, 93, 22, 51, 60, 8, 44, 4, 89, 67, 26, 45, 61, 73, _, _, _, _, _, _, 39, 23, 5, 88, 96, 79, 25, 64, 2, 49, 40, 7, 56, 65, 53, 27, _, _, _, _, _,
     _, 68, 94, 95, 66, 90, 21, 47, 81, 24, 84, 12, 41, 97, 1, 50, _, _, 37, _, _, _, 19, 18, 99, 10, 55, 46, 62, _, _, _, _, 36, 13, _, _],
    [_, 69, _, _, _, _, _, 26, 34, 37, 52, 64, 44, 49, 16, _, _, _, _, _, _, 20, 88, 28, 66, 6, 54, 50, 83, 78, 82, 57, 68, 94, 19, 80, _, _, _, 2, _, 41, 84, 24, 70, 81, 3, 90, 18, 12, 46, 42, 5, 62, 38, 29, 11, 89, 21, _, 75, _,
     _, _, 56, 45, 23, 67, 86, 32, 51, 33, 92, 96, 77, 9, 79, 60, 95, _, _, _, _, _, _, 14, 43, 73, 61, 13, 53, 76, 31, _, _, _, _, _, 48, _],
    [_, _, _, _, _, 27, 66, 54, 65, 64, 84, 1, 47, 3, 79, 41, 12, _, _, _, _, _, _, 39, 36, 46, 71, 9, 69, 25, 56, 21, 60, _, _, _, 72, 5, 28, _, _, 80, _, _, _, 75, 45, 94, 40, 2, 76, 6, 15, 83, 20, _, _, _, 91, _, _, 26, 22,
     100, _, _, _, 61, 89, 98, 34, 55, 18, 70, 19, 10, 37, _, _, _, _, _, _, 59, 31, 4, 62, 58, 29, 97, 77, 23, 87, 78, 90, _, _, _, _, _],
]

sudokuSolverOrtools.solve_sudoku(grid100x100)
sudokuSolverZ3.solve_sudoku(grid100x100)
