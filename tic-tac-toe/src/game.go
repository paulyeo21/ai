package src

import "fmt"

type Game struct {
	P1    Player
	P2    Player
	Board [3][3]*int
}

func (g Game) State() string {
	var output string

	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			if j == 1 {
				output += fmt.Sprintf(" | %v | ", g.Board[i][j])
				continue
			}
			output += fmt.Sprintf("%v", g.Board[i][j])
		}
		output += "\n"
	}

	return output
}

func (g Game) Winner() *Player {
	return nil
}

func (g Game) InProgress() bool {
	winner := g.Winner()
	if winner != nil {
		return false
	}

	return true
}

func (g Game) InputMove(x int, y int, p Player) {
	*g.Board[x][y] = p.Marker
}
