(function solve(){
    Array.prototype.last = function(){
        return this[this.length -1];
    }
    Array.prototype.skip = function(n){
        return this.slice(n,this.length);
    }

    Array.prototype.take = function(n){
        return this.slice(0,n);
    }

    Array.prototype.sum = function(){
       let result = 0;
       for (let i = 0; i< this.length; i++){
           result += this[i];
       }
       return result;
    }

    Array.prototype.average = function(){
        return this.sum()/this.length;
     }

})()

var testArray = [1, 2, 3];

console.log(testArray.skip(1)[1])