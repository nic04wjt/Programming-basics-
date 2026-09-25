import helper

def main():
    # 1. Load the data using Pandas
    df = helper.load_csv("data.csv")
    
    # 2. Clean data and run math operations using Numpy
    y_data = helper.process_data(df, "Prices")
    
    # 3. Plot the final chart using Matplotlib
    helper.plot_data(df, "Dates", y_data)

if __name__ == "__main__":
    main()
