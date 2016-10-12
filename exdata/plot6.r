library('ggplot2')
library('reshape2')
Baltimore<-NEI[NEI$fips=='24510',]
LA<-NEI[NEI$fips=='06037',]
s_vehicle<-SCC[grep('Vehicle',SCC$Short.Name),]
Bal_em<-Baltimore[Baltimore$SCC %in% s_vehicle$SCC,c('year','Emissions')]
LA_em<-LA[LA$SCC %in% s_vehicle$SCC,c('year','Emissions')]

Bal_total<-aggregate(Emissions~year,data=Bal_em,FUN=sum)
LA_total<-aggregate(Emissions~year,data=LA_em,FUN=sum)

emi1<-data.frame(matrix(nrow=4,ncol=0))
emi2<-data.frame(matrix(nrow=4,ncol=0))

emi1['year']<-Bal_total$year
emi2['year']<-Bal_total$year
emi1['Baltimore']<-Bal_total$Emissions
emi1['LA']<-LA_total$Emissions
emi2['Baltimore']<-Bal_total$Emissions/Bal_total$Emissions[1]
emi2['LA']<-LA_total$Emissions/LA_total$Emissions[1]
d1=melt(emi1,id=1)
d2=melt(emi2,id=1)
d1['type']=list(rep('Absolute (T)',4))
d2['type']=list(rep('Rate (with Emissions in 1999 as 1)',4))
d=rbind(d1,d2)


g<-ggplot(data=d,aes(x=as.factor(year),y=value,col=variable))+geom_point()+geom_line(aes(group=variable))+facet_wrap(~type,scales='free',nrow=2)+xlab('year')+ylab('Emissions')+scale_colour_discrete(name  ="Location",breaks=c("Baltimore", "LA"),labels=c("Baltimore City", "Los Angeles County"))+ggtitle('Changes in Total Emissions from Motor Vehicle (1999-2008)')

ggsave('plot6.png',width = 6,height = 5)
