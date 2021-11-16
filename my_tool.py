
def clear_screen(x):
    print("\n" * x)
    print('screen cleared')

def file_read_app(file):
    f = open(file) 
    next(f)
    data_t = []
    # for line in f.readlines():
    for line in f: 
        data_t.append("19" + line)
    f.close()
    return data_t

def file_r(file):
    f = open(file) 
    next(f)
    data_t = []
    for line in f: 
        data_t.append(line)
    f.close()
    return data_t

def date_format(data_t):
    time = []
    date = []
    for line in data_t:
         time.append(line.split(",")[0])
    for t in time:
        t_fm = t[:4] + '-' + t[4:6] + '-' + t[6:]
        date.append(t_fm)
    return date

def close(data_t):
    value = []
    for line in data_t:
         value.append(float(line.split(",")[1][:-1]))
    close = value
    return close




# this part is for calculating the mean
def mean(close):
    sum = 0.0
    n = 0
    mean = []
    while n <= len(close):
        if n == 0:
            mean.append(0)
            sum = sum + close[n]
            n = n + 2
        elif n <= len(close):
            sum = sum + close[n-1]
            mean.append(sum / n)
            n = n + 1
    return mean
    
    
# this part is for calculating the median
def median(close):
    m = 0
    median = []      
    while m <= len(close):
        if m == 0:
            median.append(0)
            m = m + 2
        elif m <= len(close) and m % 2 == 0:
            # print(m//2)
            new_median = (close[m // 2] + close[m // 2 -1])/2
            median.append(new_median)
            m = m + 1
        elif m <= len(close) and m % 2 != 0:
            median.append(close[m // 2])
            m = m + 1
    return median

# this part is for calculating the up and down
def up_down(close):
    l = 0
    updown = []
    while l <= len(close):
        if l == 0:
            updown.append(0)
            l = l + 2
        else:
            updown.append(close[l-1]-close[l-2])
            l = l + 1
    return updown
# this part is for calculating the gain and loss
def gain_loss(close):
    q = 0
    gainloss = []
    while q <= len(close):
        if q == 0:
            gainloss.append(0)
            q = q + 2
        else:
            gainloss.append((close[q-1]-close[q-2])/close[q-2])
            q = q + 1  
    return gainloss
    
def write(date, close, mean, median, updown, gainloss, output_file):               
    date.insert(0, "Date")
    close.insert(0, "Close")
    mean.insert(0, "Mean")
    median.insert(0, "Median")
    updown.insert(0, "Up/Down")
    gainloss.insert(0, "Gain%/Loss%")
    write = open(output_file, 'w')
    for i in range(len(close)):
        line = str(date[i]) + ',' + str(close[i]) + ',' + str(mean[i]) + ',' + str(median[i]) + ',' + str(updown[i]) + ',' + str(gainloss[i]) 
        write.writelines(line + '\n')
    write.close()   


def doublecheck(file):
    doublecheck = open(file, 'r')
    for i in doublecheck.readlines():
        print(i)
    doublecheck.close()
    

def date_rev(data_t):
    t = []
    date = []
    for line in data_t:
         # print(line.split(",")[0])
         t.append(line.split(",")[0])   
         time = t[::-1]
    import datetime as dt
    for i in time:
         date.append(dt.datetime.strptime(i,'%m/%d/%Y').strftime('%Y-%m-%d'))
    return date

def close_rev(data_t):        
    c = []
    for line in data_t:
         c.append(float(line.split(",")[4]))
         close = c[::-1]
    return close

def plot(date,close,mean,median,updown,gainloss):
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    # ticker_spacing = date
    # ticker_spacing = 200
    plt.title('Close price, Mean, Median, Up&down and Gain&loss')
    plt.plot(date[:101], close[:101], color = 'green', label = 'Close price')
    plt.plot(date[:101], mean[:101], color = 'grey', label = 'Mean')
    plt.plot(date[:101], median[:101], color = 'blue', label = 'Median')
    plt.plot(date[:101], updown[:101], color = 'yellow', label = 'Up and down')
    plt.plot(date[:101], gainloss[:101], color = 'red', label = 'Gain and loss')
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.show()

def main():
    file_read_app()
if __name__ == '__main__':
    main()
        
        
        
        
        
        
        
        