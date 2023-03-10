import numpy as np
from numba import njit


TILE_TILE = np.array(
    [[1, 11, 12, 17, -1, -1],  # 0
     [0, 2, 17, -1, -1, -1],  # 1
     [1, 3, 16, 17, -1, -1],  # 2
     [2, 4, 16, -1, -1, -1],  # 3
     [3, 5, 15, 16, -1, -1],  # 4
     [4, 6, 15, -1, -1, -1],  # 5
     [5, 7, 14, 15, -1, -1],  # 6
     [6, 8, 14, -1, -1, -1],  # 7
     [7, 9, 13, 14, -1, -1],  # 8
     [8, 10, 13, -1, -1, -1],  # 9
     [9, 11, 12, 13, -1, -1],  # 10
     [0, 10, 12, -1, -1, -1],  # 11
     [0, 10, 11, 13, 17, 18],  # 12
     [8, 9, 10, 12, 14, 18],  # 13
     [6, 7, 8, 13, 15, 18],  # 14
     [4, 5, 6, 14, 16, 18],  # 15
     [2, 3, 4, 15, 17, 18],  # 16
     [0, 1, 2, 12, 16, 18],  # 17
     [12, 13, 14, 15, 16, 17]]  # 18
)

POINT_POINT = np.array(
    [[1, 29, -1],  # 0
     [0, 2, 46],  # 1
     [1, 3, -1],  # 2
     [2, 4, -1],  # 3
     [3, 5, 45],  # 4
     [4, 6, -1],  # 5
     [5, 7, 43],  # 6
     [6, 8, -1],  # 7
     [7, 9, -1],  # 8
     [8, 10, 42],  # 9
     [9, 11, -1],  # 10
     [10, 12, 40],  # 11
     [11, 13, -1],  # 12
     [12, 14, -1],  # 13
     [13, 15, 39],  # 14
     [14, 16, -1],  # 15
     [15, 17, 37],  # 16
     [16, 18, -1],  # 17
     [17, 19, -1],  # 18
     [18, 20, 36],  # 19
     [19, 21, -1],  # 20
     [20, 22, 34],  # 21
     [21, 23, -1],  # 22
     [22, 24, -1],  # 23
     [23, 25, 33],  # 24
     [24, 26, -1],  # 25
     [25, 27, 31],  # 26
     [26, 28, -1],  # 27
     [27, 29, -1],  # 28
     [0, 28, 30],  # 29
     [29, 31, 47],  # 30
     [26, 30, 32],  # 31
     [31, 33, 49],  # 32
     [24, 32, 34],  # 33
     [21, 33, 35],  # 34
     [34, 36, 50],  # 35
     [19, 35, 37],  # 36
     [16, 36, 38],  # 37
     [37, 39, 51],  # 38
     [14, 38, 40],  # 39
     [11, 39, 41],  # 40
     [40, 42, 52],  # 41
     [9, 41, 43],  # 42
     [6, 42, 44],  # 43
     [43, 45, 53],  # 44
     [4, 44, 46],  # 45
     [1, 45, 47],  # 46
     [30, 46, 48],  # 47
     [47, 49, 53],  # 48
     [32, 48, 50],  # 49
     [35, 49, 51],  # 50
     [38, 50, 52],  # 51
     [41, 51, 53],  # 52
     [44, 48, 52]]  # 53
)

ROAD_POINT = np.array(
    [[0, 29],  # 0
     [0,  1],  # 1
     [1, 46],  # 2
     [1,  2],  # 3
     [2,  3],  # 4
     [3,  4],  # 5
     [4, 45],  # 6
     [4,  5],  # 7
     [5,  6],  # 8
     [6, 43],  # 9
     [6,  7],  # 10
     [7,  8],  # 11
     [8,  9],  # 12
     [9, 42],  # 13
     [9, 10],  # 14
     [10, 11],  # 15
     [11, 40],  # 16
     [11, 12],  # 17
     [12, 13],  # 18
     [13, 14],  # 19
     [14, 39],  # 20
     [14, 15],  # 21
     [15, 16],  # 22
     [16, 37],  # 23
     [16, 17],  # 24
     [17, 18],  # 25
     [18, 19],  # 26
     [19, 36],  # 27
     [19, 20],  # 28
     [20, 21],  # 29
     [21, 34],  # 30
     [21, 22],  # 31
     [22, 23],  # 32
     [23, 24],  # 33
     [24, 33],  # 34
     [24, 25],  # 35
     [25, 26],  # 36
     [26, 31],  # 37
     [26, 27],  # 38
     [27, 28],  # 39
     [28, 29],  # 40
     [29, 30],  # 41
     [30, 31],  # 42
     [31, 32],  # 43
     [32, 49],  # 44
     [32, 33],  # 45
     [33, 34],  # 46
     [34, 35],  # 47
     [35, 50],  # 48
     [35, 36],  # 49
     [36, 37],  # 50
     [37, 38],  # 51
     [38, 51],  # 52
     [38, 39],  # 53
     [39, 40],  # 54
     [40, 41],  # 55
     [41, 52],  # 56
     [41, 42],  # 57
     [42, 43],  # 58
     [43, 44],  # 59
     [44, 53],  # 60
     [44, 45],  # 61
     [45, 46],  # 62
     [46, 47],  # 63
     [47, 48],  # 64
     [30, 47],  # 65
     [48, 49],  # 66
     [49, 50],  # 67
     [50, 51],  # 68
     [51, 52],  # 69
     [52, 53],  # 70
     [48, 53]]  # 71
)

POINT_ROAD = np.array(
    [[0,  1, -1],  # 0
     [1,  2,  3],  # 1
     [3,  4, -1],  # 2
     [4,  5, -1],  # 3
     [5,  6,  7],  # 4
     [7,  8, -1],  # 5
     [8,  9, 10],  # 6
     [10, 11, -1],  # 7
     [11, 12, -1],  # 8
     [12, 13, 14],  # 9
     [14, 15, -1],  # 10
     [15, 16, 17],  # 11
     [17, 18, -1],  # 12
     [18, 19, -1],  # 13
     [19, 20, 21],  # 14
     [21, 22, -1],  # 15
     [22, 23, 24],  # 16
     [24, 25, -1],  # 17
     [25, 26, -1],  # 18
     [26, 27, 28],  # 19
     [28, 29, -1],  # 20
     [29, 30, 31],  # 21
     [31, 32, -1],  # 22
     [32, 33, -1],  # 23
     [33, 34, 35],  # 24
     [35, 36, -1],  # 25
     [36, 37, 38],  # 26
     [38, 39, -1],  # 27
     [39, 40, -1],  # 28
     [0, 40, 41],  # 29
     [41, 42, 65],  # 30
     [37, 42, 43],  # 31
     [43, 44, 45],  # 32
     [34, 45, 46],  # 33
     [30, 46, 47],  # 34
     [47, 48, 49],  # 35
     [27, 49, 50],  # 36
     [23, 50, 51],  # 37
     [51, 52, 53],  # 38
     [20, 53, 54],  # 39
     [16, 54, 55],  # 40
     [55, 56, 57],  # 41
     [13, 57, 58],  # 42
     [9, 58, 59],  # 43
     [59, 60, 61],  # 44
     [6, 61, 62],  # 45
     [2, 62, 63],  # 46
     [63, 64, 65],  # 47
     [64, 66, 71],  # 48
     [44, 66, 67],  # 49
     [48, 67, 68],  # 50
     [52, 68, 69],  # 51
     [56, 69, 70],  # 52
     [60, 70, 71]]  # 53
)

PORT_POINT = np.array(
    [[0, 1],
     [4, 5],
     [7, 8],
     [10, 11],
     [14, 15],
     [17, 18],
     [20, 21],
     [24, 25],
     [27, 28]]
)

POINT_TILE = np.array(
    [[0, -1, -1],  # 0
     [0, 1, -1],  # 1
     [1, -1, -1],  # 2
     [1, -1, -1],  # 3
     [1, 2, -1],  # 4
     [2, -1, -1],  # 5
     [2, 3, -1],  # 6
     [3, -1, -1],  # 7
     [3, -1, -1],  # 8
     [3, 4, -1],  # 9
     [4, -1, -1],  # 10
     [4, 5, -1],  # 11
     [5, -1, -1],  # 12
     [5, -1, -1],  # 13
     [5, 6, -1],  # 14
     [6, -1, -1],  # 15
     [6, 7, -1],  # 16
     [7, -1, -1],  # 17
     [7, -1, -1],  # 18
     [7, 8, -1],  # 19
     [8, -1, -1],  # 20
     [8, 9, -1],  # 21
     [9, -1, -1],  # 22
     [9, -1, -1],  # 23
     [9, 10, -1],  # 24
     [10, -1, -1],  # 25
     [10, 11, -1],  # 26
     [11, -1, -1],  # 27
     [11, -1, -1],  # 28
     [0, 11, -1],  # 29
     [0, 11, 12],  # 30
     [10, 11, 12],  # 31
     [10, 12, 13],  # 32
     [9, 10, 13],  # 33
     [8, 9, 13],  # 34
     [8, 13, 14],  # 35
     [7, 8, 14],  # 36
     [6, 7, 14],  # 37
     [6, 14, 15],  # 38
     [5, 6, 15],  # 39
     [4, 5, 15],  # 40
     [4, 15, 16],  # 41
     [3, 4, 16],  # 42
     [2, 3, 16],  # 43
     [2, 16, 17],  # 44
     [1, 2, 17],  # 45
     [0, 1, 17],  # 46
     [0, 12, 17],  # 47
     [12, 17, 18],  # 48
     [12, 13, 18],  # 49
     [13, 14, 18],  # 50
     [14, 15, 18],  # 51
     [15, 16, 18],  # 52
     [16, 17, 18]]  # 53
)

