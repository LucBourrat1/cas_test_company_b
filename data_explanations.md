# Explanation of the data
The folder contains four comma-delimited .csv datasets of different sizes.

Some columns can be found in several datasets:
- start_ts_utc: Start of the timestep, in UTC,
- end_ts_utc: End of the timestep, in UTC,
- start_ts: Start of the timestep, local time (CET/CEST),
- end_ts: End of the timstep, local time (CET/CEST).

More detailed descriptions for individual datasets:
- Power_Forecasts_Case.csv:
  - comp_ts_utc: Computation timestamp (datetime of the forecasts computation), in UTC,
  - utility: Trigram of the utility for which the forecast is made,
  - power: Power forecasts, in kW.

DA_Prices_Case.csv:
  - price: Day-Ahead price, in €/MWh.

Imbalances_Prices_Case.csv:
  - pos_imb_settlement_price: Positive imbalance settlement price, the price at which some surplus are bought by the Transport System Operator (RTE), when sales are higher than injections / production (€/MWh).
  - neg_imb_settlement_price : Negative imbalance settement price, the price at which Boralex has to bought back the electricity that has been oversold (€/MWh).

Power_case.csv:
  - utility: Trigram of the utility for which the power is metered,
  - power: Power production, in kW.