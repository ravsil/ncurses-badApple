#include <stdio.h>
#include <ncurses.h>
#include <time.h>

void draw(unsigned long long int sprite[36], int x, int y, int color, int pair)
{
    unsigned long long int xPos = 1;
    init_pair(pair, color, color);
    attron(COLOR_PAIR(pair));

    for (int j = 0; j < 36; j++)
    {
        for (int k = 0; k < 64; k++)
        {
            if (sprite[j] & (xPos << k))
            {
                move(y + j, x + k * 2);
                printw("  ");
            }
        }
    }
    attroff(COLOR_PAIR(pair));
}

int main()
{
    initscr();
    noecho();
    curs_set(0);
    start_color();
    init_pair(8, COLOR_BLACK, COLOR_BLACK);
    bkgd(COLOR_PAIR(8));
    int x = 10;
    int y = 3;
    unsigned long long int badApple[6584][2][36];
    FILE *f;
    f = fopen("frames.dat", "rb");
    fread(badApple, sizeof(badApple), 1, f);
    fclose(f);

    for (int i = 0; i < 6584; i++)
    {
        draw(badApple[i][0], x, y, COLOR_WHITE, 1);
        draw(badApple[i][1], x, y, COLOR_BLUE, 2);
        refresh();
        clear();

        struct timespec delay;
        delay.tv_sec = 0;
        delay.tv_nsec = 1000000000 / 31;
        nanosleep(&delay, NULL);
    }

    endwin();
    return 0;
}
