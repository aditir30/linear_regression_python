# Linear Regression using Python
In this implementation, we calculate the beta coefficients(<img src="https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_white&space;\hat{\beta}" title="\bg_white \hat{\beta}" />) as follows - 

<img src="https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_white&space;\begin{document}\\For\&space;data\&space;points\&space;d_{i}\&space;where\&space;i=1,2,...,n\&space;and\&space;each\&space;datapoint\&space;consist\&space;of\\\\y:\&space;dependent\&space;variables\\x_{i1},x_{i2},...,x_{ip}:\&space;p-independent\&space;variables\\\\\textup{We&space;calculate}\&space;\hat{\beta}\&space;as:\\\begin{equation}\hat{\beta}=&space;(\sum_{i=1}^{n}X_{i}\cdot&space;X_{i}^T)^{-1}(\sum_{i=1}^{n}X_{i}\cdot&space;y_{i})\end{equation}\end{document}&space;" title="\bg_white \begin{document}\\For\ data\ points\ d_{i}\ where\ i=1,2,...,n\ and\ each\ datapoint\ consist\ of\\\\y:\ dependent\ variables\\x_{i1},x_{i2},...,x_{ip}:\ p-independent\ variables\\\\\textup{We calculate}\ \hat{\beta}\ as:\\\begin{equation}\hat{\beta}= (\sum_{i=1}^{n}X_{i}\cdot X_{i}^T)^{-1}(\sum_{i=1}^{n}X_{i}\cdot y_{i})\end{equation}\end{document} " />

Here the dimensions of the vector are -

X : n x (p+1) matrix

<img src="https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_white&space;\hat{\beta}" title="\bg_white \hat{\beta}" /> : (p+1) x 1 vector




To run the python file:
1. Ensure the input file on which regression will be executed should be on HDFS. For my testing I have my input file on /user/<username>/linear_reg/input/. Use below command to put file on HDFS –
   > hdfs dfs -put <file_name> <hadoop-file-path>
2. Run python file on Spark using below command –
   > spark-submit lr_regression.py hadoop-input-file.csv > output-filename.out

   Example –  
   spark-submit lr_regression.py linear_reg/input/xylin.csv > xylin.out

3. The above command will execute the spark job and will write the beta matrix in *xylin.out* which you can view by running –
    > cat xylin.out
