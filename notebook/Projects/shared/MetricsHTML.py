style = '''
<style> 
body {
    background-color: #000000
}
#metrics {
    width: 95%;
    margin: 20px auto;
    display: flex;
    justify-content: space-around;
    align-items: center;
}
.head {
    padding: 5px;
    font-size: 30px;
    color: #32292f;
}
.sub-text {
    padding: 5px;
    font-size: 20px;
    color: #32292f;
}
.container {
  border-radius: 15px 50px;
  background: #89a1ef;
  padding: 20px;
  width: 200px;
  height: 150px;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}
</style>
'''

html = '''
<div id="metrics">
    <div class="container">
        <div class="sub-text">{}</div>
        <div class="head">{}</div>
    </div>
    <div class="container">
        <div class="sub-text">{}</div>
        <div class="head">{}</div>
    </div>
</div>
'''
