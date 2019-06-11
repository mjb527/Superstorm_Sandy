import csv
import plotly.plotly as plt
import plotly.graph_objs as go

def getAllHomes():
    homes_list = []
    with open(home_file, 'r') as homes:
        reader = csv.reader(homes, delimiter(', '))
        for row in reader:
            homes_list.append(row)
    return homes_list

def getAllBusinesses():
    buss_list = []
    with open('SSS_business.csv', 'r') as buss:
        reader = csv.reader(buss, delimiter(', '))
        for row in reader:
            buss_list.append(row)
    return buss_list

# create a pie chart for the states that appear, or counties if county==True
def labels(SSS_file, county, state=None):
    # labels contains the state : number_of_incidents of Super Storm Sandy, or the county if county==True and a state is provided
    labels = {}
    label_list = []
    with open(SSS_file, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        if county:
            # populate the labels for the county in the state specified, else set count to +1
            for row in reader:
                # print(row[6])
                # print(state == row[7] and row[6] not in label_list)
                if row[6] in label_list:
                    labels[row[6]] += 1
                if state == row[7] and row[6] not in label_list:
                    labels[row[6]] = 1
                    label_list.append(row[6])
                
        else:
            # populate the labels with all states that appear if new, else set count to +1
            for row in reader:
                # print(row)
                if row[7] not in label_list:
                    labels[row[7]] = 1
                    label_list.append(row[7])
                else:
                    labels[row[7]] += 1
    return labels

# return a dictionary with the population of states by abbreviation
def getPop(states):
    filename = 'census.csv'
    # print(states)
    pop = {}
    with open(filename, 'r') as censusdata:
        reader = csv.reader(censusdata, delimiter=',')
        next(reader)
        # if the row appears in the `states` list, return population in 2012
        for row in reader:
            if row[1] in states:
                pop[row[1]] = row[2]
    return pop

# create a pie chart based on the params collected from labels_sizes()
def createPie(lasz, filename='piechart'):
    trace = go.Pie(labels=list(lasz.keys()),
                   values=list(lasz.values()),
                   textinfo='label+percent+value',
                   hoverinfo='none')
    plt.iplot([trace], filename=filename)

# create a bar graph comparing the number of claims per capita in each state (people/claim)
def createRelBarChart(labels, filename):
    pops = getPop(list(labels.keys()))
    rel_data = {}
    for k in labels.keys():
        rel_data[k] = float(pops[k])/float(labels[k])
    X = list(labels.keys())
    Y = list(labels.values())
    print(X)
    trace = go.Bar(
        x=X,
        y=Y
        )
    plt.iplot(trace,filename=filename)
    
if __name__ == '__main__':
    pass
