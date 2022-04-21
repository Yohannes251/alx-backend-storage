-- lists all bands with Glam as their main style
-- ranked by their longevity
-- Column names: band_name and lifespan (in years)
-- attributes formed and split for computing the lifespan
SELECT DISTINCT `band_name`,
                IFNULL(`split`, 2020) - `formed` as `lifespan`
    FROM `metal_bands` WHERE FIND_IN_SET('Glam rock', style)
    ORDER BY `lifespan` DESC;