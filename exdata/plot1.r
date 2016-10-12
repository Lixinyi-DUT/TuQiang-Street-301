png('plot1.png')

total_em<-aggregate(NEI$Emissions, by=list(NEI$year), FUN=sum)
names(total_em)<-c('year','Emissions')
plot(total_em$year,total_em$Emissions,type='o',xaxt="n",xlab='Year',ylab='Total Emissions (T)',main='Total Emissions from PM2.5 in US (1999-2008)')
axis(1, at = seq(1999, 2008, by = 3), las=1)

dev.off()