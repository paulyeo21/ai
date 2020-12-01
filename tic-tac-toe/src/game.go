package src

type Game struct {
	P1    Player
	P2    Player
	Board Board
}

func (g Game) State() string {
	return g.Board.State()
}

func (g Game) InProgress() bool {
	winner := g.Board.Winner()
	if winner != nil {
		return false
	}

	return true
}
