package main

import (
	"bufio"
	"fmt"
	"os"

	"github.com/paulyeo21/ai/tic-tac-toe/src"
)

func main() {
	p1 := src.Player{Name: "p1"}
	p2 := src.Player{Name: "p2"}
	board := src.Board{}
	g := src.Game{
		P1:    p1,
		P2:    p2,
		Board: board,
	}

	reader := bufio.NewReader(os.Stdin)

	for g.InProgress() {
		fmt.Println(g.State())
		fmt.Print("Input move: ")
		text, _ := reader.ReadString('\n')
		fmt.Println(text)
	}
}
