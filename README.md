### Libraries used
Pandas : To process data <br>
Numpy : For mathematical calculations<br>
Matplotlib : Simple Data Visualization <br>
Seaborn : To see trend between CodeForces rating and CodeChef rating

### Why :
BitByte (Programming Club, PDPM IIITDM Jabalpur) is organising <b>M</b>ost <b>I</b>mproved <b>C</b>ompetitive<b> P</b>rogrammer <br>In which members are ranked based on improvement in rating on different platforms. <br>
Comparing users who are active only on one platform was in-accurate simple sorting, hence CC to CF rating converter modelled using Linear Regression was developed. <p>

### How
<ol>
<li> Scraped data of around 12000 from StopStalk.
<li> Solved data-discrepancies using Excel and Pandas
<li> Spotting a linear trend between CodeChef and Codeforces rating (using scatter plot)

![Scatter plot between ratings.](https://user-images.githubusercontent.com/87320561/209918341-bf33d5ec-9a33-4595-b224-2731b3bd425d.png)


<li> Parameters for best fit line were calculated.

![Regression plot for CodeChef and CodeForces Rating.](https://user-images.githubusercontent.com/87320561/209918288-38a02e41-376e-4f11-8913-2caa7d1cad9d.png)


</ol>

### Observations :
<ol>
  <li>After initial data cleaning, we had users with non-nan <b>10280</b> CodeChef and <b>7437</b> Codeforces ratings .</li>
  <li><b>6442</b> Users had both CF and CC ratings.</li>
  <li>Estimated coefficients for line y=mx+c are as follows :
    <ol>
      <li>constant (c) = -32.62926507315615</li>
      <li>slope of line (m) = 0.8315620555789324</li>
      <li> Where <b>y</b> represents <b>CodeForces rating</b> and <b>x</b> represents <b>CodeChef rating </b> </li>
    </ol>
    </li>
</ol>

![Best-fit line for linear regression](https://user-images.githubusercontent.com/87320561/209919590-d5b82715-9520-4b98-be7b-b6dd2244f5c7.png)
    
### Further development :
<ol>
<li> Update the dataset regularly over the course of <b>MICP</b>
<li> Develop a web-app for the same
</ol>