TILE_POINT = np.array(
    [[0,  1, 29, 30, 46, 47],  # 0
     [1,  2,  3,  4, 45, 46],  # 1
     [4,  5,  6, 43, 44, 45],  # 2
     [6,  7,  8,  9, 42, 43],  # 3
     [9, 10, 11, 40, 41, 42],  # 4
     [11, 12, 13, 14, 39, 40],  # 5
     [14, 15, 16, 37, 38, 39],  # 6
     [16, 17, 18, 19, 36, 37],  # 7
     [19, 20, 21, 34, 35, 36],  # 8
     [21, 22, 23, 24, 33, 34],  # 9
     [24, 25, 26, 31, 32, 33],  # 10
     [26, 27, 28, 29, 30, 31],  # 11
     [30, 31, 32, 47, 48, 49],  # 12
     [32, 33, 34, 35, 49, 50],  # 13
     [35, 36, 37, 38, 50, 51],  # 14
     [38, 39, 40, 41, 51, 52],  # 15
     [41, 42, 43, 44, 52, 53],  # 16
     [44, 45, 46, 47, 48, 53],  # 17
     [48, 49, 50, 51, 52, 53]]  # 18
)


ROAD_PRICE = np.array([1, 1, 0, 0, 0])
SETTLEMENT_PRICE = np.array([1, 1, 1, 1, 0])
CITY_PRICE = np.array([0, 0, 0, 2, 3])
DEV_CARD_PRICE = np.array([0, 0, 1, 1, 1])

__STATE_SIZE__ = 1048
__ACTION_SIZE__ = 106

# C??ng cao th?? ch???y c??ng l??u, nh??ng t??? l??? kh??ng end ???????c game gi???m
__MAX_TURN_IN_ONE_GAME__ = 800


@njit()
def initEnv():
    env = np.zeros(256, np.float64)

    # [0:19]: T??i nguy??n tr??n c??c ?? ?????t
    temp = np.array([5, 0, 0, 0, 0, 2, 2, 2, 2, 3, 3, 3, 3, 1, 1, 1, 4, 4, 4])
    np.random.shuffle(temp)
    env[0:19] = temp

    # [19]: V?? tr?? Robber
    env[19] = np.argmax(temp)

    # [20:39]: S??? tr??n c??c ?? ?????t
    temp_prob = np.zeros(19)
    temp = np.ones(19)
    temp[int(env[19])] = 0
    temp_1 = temp.copy()
    for i in range(4):
        temp_2 = np.where(temp == 1)[0]
        k = temp_2[np.random.randint(0, len(temp_2))]
        temp[k] = 0
        temp_1[k] = 0
        if i < 2:
            temp_prob[k] = 6
        else:
            temp_prob[k] = 8

        for j in TILE_TILE[k]:
            if j == -1:
                break
            else:
                temp[j] = 0

    temp = np.array([3, 3, 4, 4, 5, 5, 9, 9, 10, 10, 11, 11, 2, 12])
    np.random.shuffle(temp)
    temp_prob[np.where(temp_1 == 1)[0]] = temp
    env[20:39] = temp_prob

    # [39:48]: C??c c???ng
    temp = np.array([5, 5, 5, 5, 0, 1, 2, 3, 4])
    np.random.shuffle(temp)
    env[39:48] = temp

    # [48:53]: T??i nguy??n ng??n h??ng
    env[48:53] = 19

    # [53:58]: Th??? dev bank
    env[53:58] = np.array([14, 2, 2, 2, 5])

    # Th??ng tin ng?????i ch??i: [58,100], [100:142], [142,184], [184:226]
    for p_idx in range(4):
        s_ = 58 + 42*p_idx  # 58, 100, 142, 184
        # [+0:+5]: T??i nguy??n
        # [+5:+10]: Th??? dev
        # [+10]: ??i???m

        # [+11:+26]: ???????ng
        # [+26:+31]: Nh??
        # [+31:+35]: Th??nh ph???
        env[s_+11:s_+35] = -1

        # [+35]: S??? th??? knight ???? d??ng
        # [+36]: Con ???????ng d??i nh???t

        # [+37:+42]: T??? l??? trao ?????i v???i Bank
        env[s_+37:s_+42] = 4

    # [226]: Danh hi???u qu??n ?????i m???nh nh???t
    # [227]: Danh hi???u con ???????ng d??i nh???t
    # [228]: T???ng xx
    env[226:229] = -1

    # [229]: Pha
    # [230]: Turn

    # [231]: ??i???m ?????t th??? nh???t
    env[231] = -1

    # [232]: S??? t??i nguy??n tr??? do b??? chia

    # [233]: ??ang d??ng th??? dev g??
    env[233] = -1

    # [234]: S??? l???n s??? d???ng th??? dev
    # [235:239]: Lo???i th??? dev ???????c s??? d???ng trong turn hi???n t???i
    # [239]: S??? l???n t???o trade offer
    # [240:245]: T??i nguy??n ????a ra trong trade offer
    # [245:250]: T??i nguy??n y??u c???u trong trade offer
    # 250: L?????ng t??i nguy??n ???????c y??u c???u t???i ??a trong trade offer

    # [251:254]: Ph???n h???i c???a ng?????i ch??i ph??? v??? trade offer (?????ng ?? hay kh??ng)
    env[251:254] = -1

    # [254]: Ng?????i ch??i ??ang action (kh??ng h???n l?? ng?????i ch??i ch??nh)

    # [255]: ???? k???t th??c game hay ch??a, 1 l?? k???t th??c r???i

    return env


@njit()
def getAgentState(env_):
    env = env_.astype(np.int64)
    state = np.zeros(__STATE_SIZE__, np.float64)
    p_idx = env[254]
    turn = env[230]
    if turn >= 4 and turn <= 7:
        main_p_idx = 7 - turn
    else:
        main_p_idx = turn % 4

    # [0:95] C??y G???ch C???u L??a ???? tr??n 19 ?? ?????t
    for i in range(19):
        if env[i] != 5:
            state[5*i+env[i]] = 1

    # [95:114] V??? tr?? Robber
    state[95+env[19]] = 1

    # [114:133] Value tr??n c??c ?? ?????t
    state[114:133] = env[20:39]

    # [133:187] C??y G???ch C???u L??a ???? 3:1 Lo???i c???ng tr??n 9 c???ng
    for i in range(9):
        state[133+6*i+env[39+i]] = 1

    # [187:192] T??i nguy??n bank c??n hay kh??ng
    state[187:192] = env[48:53] > 0

    # [192] Th??? dev bank c??n hay kh??ng
    state[192] = (env[53:58] > 0).any()

    # Th??ng tin c?? nh??n
    s_ = 58 + 42*p_idx

    '''T??i nguy??n: [+0:+5]'''
    state[193:198] = env[s_:s_+5]

    '''S??? th??? dev: [+5:+10]'''
    state[198:203] = env[s_+5:s_+10]

    '''S??? ??i???m: [+10]'''
    state[203] = env[s_+10]

    '''???????ng: [+11:+83]'''
    roads = env[s_+11:s_+26]
    state[204 + roads[roads != -1]] = 1

    '''Nh??: [+83:+137]'''
    settlements = env[s_+26:s_+31]
    state[276 + settlements[settlements != -1]] = 1

    '''Th??nh ph???: [+137:+191]'''
    cities = env[s_+31:s_+35]
    state[330 + cities[cities != -1]] = 1

    '''S??? th??? knight ???? d??ng: [+191]'''
    state[384] = env[s_+35]

    '''????? d??i con ???????ng d??i nh???t: [+192]'''
    state[385] = env[s_+36]

    '''T??? l??? trao ?????i v???i ng??n h??ng: [+193:+198]'''
    state[386:391] = env[s_+37:s_+42]

    # Th??ng tin ng?????i ch??i kh??c
    for i in range(1, 4):
        e_idx = (p_idx + i) % 4
        s_e = 58 + 42*e_idx
        s_p = 391 + 185*(i-1)

        '''T???ng t??i nguy??n: [+0]'''
        state[s_p] = np.sum(env[s_e:s_e+5])

        '''T???ng s??? th??? dev: [+1]'''
        state[s_p+1] = np.sum(env[s_e+5:s_e+10])

        '''S??? ??i???m: [+2]'''
        state[s_p+2] = env[s_e+10]

        '''???????ng: [+3:+75]'''
        roads = env[s_e+11:s_e+26]
        state[s_p+3 + roads[roads != -1]] = 1

        '''Nh??: [+75:+129]'''
        settlements = env[s_e+26:s_e+31]
        state[s_p+75 + settlements[settlements != -1]] = 1

        '''Th??nh ph???: [+129:+183]'''
        cities = env[s_e+31:s_e+35]
        state[s_p+129 + cities[cities != -1]] = 1

        '''S??? th??? knight ???? d??ng: [+183]'''
        state[s_p+183] = env[s_e+35]

        '''????? d??i con ???????ng d??i nh???t: [+184]'''
        state[s_p+184] = env[s_e+36]

    # T???ng xx
    if env[228] != -1:
        state[946] = env[228]

    # Phase: [947:963]
    state[947+env[229]] = 1

    # ??i???m ?????t th??? nh???t: [963:1017]
    if env[231] != -1:
        state[963+env[231]] = 1

    # S??? t??i nguy??n ph???i b??? do b??? chia: [1017]
    state[1017] = env[232]

    # Th??? dev ??ang d??ng l?? g??: [1018:1022]
    if env[233] != -1:
        state[1018+env[233]] = 1

    # S??? l???n ???????c d??ng th??? dev: [1022]
    state[1022] = env[234]

    # Lo???i th??? dev ???????c s??? d???ng trong turn hi???n t???i: [1023:1027]
    state[1023:1027] = env[235:239]

    # S??? l???n ???????c t???o trade offer: [1027]
    state[1027] = env[239]

    # L?????ng t??i nguy??n ????a ra trong trade offer: [1028:1033]
    # L?????ng t??i nguy??n y??u c???u trong trade offer: [1033:1038]
    # Ph???n h???i c???a ng?????i ch??i ph???: [1038:1044]
    # Ng?????i ch??i ch??nh: [1044:1047]

    if main_p_idx != p_idx:
        state[1044 + (main_p_idx - p_idx) % 4 - 1] = 1

    if (state[1044:1047] == 1).any(): # Kh??ng ph???i ng?????i ch??i ch??nh
        state[1028:1033] = env[245:250]
        state[1033:1038] = env[240:245]
    else: # Ng?????i ch??i ch??nh
        state[1028:1038] = env[240:250]
        for i in range(3):
            if env[251+i] != -1:
                state[1038+2*i+env[251+i]] = 1

    # K???t th??c game hay ch??a
    state[1047] = env[255]

    return state


