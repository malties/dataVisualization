class Queue 
    { 
        constructor() 
        { 
            this.items = []; 
        } 
                    
        enqueue(element) 
        {     
        // adding element to the queue    
        this.items.push(element); 
        } 

        dequeue() 
        { 
        // removing element from the queue 
        // returns underflow when called  
        // on empty queue 
        if(this.isEmpty()) 
            return "Underflow"; 
        return this.items.shift(); 
        }

        isEmpty() 
        { 
        // return true if the queue is empty. 
        return this.items.length == 0; 
        } 
    } 