x <- rep(1:15, each=15)
y <- rep(1:15, 15)
sqnames  = sprintf("imgx%02dy%02d", x, y)
tmp =  read.table("/home/hsec/wordfeud/hist/all.txt", header=FALSE, sep=",")
dat = data.frame(tmp, make.names=FALSE, col.names=sqnames)
rm(tmp)

lll <- vector()

dat <- sapply(dat, as.data.frame, make.names=FALSE)


createsubframe <- function (v)
{


	band <- data.frame(  red=vector(mode="integer", length=256),
		  green=vector(mode="integer", length=256),
		  blue=vector(mode="integer", length=256),
		  colorvalues = 0:255)

	imgdat <-  split(v, rep(256,3))  <- band


}

out <- sapply(dat, createsubframe)







#boxplot(colorvalues$red,
#freq=TRUE, 
#main = "RGB of image x01y01",
#col = "orange",
#border = "brown",
#notch = TRUE
#)