@njit()
def get_p_point_n_all_road(state):
    p_point = np.zeros(54, np.int64)
    all_road = np.zeros(72, np.int64)
    my_road_states = state[204:276]

    temp = np.where(my_road_states == 1)[0]
    for road in temp:
        all_road[road] = 1
        p_point[ROAD_POINT[road]] = 1

    for j in range(3):
        s_ = 391 + 185*j
        e_road_states = state[s_+3:s_+75]
        e_sett_states = state[s_+75:s_+129]
        e_city_states = state[s_+129:s_+183]

        temp = np.where(e_road_states == 1)[0]
        for road in temp:
            all_road[road] = 1

        temp = np.where(e_sett_states == 1)[0]
        for i in temp:
            p_point[i] = 0

        temp = np.where(e_city_states == 1)[0]
        for i in temp:
            p_point[i] = 0

    return p_point, all_road


@njit()
def check_firstPoint(state):
    p_point, all_road = get_p_point_n_all_road(state)
    list_point = np.where(p_point == 1)[0]
    for point in list_point:
        for road in POINT_ROAD[point]:
            if road != -1 and all_road[road] == 0:
                return True

    return False


@njit()
def check_useDev(state, validActions):
    my_dev_states = state[1023:1027]
    my_road_states = state[204:276]
    bank_res = state[187:192]

    # Knight: C?? l?? ???????c d??ng
    if my_dev_states[0] == 1:
        validActions[55] = 1

    # Roadbuilding: C??n ???????ng v?? c??n v??? tr?? x??y ???????ng
    if my_dev_states[1] == 1 and np.count_nonzero(my_road_states == 1) < 15 and check_firstPoint(state):
        validActions[56] = 1

    # Yearofplenty: Ng??n h??ng c?? t??i nguy??n
    if my_dev_states[2] == 1 and (bank_res == 1).any():
        validActions[57] = 1

    # Monopoly: C?? l?? ???????c d??ng
    if my_dev_states[3] == 1:
        validActions[58] = 1


@njit()
def get_p_point_n_all_stm_city(state):
    p_point = np.zeros(54, np.int64)
    all_stm_and_city = np.zeros(54, np.int64)

    my_road_states = state[204:276]
    my_sett_states = state[276:330]
    my_city_states = state[330:384]

    temp = np.where(my_road_states == 1)[0]
    for i in temp:
        p_point[ROAD_POINT[i]] = 1

    temp = np.where(my_sett_states == 1)[0]
    for i in temp:
        all_stm_and_city[i] = 1
        p_point[i] = 0

    temp = np.where(my_city_states == 1)[0]
    for i in temp:
        all_stm_and_city[i] = 1
        p_point[i] = 0

    for j in range(3):
        s_ = 391 + 185*j
        e_sett_states = state[s_+75:s_+129]
        e_city_states = state[s_+129:s_+183]

        temp = np.where(e_sett_states == 1)[0]
        for i in temp:
            all_stm_and_city[i] = 1
            p_point[i] = 0

        temp = np.where(e_city_states == 1)[0]
        for i in temp:
            all_stm_and_city[i] = 1
            p_point[i] = 0

    return p_point, all_stm_and_city


