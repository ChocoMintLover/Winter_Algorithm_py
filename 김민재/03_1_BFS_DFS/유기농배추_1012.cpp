#include <stdio.h>
#include <string.h>         // memset함수

int horiz, verti;
int cabbage[50][50];

void moveInsect(int x, int y)
{
    if(x == horiz || y == verti || x < 0 || y < 0)
        return;

    if(cabbage[y][x] == 1)
    {
        cabbage[y][x] = 0;
        moveInsect(x + 1, y);
        moveInsect(x - 1, y);
        moveInsect(x, y + 1);
        moveInsect(x, y - 1);
    }
}


int main()
{
    int tc;              // test case
    int x, y, i, j, k;      // 양배추가 심어진 x, y좌표
    int numCabbage;
    int cnt;

    scanf("%d", &tc);

    for(i = 0; i < tc; i++)
    {

        scanf("%d%d%d", &horiz, &verti, &numCabbage);      // 가로 세로(수평, 수직)
        
        memset(cabbage, 0, sizeof(cabbage));

        cnt = 0;

        for(j = 0; j < numCabbage; j++)
        {
            scanf("%d%d", &x, &y);
            cabbage[y][x] = 1;
        }

        for(j = 0; j < verti; j++)
        {
            for(k = 0; k < horiz; k++)
            {
                if(cabbage[j][k] == 1)
                {
                    moveInsect(k, j);                       // x y 좌표 순서대로
                    cnt++;
                }
            }
        }

        printf("%d\n", cnt);
    }

    return 0;
}