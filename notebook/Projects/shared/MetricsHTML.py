style = '''
<style> 
#metrics {
    width: 95%;
    margin: 20px auto;
    font-family: arial, sans-serif;
    display: flex;
    flex-direction: column;
    text-align: center;
}
h1 {
    font-size: 2em;
    font-weight: 400;
    margin: 20px auto;
    color: ##32292f;
}
h2 {
    font-size: 1.5em;
    font-weight: 400;
    color: #32292f;
}
h3 {
    font-size: 1.2em;
    font-weight: 400;
    color: #32292f;
}
.metric-box {
    margin: 0 auto;
    background-color: #99e1d9;
    border-radius: 15px 50px 30px;
    display: inline-block;
    padding: 20px;
    margin: 10px 10px 10px 10px;
    text-align: center;
    width: 200px;
    height: 150px;
}
</style>
'''

html = '''
<div id="metrics">
    <h1>Metrics</h1>
    <div>
        <div class="metric-box">
            <h3 class="sub-text">{}</h3>
            <h2 class="head">{}</h2>
        </div>
        <div class="metric-box">
            <h3 class="sub-text">{}</h3>
            <h2 class="head">{}</h2>
        </div>    
    </div>

</div>
'''