@njit()
def getValidActions(state):
    validActions = np.zeros(__ACTION_SIZE__, np.float64)
    phase_ = np.where(state[947:963]==1)[0]
    if phase_.shape[0] == 1:
        phase = phase_[0]
    else:
        phase = -1

    trade_give_res = state[1028:1033]
    trade_take_res = state[1033:1038]
    my_res = state[193:198]
    my_road_states = state[204:276]
    my_sett_states = state[276:330]
    my_city_states = state[330:384]
    bank_res = state[187:192]
    bank_dev = state[192]
    trade_offer_time_use = state[1027]
    bank_offer_ratio = state[386:391]
    first_point_state = state[963:1017]
    robber_state = state[95:114]
    trade_response_state = state[1038:1044]
    using_dev_state = state[1018:1022]

    if phase == 11:  # Y??u c???u t??i nguy??n khi trade v???i ng?????i
        # N???u ???? c?? ??t nh???t 1 t??i nguy??n, th?? ph???i c?? action d???ng
        if (trade_take_res > 0).any():
            validActions[104] = 1

        # C??c action th??m t??i nguy??n: c??c lo???i t??i nguy??n m?? kh??ng c?? trong ph???n ????a ra
        validActions[59:64] = (trade_give_res == 0)

        return validActions

    if phase == 6:  # Ch???n c??c m?? ??un gi???a turn
        check_useDev(state, validActions)

        if (my_res > 0).any():
            if (my_res >= ROAD_PRICE).all():
                # Mua ???????ng (86)
                if np.count_nonzero(my_road_states == 1) < 15 and check_firstPoint(state):
                    validActions[86] = 1

                # Mua nh??
                if (my_res >= SETTLEMENT_PRICE).all() and np.count_nonzero(my_sett_states == 1) < 5:
                    p_point, all_stm_and_city = get_p_point_n_all_stm_city(state)
                    list_point = np.where(p_point == 1)[0]
                    for point in list_point:
                        list_road = POINT_ROAD[point][POINT_ROAD[point] != -1]
                        nearest_points = ROAD_POINT[list_road].flatten()
                        if (all_stm_and_city[nearest_points] == 0).all():
                            validActions[87] = 1
                            break

            # Mua th??nh ph??? (88)
            if (my_res >= CITY_PRICE).all() and np.count_nonzero(my_sett_states == 1) > 0 and np.count_nonzero(my_city_states == 1) < 4:
                validActions[88] = 1

            # Mua th??? dev (89)
            if (my_res >= DEV_CARD_PRICE).all() and bank_dev == 1:
                validActions[89] = 1

            # Trade v???i ng?????i (90)
            if trade_offer_time_use > 0 and (state[np.array([391, 576, 761], np.int64)] > 0).any():
                validActions[90] = 1

            # Trade v???i Bank
            if (my_res >= bank_offer_ratio).any():
                temp = np.where(my_res >= bank_offer_ratio)[0]
                for res in temp:
                    for res_1 in range(5):
                        if res_1 != res and bank_res[res_1] == 1:
                            validActions[91] = 1
                            break

                    if validActions[91] == 1:
                        break

        # K???t th??c l?????t (92)
        validActions[92] = 1

        return validActions

    if phase == 10:  # ????a ra t??i nguy??n khi trade v???i ng?????i
        # N???u ???? c?? ??t nh???t 1 t??i nguy??n, th?? ph???i c?? action d???ng
        if (trade_give_res > 0).any():
            validActions[103] = 1

        # C??c action th??m t??i nguy??n: c??c t??i nguy??n m?? b???n th??n c??
        validActions[95:100] = (my_res > trade_give_res)

        # N???u s??? lo???i t??i nguy??n b??? v??o l?? 4 th?? kh??ng cho b??? lo???i th??? 5 v??o
        if np.count_nonzero(trade_give_res > 0) == 4:
            validActions[95+np.argmin(trade_give_res)] = 0

        return validActions

    if phase == 3:  # Tr??? t??i nguy??n do b??? chia b??i
        validActions[95:100] = (my_res > 0)
        return validActions

    if phase == 12:  # Ng?????i ch??i ph??? ph???n h???i trade
        # V??o pha n??y th?? ch???c ch???n ng?????i ch??i ph??? ph???i c?? th??? trade
        validActions[93:95] = 1
        return validActions

    if phase == 15:  # Ch???n t??i nguy??n mu???n nh???n t??? ng??n h??ng
        # Ch???n nh???ng t??i nguy??n m?? ng??n h??ng c??, kh??c t??i nguy??n ????a ra
        validActions[59:64] = bank_res
        validActions[59+np.argmax(trade_give_res)] = 0
        return validActions

    if phase == 14:  # Ch???n t??i nguy??n khi trade v???i ng??n h??ng
        # Ch???n nh???ng t??i nguy??n m?? khi ch???n, ng??n h??ng c??n ??t nh???t 1 lo???i t??i nguy??n kh??c
        temp = np.where(my_res >= bank_offer_ratio)[0]
        for res in temp:
            for res_1 in range(5):
                if res_1 != res and bank_res[res_1] == 1:
                    validActions[95+res] = 1
                    break

        return validActions

    if phase == 1:  # Ch???n c??c ??i???m ?????u m??t c???a ???????ng
        p_point, all_road = get_p_point_n_all_road(state)
        if (first_point_state == 0).all(): # Ch???n ??i???m th??? nh???t
            list_point = np.where(p_point == 1)[0]
            for point in list_point:
                list_road = POINT_ROAD[point][POINT_ROAD[point] != -1]
                if (all_road[list_road] == 0).any():
                    validActions[point] = 1

            return validActions

        first_point_ = np.where(first_point_state==1)[0]
        if first_point_.shape[0] == 1:
            first_point = first_point_[0]
        else:
            first_point = -1

        if first_point != -1:
            for road in POINT_ROAD[first_point]:
                if road != -1 and all_road[road] == 0:
                    validActions[ROAD_POINT[road]] = 1

            validActions[first_point] = 0

        return validActions

    if phase == 4:  # Di chuy???n Robber
        robber_pos = np.where(robber_state == 1)[0]
        if robber_pos.shape[0] == 1:
            validActions[64:83] = 1
            validActions[64+robber_pos[0]] = 1

        return validActions

    if phase == 13:  # Ng?????i ch??i ch??nh duy???t trade
        # Action b??? qua
        validActions[105] = 1

        # Ch???n ng?????i ????? trade
        # V??o pha n??y th?? ch???c ch???n c?? ??t nh???t m???t ng?????i ?????ng ?? trade
        validActions[100:103] = trade_response_state[np.arange(1, 6, 2, np.int64)]

        return validActions

    if phase == 5:  # Ch???n ng?????i ????? c?????p t??i nguy??n
        robber_pos_ = np.where(robber_state == 1)[0]
        if robber_pos_.shape[0] == 1:
            robber_pos = robber_pos_[0]
            for i in range(3):
                s_ = 391 + 185*i
                e_sett_states = state[s_+75:s_+129]
                e_city_states = state[s_+129:s_+183]
                if state[s_] > 0: # Ch??? x??t khi c?? t??i nguy??n
                    temp_1 = np.where(e_sett_states == 1)[0]
                    temp_2 = np.where(e_city_states == 1)[0]
                    temp = np.concatenate((temp_1, temp_2))
                    for point in temp:
                        if point != -1 and point in TILE_POINT[robber_pos]:
                            validActions[83+i] = 1
                            break

        return validActions

    if phase == 2:  # ????? xx ho???c d??ng th??? dev
        # ????? xx
        validActions[54] = 1
        check_useDev(state, validActions)
        return validActions

    if phase == 0:  # Ch???n ??i???m ?????t nh?? ?????u game
        validActions[0:54] = 1

        temp = np.where(my_sett_states == 1)[0]
        for i in range(3):
            s_ = 391 + 185*i
            e_sett_states = state[s_+75:s_+129]
            temp = np.concatenate((temp, np.where(e_sett_states == 1)[0]))

        for stm in temp:
            validActions[stm] = 0
            for point in POINT_POINT[stm]:
                if point != -1:
                    validActions[point] = 0

        return validActions

    if phase == 8:  # Ch???n c??c ??i???m mua nh??
        p_point, all_stm_and_city = get_p_point_n_all_stm_city(state)
        list_point = np.where(p_point == 1)[0]
        for point in list_point:
            list_road = POINT_ROAD[point][POINT_ROAD[point] != -1]
            nearest_points = ROAD_POINT[list_road].flatten()
            if (all_stm_and_city[nearest_points] == 0).all():
                validActions[point] = 1

        return validActions

    if phase == 7:  # Ch???n t??i nguy??n khi d??ng th??? dev
        dev_using_ = np.where(using_dev_state == 1)[0]
        if dev_using_.shape[0] == 1:
            dev_using = dev_using_[0]
            if dev_using == 2: # ??ang d??ng yearofplenty
                validActions[59:64] = bank_res
            elif dev_using == 3: # ??ang d??ng monopoly
                validActions[59:64] = 1

        return validActions

    if phase == 9: # Ch???n c??c ??i???m mua th??nh ph???
        temp = np.where(my_sett_states == 1)[0]
        validActions[temp] = 1
        return validActions

    return validActions


@njit()
def find_max_road(len_, diemXP, duongDaDi, p_road, p_point):
    duongCanCheck = np.zeros(72)
    for road in POINT_ROAD[diemXP]:
        if road != -1 and p_road[road] == 1 and duongDaDi[road] == 0:
            duongCanCheck[road] = 1

    list_duongCanCheck = np.where(duongCanCheck == 1)[0]
    if len(list_duongCanCheck) == 0 or p_point[diemXP] == 0:
        if len_ > 0:
            return len_

    max_len = len_
    for road in list_duongCanCheck:
        duongDaDi_copy = duongDaDi.copy()
        duongDaDi_copy[road] = 1
        diemXP_1 = 9999
        for diem in ROAD_POINT[road]:
            if diem != diemXP:
                diemXP_1 = diem
                break

        len_1 = find_max_road(
            len_+1, diemXP_1, duongDaDi_copy, p_road, p_point)
        if len_1 > max_len:
            max_len = len_1

    return max_len


@njit()
def get_p_longest_road(env, p_idx):
    s_ = 58 + 42*p_idx
    p_road = np.zeros(72)
    p_full_point = np.zeros(54)

    temp = env[s_+11:s_+26]
    list_road = temp[temp != -1].astype(np.int32)
    p_road[list_road] = 1
    p_full_point[ROAD_POINT[list_road].flatten()] = 1

    p_point = p_full_point.copy()
    for i in range(1, 4):
        e_idx = (p_idx + i) % 4
        s_e = 58 + 42*e_idx
        temp = env[s_e+26:s_e+35]
        stm_and_city = temp[temp != -1].astype(np.int32)
        p_point[stm_and_city] = 0

    duongDaDi = np.zeros(72)
    max_len = 0
    list_full_point = np.where(p_full_point == 1)[0]
    for point in list_full_point:
        len_ = find_max_road(0, point, duongDaDi, p_road, p_point)
        if len_ > max_len:
            max_len = len_

    return max_len


