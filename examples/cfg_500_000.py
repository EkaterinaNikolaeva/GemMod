import cat_simulation.constants as const

# ----- GENERAL ----- #
PLATE_WIDTH, PLATE_HEIGHT = 1500, 1000
PLATE_H_MIN, PLATE_W_MIN = 0, 0
CATS_N = 500000

# ----- CAT ----- #
CAT_RADIUS = 0.001 * PLATE_HEIGHT
MOVE_RADIUS = CAT_RADIUS * 2
RADIUS_0 = CAT_RADIUS * 2
RADIUS_1 = RADIUS_0 * 3

# ----- PATTERNS ----- #
MOVE_PATTERN_ID = const.MOVE_PATTERN_PHIS_ID
DISTANCE = const.EUCLIDEAN_DISTANCE

# ----- VISUALISATION ----- #
COLOR_LEVEL_0 = const.RED_COLOR
COLOR_LEVEL_1 = const.YELLOW_COLOR
COLOR_LEVEL_NO = const.GREEN_COLOR

# ----- PROBABILISTIC INTERACTION ----- #
PROB_INTERACTION = const.DISABLE_PROB_INTER
