package src

type Board struct {
}

func (b Board) Winner() *Player {
	return nil
}

func (b Board) State() [3][3]*bool {
	matrix := [3][3]*bool{
		{nil, nil, nil},
		{nil, nil, nil},
		{nil, nil, nil},
	}
	return matrix
}