@njit()
def roll_xx(env):
    p_idx = int(env[254])
    dice1 = np.random.randint(1, 7)
    dice2 = np.random.randint(1, 7)
    env[228] = dice1 + dice2  # C???p nh???t xx v??o env

    if env[228] == 7:  # Check xem ai ph???i b??? b??i
        # Gi??? s??? kh??ng ai b??? chia b??i, th?? s??? sang phase di chuy???n Robber
        env[229] = 4
        for i in range(0, 4):
            e_idx = (p_idx + i) % 4
            s_e = 58 + 42*e_idx
            if np.sum(env[s_e:s_e+5]) > 7:  # Th???a, sang pha b??? b??i
                env[229] = 3  # Sang pha b??? t??i nguy??n do b??? chia
                # C???p nh???t s??? l?????ng t??i nguy??n ph???i b???
                env[232] = np.sum(env[s_e:s_e+5]) // 2
                env[254] = e_idx  # ?????i ng?????i ch??i action
                break

    else:  # Tr??? t??i nguy??n t??? ng??n h??ng
        temp = np.where(env[20:39] == env[228])[0]
        list_tile = temp[temp != env[19]]
        p_res_receive = np.zeros((4, 5))
        for i in range(4):
            s_i = 58 + 42*i

            temp = env[s_i+26:s_i+31]
            p_stm = temp[temp != -1].astype(np.int32)

            temp = env[s_i+31:s_i+35]
            p_city = temp[temp != -1].astype(np.int32)

            for tile in list_tile:
                env_tile = int(env[tile])
                for stm in p_stm:
                    if stm in TILE_POINT[tile]:
                        p_res_receive[i][env_tile] += 1

                for city in p_city:
                    if city in TILE_POINT[tile]:
                        p_res_receive[i][env_tile] += 2

        total_res_receive = np.sum(p_res_receive, axis=0)

        # Ch??? tr??? nh???ng lo???i t??i nguy??n m?? ng??n h??ng c?? ?????
        temp = np.where(env[48:53] < total_res_receive)[0]
        p_res_receive[:, temp] = 0
        total_res_receive = np.sum(p_res_receive, axis=0)

        # Tr??? t??i nguy??n
        env[48:53] -= total_res_receive  # Tr??? t??i nguy??n ng??n h??ng
        for i in range(4):
            s_i = 58 + 42*i
            # C???ng t??i nguy??n cho ng?????i ch??i
            env[s_i:s_i+5] += p_res_receive[i]

        # Sang phase ch???n m?? ??un
        env[229] = 6


@njit()
def update_new_stm(env, new_stm_pos, s_):
    # C???p nh???t t???p nh??
    r_ = np.count_nonzero(env[s_+26:s_+31] != -1)
    env[s_+26+r_] = new_stm_pos

    # C???ng 1 ??i???m
    env[s_+10] += 1

    # Ki???m tra c???ng
    for port in range(9):
        if new_stm_pos in PORT_POINT[port]:
            if env[39+port] == 5:
                env[s_+37:s_+42] = np.minimum(3, env[s_+37:s_+42])
            else:
                env[int(s_+37+env[39+port])] = 2

            break


@njit()
def useDev(env, action, s_, p_idx):
    env[s_+action-50] -= 1  # Gi???m s??? l?? dev c???a ng?????i ch??i
    env[235:239] = 0  # M???i turn ch??? ???????c s??? d???ng 1 th??? dev
    if action == 55:  # Th??? knight
        env[233] = 0
        env[234] = 1
        env[229] = 4  # Chuy???n sang pha di chuy???n Robber
        env[s_+35] += 1

        list_p_usedKnight = env[np.array([93, 135, 177, 219])]
        largestArmy = np.max(list_p_usedKnight)

        # Check l???i danh hi???u
        if env[s_+35] >= 3 and env[s_+35] == largestArmy and env[226] != p_idx:
            # N???u cddn < 3 th?? ko c???n x??t do ko th??? gi??nh danh hi???u
            # N???u cddn != longestRoad th?? c??ng ko c???n x??t do c?? x??t c??ng ko ???????c danh hi???u
            # N???u ??ang c?? danh hi???u th?? vi???c x??y ???????ng gi??p c???ng c??? danh hi???u, n??n ko c???n x??t
            list_p_check = np.where(
                list_p_usedKnight == largestArmy)[0]
            if len(list_p_check) == 1:  # Ghi nh???n danh hi???u ho???c thay ?????i danh hi???u
                if env[226] == -1:  # Ch??a c?? danh hi???u
                    env[226] = p_idx  # Ghi nh???n danh hi???u
                    env[s_+10] += 2  # C???ng ??i???m
                else:  # Thay ?????i danh hi???u
                    # Tr??? ??i???m ng?????i c??
                    env[int(58+42*env[226]+10)] -= 2
                    env[226] = p_idx  # Ghi nh???n ng?????i m???i
                    env[s_+10] += 2  # C???ng ??i???m ng?????i c??
            # N???u c?? 2 ng?????i c??ng c?? con ???????ng d??i nh???t, kh??ng thay ?????i danh hi???u

    elif action == 56:  # Roadbuilding
        env[233] = 1
        env[234] = 2
        env[229] = 1  # Chuy???n v??? pha ?????t ???????ng

    elif action == 57:  # Yearofplenty
        env[233] = 2
        env[234] = 2
        env[229] = 7

    elif action == 58:  # Monopoly
        env[233] = 3
        env[234] = 1
        env[229] = 7


@njit()
def after_useDev(env):
    env[233] = -1
    env[234] = 0
    if env[228] == -1:  # Ch??a roll xx
        env[229] = 2
        roll_xx(env)
    else:  # ???? roll xx
        env[229] = 6


@njit()
def after_Rob(env):
    if env[233] == 0:  # ??ang d??ng th??? knight
        after_useDev(env)
    else:  # V???a ????? ra 7
        env[229] = 6


@njit()
def weighted_random(p):
    a = np.sum(p)
    b = np.random.uniform(0, a)
    for i in range(len(p)):
        b -= p[i]
        if b <= 0:
            return i


