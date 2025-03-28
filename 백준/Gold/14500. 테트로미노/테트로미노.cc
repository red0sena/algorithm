#include <iostream>
#include <vector>
#include <algorithm>  // max 함수 사용을 위해
using namespace std;

int n, m;
vector<vector<int>> board;
int answer = 0;

vector<vector<pair<int, int>>> tetris = {
    {{0, 0}, {0, 1}, {1, 0}, {1, 1}},  // square
    {{0, 0}, {0, 1}, {0, 2}, {0, 3}},  // I horizontal
    {{0, 0}, {1, 0}, {2, 0}, {3, 0}},  // I vertical
    {{0, 0}, {1, 0}, {1, 1}, {2, 1}},  // Z
    {{1, 0}, {0, 1}, {1, 1}, {2, 0}},  // Z rotated
    {{1, 0}, {1, 1}, {0, 1}, {0, 2}},  
    {{0, 0}, {0, 1}, {1, 1}, {1, 2}},
    {{0, 0}, {1, 0}, {2, 0}, {2, 1}},  // L
    {{0, 1}, {1, 1}, {2, 0}, {2, 1}},
    {{0, 0}, {0, 1}, {1, 0}, {2, 0}},
    {{0, 0}, {0, 1}, {1, 1}, {2, 1}},
    {{1, 0}, {0, 1}, {1, 1}, {1, 2}},
    {{0, 0}, {0, 1}, {0, 2}, {1, 1}},
    {{0, 0}, {1, 0}, {1, 1}, {1, 2}},
    {{1, 0}, {1, 1}, {1, 2}, {0, 2}},
    {{0, 0}, {0, 1}, {0, 2}, {1, 0}},
    {{0, 0}, {0, 1}, {0, 2}, {1, 2}},
    {{0, 0}, {1, 0}, {1, 1}, {2, 0}},
    {{1, 0}, {0, 1}, {1, 1}, {2, 1}}   // T
};

// 각 테트리스 모양의 최대 이동 범위를 미리 계산
struct ShapeBounds {
    int maxX, maxY;
};

vector<ShapeBounds> bounds;

void initBounds() {
    bounds.resize(19);
    for(int i = 0; i < 19; i++) {
        int maxX = 0, maxY = 0;
        for(int j = 0; j < 4; j++) {
            maxX = max(maxX, tetris[i][j].first);
            maxY = max(maxY, tetris[i][j].second);
        }
        bounds[i] = {maxX, maxY};
    }
}

void solution(int x, int y) {
    for(int i = 0; i < 19; i++) {
        // 모양이 보드를 벗어나는지 사전에 체크
        if(x + bounds[i].maxX >= n || y + bounds[i].maxY >= m) {
            continue;
        }
        
        int tmp = 0;
        for(int j = 0; j < 4; j++) {
            tmp += board[x + tetris[i][j].first][y + tetris[i][j].second];
        }
        answer = max(answer, tmp);
    }
}

int main() {
    // 빠른 입력을 위한 설정
    scanf("%d %d", &n, &m);
    board.resize(n, vector<int>(m));
    
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            scanf("%d", &board[i][j]);
        }
    }
    
    // 테트리스 모양의 경계 계산
    initBounds();
    
    // 각 위치에서 계산
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            solution(i, j);
        }
    }
    
    printf("%d\n", answer);
    
    return 0;
}