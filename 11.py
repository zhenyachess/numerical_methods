from numpy import array, zeros, math

def f_dif(x, y):
	return -x*y
	#return (1+x)*math.e**(x*(1-x)) + 2*(2-x)*y

#границы отрезка
a=1
b=6

# начальное условие y(x_0)=y_0
y__0=1

# величина шага
h=0.05

# определяем необходимое количество строк в таблице
cnt_temp=round((b-a)/h + 1)

# создали таблицы с нулями, но нулевая строка определена числами
x = zeros(cnt_temp, float)
y_3 = zeros(cnt_temp, float) # для 3-го порядка точности
y_4 = zeros(cnt_temp, float) # для 4-го порядка точности
x[0]=0
y_3[0]=y_4[0]=1

# определили таблицу x
for i in range(1, cnt_temp, +1):
	x[i]=x[i-1]+h
	# вычисление для 3-го порядка точности
	k_1_3=h*f_dif(x[i] , y_3[i-1])
	k_2_3=h*f_dif(x[i] + h/3   , y_3[i-1] + k_1_3/3)
	k_3_3=h*f_dif(x[i] + 2*h/3 , y_3[i-1] + 2*k_2_3/3)
	delta_y_3=(k_1_3 + 3*k_3_3)/4
	y_3[i]=y_3[i-1] + delta_y_3
	# вычисление для 4-го порядка точности
	k_1_4=h*f_dif(x[i] , y_4[i-1])
	k_2_4=h*f_dif(x[i] + h/4 , y_4[i-1] + k_1_4/4)
	k_3_4=h*f_dif(x[i] + h/2 , y_4[i-1] + k_2_4/2)
	k_4_4=h*f_dif(x[i] + h   , y_4[i-1] + k_1_4 - 2*k_2_4 + 2*k_3_4)
	delta_y_4=(k_1_4 + 4*k_3_4 + k_4_4)/6
	y_4[i]=y_4[i-1] + delta_y_4

print(x)
print(y_3)
print(y_4)
