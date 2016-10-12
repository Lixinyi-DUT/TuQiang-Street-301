library('ggplot2')
library('reshape2')

coal_scc<-SCC[grep('Coal',SCC$Short.Name),]
coal<-NEI[NEI$SCC %in% coal_scc$SCC,]
em<-aggregate(Emissions~year,data=coal,FUN=function(x) c(mean(x),median(x),sum(x),length(x)))
e<-as.data.frame(em$Emissions)
names(e)<-c('Mean','Median','Total','Records')
all_coal<-melt(cbind(em[,'year'],e),id.vars=1)
names(all_coal)[1]<-'year'

g<-ggplot(data=all_coal,aes(x=as.factor(year),y=value,col=variable))+geom_point()+geom_line(aes(group=variable))+facet_wrap(~variable,ncol=2,scales='free')+theme(legend.position="none")+xlab('Year')+ylab('Emissions (T)')+ggtitle('Records for Emissions from Coal Combustion-related Sources')

ggsave(file='plot4.png',width = 6,height = 4)