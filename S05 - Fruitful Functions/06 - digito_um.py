# DIGITO UM
# faz uma funçao recursiva de X/2 sempre q o resultado for impar retorna n + 1
def count_1s(X):
    if X > 0:
        if X % 2 == 0:
#            count = count_1s(X // 2)
            return count_1s(X // 2)
#        else:
#            count = count_1s(X // 2)
        return count_1s(X // 2) + 1
    return X
print(count_1s(16)) # 1
print(count_1s(5)) # 2
print(count_1s(28)) # 3
print(count_1s(15)) # 4
print(count_1s(256)) # 1