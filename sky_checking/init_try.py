from rubin_scheduler.utils.consdb import ConsDBVisits, load_consdb_visits, query_consdb
from rubin_scheduler.scheduler.utils import SchemaConverter
import pandas as pd
from lsst.summit.utils import ConsDbClient 


if __name__ == "__main__":
    with open(".lsst/consdb_token", "r") as f:
        token = f.read()
    consdb = ConsDbClient(f"https://user:{token}@usdf-rsp.slac.stanford.edu/consdb")

    instrument = "lsstcomcam"
    query = f"SELECT column_name FROM information_schema.columns where table_schema = 'cdb_{instrument}'"
    query_results: pd.DataFrame = consdb.query(query).to_pandas()

    token = token.strip()
    day_obs: str = "2024-06-26"
    #url = f"https://user:{token}@usdf-rsp.slac.stanford.edu/consdb"
    consdb_visits: ConsDBVisits = load_consdb_visits("lsstcomcamsim", day_obs, url=url)
    schema_converter: SchemaConverter = SchemaConverter()

    opsim: pd.DataFrame = consdb_visits.opsim


    # how to grab the schemas
    que = ("SELECT table_schema,table_name " 
    "FROM information_schema.tables " 
    "ORDER BY table_schema,table_name;")

    ack = query_consdb(que)
    