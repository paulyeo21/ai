package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"

	"github.com/paulyeo21/ai/tic-tac-toe/src"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("Input player1 name: ")

	p1, _ := reader.ReadString('\n')

	fmt.Print("Input player2 name: ")

	p2, _ := reader.ReadString('\n')

	g := src.Game{
		P1: src.Player{
			Name:   strings.Trim(p1, "\n"),
			Marker: 0,
		},
		P2: src.Player{
			Name:   strings.Trim(p2, "\n"),
			Marker: 1,
		},
		Board: [3][3]*int{
			{nil, nil, nil},
			{nil, nil, nil},
			{nil, nil, nil},
		},
	}

	p1Turn := true

	for g.InProgress() {
		fmt.Println(g.State())

		var p src.Player

		if p1Turn {
			p = g.P1
		} else {
			p = g.P2
		}

		fmt.Printf("%s: ", p.Name)

		move, _ := reader.ReadString('\n')
		fmt.Println(move)

		input := strings.Split(move, " ")
		g.InputMove(int(input[0]), int(input[1]), p)

		p1Turn = !p1Turn
	}
}