@njit()
def stepEnv(env, action):
    phase = env[229]
    p_idx = int(env[254])
    s_ = 58 + 42*p_idx

    if phase == 11:  # Y??u c???u t??i nguy??n khi trade v???i ng?????i
        check = False
        if action == 104:  # K???t th??c
            check = True
        else:  # Th??m t??i nguy??n
            env[186+action] += 1
            if np.sum(env[245:250]) == env[250]:  # L?????ng t??i nguy??n ?????t ?????n t???i ??a
                check = True

        if check:
            env[250] = 0
            for i in range(1, 5):
                e_idx = (p_idx + i) % 4
                s_e = 58 + 42*e_idx

                if i == 4:  # Quay v??? ng?????i ch??i ch??nh, kh??ng c?? ai trade,
                    env[229] = 6  # V??? lu??n phase ch???n m?? ??un
                    env[240:250] = 0  # Reset trade
                    env[251:254] = -1  # Reset ph???n h???i ng?????i ch??i ph???
                    break

                if (env[s_e:s_e+5] < env[245:250]).any():
                    env[250+i] = 0
                else:
                    env[229] = 12
                    env[254] = e_idx
                    break

        return

    if phase == 6:  # Ch???n c??c m?? ??un gi???a turn
        if action == 92:  # K???t th??c l?????t
            env[239] = 1  # Reset l???i s??? l???n t???o trade offer
            env[230] += 1  # T??ng turn
            n_idx = env[230] % 4
            s_n = int(58 + 42*n_idx)
            env[254] = n_idx  # Ng?????i ??i ti???p theo

            # Ki???m tra th??? dev c?? th??? s??? d???ng
            env[235:239] = env[s_n+5:s_n+9] > 0

            # T???ng xx
            env[228] = -1

            # Pha
            env[229] = 2

            if (env[235:239] == 0).all():
                roll_xx(env)

            return

        if action == 90:  # Trade v???i ng?????i
            env[239] -= 1  # Gi???m s??? l???n ???????c t???o trade offer v???i ng?????i ch??i
            env[229] = 10  # Sang pha ????a ra t??i nguy??n khi t???o trade

            # Ki???m tra l?????ng t??i nguy??n t???i ??a
            max_res = 0
            for i in range(1, 4):
                e_idx = (p_idx + i) % 4
                s_e = 58 + 42*e_idx
                a = np.sum(env[s_e:s_e+5])
                if a > max_res:
                    max_res = a

            env[250] = max_res  # L?????ng t??i nguy??n t???i ??a ???????c ????a v??o trong trade

            return

        if action == 91:  # Trade v???i bank
            env[229] = 14

            return

        if action == 86:  # Mua ???????ng
            env[s_:s_+5] -= ROAD_PRICE  # Tr??? t??i nguy??n
            env[48:53] += ROAD_PRICE
            env[229] = 1  # Chuy???n sang pha ?????t ???????ng

            return

        if action == 89:  # Mua th??? dev, kh??ng chuy???n pha
            env[s_:s_+5] -= DEV_CARD_PRICE  # Tr??? t??i nguy??n mua th??? dev
            env[48:53] += DEV_CARD_PRICE
            temp = env[53:58]

            dev_idx = weighted_random(temp)
            env[53+dev_idx] -= 1  # type: ignore # Tr??? th??? dev ??? ng??n h??ng
            env[s_+5+dev_idx] += 1  # type: ignore # C???ng th??? dev cho ng?????i ch??i

            # N???u th??? dev v???a nh???n l?? th??? vp (dev_idx = 4) th?? c???ng ??i???m cho ng?????i ch??i
            # if dev_idx == 4:
            #     env[s_+10] += 1
            # Note: Kh??ng ???????c c???ng do nh?? th??? c??c ng?????i kh??c s??? bi???t

            return

        if action >= 55 and action < 59:  # D??ng th??? dev
            useDev(env, action, s_, p_idx)

            return

        if action == 87:  # Mua nh??
            env[s_:s_+5] -= SETTLEMENT_PRICE
            env[48:53] += SETTLEMENT_PRICE
            env[229] = 8  # Sang pha mua nh??

            return

        if action == 88:  # Mua th??nh ph???
            env[s_:s_+5] -= CITY_PRICE
            env[48:53] += CITY_PRICE
            env[229] = 9  # Chuy???n sang pha mua th??nh ph???

            return

    if phase == 10:  # ????a ra t??i nguy??n khi trade v???i ng?????i
        if action == 103:  # K???t th??c
            env[229] = 11  # Chuy???n sang pha y??u c???u t??i nguy??n

        else:  # Th??m t??i nguy??n
            env[145+action] += 1
            if np.sum(env[240:245]) == np.sum(env[s_:s_+5]):  # ???? b??? h???t t??i nguy??n
                env[229] = 11

        return

    if phase == 3:  # Tr??? t??i nguy??n do b??? chia b??i
        env[s_+action-95] -= 1  # Tr??? t??i nguy??n c???a ng?????i ch??i
        env[action-47] += 1  # Tr??? t??i nguy??n n??y cho ng??n h??ng

        env[232] -= 1  # Gi???m s??? l?????ng th??? c???n tr???
        if env[232] == 0:  # ???? tr??? ?????
            for i in range(1, 5):
                e_idx = (p_idx + i) % 4
                s_e = 58 + 42*e_idx
                if e_idx == env[230] % 4:  # Quay v??? ng?????i ch??i ch??nh
                    env[229] = 4  # Sang pha di chuy???n Robber
                    env[254] = e_idx  # Chuy???n ng?????i action
                    break
                else:
                    if np.sum(env[s_e:s_e+5]) > 7:
                        # C???p nh???t s??? l?? ph???i b???
                        env[232] = np.sum(env[s_e:s_e+5]) // 2
                        env[254] = e_idx  # Chuy???n ng?????i action
                        break

        return

    if phase == 12:  # Ng?????i ch??i ph??? ph???n h???i trade
        r_ = int(p_idx - env[230]) % 4
        env[250+r_] = action - 93

        for i in range(1, 4):
            next_idx = (p_idx + i) % 4
            s_n = 58 + 42*next_idx
            env[254] = next_idx
            if next_idx == env[230] % 4:  # Chuy???n v??? ng?????i ch??i ch??nh
                if (env[251:254] == 0).all():  # Kh??ng ai trade
                    env[229] = 6  # V??? lu??n phase ch???n m?? ??un
                    env[240:250] = 0  # Reset trade
                    env[251:254] = -1  # Reset ph???n h???i ng?????i ch??i ph???
                else:
                    env[229] = 13

                break

            if (env[s_n:s_n+5] < env[245:250]).any():
                env[250+r_+i] = 0
            else:
                env[229] = 12
                break

        # if r_ == 3:  # Chuy???n v??? ng?????i ch??i ch??nh
        #     if (env[251:254] == 0).all():  # Kh??ng ai trade
        #         env[229] = 6  # V??? lu??n phase ch???n m?? ??un
        #         env[240:250] = 0  # Reset trade
        #         env[251:254] = -1  # Reset ph???n h???i ng?????i ch??i ph???
        #     else:
        #         env[229] = 13
        # Note: ??o???n n??y x??? l?? thi???u

        return

    if phase == 15:  # Ch???n t??i nguy??n mu???n nh???n t??? ng??n h??ng
        res_idx = action - 59

        # Ng?????i ch??i
        env[s_+res_idx] += 1
        env[s_:s_+5] -= env[240:245]

        # Ng??n h??ng
        env[48+res_idx] -= 1
        env[48:53] += env[240:245]

        env[240:245] = 0
        env[229] = 6

        return

    if phase == 14:  # Ch???n t??i nguy??n khi trade v???i ng??n h??ng
        res_idx = action - 95
        env[240+res_idx] = env[s_+37+res_idx]

        env[229] = 15

        return

    if phase == 1:  # Ch???n c??c ??i???m ?????u m??t c???a ???????ng
        if env[231] == -1:  # Ch??a c?? ??i???m ?????t th??? nh???t
            env[231] = action

            return

        # T??m con ???????ng t????ng ???ng v?? thay ?????i t???p ???????ng
        for road in np.where(ROAD_POINT == env[231])[0]:
            if action in ROAD_POINT[road]:
                i = np.count_nonzero(env[s_+11:s_+26] != -1)
                env[s_+11+i] = road
                break

        # Check con ???????ng d??i nh???t
        env[s_+36] = get_p_longest_road(env, p_idx)
        list_p_longestRoad = env[np.array([94, 136, 178, 220])]
        longestRoad = np.max(list_p_longestRoad)

        # Check l???i danh hi???u
        if env[s_+36] >= 5 and env[s_+36] == longestRoad and env[227] != p_idx:
            # N???u cddn < 5 th?? ko c???n x??t do ko th??? gi??nh danh hi???u
            # N???u cddn != longestRoad th?? c??ng ko c???n x??t do c?? x??t c??ng ko ???????c danh hi???u
            # N???u ??ang c?? danh hi???u th?? vi???c x??y ???????ng gi??p c???ng c??? danh hi???u, n??n ko c???n x??t
            list_p_check = np.where(list_p_longestRoad == longestRoad)[0]
            if len(list_p_check) == 1:  # Ghi nh???n danh hi???u ho???c thay ?????i danh hi???u
                if env[227] == -1:  # Ch??a c?? danh hi???u
                    env[227] = p_idx  # Ghi nh???n danh hi???u
                    env[s_+10] += 2  # C???ng ??i???m
                else:  # Thay ?????i danh hi???u
                    env[int(58+42*env[227]+10)] -= 2  # Tr??? ??i???m ng?????i c??
                    env[227] = p_idx  # Ghi nh???n ng?????i m???i
                    env[s_+10] += 2  # C???ng ??i???m ng?????i c??
            # N???u c?? 2 ng?????i c??ng c?? con ???????ng d??i nh???t, kh??ng thay ?????i danh hi???u

        # X??a ??i???m ?????t th??? nh???t
        env[231] = -1

        # 8 turn ?????u: K???t th??c turn, chuy???n ng?????i ch??i, n???u l?? turn 8 th?? ch??? chuy???n pha
        if env[230] <= 7:
            env[230] += 1
            if env[230] == 8:  # Ch??? chuy???n pha
                env[239] = 1  # C??i l???i s??? l???n t???o trade offer
                env[229] = 2  # Sang pha 2: ????? xx ho???c d??ng th??? dev
                roll_xx(env)  # Ch??a th??? c?? th??? dev trong tr?????ng h???p n??y
            else:  # Thay ?????i ng?????i ch??i, chuy???n pha
                env[229] = 0  # Chuy???n sang pha ?????t nh?? ?????u game
                if env[230] < 4:
                    env[254] = env[230]
                else:
                    env[254] = 7 - env[230]

        else:  # C??c turn gi???a game
            if env[223] != 1:  # Kh??ng d??ng th??? roadbuilding, v??? pha 6
                env[229] = 6

                return

            if env[233] == 1:  # ??ang d??ng th??? roadbuilding
                env[234] -= 1
                # Ho???c l?? h???t l?????t d??ng, ho???c ????? 15 ???????ng, ho???c h???t v??? tr?? x??y ???????ng
                check = True
                # if env[234] == 0 or (env[s_+11:s_+26] != -1).all():
                if env[234] == 0 or env[s_+25] != -1:
                    check = False

                if check:
                    check = False
                    p_point = np.zeros(54)
                    all_road = np.zeros(72)

                    # ???????ng v?? ??i???m c???a ng?????i ch??i
                    temp = env[s_+11:s_+26].astype(np.int32)
                    # list_road = temp[temp != -1].astype(np.int32)
                    # all_road[list_road] = 1
                    # p_point[ROAD_POINT[list_road].flatten()] = 1

                    for road in temp:
                        if road == -1:
                            break
                        else:
                            all_road[road] = 1
                            p_point[ROAD_POINT[road]] = 1

                    for i in range(1, 4):
                        e_idx = (p_idx + i) % 4
                        s_e = 58 + 42*e_idx

                        temp = env[s_e+11:s_e+26].astype(np.int32)
                        # list_road = temp[temp != -1].astype(np.int32)
                        # all_road[list_road] = 1
                        for road in temp:
                            if road == -1:
                                break
                            else:
                                all_road[road] = 1

                        temp = env[s_e+26:s_e+31].astype(np.int32)
                        # stm_and_city = temp[temp != -1].astype(np.int32)
                        # p_point[stm_and_city] = 0

                        for stm in temp:
                            if stm == -1:
                                break
                            else:
                                p_point[stm] = 0

                        temp = env[s_e+31:s_e+35].astype(np.int32)
                        for city in temp:
                            if city == -1:
                                break
                            else:
                                p_point[city] = 0

                    list_point = np.where(p_point == 1)[0]
                    for point in list_point:
                        # nearest_roads = POINT_ROAD[point][POINT_ROAD[point] != -1]
                        # if (all_road[nearest_roads] == 0).any():
                        #     check = True
                        #     break
                        for road in POINT_ROAD[point]:
                            if road != -1 and all_road[road] == 0:
                                check = True
                                break

                        if check:
                            break

                if not check:  # K???t th??c tr???ng th??i s??? d???ng th??? roadbuilding
                    after_useDev(env)

                return

        return

    if phase == 4:  # Di chuy???n Robber
        robber_pos = action - 64
        env[19] = robber_pos  # C???p nh???t v??? tr?? Robber

        # X??t xem c?? c?????p ???????c t??i nguy??n c???a ai hay ko
        check = False
        for i in range(4):
            if i != p_idx:
                s_i = 58 + 42*i
                if (env[s_i:s_i+5] > 0).any():  # N???u ng?????i n??y c?? t??i nguy??n
                    temp = env[s_i+26:s_i+35].astype(np.int32)
                    # stm_and_city = temp[temp != -1]
                    for point in temp:
                        if point != -1 and point in TILE_POINT[robber_pos]:
                            env[229] = 5
                            check = True
                            break

            if check:
                break

        if not check:  # Kh??ng c?????p ???????c c???a ai
            after_Rob(env)

        return

    if phase == 13:  # Ng?????i ch??i ch??nh duy???t trade
        if action == 105:  # B??? qua h???t
            env[229] = 6  # V??? lu??n phase ch???n m?? ??un
            env[240:250] = 0  # Reset trade
            env[251:254] = -1  # Reset ph???n h???i ng?????i ch??i ph???

            return

        e_idx = (p_idx + action - 99) % 4
        s_e = 58 + 42*e_idx

        # Ng?????i ch??i ch??nh
        env[s_:s_+5] -= env[240:245]
        env[s_:s_+5] += env[245:250]

        # Ng?????i ch??i ph???
        env[s_e:s_e+5] -= env[245:250]
        env[s_e:s_e+5] += env[240:245]

        env[229] = 6  # V??? pha ch???n m?? ??un
        env[240:250] = 0
        env[251:254] = -1  # Reset ph???n h???i ng?????i ch??i ph???

        return

    if phase == 5:  # Ch???n ng?????i ????? c?????p t??i nguy??n
        e_idx = (p_idx + action - 82) % 4
        s_e = 58 + 42*e_idx
        temp = env[s_e:s_e+5]  # T??i nguy??n

        res_idx = weighted_random(temp)
        env[s_e+res_idx] -= 1  # type: ignore # Tr??? t??i nguy??n c???a ng?????i b??? c?????p
        env[s_+res_idx] += 1  # type: ignore # C???ng t??i nguy??n cho ng?????i c?????p

        after_Rob(env)

        return

    if phase == 2:  # ????? xx ho???c d??ng th??? dev
        if action == 54:  # ????? x??c x???c
            roll_xx(env)

            return

        useDev(env, action, s_, p_idx)

        return

    if phase == 0:  # Ch???n ??i???m ?????t nh?? ?????u game
        update_new_stm(env, action, s_)

        # N???u l?? l???n 2 th?? c???ng t??i nguy??n
        if env[s_+10] == 2:
            temp = POINT_TILE[action][POINT_TILE[action] != -1]
            nearest_tiles = temp[env[temp] != 5]
            for tile in nearest_tiles:
                env_tile = int(env[tile])
                env[s_+env_tile] += 1  # C???ng t??i nguy??n cho ng?????i ch??i
                env[48+env_tile] -= 1  # Tr??? t??i nguy??n ??? ng??n h??ng

        # Chuy???n sang pha ?????t ???????ng
        env[231] = action  # ??i???m ?????t th??? nh???t
        env[229] = 1  # Chuy???n sang pha 1: ?????t ???????ng

        return

    if phase == 8:  # Ch???n c??c ??i???m mua nh??
        update_new_stm(env, action, s_)

        # Check xem nh?? v???a x??y c?? n???m tr??n con ???????ng c???a ai kh??c hay ko
        check = False
        w_idx = 9999

        for i in range(1, 4):
            e_idx = (p_idx + i) % 4
            s_e = 58 + 42*e_idx

            temp = env[s_e+11:s_e+26]
            list_road = temp[temp != -1].astype(np.int32)
            count = 0
            for road in POINT_ROAD[action]:
                if road != -1 and road in list_road:
                    count += 1

            if count == 2:
                check = True
                w_idx = e_idx
                break

        if check:  # Ng?????i n??y v???a x??y nh?? c???t ???????ng ng?????i kh??c
            s_w = 58 + 42*w_idx
            env[s_w+36] = get_p_longest_road(env, w_idx)
            list_p_longestRoad = env[np.array([94, 136, 178, 220])]
            longestRoad = np.max(list_p_longestRoad)

            if longestRoad < 5:
                if env[227] != -1:  # C?? ??ng c?? danh hi???u, ch???ng t??? v???a b??? c?????p
                    env[int(58+42*env[227]+10)] -= 2  # Tr??? ??i???m
                    env[227] = -1  # Thu h???i danh hi???u
                #  N???u ch??a ai c?? danh hi???u th?? b??? qua
            else:
                list_p_check = np.where(list_p_longestRoad == longestRoad)[0]
                if len(list_p_check) == 1:  # C?? ????ng 1 ??ng c?? con ???????ng d??i nh???t
                    if env[227] == -1:  # Ch??a c?? ai c?? danh hi???u
                        env[227] = list_p_check[0]  # B??n ch??i ghi nh???n
                        env[int(58+42*env[227]+10)] += 2  # C???ng ??i???m
                    else:  # C?? ??ng ???? c?? danh hi???u
                        if env[227] != list_p_check[0]:  # Thay ?????i danh hi???u
                            env[int(58+42*env[227]+10)] -= 2  # Tr??? ??i???m ??ng c??
                            env[227] = list_p_check[0]  # B??n ch??i ghi nh???n
                            # C???ng ??i???m ??ng m???i
                            env[int(58+42*env[227]+10)] += 2
                        #  N???u c??ng l?? m???t ng?????i th?? kh??ng thay ?????i danh hi???u
                else:  # C?? t??? 2 ??ng tr??? l??n c??ng c?? con ???????ng d??i nh???t
                    # ??ang c?? ng?????i c?? danh hi???u, nh??ng con ???????ng kh??ng d??i nh???t
                    if env[227] != -1 and env[227] not in list_p_check:
                        env[int(58+42*env[227]+10)] -= 2  # Tr??? ??i???m
                        env[227] = -1
                    # Ho???c l?? ch??a ai c?? danh hi???u, ho???c l?? danh hi???u n???m trong list th?? ko c???n check

        env[229] = 6  # V??? pha ch???n m?? ??un

        return

    if phase == 7:  # Ch???n t??i nguy??n khi d??ng th??? dev
        if env[233] == 2:  # ??ang d??ng th??? yearofplenty
            env[action-11] -= 1  # Tr??? t??i nguy??n cho ng??n h??ng
            env[s_+action-59] += 1  # C???ng t??i nguy??n cho ng?????i ch??i

            # Gi???m s??? l???n s??? d???ng th??? xu???ng
            env[234] -= 1

            # N???u h???t s??? l???n s??? d???ng ho???c ng??n h??ng h???t t??i nguy??n
            if env[234] == 0 or (env[48:53] == 0).all():
                after_useDev(env)

            return

        if env[233] == 3:  # ??ang d??ng th??? monopoly
            sum_res = 0
            res_idx = action - 59
            for i in range(1, 4):
                e_idx = (p_idx + i) % 4
                s_e = 58 + 42*e_idx
                sum_res += env[s_e+res_idx]
                env[s_e+res_idx] = 0

            env[s_+res_idx] += sum_res
            after_useDev(env)

            return

    if phase == 9:  # Ch???n c??c ??i???m mua th??nh ph???
        # C???p nh???t t???p nh??
        r_ = np.count_nonzero(env[s_+31:s_+35] != -1)
        env[s_+31+r_] = action

        # X??a nh?? v???a ???????c n??ng c???p l??n th??nh ph???
        temp = env[s_+26:s_+31]
        for i in range(5):
            if temp[i] == action:
                temp[i] = -1
                break

        temp = temp[temp != -1]
        env[s_+26:s_+31] = -1
        env[s_+26:s_+26+len(temp)] = temp

        # C???ng ??i???m
        env[s_+10] += 1

        env[229] = 6  # Sang pha ch???n m?? ??un

        return

    return


