#include <iostream>
#include <cstring>

int main() {
    int c[] = {1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859, 8000, 9261};
    int x;

    while (std::cin >> x) {
        if (!x) {
            break;
        }

        long int resposta[x + 1];
        memset(resposta, 0, sizeof(resposta));
        resposta[0] = 1;

        for (int j = 0; j < 21; ++j) {
            if (c[j] <= x) {
                for (int i = c[j]; i <= x; ++i) {
                    resposta[i] += resposta[i - c[j]];
                }
            } else {
                break;
            }
        }

        std::cout << resposta[x] << std::endl;
    }

    return 0;
}
