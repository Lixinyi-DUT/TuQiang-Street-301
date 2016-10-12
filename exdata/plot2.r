png('plot2.png')

Baltimore<-NEI[NEI$fips=='24510',]
Bal_total<-aggregate(Baltimore$Emissions, by=list(Baltimore$year), FUN=sum)
names(Bal_total)<-c('year','Emissions')
plot(Bal_total$year,Bal_total$Emissions,type='o',xaxt="n",xlab='Year',ylab='Total Emissions (T)',main='Total Emissions from PM2.5 in Baltimore City')
axis(1, at = seq(1999, 2008, by = 3), las=1)

dev.off()
