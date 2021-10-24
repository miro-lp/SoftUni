function solution(argument){
    let finallResult = []
    if (argument == 'upvote'){
        this.upvotes +=1
    }else if(argument == 'downvote'){
        this.downvotes +=1
    }
    
    let obfocusUpvote
    let obfocusDownvote
    let votes = this.upvotes + this.downvotes
    if (votes >50){
        obfocusUpvote = Math.ceil(this.upvotes*1.25)
        obfocusDownvote = Math.ceil(this.downvotes*1.25)
    }else{
        obfocusUpvote = this.upvotes
        obfocusDownvote = this.downvotes
    }
    let rating = this.upvotes - this.downvotes
    if (obfocusUpvote>obfocusDownvote){
        obfocusDownvote = obfocusUpvote - rating
    }else{
        obfocusUpvote = obfocusDownvote + rating
    }
    finallResult.push(obfocusUpvote)
    finallResult.push(obfocusDownvote)
    
    finallResult.push(rating)
    let ratingWords 
    if ((this.upvotes/votes)*100>66 && votes>=10){
        ratingWords = 'hot'
    }else if(rating>=0 && votes>100){
        ratingWords = 'controversial'
    }else if(rating<0 && votes >=10){
        ratingWords = 'unpopular'
    }else {
        ratingWords = 'new'
    }
    finallResult.push(ratingWords)
    if(argument == 'score'){
       return finallResult
    }

}

let post = {
    id: '3',
    author: 'emil',
    content: 'wazaaaaa',
    upvotes: 100,
    downvotes: 100
};
solution.call(post, 'upvote');
solution.call(post, 'downvote');
let score = solution.call(post, 'score'); // [127, 127, 0, 'controversial']
for (i=0; i<50; i++){
    solution.call(post, 'downvote')
}

score = solution.call(post, 'score');     
console.log(score)
console.log(post.downvotes)


var forumPost = {
    id: '2',
    author: 'gosho',
    content: 'whats up?',
    upvotes: 120,
    downvotes: 30
};

console.log(solution.call(forumPost, 'score'))