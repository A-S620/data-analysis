from typing import Dict, List

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
.metrics-display {
    display: flex;
    flex-direction: row;
    justify-content: center;
}
.metric-box {
    margin: 0 auto;
    background-color: #99e1d9;
    border-radius: 15px 50px 30px;
    padding: 20px;
    margin: 10px 10px 10px 10px;
    text-align: center;
    width: 200px;
    height: 150px;
}
</style>
'''
htmlTitle = '''
<h1>{}</h1>
'''
metricBox = '''
<div>
    <div class="metric-box">
        <h3 class="sub-text">{}</h3>
        <h2 class="head">{}</h2>
    </div>  
</div>
'''


def metrics_html(title, metrics: List[Dict[str, str]]):
    metric_box = ''
    for metric in metrics:
        metric_box += metricBox.format(metric['title'], metric['metric'])
    return style + '''<div id="metrics">''' + htmlTitle.format(title) + '''<div class="metrics-display">''' \
        + metric_box + '''</div>''' + '''</div> '''
