'''
���ϸ� : Ex13-3-appendHello.py

a (append mode) : �߰� ���
'''
file = open('hello.txt', 'at', encoding = 'UTF-8')
file.write('Hello\n')
file.write('Nice to meet you\n')
print('hello.txt ���Ͽ� ���ο� ������ �߰� �Ǿ����ϴ�.')
file.close