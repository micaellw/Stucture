import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;

public class TowersOfHanoi extends JFrame implements ActionListener, Runnable {
    int n = 9;
    String[] Num = { "9", "8", "7", "6", "5", "4", "3", "2" };
    int fwidth = 1000, fheight = 600;
    JButton Reset = new JButton("Reset");
    JButton exit = new JButton("Exit");
    JButton move1 = new JButton("Move");
    JButton move2 = new JButton("Move");
    JButton move3 = new JButton("Move");
    JButton Start = new JButton("Solve");

    JComboBox<String> Level = new JComboBox<>(Num);

    Rectangle[] peg = new Rectangle[3];
    Rectangle[] disk;
    JLabel count_moves = new JLabel("Moves: 0");
    JLabel Min = new JLabel("Min: ");
    JLabel Dif = new JLabel("Difficul");
    int[][] peg_capacity;
    int[] h;
    int selectedFromPeg = -1;
    int moves = 0;
    int num;
    Thread t = new Thread(this);

    public TowersOfHanoi() {
        initComponents();
        setupGame(n);
    }

    private void initComponents() {
        setLayout(null);
        setSize(fwidth, fheight);
        setTitle("Towers Of Hanoi");
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        Reset.setBounds(50, 520, 100, 40);
        Reset.addActionListener(this);

        Start.setBounds(705, 520, 100, 40);
        Start.addActionListener(this);

        exit.setBounds(170, 520, 100, 40);
        exit.addActionListener(this);

        move1.setBounds(105, 450, 100, 40);
        move1.addActionListener(this);

        move2.setBounds(405, 450, 100, 40);
        move2.addActionListener(this);

        move3.setBounds(705, 450, 100, 40);
        move3.addActionListener(this);

        Level.setBounds(105, 50, 100, 20);
        Level.addActionListener(this);

        count_moves.setBounds(230, 48, 100, 25);
        Min.setBounds(500, 48, 100, 25);
        Dif.setBounds(130, 30, 100, 20);

        add(Dif);
        add(Min);
        add(count_moves);
        add(Reset);
        add(Start);
        add(exit);
        add(move1);
        add(move2);
        add(move3);
        add(Level);

        peg = new Rectangle[3];
        for (int i = 0; i < 3; i++) {
            peg[i] = new Rectangle(150 + i * 300, 200, 20, 220);
        }

        disk = new Rectangle[n];
        peg_capacity = new int[3][n];
        h = new int[3];

        setupGame(n);
    }

    private void setupGame(int n) {
        for (int i = 0; i < n; i++) {
            disk[i] = new Rectangle(100, 400 - i * 20, 200 - i * 20, 20);
            peg_capacity[0][i] = i + 1;
        }
        h[0] = n;
        h[1] = 0;
        h[2] = 0;
        moves = 0;
        count_moves.setText("Moves: " + moves);
        repaint();
        Min.setText("Min Move : " + HN(n));
    }

    public void moveDisk(int from, int to) {
        if (h[from] == 0) {
            JOptionPane.showMessageDialog(this, "No disk to move from this peg!");
            return;
        }
        if (h[to] > 0 && peg_capacity[to][h[to] - 1] > peg_capacity[from][h[from] - 1]) {
            JOptionPane.showMessageDialog(this, "Cannot place larger disk on smaller disk!");
            return;
        }

        peg_capacity[to][h[to]] = peg_capacity[from][h[from] - 1];
        h[to]++;
        h[from]--;
        moves++;
        count_moves.setText("Moves: " + moves);
        repaint();

    }

    public void run() {
        Hanoi(n, 1, 3, 2);
    }

    public void handleMove(int pegNumber) {
        if (selectedFromPeg == -1) {
            selectedFromPeg = pegNumber;
        } else {
            moveDisk(selectedFromPeg, pegNumber);
            selectedFromPeg = -1;
        }
    }

    public void Hanoi(int diskCount, int from, int dest, int by) {
        if (diskCount == 1) {
            int hor_displacement = 260;
            try {
                Thread.sleep(100);

                peg_capacity[dest - 1][h[dest - 1]] = peg_capacity[from - 1][--h[from - 1]];

                if ((from == 1 && dest == 2) || (from == 3 && dest == 2))
                    hor_displacement = hor_displacement;
                else if ((from == 1 && dest == 3) || (from == 2 && dest == 3))
                    hor_displacement = hor_displacement * 2;
                else if ((from == 3 && dest == 1) || (from == 2 && dest == 1))
                    hor_displacement = 0;

                num = peg_capacity[dest - 1][h[dest - 1]++];
                disk[num - 1].setLocation(150 + num * 12 + hor_displacement, 475 - (h[dest - 1] - 1) * 25);
                repaint();
                moves++;
                count_moves.setText("Moves: " + moves);
            } catch (InterruptedException e) {

            }
        } else {
            Hanoi(diskCount - 1, from, by, dest);
            Hanoi(1, from, dest, by);
            Hanoi(diskCount - 1, by, dest, from);
        }
    }

    public void paint(Graphics g) {
        super.paint(g);
        g.setColor(Color.GRAY);

        for (int i = 0; i < 3; i++) {
            g.fillRect(peg[i].x, peg[i].y, peg[i].width, peg[i].height);
        }
        g.drawLine(100, 420, 850, 420);

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < h[i]; j++) {
                int diskNum = peg_capacity[i][j] - 1;
                g.setColor(Color.CYAN);
                g.fillRoundRect(peg[i].x - (disk[diskNum].width / 2 - peg[i].width / 2), 400 - j * 20,
                        disk[diskNum].width, disk[diskNum].height, 10, 10);
                g.setColor(Color.BLACK);
                g.drawRoundRect(peg[i].x - (disk[diskNum].width / 2 - peg[i].width / 2), 400 - j * 20,
                        disk[diskNum].width, disk[diskNum].height, 10, 10);
            }
        }
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == Start) {
            t = new Thread(this);
            t.start();
        } else if (e.getSource() == Reset) {
            setupGame(n);
        } else if (e.getSource() == exit) {
            System.exit(0);
        } else if (e.getSource() == move1) {
            handleMove(0);
        } else if (e.getSource() == move2) {
            handleMove(1);
        } else if (e.getSource() == move3) {
            handleMove(2);
        } else if (e.getSource() == Level) {
            int level = 9 - Level.getSelectedIndex();
            n = level;
            setupGame(n);
        }
    }

    public static int HN(int n) {
        if (n > 0) {
            return 2 * HN(n - 1) + 1;
        }
        return 0;
    }

    public static void main(String[] args) {
        TowersOfHanoi toh = new TowersOfHanoi();
        toh.setVisible(true);
    }
}