@njit()
def checkEnded(env):
    # Ng?????i ch??i ch??? c?? th??? chi???n th???ng khi t???i l?????t c???a m??nh
    # K??? c??? tr?????ng h???p: A c?? 9 ??i???m, B c?? con ???????ng d??i nh???t,
    # C c?? 9 ??i???m. C x??y nh?? ph?? ???????ng c???a B, A ???????c con ???????ng
    # d??i nh???t, c?? 11 ??i???m, C ch??? c?? 10 ??i???m nh??ng v???n chi???n th???ng
    # m???c cho A c?? nhi???u ??i???m h??n C
    ##
    main_p_idx = int(env[230]) % 4
    all_total_score = env[np.array([68, 110, 152, 194])] \
        + env[np.array([67, 109, 151, 193])]

    if all_total_score[main_p_idx] > 9:
        list_more_than_9 = np.where(all_total_score > 9)[0]
        max_score = np.max(all_total_score)

        # Ch??? c?? th??? c?? t???i ??a 2 ng?????i ch??i tr??n 9 ??i???m c??ng l??c
        # N???u c?? 2 ng?????i ch??i tr??n 9 ??i???m th?? kh??ng th??? c?? ng?????i ch??i c?? 12 ??i???m
        if len(list_more_than_9) == 2:
            # 2 ng?????i ch??i c?? c??ng s??? ??i???m cao nh???t
            if (all_total_score[list_more_than_9] == max_score).all():
                return main_p_idx + 100

            # Ng?????i ch??i chi???n th???ng c?? ??i???m cao nh???t
            if all_total_score[main_p_idx] == max_score:
                return main_p_idx + 200

            # Ng?????i ch??i chi???n th???ng kh??ng c?? ??i???m cao nh???t
            return main_p_idx + 300

        # ?????n ????y th?? t???c l?? ng?????i ch??i ch??nh c?? ??i???m cao nh???t
        if all_total_score[main_p_idx] == 12:
            return main_p_idx + 400

        # Ch??? ????n gi???n l?? chi???n th???ng v???i 10 ho???c 11 ??i???m, kh??ng c?? g?? ?????c bi???t
        return main_p_idx

    return -1


