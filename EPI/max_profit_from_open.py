"""
First create a list of stock prices using random.triangular. It will generate
floats between 30 and 45 with a mode of 37. Good for stock price lists.
    - Challenge question: What is the max profit that could have been made by
        buying and then selling a single share over a given day range.
    - Constraint: Buying and selling have to take place at the beginning of the
        day and you have to sell when the price is higher than the current hold
This solution iterates through the entire price list once == O(n) complexity
"""
import random


class ProfitFromOpen:
    def __init__(self):
        self.price_open = 0
        self.profit_list = []
        self.profit = 0

    def main(self):
        self.generate_stock_prices()
        self.calculate_max_profit()
        print('The max profit is : {0}'.format(self.profit))
        # for item in self.profit_list:
        #     print(item)

    def generate_stock_prices(self):
        """
        Generate floats between 30 and 45 with a mode of 37
        """
        i = 0
        price_list = []
        while i < 1000:
            # price_list.append(random.randrange(30., 45.))
            price_list.append(random.triangular(30, 45, 37))
            i += 1
        return price_list

    def calculate_max_profit(self):
        """
        Establish the price list. Buy on the first day. for each item in the
        price list, if the price is greater than the current price that you own,
        you made a profit. Sell, append that profit to the list, and then buy
        back in on the next day's open if there is a next day in the list.
        Finally, if your new profit is greater than any other profit, that's the
        new max profit. Max profit is what we were seeking, so you're done.
        """
        price_list = self.generate_stock_prices()
        current_price = price_list[0]
        for i in range(len(price_list)):
            if price_list[i] > current_price:
                # sale
                new_profit = price_list[i] - current_price
                self.profit_list.append(new_profit)
                if i+1 < len(price_list):
                    # buy back in at the next open
                    current_price = price_list[i + 1]
                if new_profit > self.profit:
                    # if this profit is greater than the last max profit, replace it
                    self.profit = new_profit
        if self.profit == 0:
            print('You bought at the peak, sorry. No profit to be had')


if __name__ == '__main__':
    profit_max = ProfitFromOpen()
    profit_max.main()
