#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Struct para guardar os dados de cada linha
struct X {
    long int startDay;
    long int endDay;
    long int reward;
};

// Função de comparação para ordenar as atividades com base no endDay
bool Compara_EndDays(const X& a, const X& b) {
    return a.endDay < b.endDay;
}

long int Busc_Bin(vector<X>& activities, long int startDay) {
    long int left = 0;
    long int right = activities.size() - 1;
    long int result = -1;

    while (left <= right) {
        long int mid = left + (right - left) / 2;

        if (activities[mid].endDay < startDay) {
            result = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return result;
}

int main() {
    long int n;
    cin >> n;

    vector<X> V(n);

    // Preenche o vetor de atividades
    for (int i = 0; i < n; ++i) {
        cin >> V[i].startDay >> V[i].endDay >> V[i].reward;
    }

    // Ordena as atividades com base no fim (endDay) usando a função sort
    sort(V.begin(), V.end(), Compara_EndDays);

    vector<long int> dp(n);

    dp[0] = V[0].reward; // Inicializa o primeiro elemento da dp

    // Calcula a dp
    for (int i = 1; i < n; i++) {
        // Utiliza a busca binária para encontrar a posição da última atividade que termina antes do início da atividade atual
        long int h = Busc_Bin(V, V[i].startDay);
        long int prev = 0;
        if (h != -1) {
            prev = dp[h];
        } 
        dp[i] = max(dp[i - 1], V[i].reward + prev);
    }

    // Imprime o resultado
    cout << dp[n - 1] << endl;

    return 0;
}