@njit()
def getReward(state):
    main_p_idx_ = np.where(state[1044:1047] == 1)[0]
    if main_p_idx_.shape[0] == 0:
        main_p_idx = 0
    elif main_p_idx_.shape[0] == 1:
        main_p_idx = main_p_idx_[0] + 1
    else:
        main_p_idx = -1

    if main_p_idx == 0:  # ?????n l?????t c???a b???n th??n
        # Th???ng ho???c ch??a k???t th??c game
        if state[203] > 9: # H??n 9 ??i???m => auto th???ng
            return 1

        if state[1047] == 1: # ???? h???t game
            return 0

        return -1

    # Kh??ng ph???i l?????t c???a b???n th??n
    # Thua ho???c ch??a k???t th??c game
    # Ng?????i ch??i ch??nh c?? h??n 9 ??i???m => thua
    if state[208+185*main_p_idx] > 9:
        return 0

    if state[1047] == 1: # ???? h???t game
        return 0

    # Ng?????i ch??i ch??nh ch??a c?? tr??n 9 ??i???m, ch??a k???t th??c game
    return -1


@njit()
def getStateSize():
    return __STATE_SIZE__


@njit()
def getActionSize():
    return __ACTION_SIZE__


@njit()
def getAgentSize():
    return 4


def one_game_normal(p0, list_other, per_player, per1, per2, per3, p1, p2, p3):
    env = initEnv()

    winner = -1
    while env[230] < __MAX_TURN_IN_ONE_GAME__:
        p_idx = int(env[254])
        state = getAgentState(env)
        if list_other[p_idx] == -1:
            action, per_player = p0(state, per_player)
            validActions = getValidActions(state)
            if validActions[action] != 1:
                raise Exception("Action kh??ng h???p l???")
        elif list_other[p_idx] == 1:
            action, per1 = p1(state, per1)
        elif list_other[p_idx] == 2:
            action, per2 = p2(state, per2)
        else:
            action, per3 = p3(state, per3)

        stepEnv(env, action)
        winner = checkEnded(env)
        if winner != -1:
            break

    env[255] = 1
    env[np.array([68, 110, 152, 194])] += env[np.array([67, 109, 151, 193])]

    env[229] = 2
    p0_idx = np.where(list_other==-1)[0][0]
    for p_idx in range(4):
        env[254] = p_idx
        state = getAgentState(env)
        if list_other[p_idx] == -1:
            action, per_player = p0(state, per_player)
        elif list_other[p_idx] == 1:
            action, per1 = p1(state, per1)
        elif list_other[p_idx] == 2:
            action, per2 = p2(state, per2)
        else:
            action, per3 = p3(state, per3)

    if p0_idx == winner: result = 1
    else: result = 0
    return result, per_player


@njit()
def one_game_numba(p0, list_other, per_player, per1, per2, per3, p1, p2, p3):
    env = initEnv()

    winner = -1
    while env[230] < __MAX_TURN_IN_ONE_GAME__:
        p_idx = int(env[254])
        state = getAgentState(env)
        if list_other[p_idx] == -1:
            action, per_player = p0(state, per_player)
            validActions = getValidActions(state)
            if validActions[action] != 1:
                raise Exception("Action kh??ng h???p l???")
        elif list_other[p_idx] == 1:
            action, per1 = p1(state, per1)
        elif list_other[p_idx] == 2:
            action, per2 = p2(state, per2)
        else:
            action, per3 = p3(state, per3)

        stepEnv(env, action)
        winner = checkEnded(env)
        if winner != -1:
            break

    env[255] = 1
    env[np.array([68, 110, 152, 194])] += env[np.array([67, 109, 151, 193])]

    env[229] = 2
    p0_idx = np.where(list_other==-1)[0][0]
    for p_idx in range(4):
        env[254] = p_idx
        state = getAgentState(env)
        if list_other[p_idx] == -1:
            action, per_player = p0(state, per_player)
        elif list_other[p_idx] == 1:
            action, per1 = p1(state, per1)
        elif list_other[p_idx] == 2:
            action, per2 = p2(state, per2)
        else:
            action, per3 = p3(state, per3)

    if p0_idx == winner: result = 1
    else: result = 0
    return result, per_player


def n_games_normal(p0, num_game, per_player, list_other, per1, per2, per3, p1, p2, p3):
    win = 0
    for _ in range(num_game):
        np.random.shuffle(list_other)
        winner, per_player = one_game_normal(p0, list_other, per_player, per1, per2, per3, p1, p2, p3)
        win += winner

    return win, per_player


@njit()
def n_games_numba(p0, num_game, per_player, list_other, per1, per2, per3, p1, p2, p3):
    win = 0
    for _ in range(num_game):
        np.random.shuffle(list_other)
        winner, per_player = one_game_numba(p0, list_other, per_player, per1, per2, per3, p1, p2, p3)
        win += winner

    return win, per_player


@njit()
def bot_lv0(state, perData):
    validActions = getValidActions(state)
    arr_action = np.where(validActions==1)[0]
    idx = np.random.randint(0, arr_action.shape[0])
    return arr_action[idx], perData


import importlib.util, json, sys
try:
    from setup import SHOT_PATH
except:
    pass


def load_module_player(player):
    spec = importlib.util.spec_from_file_location('Agent_player', f"{SHOT_PATH}Agent/{player}/Agent_player.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@njit()
def check_run_under_njit(Agent):
    return True


def numba_main_2(p0, num_game, per_player, level, *args):
    list_other = np.array([1, 2, 3, -1], dtype=np.int64)
    try: check_njit = check_run_under_njit(p0)
    except: check_njit = False

    if level == 0:
        per_agent_env = np.array([0], dtype=np.int64)
        if check_njit:
            return n_games_numba(p0, num_game, per_player, list_other, per_agent_env, per_agent_env, per_agent_env, bot_lv0, bot_lv0, bot_lv0)
        else:
            return n_games_normal(p0, num_game, per_player, list_other, per_agent_env, per_agent_env, per_agent_env, bot_lv0, bot_lv0, bot_lv0)

    env_name = sys.argv[1]
    if len(args) > 0:
        dict_level = json.load(open(f'{SHOT_PATH}Log/check_system_about_level.json'))
    else:
        dict_level = json.load(open(f'{SHOT_PATH}Log/level_game.json'))

    if str(level) not in dict_level[env_name]:
        raise Exception('Hi???n t???i kh??ng c?? level n??y')

    lst_agent_level = dict_level[env_name][str(level)][2]

    p1 = load_module_player(lst_agent_level[0])
    p2 = load_module_player(lst_agent_level[1])
    p3 = load_module_player(lst_agent_level[2])
    per_level = []
    for i in range(3):
        data_agent_env = np.load(f'{SHOT_PATH}Agent/{lst_agent_level[i]}/Data/{env_name}_{level}/Train.npy',allow_pickle=True)
        if i == 0:
            per_level.append(p1.convert_to_run(data_agent_env))
        elif i == 1:
            per_level.append(p2.convert_to_run(data_agent_env))
        else:
            per_level.append(p3.convert_to_run(data_agent_env))

    if check_njit:
        return n_games_numba(p0, num_game, per_player, list_other, per_level[0], per_level[1], per_level[2], p1.Test, p2.Test, p3.Test)
    else:
        return n_games_normal(p0, num_game, per_player, list_other, per_level[0], per_level[1], per_level[2], p1.Test, p2.Test, p3.Test)