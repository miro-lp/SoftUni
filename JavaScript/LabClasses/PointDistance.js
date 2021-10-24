class Point{
    constructor(x,y){
        this.x = x
        this.y = y
    }

    static distance(a,b){
        let distanceX = Math.abs(a.x-b.x)
        let distanceY = Math.abs(a.y-b.y)

        return Math.sqrt(distanceX**2+distanceY**2)
    }
}

let p1 = new Point(5, 5);
let p2 = new Point(9, 8);
console.log(Point.distance(p1, p2));
