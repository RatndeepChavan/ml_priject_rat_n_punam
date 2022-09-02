from django.shortcuts import render
import pickle

# Create your views here.
# with open('a1/static/model.iris', 'rb') as f: mm = pickle.load(f)
# print(mm.predict([[5.1, 3.5, 1.4, 0.2], [4.9, 3, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2]]))


def hm(request):
    if request.method == 'POST':
        with open('a1/static/model.iris', 'rb') as f: mm = pickle.load(f)
        dt = []
        dt.append(request.POST['i1'])
        dt.append(request.POST['i2'])
        dt.append(request.POST['i3'])
        dt.append(request.POST['i4'])
        dt = [list(map(float, dt))]
        pd = mm.predict(dt)
        # if pd == 0 : op = 'Iris Setosa'
        # elif pd == 1 : op = 'Iris Versicolour'
        # elif pd == 2 : op = 'Iris Virginica'
        return render(request, 'hm.html', {'pd':pd})
    return render(request, 'hm.html')