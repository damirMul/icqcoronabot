from gateway.worldometer_gateway import WorldOMeterGateway
from services.parser_service import ParserService
import schedule
import time
def zxc():
    if __name__ == "__main__":

        worldometer_gateway = WorldOMeterGateway()
        parser_service = ParserService()

        latest_data = worldometer_gateway.fetch()
        output = parser_service.create_df_worldometer(latest_data)
        last_updated = parser_service.parse_last_updated(latest_data)
        output.to_csv(r'./cases.csv', index=None)
        output.set_index("Country/Other").to_json(r"./cases.json", orient="index")
        print(last_updated)
        print(output)
schedule.every(10).minutes.do(zxc)
while True:
    schedule.run_pending()
    time.sleep(1)
