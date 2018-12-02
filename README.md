# testing_csv
In this we have converted PDF tables to xml and json files and provided them a gui Interface

#### Project Description
### Title : Table Reading & Understanding in Documents/Images

### Abstract
In this project we will be analysing tables by using computer vision for the detection of the tables in Images/PDF for the maximum precision and after detection of the words then would be converting into different forms for the analysis by the end users

### Key focus that we kept before implementing our product is:
1. Whole process should be fully automated
2. Process should be economical for the maximising use-case 

### For the Computer Vision we will be using Open Source Library i.e.
1. OpenCV : for analysis of text in images and pdf
  - For reducing the hindrance of the background color
  - For converting the color images into grayscale this would help us to reduce the loss in images while converting
2. Camelot
  - For conversion of the images into dataframes that would help us to convert into different forms and help us to perform  calculations on data
3. pdf2Text
  - For the analysis of two tables on the same page and for the analysis of the loss in data produced

& for the analysis part in different forms and formats we would be using 
4. Pandas
- For calculations on data like pivot table and analysis of data in different streams
5. Pymysql
- For sending the data into database so that we could use sql queries in bulk data for better analysis increase its usability.

## For the interface to the end user we will be using 
Tkinter : for the making of the project interface

## Our method would be analysing 
images/pdf in 99.2% precision in which there would no loss of data would take place
As we are using computer vision for the analysis our second focus is to use minimum amount of computation and targeting maximum output to make our product usable economically

With our method users won’t be requiring any pre-trained dataset.

After our theoretical analysis we found that our methodology would be taking 1.2s for each analysis of tables in pdf and then we would be converting in different formats

Best thing of our methodology is that it can be combined with any different number of forms whether to combine in web-interface or graphical-user-interface.

To make this process simple we have provided an desktop application interface using tkinter

### Desktop Images
[Desktop Application](https://i.imgur.com/nOAJ4So.png)
[Locating File](https://i.imgur.com/DWzO4tN.png)

### Cons
1. This project does not work for streaming tables in PDFs
2. For Images
  -- We would be converting images into pdf using FPDF for the final Challenge but due to some technical glitch in GUI we did not introduced feature in this version
 
