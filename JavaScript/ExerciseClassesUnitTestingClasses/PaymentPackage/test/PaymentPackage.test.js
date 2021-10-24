let PaymentPackage = require('../PaymentPackage')
let assert = require('chai').assert

describe("Testing PaymentPackage module", function() {
   describe('constructor',function (){
       it('When all paramiter are valid expect initialize', function(){
           let pp = new PaymentPackage('something', 22)
           assert.equal('something', pp.name)
           assert.equal(22,pp.value)
       })

       it('When all paramiter are valid expect vat equal 20 and active to be true', function(){
        let pp = new PaymentPackage('something', 22)
        assert.equal(true, pp.active)
        assert.equal(20, pp.VAT)

    })

       it('When name is empty string expect thtow error', function(){
        
        assert.throws(()=> new PaymentPackage('', 22), Error, /Name must be a non-empty string/)
    })
    it('When name is not a string expect thtow error', function(){
        
        assert.throws(()=> new PaymentPackage(['name'], 22), Error, /Name must be a non-empty string/)
    })
    
    it('When value is not a number expect thtow error', function(){
        
        assert.throws(()=> new PaymentPackage('name', 'not number'), Error, /Value must be a non-negative number/)
    })

    
    it('When value is negative number expect thtow error', function(){
        
        assert.throws(()=> new PaymentPackage('name', -10), Error, /Value must be a non-negative number/)
    })

   });
   describe('Set methods',function (){
    it('When new name and value is valid expect to be set', function(){
        let pp = new PaymentPackage('something', 22)
        pp.name = 'name'
        pp.value = 35
      
        assert.equal('name', pp.name)
        assert.equal(35, pp.value)
    })

    it('When new value is null expect to be set', function(){
        let pp = new PaymentPackage('something', 22)
        pp.value = 0
      
        assert.equal(0, pp.value)
    })

    it('When new name not valid expect Error', function(){
        let pp = new PaymentPackage('something', 22)
       
        pp.value = 35
      
        assert.throws(()=>  pp.name = 20, Error, /Name must be a non-empty string/)
        assert.equal(35, pp.value)
    })

    it('When new value not valid expect Error', function(){
        let pp = new PaymentPackage('something', 22)
       
        pp.name = 'name'
      
        assert.throws(()=>  pp.value = [2,3], Error, /Value must be a non-negative number/)
        assert.equal('name', pp.name)
    })



    it('When VAT is valid expect to be set', function(){
        let pp = new PaymentPackage('something', 22)
        pp.VAT = 25
      
        assert.equal(25,pp.VAT)
    })

    it('When VAT is not a number expect Error', function(){
        let pp = new PaymentPackage('something', 22)
              
        assert.throws(()=> pp.VAT = 'not number', Error, /VAT must be a non-negative number/)
    })

    it('When VAT is negative numbre expect Error', function(){
        let pp = new PaymentPackage('something', 22)
              
        assert.throws(()=> pp.VAT = - 22, Error, /VAT must be a non-negative number/)
    })

    it('When active is valid expect to be set', function(){
        let pp = new PaymentPackage('something', 22)
        pp.active = false
      
        assert.equal(false, pp.active)
    })

    it('When active is not boolean expect Error', function(){
        let pp = new PaymentPackage('something', 22)
              
        assert.throws(()=> pp.active = - 22, Error, /Active status must be a boolean/)
    })

   });
   describe('toString method',function (){
    it('When active is true', function(){
        let pp = new PaymentPackage('something', 22)
      
        assert.equal('Package: something\n- Value (excl. VAT): 22\n- Value (VAT 20%): 26.4', pp.toString())
    })

    it('When active is false', function(){
        let pp = new PaymentPackage('something', 22)
        pp.active = false
      
        assert.equal('Package: something (inactive)\n- Value (excl. VAT): 22\n- Value (VAT 20%): 26.4', pp.toString())
    })

   });


});
