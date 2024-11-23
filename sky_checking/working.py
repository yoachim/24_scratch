from rubin_scheduler.utils.consdb import load_consdb_visits, query_consdb
import pandas as pd


if __name__ == "__main__":
    day_obs = "2024-06-26"
    consdb_visits = load_consdb_visits("lsstcomcamsim", day_obs)

    # now can access various things
    sky = consdb_visits.sky_e_per_pixel

    cols_wanted = ["band", "ra", "decl", "obs_start_mjd",
                   "sky_e_per_pixel", "sky_mag_per_asec", "shut_time"]

    df = pd.DataFrame()
    for col in cols_wanted: 
        df[col] = getattr(consdb_visits, col)

