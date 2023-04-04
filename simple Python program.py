# name = input("Who's there? ")
# msg = "Sorry " + name + ". I thought you were someone else!"
# print(msg)

# Downloads Qantas share price beginning 1 January 2020
import yfinance                                           # (1)
tic = "QAN.AX"                                            # (2)
start = '2020-01-01'                                      # (3)
end = None                                                # (4)
df = yfinance.download(tic, start, end, ignore_tz=True)   # (5)
print(df)                                                 # (6)
df.to_csv('qan_stk_prc.csv')


# happy = 5
# if happy:
#     print("I am happy")

# happy = 0
# if happy:
#     print("I am happy")

# for v in ("string", True, 1):
#     print(v)

# tickers = set()
# tickers.add("QAN.AX")
# tickers.add("QAN.AX")
# tickers.add("WES.AX")
#
# for tic in tickers:
#     print(tic)

# d = {
#     "beauty": True,
#     "truth": True,
#     "red wheelbarrow": 100000,
#     5: "fingers",
#     }
# for key in d:
#     print(key)
