"""
수직선 위에 로봇이 하나 놓여 있다. 현재 로봇의 좌표는 0이다.
로봇은 아래 두 종류의 명령어만 이해할 수 있다.
-    L: 왼쪽으로 한 칸 이동한다. 로봇의 좌표가 1 감소하게 된다.
-    R: 오른쪽으로 한 칸 이동한다. 로봇의 좌표가 1 증가하게 된다.
로봇에게 입력할 명령어를 나타내는 문자열 S가 주어진다.
다만, 문자열 중 일부는 물음표(‘?’)로 채워져 있는데, 이 부분은 당신이 L 또는 R로 대체해야 한다.
물음표를 모두 대체한 이후, 당신은 로봇에 명령어를 순서대로 입력하면서, 로봇이 원점으로부터 얼마나 멀리 떨어졌는지를 기록할 것이다.
당신은 물음표를 적절히 대체하여 로봇과 원점 사이의 최대 거리를 최대화하고자 한다.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스는 한 개의 줄로 이루어진다.
각 줄에는 길이가 1 이상 50 이하인, L,R,?로만 구성된 문자열 S가 주어진다.

[출력]
각 테스트 케이스마다, 문자열 S의 물음표를 L 또는 R로 적절히 대체하여 로봇과 원점 사이의 최대 거리를 최대화했을 때, 이 최대 거리를 한 줄에 하나씩 출력한다.
"""

n = int(input())

for i in range(n):
    s = input()
    
    q_count = 0
    l_count = 0
    r_count = 0      
    result = 0
    
    l_result_list = []
    r_result_list = []
    
    for j in range(len(s)):
        if s[j] == '?':
            q_count += 1
        elif s[j] == 'L':
            l_count += 1
        elif s[j] == 'R':
            r_count += 1           
       
    
    for j in range(len(s)):
            if s[j] == 'L':
                result -= 1
            elif s[j] == 'R':
                result += 1
            elif s[j] == '?':
                result -= 1            
            l_result_list.append(result)       

    result = 0
    for j in range(len(s)):
            if s[j] == 'L':
                result -= 1
            elif s[j] == 'R':
                result += 1
            elif s[j] == '?':
                result += 1
            r_result_list.append(result) 

    
    for j in range(len(s)):
        l_result_list[j] = abs(l_result_list[j])
        r_result_list[j] = abs(r_result_list[j])
        
        
    
    print(max(max((l_result_list)), max(r_result_list)))    
    