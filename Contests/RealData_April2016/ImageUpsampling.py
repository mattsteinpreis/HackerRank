def get_loc(shape, coef):
    r = shape[0]
    c = shape[1]
    ds_locs = []
    us_locs = []
    for i in range(r):
        for j in range(c):
            if i % coef == 0 and j % coef == 0:
                ds_locs.append((i, j))
            else:
                us_locs.append((i, j))
    return ds_locs, us_locs


def get_pixels_ds(ds, pxls):
    comb = {}
    for loc, pxl in zip(ds, pxls):
        comb[loc] = pxl
    return comb


def bilinear_interpolation(pixels_ds, coef, shape_ds, shape_us):
    # interpolate rows (only rows with values from pixels_ds)
    pixels_us = {}
    for i in range(0, shape_us[0], coef):
        for j in range(shape_us[1]):
            if i % coef == 0 and j % coef == 0:
                pixels_us[(i, j)] = pixels_ds[(i, j)]
                continue
            if j < (shape_ds[1] - 1) * coef:
                l_loc = (i, j - (j % coef))
                r_loc = (i, j + (coef - (j % coef)))
            else:
                r_loc = (i, j - (j % coef))
                l_loc = (i, j - (j % coef) - coef)
            fx_1 = pixels_ds[(l_loc[0], l_loc[1])]
            fx_2 = pixels_ds[(r_loc[0], r_loc[1])]
            new_pxl = []
            for ii in range(3):
                val1 = fx_1[ii] * (r_loc[1] - j) / coef
                val2 = fx_2[ii] * (j - l_loc[1]) / coef
                val = int(max(min(val1 + val2, 255), 0))
                new_pxl.append(val)
            pixels_us[(i, j)] = tuple(new_pxl)

    # interpolate columns (skip already filled rows)
    # pull values from pixels_us
    for j in range(shape_us[1]):
        for i in range(0, shape_us[0]):
            if i % coef == 0:
                continue
            if i < (shape_ds[0] - 1) * coef:
                l_loc = (i - (i % coef), j)
                r_loc = (i + (coef - (i % coef)), j)
            else:
                r_loc = (i - (i % coef), j)
                l_loc = (i - (i % coef) - coef, j)
            fx_1 = pixels_us[(l_loc[0], l_loc[1])]
            fx_2 = pixels_us[(r_loc[0], r_loc[1])]
            new_pxl = []
            for ii in range(3):
                val1 = fx_1[ii] * (r_loc[0] - i) / coef
                val2 = fx_2[ii] * (i - l_loc[0]) / coef
                val = int(max(min(val1 + val2, 255), 0))
                new_pxl.append(val)
            pixels_us[(i, j)] = tuple(new_pxl)
    return pixels_us


def print_rows(p, shape):
    r = shape[0]
    c = shape[1]
    for i in range(r):
        row_list = []
        for j in range(c):
            tup_str = ','.join([str(n) for n in p[(i, j)]])
            row_list.append(tup_str)
        print(' '.join(row_list))


def parse_input_pixels(nrows):
    pixels = []
    for i in range(nrows):
        pixel_strings = input().split()
        for ps in pixel_strings:
            pl = [int(s) for s in ps.split(sep=',')]
            pixels.append(tuple(pl))
    return pixels


def test():
    shape_ds = (3, 3)
    sample_coef = 2
    shape_us = (6, 6)
    locations_ds, locations_us = get_loc(shape_us, sample_coef)

    rgb_ds = [(0, 0, 200), (0, 0, 10), (10, 0, 0),
              (90, 90, 50), (90, 90, 10), (255, 255, 255),
              (100, 100, 88), (80, 80, 80), (15, 75, 255)]
    pixels_ds = get_pixels_ds(locations_ds, rgb_ds)
    pixels_us = bilinear_interpolation(pixels_ds, sample_coef, shape_ds, shape_us)
    print_rows(pixels_us, shape_us)


def hacker_rank():
    ui = [int(ch) for ch in input().split()]
    shape_ds = (ui[0], ui[1])
    coefficient = ui[2]
    ui = [int(ch) for ch in input().split()]
    shape_us = (ui[0], ui[1])
    locations_ds, locations_us = get_loc(shape_us, coefficient)
    rgb_ds = parse_input_pixels(shape_ds[0])
    pixels_ds = get_pixels_ds(locations_ds, rgb_ds)
    pixels_us = bilinear_interpolation(pixels_ds, coefficient, shape_ds, shape_us)
    print_rows(pixels_us, shape_us)

if __name__ == "__main__":
    test()


