library('ggplot2')

#png('plot3.png',width = 640, height = 480, bg = "transparent")
Baltimore<-NEI[NEI$fips=='24510',]
Bal_em=aggregate(Emissions~year+type,data=Baltimore,FUN=sum)

g<-ggplot(data=Bal_em, aes(x=as.factor(year), y=Emissions, col=type)) +geom_line(aes(group=type))+geom_point()+facet_wrap(~type,ncol=2,scales = "free")+xlab('Year')+ylab('Emissions (T)')+theme(legend.position="none")+ggtitle('Total Emissions from Four Types of Sources')
print(g)

ggsave(file='plot3.png',width = 6,height = 4)