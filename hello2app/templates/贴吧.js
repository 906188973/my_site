        var wrap = document.querySelector('.wrap'),
            prev = document.querySelector('.prev'),
            next = document.querySelector('.next'),
            tbPromo = document.querySelector('.tp_lb'),
            dot = document.querySelectorAll('.promo-nav li');
        var timer = null,
            index = 0;
            console.log(wrap)
        
        var goIndex = function(){
            for(i = 0; i < dot.length; i++) {
                dot[i].className = '';
            }
            dot[index].className = 'selected';
        }
        // 点击上一张实现跳转
        prev.onclick = function () {
            prev_pic();
        }
        next.onclick = function () {
            next_pic();
        }
        dot.onclick = function() {
            dot_pic();
        }
        // 实现自动轮播
        function auto_play () {
            timer = setInterval(function(){
                next_pic()
            }, 2000)
        }
        auto_play();
        
        // 图片轮播实现原理
        function prev_pic() {
            var newLeft,
                left = parseInt(wrap.style.left);
            if (left == 0) {
                newLeft = -822;
            } 
            else {
                newLeft = left + 274;
            }
            // var newLeft = parseInt(wrap.style.left);
            wrap.style.left = newLeft + 'px';
            // 改变当前圆点索引
            index--;
            if (index < 0) {
                index=3;
            }
            changeDot();
        }
        function next_pic() {
            var newLeft,
                left = parseInt(wrap.style.left);
            if (left == -822) {
                newLeft = 0;
            } 
            else {
                newLeft = left - 274;
            }

            // var newLeft = parseInt(wrap.style.left);
            wrap.style.left = newLeft + 'px';
             // 改变当前圆点索引
             index++;
            if (index > 3) {
                index=0;
            }
            changeDot();
        }

        // 鼠标移过时停止轮播
        tbPromo.onmouseenter = function () {
            clearInterval(timer);
        }
        tbPromo.onmouseleave = function () {
            auto_play();
        }

        // 实现圆点样式变化
        function changeDot () {
            for(i = 0; i < dot.length; i++) {
                dot[i].className = '';
            }
            dot[index].className = 'selected';
        }
        for (var i = 0; i < dot.length; i++){
            (function(i){
                dot[i].onclick = function () {
                    // var pointIndex = this.getComputedStyle('data-index')
                    var dis = index - i;
                    // if(index == 3 && parseInt(wrap.style.left)!==-822){
                    //     dis = dis - 4;     
                    // }
                    //和使用prev和next相同，在最开始的照片5和最终的照片1在使用时会出现问题，导致符号和位数的出错，做相应地处理即可
                    // if(index == 0 && parseInt(wrap.style.left)!== -274){
                    //     dis = 4 + dis;
                    // }
                    wrap.style.left = (parseInt(wrap.style.left) +  dis * 274)+"px";
                    // wrap.style.left = (pointIndex * 274)+"px";
                    index = i;
                    changeDot();
                }
            })(i);            
        }
           