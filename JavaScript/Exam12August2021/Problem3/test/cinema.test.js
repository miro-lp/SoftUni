const cinema = require('../cinema')
const assert = require('chai').assert

describe('Testing showMovies', ()=>{
    it('When empty array expect a message',()=>{
        let actualResult = cinema.showMovies([])
        let expectedResulet = 'There are currently no movies to show.'

        assert.equal(expectedResulet, actualResult)
    })

    it('When valid array expect sting of movies',()=>{
        let actualResult = cinema.showMovies(['Venum', 'The ring', 'Saw', 'The firestarter'])
        let expectedResulet = 'Venum, The ring, Saw, The firestarter'

        assert.equal(expectedResulet, actualResult)
    })
})

describe('Testing ticketPrice', ()=>{
    it('When invalid schedule expect an Error',()=>{
        
        assert.throw(()=>cinema.ticketPrice('Student'), Error/'Invalid projection type.')
    })

    it('When normal schedule expect a price',()=>{
        let actualResult = cinema.ticketPrice('Normal')
        let expectedResulet = 7.5

        assert.equal(expectedResulet, actualResult)
    })

    it('When Premiere schedule expect a price',()=>{
        let actualResult = cinema.ticketPrice('Premiere')
        let expectedResulet = 12.0

        assert.equal(expectedResulet, actualResult)
    })

    it('When Discount schedule expect a price',()=>{
        let actualResult = cinema.ticketPrice('Discount')
        let expectedResulet = 5.5

        assert.equal(expectedResulet, actualResult)
    })

    

})

describe('Testing swapSeatsInHall', ()=>{
    it('When fist seat is equal second seat expect a message',()=>{
        let actualResult = cinema.swapSeatsInHall(2,2)
        let expectedResulet = "Unsuccessful change of seats in the hall."

        assert.equal(expectedResulet, actualResult)
    })

    it('When fist seat is float expect a message',()=>{
        let actualResult = cinema.swapSeatsInHall(2.2,2)
        let expectedResulet = "Unsuccessful change of seats in the hall."

        assert.equal(expectedResulet, actualResult)
    })

    it('When second seat is float expect a message',()=>{
        let actualResult = cinema.swapSeatsInHall(2,2.2)
        let expectedResulet = "Unsuccessful change of seats in the hall."

        assert.equal(expectedResulet, actualResult)
    })

    it('When both seats are under 0 expect a message',()=>{
        let actualResult = cinema.swapSeatsInHall(-3,-5)
        let expectedResulet = "Unsuccessful change of seats in the hall."

        assert.equal(expectedResulet, actualResult)
    })

    it('When second seat is under 0 expect a message',()=>{
        let actualResult = cinema.swapSeatsInHall(4,-5)
        let expectedResulet = "Unsuccessful change of seats in the hall."

        assert.equal(expectedResulet, actualResult)
    })

    it('When first seat is under 0 expect a message',()=>{
        let actualResult = cinema.swapSeatsInHall(-4, 5)
        let expectedResulet = "Unsuccessful change of seats in the hall."

        assert.equal(expectedResulet, actualResult)
    })

    it('When first seat is zero expect a message',()=>{
        let actualResult = cinema.swapSeatsInHall(0,5)
        let expectedResulet = "Unsuccessful change of seats in the hall."

        assert.equal(expectedResulet, actualResult)
    })

    it('When second seat is zero expect a message',()=>{
        let actualResult = cinema.swapSeatsInHall(4,0)
        let expectedResulet = "Unsuccessful change of seats in the hall."

        assert.equal(expectedResulet, actualResult)
    })

    it('When both seats are zero expect a message',()=>{
        let actualResult = cinema.swapSeatsInHall(0,0)
        let expectedResulet = "Unsuccessful change of seats in the hall."

        assert.equal(expectedResulet, actualResult)
    })

    it('When both seats are over 20 expect a message',()=>{
        let actualResult = cinema.swapSeatsInHall(24, 23)
        let expectedResulet = "Unsuccessful change of seats in the hall."

        assert.equal(expectedResulet, actualResult)
    })

    it('When first seat is over 20 expect a message',()=>{
        let actualResult = cinema.swapSeatsInHall(24, 4)
        let expectedResulet = "Unsuccessful change of seats in the hall."

        assert.equal(expectedResulet, actualResult)
    })

    it('When second seat is over 20 expect a message',()=>{
        let actualResult = cinema.swapSeatsInHall(20, 24)
        let expectedResulet = "Unsuccessful change of seats in the hall."

        assert.equal(expectedResulet, actualResult)
    })

    it('When both seats are missing expect a message',()=>{
        let actualResult = cinema.swapSeatsInHall()
        let expectedResulet = "Unsuccessful change of seats in the hall."

        assert.equal(expectedResulet, actualResult)
    })

    it('When on seat is missing expect a message',()=>{
        let actualResult = cinema.swapSeatsInHall(3)
        let expectedResulet = "Unsuccessful change of seats in the hall."

        assert.equal(expectedResulet, actualResult)
    })

    it('When both seats are strings expect a message',()=>{
        let actualResult = cinema.swapSeatsInHall('a','b')
        let expectedResulet = "Unsuccessful change of seats in the hall."

        assert.equal(expectedResulet, actualResult)
    })

    it('When second seat is strings expect a message',()=>{
        let actualResult = cinema.swapSeatsInHall(2,'b')
        let expectedResulet = "Unsuccessful change of seats in the hall."

        assert.equal(expectedResulet, actualResult)
    })


    it('When both seat are valid expect to be changed',()=>{
        let actualResult = cinema.swapSeatsInHall(4,9)
        let expectedResulet = "Successful change of seats in the hall."

        assert.equal(expectedResulet, actualResult)
    })

    it('When first seat is 20 expect to be changed',()=>{
        let actualResult = cinema.swapSeatsInHall(20,9)
        let expectedResulet = "Successful change of seats in the hall."

        assert.equal(expectedResulet, actualResult)
    })
})